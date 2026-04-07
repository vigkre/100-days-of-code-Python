from bs4 import BeautifulSoup

with open(r"C:\Users\nxg08329\Repos - Personal\100-days-of-code-Python\day-45-web-scraping-bs4\bs4-start\website.html") as website_contents:
    contents: str = website_contents.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.name)
print(soup.title.string)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

name = soup.select_one("#name")
print(name)

headings = soup.select(".heading")
print(headings)