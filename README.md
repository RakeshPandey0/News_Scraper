# Web Scraper Project

This project is designed to scrape news articles from various websites using a modular approach. Each website has its own dedicated scraper module.

## Usage

To scrape a website, run the following command:

```bash
python scraper.py [website_name]
```

Replace `[website_name]` with the name of the website you want to scrape, as defined in `websites.json`. Example: 'ekantipur'

## Configuration

The `websites.json` file contains configurations for each website, specifying the module to use. Example:

```json
{
    "ekantipur": {
        "module": "ekantipur_scraper"
    }
}
```

## Contributing

Feel free to submit issues or pull requests for new features or bug fixes.
