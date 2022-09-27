import requests
from bs4 import BeautifulSoup
import os

url = "https://www.akc.org/dog-breeds/"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
images = soup.find_all('img')

for image in images:
    name = image['alt']
    link = image['data-src']

    if (link == "/wp-content/themes/akc/component-library/assets/img/1x1.trans.gif"):continue

    modifiedName = name.replace(' ', '_').replace('.', '')
    fileName = modifiedName + '.jpg'

    with open(os.path.join('/Users/shiii266/Documents/Developer/ProjectBracket/ProjectBracket-ML/backend/assets/data/images/dogs', fileName), 'wb') as f:
        im = requests.get(link)
        f.write(im.content)         # Returns contents in bytes

# TODO: try click()
   

                 