# SummarizeGoogleScholar

A Python tool that automatically generates personalized email drafts for professors based on their Google Scholar publications. This tool helps researchers and students craft meaningful outreach emails by analyzing the professor's recent work and matching it with the sender's background.

## Features

- Scrapes Google Scholar profiles to extract publication information
- Retrieves paper titles and abstracts
- Generates personalized email drafts using GPT-4
- Supports sorting papers by citations or publication year
- Implements rate limiting and random delays to avoid blocking
- Uses browser-like headers for reliable scraping

## Prerequisites

- Python 3.x
- OpenAI API key
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/SummarizeGoogleScholar.git
cd SummarizeGoogleScholar
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Import the required modules:
```python
from her import Her
from scraper import get_scholar_papers, get_paper_details
```

2. Get papers from a Google Scholar profile:
```python
results = get_scholar_papers(
    "https://scholar.google.com/citations?user=PROFESSOR_ID&hl=en",
    sort_by="year",  # or "citations"
    num_papers=5
)
```

3. Get details for each paper:
```python
all_papers = []
for link in results:
    paper_info = get_paper_details(link)
    all_papers.append(paper_info)
```

4. Generate a personalized email:
```python
resume = """
Your resume text here
"""

her = Her()
email_draft = her.write_email(resume, all_papers)
```

## Project Structure

- `scraper.py`: Contains functions for scraping Google Scholar profiles and paper details
- `her.py`: Implements the email generation logic using GPT-4
- `main.ipynb`: Example Jupyter notebook demonstrating usage
- `.env`: Configuration file for API keys (not included in repository)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is intended to assist in writing personalized emails. Please ensure that all generated content is reviewed and modified as needed before sending. The tool should be used responsibly and in accordance with Google Scholar's terms of service.
