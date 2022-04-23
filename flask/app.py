from flask import Flask,redirect,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy

# from app import result

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)


# models
# class Laptops(db.Model):
#     {}



@app.route('/')
def welc():
    return render_template('welcome.html')

@app.route('/whom')
def whom():
    return render_template('whom.html')

@app.route('/myself')
def myself():
    return render_template('myself.html')

@app.route('/gaming')
def gaming():
    return render_template('purpose/gaming.html')

@app.route('/studying')
def studying():
    return render_template('purpose/studying.html')

@app.route('/programing')
def programing():
    return render_template('purpose/programing.html')

@app.route('/editing')
def editing():
    return render_template('purpose/editing.html')

@app.route('/casual')
def casual():
    return render_template('purpose/casual.html')

@app.route('/office')
def office():
    return render_template('purpose/office.html')

if __name__=='__main__':
    db.create_all()
    app.run(debug=True)