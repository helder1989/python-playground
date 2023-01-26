from web_scraping import WebScraping

url = "https://www.airbnb.com.br/"
web_scraping = WebScraping(url)
print(web_scraping.get_rooms())