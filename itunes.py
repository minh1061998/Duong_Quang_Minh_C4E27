from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL


url = "https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)

raw_data = conn.read()
html_content = raw_data.decode("utf-8")
# print(html_content)

soup = BeautifulSoup(html_content, 'html.parser')
section = soup.find("section", "section chart-grid")

div=section.div
ul=div.ul
li_list = ul.find_all("li")
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1, # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
}
new_list=[]
for li in li_list:
    h3=li.h3
    h4=li.h4
    title = h3.string
    artist = h4.string

    new = OrderedDict({
        "Title": title.lstrip().rstrip(),
        "Artist": artist,
    })
    new_list.append(new)

    dl = YoutubeDL(options)
    dl.download([title])

# pyexcel.save_as(records = new_list, dest_file_name = "itunes.xlsx")