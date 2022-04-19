
from sqlite3 import connect
from flask import Flask, render_template, request, url_for, redirect, flash, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from users import usersDataList
from users import liste,liste2,liste3,liste4, time_point10, x_list10, y_list10,time_point25, x_list25, y_list25, time_point34, x_list34, y_list34, time_point37, x_list37, y_list37


username = ""
password = ""

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "secretkey"


def filtreleme_10(p,xl,yl,s,e):
    filtreli_10 = []
    
    for i in range(1440):
        f_10 = {
        "x":0,
        "y":0,
        }
        if p[i] >= s and p[i] <= e:
            f_10.update({"x": xl[i]})
            f_10.update({"y": yl[i]})
            filtreli_10.append(f_10)
    return filtreli_10


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':       
        username = request.form.get('inputUsername')
        password = request.form.get('inputPassword')
        
        if username in usersDataList and password in usersDataList:
            if username == "gulay":
                return render_template('profile.html',coordinates = liste, coordinates2 = liste2, name = username)
            elif username == "nisa":
                return render_template('profile.html', coordinates3 = liste3, coordinates4 = liste4, name = username)
            else:
                return render_template('profile.html',coordinates = liste, coordinates2 = liste2, coordinates3 = liste3, coordinates4 = liste4, name = "admin")          
        else:
            flash('There is no such a user',category='error')
            return redirect(url_for('login'))
        
    return render_template("login.html")

@app.route('/profile', methods = ['GET','POST'])
def profile():        
    return render_template('profile.html',coordinates = liste, coordinates2 = liste2, coordinates3 = liste3, coordinates4 = liste4)

@app.route('/choise')
def choise():     
    return render_template("choise.html")   

@app.route('/maps')
def maps():
    startchoise = "00:00"
    endchoise = "24:00"
    car = "10"
    
    startchoise = startchoise.split(":")
    s = int(startchoise[0])*60 + int(startchoise[1])
    endchoise = endchoise.split(":")
    e = int(endchoise[0])*60 + int(endchoise[1])

    if s < e:
        if car == "10":
            f = filtreleme_10(time_point10,x_list10,y_list10,s,e)
            return render_template('maps.html', filter_coordinates = f)
        return render_template('maps.html')


if __name__=='__main__':
    app.run(debug=True)

