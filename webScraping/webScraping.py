import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com/"

r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup)

title = soup.title
#print(title)

#print(type(title))

# print(title.string)
# print(type(title.string))

# print(type(soup))
# print(type(title))
# print(type(title.string))


#to print all paragraphs
paras = soup.find_all('p')
# print(paras)

#to find anchor tags
anchors = soup.find_all('a')

# print(anchors)


# print(soup.find('p'))

# print(soup.find('p')['class'])


# find all the element with class name lead 

# print(soup.find_all('p', class_='lead'))

# print(soup.find('p').get_text())

# print(soup.get_text())

# getting all links of this page
anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://codewithharry.com"+link.get('href')
        all_links.add(linkText)
# print(all_links)


markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string))


navbarSupportedContent = soup.find(id='navbarSupportedContent')
# print(navbarSupportedContent)


navbarSupportedContent = soup.find(id='navbarSupportedContent')
# print(navbarSupportedContent.children)


navbarSupportedContent = soup.find(id='navbarSupportedContent')
# print(navbarSupportedContent.contents)

# for elem in navbarSupportedContent.contents:
    # print(elem)

# for elem in navbarSupportedContent.children:
#     print(elem)

# for item in navbarSupportedContent.strings:
#     print(item)

# for item in navbarSupportedContent.stripped_strings:
#     print(item)


# print(navbarSupportedContent.parent)

# for item in navbarSupportedContent.parents:
    # print(item)


# for item in navbarSupportedContent.parents:
#     print(item.name)


# a space also a sibling
# print(navbarSupportedContent.next_sibling)
# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)


# elem = soup.select('#loginModal')
# print(elem)

# elem = soup.select('.modal-footer')
# print(elem)