from bs4 import BeautifulSoup
import requests

def getEmojiList(searchStr):
    URL = 'https://emojipedia.org/search/?q=' + searchStr
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find('ol', 'search-results')
    #print(result)
    elements = result.find_all('span', 'emoji')
    emojis = []
    for e in elements:
        emojis.append(e.contents[0])
    
    emojiNames = []
    elements = result.find_all('a')
    for e in elements:
        emojiNames.append(e.contents[1].strip(' '))
    
    emojiDict = dict(zip(emojiNames, emojis))
    print(emojiDict)
    return emojiDict
    
getEmojiList('tree')
    