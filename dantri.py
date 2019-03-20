from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
# 1.Create connection
url ="https://dantri.com.vn"
conn = urlopen(url)

# 1.1.Download Page
raw_data = conn.read()
html_content = raw_data.decode("utf-8")

with open("dantri.html","wb") as f:
    f.write(raw_data)

# # 2.Find ROI
# soup = BeautifulSoup(html_content, 'html.parser')
# ul = soup.find('ul','ul1 ulnew')


# # 3. Extract ROI
# li_list = ul.find_all("li")
# new_list = []
# for li in li_list:
#     h4 = li.h4
#     a = h4.a   
#     title = a.string 
#     link = url + a["href"]

#     new = OrderedDict({
#         "Title": title.lstrip().rstrip(),
#         "Link": link,
#     })
#     new_list.append(new)

# # 4.Save Data
# pyexcel.save_as(records = new_list, dest_file_name = "dantri.xlsx")