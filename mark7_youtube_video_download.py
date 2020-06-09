import webbrowser

url = input("Enter the Video URL which you want tot download : ")

url = url[:12]+'ss'+url[12:]

webbrowser.open(url)
