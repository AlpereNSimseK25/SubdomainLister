import requests

def makeRequest(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

hedefInput = "google.com"

with open("subdomainlist.txt","r") as subdomainList:
    for word in subdomainList:
        word = word.strip() # parantez içi boş bırakılırsa boşluklardan arındırır. parantez içine bir karakter girilirse stringleri  o karakterden kurtarır
        url = "http://" + word + "." + hedefInput
        response = makeRequest(url)
