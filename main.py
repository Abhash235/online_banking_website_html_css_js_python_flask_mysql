from flask import Flask, render_template,request,redirect,url_for,flash,session
import mysql.connector

app = Flask(__name__)
app.secret_key = "9f8a7c6e5d4b3a2f1c0e9d8b7a6f5e4c"

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="online_banking"
)
cursor = db.cursor()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/signup",methods=["GET", "POST"])
def signup():
        if request.method == "POST":
            name = request.form["fullname"]
            email = request.form["email"]
            mobile_no = request.form["mobile_no"]
            acc_no = request.form["acc_no"]
            acc_type = request.form["acc_type"]
            balance = float(request.form["balance"])
            password = request.form["password"]

        #      # check existing user
        # query = "SELECT * FROM signup WHERE email=%s OR phone=%s"
        # cursor.execute(query,(email,phone))

        # user = cursor.fetchone()

        # if user:
        #     return render_template("signup.html",
        #                            error="Email or Phone already registered")

            query = "INSERT INTO signup (user_name, email,mobile,account_no,acc_type, balance, password) VALUES (%s, %s, %s,%s, %s, %s,%s)"
            values = (name, email,mobile_no,acc_no,acc_type, balance, password)

            cursor.execute(query, values)
            db.commit()

            # AUTO LOGIN AFTER SIGNUP
            session["user"] = email
            flash("Account Created Successfully ✅", "success")
            return redirect(url_for("index"))

        return render_template("signup.html")


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
            print(user)

            if user: 
               
                session["user"] = email
                session["acc_no"] = user[4]  
                flash("Login Successful ✅", "success")
                return redirect(url_for("index"))
            else:
                flash("Invalid Credentials ❌", "error")
                return redirect(url_for("login"))

        return render_template("login.html") 

    
@app.route("/logout")
def logout():

    session.clear()
    flash("Logged out successfully", "success")
    return redirect(url_for("index"))

@app.route("/profile")
def profile():

    if "user" not in session:
        return redirect(url_for("login"))

    email = session.get("user")
    cursor.execute(
        "SELECT user_name, email, mobile, account_no, acc_type, balance FROM signup WHERE email=%s",
        (email,)
    )
    row = cursor.fetchone()

    user = None
    if row:
        user = {
            "user_name": row[0],
            "email": row[1],
            "mobile": row[2],
            "account_no": row[3],
            "acc_type": row[4],
            "balance": row[5],
        }

    return render_template("profile.html", user=user)


@app.route("/about")
def about():
    return render_template("about.html")

# @app.route("/transfer")
# def transection():
#     return render_template("transection.html")

@app.route("/transfer", methods=["GET","POST"])
def transection():

    if 'acc_no' not in session:
        return redirect("/login")

    sender_acc = session['acc_no']

    if request.method == "POST":
        # sender_acc = session['acc_no']   # logged user account
        receiver_acc = request.form['receiver']
        amount = float(request.form['amount'])
        remark = request.form['remark']

        if sender_acc == receiver_acc:
            return "Cannot transfer to same account"

        if amount <= 0:
            return "Invalid amount"

        # check sender balance
        cursor.execute("SELECT balance FROM signup WHERE account_no=%s",(sender_acc,))
        sender = cursor.fetchone()

        if sender[0] < amount:
            return "Insufficient Balance"

        # check receiver exists
        cursor.execute("SELECT balance FROM signup WHERE account_no=%s",(receiver_acc,))
        receiver = cursor.fetchone()

        if receiver is None:
            return "Receiver not found"

        # deduct sender balance
        cursor.execute("""
        UPDATE signup 
        SET balance = balance - %s 
        WHERE account_no=%s
        """,(amount,sender_acc))

        # add receiver balance
        cursor.execute("""
        UPDATE signup 
        SET balance = balance + %s 
        WHERE account_no=%s
        """,(amount,receiver_acc))

        # record transaction
        cursor.execute("""
        INSERT INTO transactions(sender_acc,receiver_acc,amount,remark)
        VALUES(%s,%s,%s,%s)
        """,(sender_acc,receiver_acc,amount,remark))

        db.commit()

        # return "Transfer Successful"
        flash("Money transferred successfully ✅", "success")
        return redirect(url_for("index"))

    return render_template("transection.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/history")
def history():

    if 'acc_no' not in session:
        return redirect("/login")

    acc_no = session['acc_no']

    cursor.execute("""
    SELECT * FROM transactions 
    WHERE sender_acc=%s OR receiver_acc=%s
    ORDER BY date DESC
    """,(acc_no,acc_no))

    data = cursor.fetchall()

    return render_template("history.html",data=data)


@app.route("/forgotpassword")
def forgotpassword():
    return render_template("forgotpassword.html")

if __name__ == "__main__":
    app.run(debug=True,port=8000)    