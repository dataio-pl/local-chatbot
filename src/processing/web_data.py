from .. import logger
from langchain.schema import Document
from langchain.document_loaders import WebBaseLoader

def load_the_web_data(url: str) -> list[Document]:
  '''
  Load the web data

  Parameters
  ----------
  url : str
    The URL to the web data

  Returns
  -------
  list[Document]
    The list of pages
  '''

  try:
    loader = WebBaseLoader(url)
    return loader.load()
  except Exception as e:
    logger.error(f"[ERROR]: Error while loading the web data: {e}")
    return