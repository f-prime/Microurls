from flask import Flask, request, redirect, render_template, url_for
import sqlite3
import random
c = sqlite3.connect("microurls.sqlite")
cur = c.cursor()
app = Flask(__name__)

@app.route("/url/<id>")
def show_url(id):
    pass

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
	url = request.form['url']
	cur.execute("INSERT INTO urls (url) VALUES (?)", [url])
        cur.execute("SELECT id FROM urls WHERE url=?", [url])
        urlid = cur.fetchall()
        for x in urlid:
	    for a in x:
		urlid = url_for("show_url", id=a)
		urlid = urlid.strip("/url/")
		return "URL: <a href=http://microurls.org/"+urlid+">"+"http://microurls.org/"+urlid+"</a>"
    return render_template("index.html")
@app.route("/<id>", methods=['GET', 'POST'])
def url(id):
    cur.execute("SELECT url FROM urls WHERE id=?", [id])
    fetch = cur.fetchall()   
    for x in fetch:
	for url in x:
            return redirect(url)
    


if __name__ == "__main__":
    app.run('')
