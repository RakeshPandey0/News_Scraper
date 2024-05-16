import json
import sys
from importlib import import_module

def load_website_scraper(website_name):
    try:
        # Load website configurations from JSON file
        with open('../config/websites.json') as f:
            website_configs = json.load(f)

        # Check if website name exists in configurations
        if website_name not in website_configs:
            raise ValueError(f"Invalid website name: {website_name}")

        # Import the corresponding scraper module
        scraper_module = import_module(f"{website_configs[website_name]['module']}")

        # Call the scrape function from the imported module
        scraper_module.scrape()

    except FileNotFoundError:
        print("Website configurations file not found.")
        sys.exit(1)

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)

    except ImportError:
        print(f"Error importing scraper module for {website_name}.")
        sys.exit(1)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python scraper.py [website_name]")
        sys.exit(1)

    website_name = sys.argv[1]
    load_website_scraper(website_name)

if __name__ == "__main__":
    main()
