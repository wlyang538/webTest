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

@app.route("/do/register", methods=["GET", "POST"])
def get_register():
    if request.method == "GET":
         return render_template("Rigis.html")
    else:
        userId = request.form.get("userId")
        pw = request.form.get("pw")
        gender = request.form.get("sex")
        hobby = request.form.getlist("hobby")
        city = request.form.get("city")
        detail = request.form.get("detail")

        print(userId, pw, gender, hobby, city, detail)
        return "Register successful."


if __name__ == '__main__':
    app.run()