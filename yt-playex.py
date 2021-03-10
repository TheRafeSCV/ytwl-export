from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path
import csv, os

yt_html = Path(input("Input File path/filename: "))
while not yt_html.exists() or yt_html.suffix != ".txt":
    yt_html = Path(input("Invalid path/filename '" + str(yt_html) + "'. Please chose a different path/filename: "))

file_out = Path(input("Output filename (path will be same as input): "))
if file_out.suffix != ".csv":
    file_out = Path(os.path.join(str(file_out) + ".csv"))
file_out = Path(yt_html.parents[0] / file_out)

while file_out.exists():
    file_out = Path(input("It appears as though a file with the name '" + str(file_out) + "' already exists. Please choose a different file name: "))
    if file_out.suffix != ".csv":
        file_out = Path(os.path.join(str(file_out) + ".csv"))
    file_out = Path(yt_html.parents[0] / file_out)

timerStart = datetime.today()

with open(yt_html, 'r', encoding="utf8") as yt_code:
    data = yt_code.read()

soup = BeautifulSoup(data, features="html.parser")
ytlinks = soup.find_all('a', id="video-title")

with open(file_out, mode='w', newline='', encoding='utf-8') as yt_wl:
    yt_app = csv.writer(yt_wl, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    yt_app.writerow(['Title', 'Link'])
    for ytlink in ytlinks:
        yt_app.writerow([ytlink.text.strip(), 'https://www.youtube.com' + ytlink.get('href').split("&list")[0]])
    yt_app.writerow(['COUNT: ' + str(len(ytlinks)), 'RUN: ' + datetime.today().strftime('%Y-%m-%d-%H:%M:%S')])
yt_wl.close()

timerEnd = datetime.today() - timerStart

print('Successfully wrote ' + str(len(ytlinks)) + ' rows to file: ' + str(file_out) + ". Completed in " + str(timerEnd))
