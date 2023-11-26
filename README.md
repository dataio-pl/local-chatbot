# local-chatbot

This is a chatbot that runs locally on your computer. It is a simple chatbot that can answer questions related to the pdf dockument

## Installation

Use the packet manager (poetry)[https://python-poetry.org/] to install the dependencies.

```bash
poetry install
```

## Usage

```bash
poetry run python3 -m src.main --help

usage: main.py [-h] [--url URL] [--file_path FILE_PATH] [--start_page START_PAGE] [--end_page END_PAGE]
               [--store STORE] [--question QUESTION] [--top_k TOP_K]

options:
  -h, --help            show this help message and exit
  --url URL
  --file_path FILE_PATH
  --start_page START_PAGE
  --end_page END_PAGE
  --store STORE
  --question QUESTION
  --top_k TOP_K
```


```bash
poetry run python3 -m src.main --url "https://site.financialmodelingprep.com/" --question "Whould you like to sumarise some sample headline news?" --store True

Yes, here are some sample headline news summaries:

1. Sam Altman to return as CEO of OpenAI after reaching a preliminary agreement.
2. Kohl's stock plunges 11% following Q3 earnings, marking the seventh consecutive quarter of falling results.
3. Apple's unit sales fall 4% during China's two-week Singles Day sales event.
```
