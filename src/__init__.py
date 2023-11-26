from dotenv import load_dotenv
from rich.logging import RichHandler
import click
import logging

load_dotenv()  # Load environment variables from .env file

LOGGER_NAME = "local-chatbot"
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[RichHandler(rich_tracebacks=True, tracebacks_suppress=[click])]
)
logger = logging.getLogger(LOGGER_NAME)
logging.getLogger("numexpr").setLevel(logging.ERROR)
