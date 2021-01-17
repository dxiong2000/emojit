from textblob import TextBlob
import random
from scrape import getEmojiList
def tagWords(inputString):
    string = TextBlob(inputString)
    sets = set(['NN', 'NNS', 'PRP', 'VBD'])
    for word in string.tags:
        if(word[1] in sets and len(word[0]) > 1):
            emoji = getEmojiList(word[0])
            if(emoji):
                num = random.randint(0,10)
                emote = list(emoji.values())[random.randint(0,int(len(emoji.values())/2))]
                if(num<=5):
                    newString += word[0] + emote + " "
                elif(num<=7):
                    newString += word[0] + emote + emote + " "
                elif(num<=9):
                    newString += word[0] + emote + emote + emote + " "
                else: #num==10
                    newString += emote + emote + word[0] + emote + emote + " "
            else:
                newString += word[0] + " "
        else:
            newString += word[0] + " "
    return newString