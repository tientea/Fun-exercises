import requests
from bs4 import BeautifulSoup as soup

#request info from the guardian website
url = 'https://www.theguardian.com/international'
guardian = requests.get(url)
guardian_html = soup(guardian.text,"html.parser")

#extract headings and save it into a file
file_name = input("Please give the file a name: ")
with open(file_name,'wb') as new_file:
    for heading in guardian_html.find_all('a',{'class':'u-faux-block-link__overlay js-headline-text'}):  
        if heading.a:
            new_file.write(heading.a.text.replace("\n"," ").encode('utf-8').strip())
        else:
            new_file.write(heading.contents[0].encode('utf-8').strip())