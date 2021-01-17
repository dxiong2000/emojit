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
        emojis.append(emoji)
    
    emojiNames = []
    elements = result.find_all('a')
    
    # no results
    if elements[0].contents[0] == 'random emoji':
        return {}
    
    for e in elements:
        if len(e.contents) > 1:
            emojiNames.append(e.contents[1].strip(' '))
        else:
            emojiNames.append(e.contents[0].strip(' '))
    
    emojiDict = dict(zip(emojiNames, emojis))
    
    #print(emojiDict)
    return emojiDict