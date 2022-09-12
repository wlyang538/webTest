from flask import Flask, render_template

app = Flask(__name__)

# create the map relationship of webset /show/info and function index()
@app.route("/show/info")
def indx():
    # return "China Union"
    return render_template("index.html")

@app.route("/get/news")
def get_news():
    return render_template("get_news.html")

@app.route("/user/list")
def user_list():
    return render_template("userlist.html")

if __name__ == '__main__':
    app.run()