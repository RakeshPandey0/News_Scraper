import requests
from bs4 import BeautifulSoup
import json


def scrape():
    url = "https://ekantipur.com/"
    processed_data_path = "../data/processed/processed_data_ekantipur.json"

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'lxml')
        main_news_section = soup.find('section', class_="main-news layout1")

        if not main_news_section:
            print("Main news section not found.")
            return

        news_list = []

        titles = [h2.text.strip() for h2 in main_news_section.find_all('h2')]
        links = [a['href'] for a in main_news_section.find_all(
            'a', attrs={'data-type': 'title'})]
        summaries = [p.text.strip() for p in main_news_section.find_all('p')]
        images = [img['src']
                  for img in main_news_section.find_all('img', src=True)]

        for i, title in enumerate(titles):
            news = {
                "id": i,
                "title": title,
                "link": links[i] if i < len(links) else '',
                "summary": summaries[i] if i < len(summaries) else '',
                "image": images[i] if i < len(images) else ''
            }
            news_list.append(news)

        with open(processed_data_path, "w", encoding='utf-8') as json_file:
            json.dump(news_list, json_file, indent=2, ensure_ascii=False)

    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


scrape()
