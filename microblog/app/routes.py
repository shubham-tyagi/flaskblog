from app import app
from flask import render_template,flash,redirect,url_for
from app.forms import loginFrom
@app.route('/')
@app.route('/index')
def index():
    user={'username':'Shubham'}
    
    posts=[
        {
            'author':{'username':'John'},
            'body':'Beautiful day in portland!'
        },
        {
            'author':{'username':'susan'},
            'body':'The avenge  rs movie was so cool!'
        }
     ]

    return render_template('index.html',title='Home',user=user,posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    form=loginFrom()

    if form.validate_on_submit():
        flash('login requested for user {} , remember_me = {} '.format(
            form.username.data,form.remember_me.data))
        return redirect( url_for('index') )

    return render_template('login.html',title='Sign In',form=form)
