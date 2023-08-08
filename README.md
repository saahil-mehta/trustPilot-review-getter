# Trustpilot Review Scraper

This repository contains a collection of Python scripts and notebooks for web scraping and data processing. It includes the `trustPilotFetch.py` module, which fetches and analyzes reviews from Trustpilot, enabling pitching teams to draw company-specific insights for their presentations.

## Table of Contents
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Authors](#authors)
- [License](#license)

## Getting Started

These instructions will guide you through setting up the project locally.

### Prerequisites

- Python 3.7+
- pandas
- BeautifulSoup4
- requests

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/trustpilot-review-scraper.git
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   (generate the above with pipreqs if not present.)
   ```

## Usage

### trustPilotFetch.py

The `trustPilotFetch.py` module provides a function `fetch_reviews` for scraping reviews from Trustpilot.com.

Example:

```python
from trustpilotFetch import fetch_reviews

brand = "www.mojainsurance.co.uk"
pages_to_fetch = 5
data = fetch_reviews(brand, pages_to_fetch)
```

You can find a detailed example in the `main.ipynb` notebook.

## Dependencies

- [pandas](https://pandas.pydata.org/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [requests](https://docs.python-requests.org/en/latest/)

## Authors

- Saahil Mehta - saahil.mehta@digitas.com

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
```

You can further customize this README with additional sections, links to documentation, screenshots, etc., as per your project's needs. Make sure to update the URLs and other specific details to match your actual project setup.
