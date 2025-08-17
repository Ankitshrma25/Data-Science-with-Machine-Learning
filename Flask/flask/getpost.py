from flask import Flask, render_template,request
 
'''
It creates a instace of the flask class,
which will be your WSGI (Web Server Gateway Interface) application

'''
###WSGI Application
app=Flask(__name__)


##Home page
@app.route("/")
def welcome():
    return "<HTML><H1>Welcome to the course</H1></HTML>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f"Hello {name}"
    return render_template('form.html')

@app.route('/submit',methods=['POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f"Hello {name}"
    return render_template('form.html')



## Entery point of the app.py file

if __name__=="__main__":
    app.run(debug=True)
    