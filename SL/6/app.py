from flask import Flask,redirect,render_template,request,url_for,session

app=Flask(__name__)
app.secret_key="secret1"

@app.route("/",methods=['POST','GET'])
def index():
    amt=0
    price=[10,20,13]
    index=0
    if request.method == 'GET':
        return render_template('index.html')

    if request.method =='POST':
        if request.form['egg']=="" or request.form['bread']=="" or request.form['milk']=="":
            return render_template('index.html',amt=amt,msg="All fields are required")
       
        if int(request.form['egg'])<0 or  int(request.form['bread'])<0 or  int(request.form['milk'])<0:
            return render_template('index.html',amt=amt,msg="Enter positive values")

        else:
            for item in ['egg','bread','milk']:
                amt+=price[index]*int(request.form[item])
                index=index+1

            return render_template('index.html',amt=amt,msg="Ordered Successfully")


if __name__=='__main__':
    app.run(debug=True)