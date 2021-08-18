# Simple HTML Parser, coded by Emre Demirbag https://github.com/emre-demirbag
# New York Times Mini Crossword Puzzle,by Joel Fagliano,(https://www.nytimes.com/crosswords/game/mini)
#requests:(http://docs.python-requests.org/en/master/),
#soup:(https://www.crummy.com/software/BeautifulSoup/bs4/doc/)



# Import the required modules
import requests
from bs4 import BeautifulSoup as Soup
import json


session = requests.Session()

def getHTML(url):

# session.get(url) returns a response that is saved
# in a response object called resp.
    resp = session.get(url)

# BeautifulSoup will create a
# parsed tree in soup.

    soup = Soup(resp.content, "lxml")

    return soup



def getColoumns(soup):
    # soup.find_all finds the div's, all having the same
    # class "ClueList-wrapper--3m-kd" that is
    # stored NyTimes Mini Crosswords web site
    # https://www.nytimes.com/crosswords/game

    cluewrap = soup.find_all("div", {"class": "ClueList-wrapper--3m-kd"})
    # Initialise the required variables
    html = ""
    res = []

# Iterate cluewrap and clutext check for the html tags
# to get the information of each clues.

    for i in cluewrap:

        clueListTitle = i.findAll("h3")

        title = i.find('h3', attrs={'class': 'ClueList-title--1-3oW'})

        html += "=== " + clueListTitle[0].text + " ===" + "\n"

        cluetext = i.findAll("li")

        for j in cluetext:
            span = j.findAll("span")
            title[0] = title.text.strip()
            html += " " + span[0].text.strip() + " " + span[1].text.strip() + "\n"
            # Create a dictionary with the above clue information
            data = {'group': title.text.strip(), 'number': span[0].text.strip(), 'string': span[1].text.strip()}
            # Append the dictionary to the list
            res.append(data)
    print(html)

    return res

# Main Function
if __name__ == "__main__":
    url = "https://www.nytimes.com/crosswords/game/mini"
    # Enter the url of website
    s = getHTML(url)
    res = getColoumns(s)

    # Convert the python objects into json object and export
    # it to clues.json file.

    with open('clues.json', 'w', encoding='latin-1') as outfile:
        json.dump(res, outfile, indent=8, ensure_ascii=False)

print("Created Json File")



