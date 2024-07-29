import pandas
import re
import lxml
import jupyter
d=pandas.DataFrame([['Andy',46,'Engineer'],['Jane',33,'Nurse']],columns=["Name","Age","Occupation"],index=["ID1","ID2"])
# print(type(d))
# print(d)
# print(d.Name)
# print(d.Age)
# print(type(d.Age))

#### Read table in a web page.

url="https://en.wikipedia.org/wiki/Python_(programming_language)"

html_page = pandas.read_html(url)
# print(type(html_page))
# print(html_page)
html_page_table =  pandas.read_html(url)[1]
# print(html_page_table)
data = html_page_table.to_string()
s1=re.findall(r"\n\d{1,}\s(.+?)\smutable",data)
print(s1)