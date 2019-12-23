from flask import Flask,redirect,render_template,url_for,request
import re
import time 

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='GET':
        return render_template('index.html',res='')

    if request.method=='POST':
        if request.form['m1']=='' or request.form['m2']=='' or request.form['m3']=='':
            return render_template('index.html',res='Please fill all fields')
        
        else:
            try:
                time.strptime(request.form['dob'],'%d/%m/%Y')
            except ValueError:
                return render_template('index.html',res='Enter Correct DOB')
        
        if re.match('^[1][A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]$',request.form['usn']):
            sum= int(request.form['m1'])+int(request.form['m2'])+int(request.form['m3'])
            avg=sum/3

            res='Result is'+str(avg)
            return render_template('index.html',res=res)
        else:
            return render_template('index.html',res='Invalid USN')
                
if __name__=='__main__':
    app.run(debug=True)