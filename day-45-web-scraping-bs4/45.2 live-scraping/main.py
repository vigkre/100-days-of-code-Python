from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_tag = soup.find(name="a", class_="storylink") # find gets the tag
article_text = article_tag.get_text()
article_link = article_tag.get("href")
article_score = soup.find(name="span", class_="score")
print(f"{article_link} has {article_score.get_text()}")

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.get("href")
    article_links.append(link)

article_scores = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_scores)

# highest upvoted article
highest_vote = max(article_scores)
highest_vote_index = article_scores.index(highest_vote)

print(article_texts[highest_vote_index])
print(article_links[highest_vote_index])
