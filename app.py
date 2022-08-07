from flask import Flask,render_template,request,url_for
import pandas

app = Flask(__name__)

@app.route("/")
def helo():
        return render_template("txt.html")
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        if request.form.get("login"):
            return render_template("login.html")
        if request.form.get("register"):
            return render_template("register.html")
    else:
        return render_template("login.html")
@app.route("/register" ,methods=["POST","GET"])
def register():
    if request.method =="POST":
        register_name = request.form.get("r_name")
        register_password = request.form.get("r_pass")
        email = request.form.get("r_email")
        confirm_password = request.form.get("rc_pass")

        if register_password == confirm_password:

            file = open("users.csv","a+")
            file.write(f"\n{register_name},{register_password},{email}")
            file.close()




            return render_template("registersucces.html")
        else:
            return "<script>alert('Password entered Mis-Matched. Try again !')</script>"
    else:
        return render_template("register.html")





@app.route("/l_result",methods=["POST","GET"])
def l_result():
    if request.method == "POST":
        name = request.form.get("login_name")
        password = request.form.get("login_password")
        tocheck = pandas.read_csv("users.csv")
        login_names = tocheck["Name"]
        login_passwords = tocheck["Password"]
        for i in range(len(login_names)):
            if login_names[i] == name and login_passwords[i] == password:

                return render_template("loginsuccess.html")

        else:
            return render_template("registerbt.html")







if __name__ == "__main__":
    app.run(debug=True)