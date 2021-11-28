from flask import Flask, request, render_template
from glob import glob
import json
from peoplelist import p_list
from jsontext import jsontext

app = Flask(__name__)

home_b = "<br><h3><a href=/>Home</a></h3>"

@app.route("/")
def main():
    names, info = p_list("/home/ravidh/wis-advanced-python-2021-2022/students/")
    names.sort()
    all_names = {}
    for name in names:
        all_names[name] = name.split(' ')

    return render_template('home.html', title = "People Search Engine", names = all_names)

@app.route("/result")
def result():
    names, info = p_list("/home/ravidh/wis-advanced-python-2021-2022/students/",request.args.get('text',''))
    names.sort()
    all_names = {}
    for name in names:
        all_names[name] = name.split(' ')

    if len(info) > 0:
        info_len = 1
    else:
        info_len = 0

    return render_template('search_names.html', title = "People Search Engine", names = all_names, info_len = info_len)

@app.route("/<name>")
def name_info(name):
    names, info = p_list("/home/ravidh/wis-advanced-python-2021-2022/students/")
    for i in info:
        if name in i["name"]:
            return render_template('include/search_line.html') + jsontext(i) + home_b
