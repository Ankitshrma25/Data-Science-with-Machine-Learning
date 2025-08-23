## Building URL Dynamically
## Variable Rule
## Jinja 2 Template Engine

### Jinja2 Template Engine

'''
{{  }}  expression to print output in HTML
{%...%} condtions, for loops
{#...#} this is for comments
'''

from flask import Flask, render_template,request,redirect,url_for
 
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

@app.route('/submit_name',methods=['POST','GET'])
def submit_name():
    if request.method=='POST':
        name=request.form['name']
        return f"Hello {name}"
    return render_template('form.html')


@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    
    return render_template('result.html',results=res)

## Variable Rule
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"

    exp={'score':score,"res":res}
    
    return render_template('result.html',results=exp)
@app.route('/successif/<int:score>')
def successif(score):


    return render_template('result.html',results=score)


@app.route('/fail/<int:score>')
def fail(score):
   
    return render_template('result.html',results=score)
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    return redirect(url_for('successres',score=int(total_score)))       

    



## Entery point of the app.py file

if __name__=="__main__":
    app.run(debug=True)
    