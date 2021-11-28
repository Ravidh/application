from flask import Flask, request, render_template
from glob import glob
import json
from peoplelist import p_list
from jsontext import jsontext

app = Flask(__name__)

directory = "/home/ravidh/wis-advanced-python-2021-2022/students/"
names, info = p_list(directory)
names.sort()

home_b = "<br><h3><a href=/>Home</a></h3>"

@app.route("/")
def main():
    all_names = {}
    for name in names:
        all_names[name] = name.split(' ')

    return render_template('home.html', title = "People Search Engine", names = all_names)

@app.route("/result")
def result():
    names_res, info_res = p_list(directory,request.args.get('text',''))
    names_res.sort()
    all_names_res = {}
    for name in names_res:
        all_names_res[name] = name.split(' ')

    if len(info_res) > 0:
        info_len = 1
    else:
        info_len = 0

    return render_template('search_names.html', title = "People Search Engine", names = all_names_res, info_len = info_len)

@app.route("/<name>")
def name_info(name):
    for i in info:
        if name in i["name"]:
            return render_template('include/search_line.html') + jsontext(i) + home_b
