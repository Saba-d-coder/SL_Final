from flask import Flask,request,render_template,url_for,redirect,session
import time

app=Flask(__name__)

app.secret_key="Secret"

@app.route("/",methods=['POST','GET'])
def index():
    try:
        bal=session["balance"]
        count=session["count"]
    except KeyError:
        count=session["count"]=0
        bal=session["balance"]=8000

    if request.method=='GET':
        return render_template('index.html',bal=bal,msg="try again")

    if request.method == 'POST':
        if request.form["amount"]=="":
            return render_template('index.html',bal=bal,msg="Amount required")
        
        if int(request.form["amount"]) <0:
            return render_template('index.html',bal=bal,msg="Cannot be -ve")

        if session["count"]==5:
            return render_template('index.html',bal=bal,msg="Limit exceeded")
        
        if request.form["action"]=="withdraw":
            if int(request.form["amount"]) >session["balance"]:
                return render_template('index.html',bal=bal,msg="Cannot be greater than bal")
            
            elif int(request.form["amount"]) > 5000:
                return render_template('index.html',bal=bal,msg="Cannot withdraw more than 5000")

            else:
                bal=bal-int(request.form["amount"])
                session["balance"]=bal
                session["count"]=session["count"]+1
                return render_template('index.html',bal=bal,msg="Withdrawn successfully")

        elif request.form["action"]=='deposit':
            bal=bal+int(request.form["amount"])
            session["balance"]=bal
            session["count"]=session["count"]+1
            return render_template('index.html',bal=bal,msg="Deposited successfully")


if __name__=='__main__':
    app.run(debug=True)


