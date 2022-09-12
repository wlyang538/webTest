from flask import Flask, render_template, request

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

@app.route("/Regis")
def Regis():
    return render_template("Regis.html")

@app.route("/get/register", methods=["GET"])
def get_register():
    print(request.args)
    return "Register successful."

@app.route("/post/register", methods=["POST"])
def post_register():
    print(request.form)
    return "Register successful."

if __name__ == '__main__':
    app.run()