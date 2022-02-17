import urllib.request,json

def getMemeList(url):
    data=json.load(urllib.request.urlopen(url))
    print("done fetching")
    return data["data"]

URL= "http://alpha-meme-maker.herokuapp.com/"

list=getMemeList(URL)

    
def printMemeList(memeList, symbol, maxRange):
    for item in memeList:
        print(symbol+symbol+symbol+symbol+symbol+symbol+symbol+symbol+symbol)
        print(item["name"])
        print(item["bottomText"])
        string=""
        for x in range(maxRange, 0, -1):
            string += symbol
        print(string)
    
printMemeList(list, "#", 22)
