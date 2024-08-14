
# Amazon Product Scraper

This project demonstrates a web scraping tool designed to extract product data from Amazon Egypt.

## Features

- Scrapes product names, ratings, reviews and prices.
- Handles pagination to retrieve multiple pages of results.
- Includes error handling for network requests.

## Project Structure

```
.
├── main.ipynb  # Jupyter notebook containing the main scraping logic
├── functions.py  # Helper functions for extracting data from HTML
├── data/
│ └── products.csv # Sample output of the scraped data
├── README.md  # Project documentation
└── requirements.txt  # List of Python dependencies
```

## Getting Started

### Prerequisites

- `requests`
- `beautifulsoup4`
- `pandas`

Install the required packages:

```bash
pip install -r requirements.txt
```

### Usage

Run the Jupyter notebook `main.ipynb` to start the web scraping process. The results will be stored in a CSV file.

### Functions

The helper functions are defined in `functions.py`:

- `get_product_name(container)`: Extracts the product name from a container.
- `get_product_rating(container)`: Extracts the product rating.
- `get_product_nreviews(container)`: Extracts the number of reviews.
- `get_product_price(container)`: Extracts the product price.

### Output

The scraped data includes the following fields:

- **Name**: The name of the product.
- **Price (EGP)**: The price of the product in Egyptian Pounds.
- **Rating**: The average rating of the product.
- **Reviews**: The number of reviews for the product.
- **Keyword**: The search term used to query Amazon's search page.

### Example Output

```json
{
    "Name": "Sample Product",
    "Price (EGP)": "399.99",
    "Rating": "4.5",
    "Reviews": "123",
    "Keyword": "top rated"
}
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
