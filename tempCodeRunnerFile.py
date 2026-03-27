@app.route("/login",methods=["GET","POST"])
def login():
        if request.method == "POST":
            name = request.form["name"]
            email = request.form["email"]
            password = request.form["password"]

            query = "SELECT * FROM signup WHERE email=%s AND password=%s"
            values = (email, password)

            cursor.execute(query, values)
            user = cursor.fetchone()

            if user: 
                session["user"] = email
                session["acc_no"] = user[4]  
                flash("Login Successful ✅")
                return redirect(url_for("index"))
            else:
                flash("Invalid Credentials ❌")
                return redirect(url_for("login"))

        return render_template("login.html") 