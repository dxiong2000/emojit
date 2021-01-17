from bs4 import BeautifulSoup
import requests

def getEmojiList(searchStr):
    URL = 'https://emojipedia.org/search/?q=' + searchStr
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find('ol', 'search-results')
    
    elements = result.find_all('span', 'emoji')
    emojis = []
    for e in elements:
        emoji = e.contents[0].strip(' ')
        if len(emoji) > 1:
            emoji = emoji[0]
        emojis.append(f'U+{ord(emoji):X}')
    
    emojiNames = []
    elements = result.find_all('a')
    for e in elements:
        emojiNames.append(e.contents[1].strip(' '))
    
    emojiDict = dict(zip(emojiNames, emojis))
    
    print(emojiDict)
    return emojiDict
    