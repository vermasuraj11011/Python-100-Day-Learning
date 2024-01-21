from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')

print(soup.title)
print(soup.title.string)
print(soup.ul.li)
print(soup.find_all(name='li'))
print(soup.find_all(name='li')[2])

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)
