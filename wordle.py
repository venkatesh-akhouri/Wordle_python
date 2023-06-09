#we will web scarape four letter words/five letter words
#randomly pick a word
#tell the length
#playerhas to guess it

from bs4 import BeautifulSoup
import requests
import random
import string




url="https://games4esl.com/list-of-5-letter-words/"
req=requests.get(url) #will return the content of the page
print(req.text)    #this will store the response
res=BeautifulSoup(req.text,'html.parser')
#print(res.prettify())

#now we have to find all the words.
#since they will be associated with a tag, we will find the tag and save them in a set
wordList=[]

## parent tag seems to be article
tags=res.article
ul_tags=tags.find_all('ul')
for ul_tag in ul_tags:
    li_tag=ul_tag.find_all('li')
    for words in li_tag:
        if len(words.string) == 5:
            wordList.append(words.string)
            #print(str(words.string)+ ' added')

wordList.sort()
print(len(wordList))
#print(wordList)

#now that we have our wordlist
#let us create a function to return a word

def selectWord(wordList):
    word=random.choice(wordList)
    return(word)


word=selectWord(wordList)
print(word)
def printWord(guess,word):
    res=''
    for i in range(5):

        if guess[i]==word[i]:
            res=res+guess[i]
        else:
            res=res+" __ "
    print(res)



def wrong_letters(guess,words):
    letters_in_word=set(words)
    not_in_word=set()
    for i in range(5):
        if guess[i] not in letters_in_word:
            not_in_word.add(guess[i])
    return(not_in_word)


def wrongPosition(guess,word):
    #the guessed letter exists in the word but not at correct position
    #lets get the indexes
    for i in range(5):
        if guess[i] in word and guess[i]!=word[i]:
            print(guess[i]+ ' is at wrong position')


def play(word):
    print("Welcome to wordle")
    print("Guess the word, you have 5 chance")
    chances_left=5
    available_letters=set(string.ascii_lowercase)
    while(chances_left>0):
        guess=input('enter your guess ')
        if(guess==word):
            printWord(guess, word)
            print("congratulations ")
            print("thanx for playing")

            break #break out of the loop after guessing the right word
        else:
            not_in_word=wrong_letters(guess,word)
            print('these letters are not in word '+str(not_in_word))
            wrongPosition(guess, word)
            available_letters=available_letters-not_in_word
            print('available letters '+str(available_letters))
            printWord(guess,word)
            chances_left-=1
            if chances_left==0:
                print('chances over, thanx for playing')


play(word)






















