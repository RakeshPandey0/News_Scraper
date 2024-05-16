import requests
from bs4 import BeautifulSoup
import json

def scrape():
    try:

        # final news dataframe
        news_list = []

        # Website URL
        url = "https://ekantipur.com/"

        # Fetch HTML content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors


        
        raw_data_path = "../data/raw/raw_data_ekantipur.html"
        processed_data_path = "../data/processed/processed_data_ekantipur.json"
        with open(raw_data_path, 'w', encoding='utf-8') as raw:
            raw.write(response.text)
        
        with open(raw_data_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        soup = BeautifulSoup(html_content, 'lxml')
        
        main_news_section = soup.find('section', class_="main-news layout1")


        if main_news_section:
            #Extract the titles
            titles = [article.text.strip() for article in main_news_section.find_all('h2')]

            #Extract the news_links
            news_link = [article.get('href') for article in soup.find_all('a', attrs={'data-type': 'title'})]

            #Extract the summary
            summary = [summary.text.strip() for summary in main_news_section.find_all('p')]

            #Extract image source
            image_src = [image['src'] for image in soup.find_all('img', src=True)]

        

        # print(titles)
        # print(news_link)
        # print(summary)
        # print(image_src)
        
        # Initialize an empty list to store news articles
        news_list = []

        # Loop through each news article
        for i, title in enumerate(titles):
            # Create a new dictionary for each news article
            news = {}

            # Add data to the news dictionary
            news["id"] = i
            news["title"] = titles[i]
            news["link"] = news_link[i]
            news["summary"] = summary[i]
            news["image"] = image_src[i]

            # Append the news dictionary to the news_list
            news_list.append(news)

        


    except requests.RequestException as e: 
        print(f"Error fetching {url}: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    with open(processed_data_path, "w") as json_file:
            json.dump(news_list, json_file, indent=2)
# Call the scrape function when this file is executed
# if __name__ == "__main__":
#     scrape()
