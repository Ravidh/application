from flask import Flask, request
from glob import glob
import json
from peoplelist import p_list
from jsontext import jsontext

app = Flask(__name__)

home_b = "<br><h3><a href=/>Home</a></h3>"
search_code = '''
     <br><form action="/result" method="GET">
         <input name="text">
         <input type="submit" value="Go!">
     </form><br>
     '''

@app.route("/")
def main():
    names, info = p_list("/home/ravidh/wis-advanced-python-2021-2022/students/")
    names.sort()
    names_links = []

    for name in names:
        link = "<a href=/"+name.split(' ')[0]+">"+name+"</a>"
        names_links.append(link)

    names_links.append(home_b)
    list_names = '<br>'.join(names_links)
    return search_code+list_names

@app.route("/result")
def result():
    names, info = p_list("/home/ravidh/wis-advanced-python-2021-2022/students/",request.args.get('text',''))
    names.sort()
    names_links = []

    for name in names:
        link = "<a href=/"+name.split(' ')[0]+">"+name+"</a>"
        names_links.append(link)

    if len(info) == 0:
        names_links.insert(0,"No mathes found!<br>")

    names_links.append(home_b)
    list_names = '<br>'.join(names_links)
    return search_code + list_names

@app.route("/<name>")
def name_info(name):
    names, info = p_list("/home/ravidh/wis-advanced-python-2021-2022/students/")
    for i in info:
        if name in i["name"]:
            return search_code + jsontext(i) + home_b
