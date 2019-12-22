from flask import Flask,redirect,render_template,request,url_for,session

app=Flask(__name__)
app.secret_key="secret"

@app.route("/",methods=['POST','GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method =='POST':
        for item in ['egg','bread','milk']:
            if item not in session:
                session[item]= int(request.form[item])
            else:
                session[item]+=int(request.form[item])

        return redirect(url_for('cart'))

@app.route("/cart",methods=['POST','GET'])
def cart():
    cart=[]
    amt=0
    price=[10,20,13]
    index=0

    for item in ['egg','bread','milk']:
        cart.append({"name":item.capitalize(),"quantity":session[item]})
        amt+=price[index]*session[item]
        index=index+1

    return render_template('cart.html',cart=cart,amt=amt)

if __name__=='__main__':
    app.run(debug=True)