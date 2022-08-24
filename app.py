
import email
from flask import Flask,redirect,url_for,render_template,request
import pickle

app=Flask(__name__)


model=pickle.load(open('spam_detection.pkl','rb'))


@app.route('/')
def Hello():
    return render_template('index.html')

'''@app.route('/result/<decision>')
def result(decision):
    return render_template('results.html',result=decision)'''



@app.route('/submit',methods=['POST','GET'])
def submit():
    decision=''
    if request.method=='POST':
        email=[request.form['email']]
        res=model.predict(email)
        if res[0]=='spam':
            decision='SPAM'
        else:
            decision='NOT SPAM'
    
    
    return render_template('results.html',des=decision)




if __name__=="__main__":
    app.run(debug=True)