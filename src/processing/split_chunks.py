from .. import logger
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_to_chunks(pages: list[Document], chunk_size: int = 1024, chunk_overlap: int = 128) -> list[Document]:
  '''
  Split the pages into chunks

  Parameters
  ----------
  pages : list[Document]
    The list of pages

  Returns
  -------
  list[Document]
    The list of chunks
  '''

  try:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_documents(pages)
  except Exception as e:
    logger.error(f"[ERROR]: Error while splitting the pages: {e}")
    return