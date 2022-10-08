from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
y_combinator_web = response.text
# print(y_combinator_web)

soup = BeautifulSoup(y_combinator_web, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.get_text()
    article_texts.append(article_text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

largest_upvote = max(article_upvotes)
largest_upvote_position = article_upvotes.index(largest_upvote)
largest_upvote_title = article_texts[largest_upvote_position]
largest_upvote_link = article_links[largest_upvote_position]

print(largest_upvote_title)
print(largest_upvote_link)
print(largest_upvote)

# import lxml
#
# with open("website.html", encoding="utf8") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
# print(soup.title.string)
# print(soup.prettify())
# print(soup.p)
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h3", class_="karthikeyan-heading")
# print(heading)