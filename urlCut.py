import pyperclip

url = pyperclip.paste()

if url[0:8] == "https://":
    url = url[8:]

if url[0:7] == "http://":
    url = url[7:]

for i in range(len(url)-2):
    if url[i:(i+3)] == "www":
        url = url[i:]
        break

for i in range(len(url)):
    if url[i] == "/":
        url = url[:i+1]
        break

print(url)

pyperclip.copy(url)