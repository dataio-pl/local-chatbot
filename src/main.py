from . import logger
from argparse import ArgumentParser
from dataclasses import dataclass
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from time import time

from src.processing.pdf_data import load_the_pdf_data, clean_pdf_pages
from src.processing.split_chunks import split_to_chunks
from src.processing.vectorstore import store_chunks_into_vectorstore
from src.processing.web_data import load_the_web_data

# https://docs.python.org/3/library/dataclasses.html
@dataclass
class Config:
  url: str
  file_path: str
  start_page: int
  end_page: int
  store: bool
  question: str
  top_k: int

def main(config: Config):
  logger.info("[INFO]: Starting the application ...")

  if config.url:
    pages = load_the_web_data(config.url)
    chunks = split_to_chunks(pages=pages)
  elif config.file_path:
    pages = load_the_pdf_data(config.file_path)

    logger.info(f"[INFO]: Data loaded successfully: {len(pages)} pages")

    filtered_pages = [clean_pdf_pages(page) for page in pages if config.start_page <= page.metadata["page"] <= config.end_page]

    logger.info(f"[INFO]: Filtered page in the following range: [{config.start_page}, {config.end_page}]")

    chunks = split_to_chunks(pages=filtered_pages)

  logger.info(f"[INFO]: Split documents into {len(chunks)} chunks")

  vectorstore = store_chunks_into_vectorstore(chunks, config.store)

  logger.info("[INFO]: Generating answer with LLM")

  template = """Use the following pieces of context to answer the question at the end.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    {context}
    Question: {question}
    Helpful Answer:"""

  QA_CHAIN_PROMPT = PromptTemplate.from_template(template=template)

  llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.0)
  qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
  )

  t1 = time()
  answer = qa_chain({"query": config.question})
  t2 = time()
  logger.info(f"[INFO]: Elapsed time: {t2 - t1} seconds")

  print(answer["result"])

if __name__ == "__main__":
  parser = ArgumentParser()
  parser.add_argument("--url", type=str)
  parser.add_argument("--file_path", type=str)
  parser.add_argument("--start_page", type=int)
  parser.add_argument("--end_page", type=int)
  parser.add_argument("--store", type=bool, default=False)
  parser.add_argument("--question", type=str, default="Would you please summarize the document?")
  parser.add_argument("--top_k", type=int, default=4)
  args = parser.parse_args()

  if args.url and args.file_path:
    print("[ERROR]: Please provide either --url or --file_path, not both.")
    exit()

  if args.url and (args.start_page or args.end_page):
    print("[ERROR]: --start_page and --end_page cannot be used with the --url.")
    exit()

  config = Config(
    url=args.url,
    file_path=args.file_path,
    start_page=args.start_page,
    end_page=args.end_page,
    store=args.store,
    question=args.question,
    top_k=args.top_k
  )

  main(config)
