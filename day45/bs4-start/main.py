from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(response.text, "html.parser")
#print(soup.prettify())


news_set = soup.find_all(name="span", class_="titleline")
news_titles = []
news_links = []


for news in news_set:
    news_title = news.getText()
    news_link = news.a.get('href')

    news_titles.append(news_title)
    news_links.append(news_link)

news_upvote_set = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(news_titles)
print(news_links)
print(news_upvote_set)

largest_num = max(news_upvote_set)
largest_idx = news_upvote_set.index(largest_num)
print(f"max_vote_news : {news_titles[largest_idx]}\nlink : {news_links[largest_idx]}\nvote : {largest_num}")


max_vote_idx = -1
max_vote = 0
for i in range(len(news_upvote_set)):
    if news_upvote_set[i] > max_vote:
        max_vote = news_upvote_set[i]
        max_vote_idx = i
print(f"max_vote_news : {news_titles[max_vote_idx]}\nlink : {news_links[max_vote_idx]}\nvote : {max_vote}")

# first_news = news_set[0]
# first_news_text = first_news.getText()
# first_news_link = first_news.a.attrs["href"]
# first_news_upvote = soup.find(name="span", class_="score").getText()
#
# #print(first_news)
# print(first_news_text)
# print(first_news_link)
# print(first_news_upvote)













#import lxml

#with open("website.html","r") as file:
#    contents = file.read()
#    print(contents)

#soup = BeautifulSoup(contents, "html.parser")
#print(soup.title)
#print(soup.prettify())

#all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

#heading = soup.find("h1",id="name")
#print(heading)
#section_heading = soup.find(name="h3", class_="heading")
#print(section_heading)

# company_url = soup.select_one(selector="p a")
# name = soup.select_one(selector="#name")
#print(company_url)
#print(name)

# headings = soup.select(".heading")
# print(headings)
