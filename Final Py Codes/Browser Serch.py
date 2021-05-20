import webbrowser
url = 'https://www.google.de/search?q='

suchbegriff = input("Bitte Suchbegriff eingeben: ")
webbrowser.open(url+suchbegriff)