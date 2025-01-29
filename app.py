from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registration.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    school = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    day = db.Column(db.String(200), nullable=False)
    time = db.Column(db.String(200), nullable=False)
    remarks = db.Column(db.String(500))

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        school = request.form['school']
        subject = ', '.join(request.form.getlist('subject'))
        day = ', '.join(request.form.getlist('day'))
        time = ', '.join(request.form.getlist('time'))
        remarks = request.form['remarks']

        new_registration = Registration(name=name, school=school, subject=subject,
                                        day=day, time=time, remarks=remarks)
        db.session.add(new_registration)
        db.session.commit()

        return render_template('thank_you.html')

if __name__ == '__main__':
    db.create_all()  # 创建数据库表
    app.run(debug=True)
