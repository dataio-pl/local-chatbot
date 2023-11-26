from .. import logger
from langchain.schema import Document
from langchain.document_loaders import PyPDFLoader

def clean_pdf_pages(page: Document) -> Document:
  '''
  Clean the pages

  Parameters
  ----------
  page : Document
    The page to clean

  Returns
  -------
  Document
    The cleaned page
  '''

  content = page.page_content
  lines = content.split("\n")
  header = lines[0]

  if "Chapter" in header or "Item" in header:
    clean_content = "\n".join(lines[1:])
    page.page_content = clean_content
  return page

def load_the_pdf_data(file_path: str) -> list[Document]:
  '''
  Load the PDF file

  Parameters
  ----------
  file_path : str
    The path to the PDF file

  Returns
  -------
  list[Document]
    The list of pages
  '''

  try:
    loader = PyPDFLoader(file_path=file_path)
    return loader.load()
  except Exception as e:
    logger.error(f"[ERROR]: Error while loading the PDF file: {e}")
    return