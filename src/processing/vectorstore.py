from .. import logger
from langchain.vectorstores import Chroma
from langchain.schema import Document
from langchain.embeddings import OpenAIEmbeddings

def store_chunks_into_vectorstore(chunks: list[Document], store: bool, persist_directory: str = "db") -> Chroma:
  '''
  Store the chunks into the vectorstore

  Parameters
  ----------
  chunks : list[Document]
    The list of chunks
  store : bool
    Whether to store the chunks into the vectorstore
  persist_directory : str
    The directory to store the vectorstore

  Returns
  -------
  Chroma
    The vectorstore
  '''

  if bool(store):
    logger.info("[INFO]: Embedding chunks into the Chroma database ...")

    try:
      logger.info("[INFO]: Chunks indexed into Chroma")
      return Chroma.from_documents(
        documents=chunks,
        embedding=OpenAIEmbeddings(),
        persist_directory=persist_directory,
      )
    except Exception as e:
      logger.error(f"[ERROR]: Error while indexing the chunks: {e}")
      return
  else:
    try:
      return Chroma(
        persist_directory=persist_directory,
        embedding_function=OpenAIEmbeddings(),
      )
    except Exception as e:
      logger.error(f"[ERROR]: Error while loading the vectorstore: {e}")
      return