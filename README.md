
# Exa Search Engine

A simple Python search engine powered by the Exa API.

## Features

- Search across the web
- Search social media domains
- Display result titles and URLs
- Configurable search modes

## Requirements

- Python 3.10 or newer
- An Exa API key

## Setup

1. Clone or download this repository.
2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate it on Windows PowerShell:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set your Exa API key in PowerShell:

   ```powershell
   $env:EXA_API_KEY = "your-api-key"
   ```

6. Run the application:

   ```bash
   python main.py
   ```

## Security

Never commit your API key or `.env` file to GitHub.

## License

MIT
