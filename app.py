from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'  # 使用SQLite数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 定义数据库模型
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    school = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    days = db.Column(db.String(200), nullable=False)
    time = db.Column(db.String(50), nullable=False)
    remarks = db.Column(db.String(500), nullable=True)

# 创建表
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 获取表单数据
        name = request.form['name']
        school = request.form['school']
        subject = request.form['subject']
        days = request.form.getlist('day')
        time = request.form['time']
        remarks = request.form['remarks']

        # 保存数据到数据库
        new_student = Student(name=name, school=school, subject=subject, 
                              days=",".join(days), time=time, remarks=remarks)
        db.session.add(new_student)
        db.session.commit()

        # 重定向到感谢页面
        return redirect(url_for('thank_you', name=name, school=school))
    
    return render_template('form.html')

@app.route('/thank-you')
def thank_you():
    name = request.args.get('name')
    school = request.args.get('school')
    return render_template('thank_you.html', name=name, school=school)

if __name__ == '__main__':
    app.run(debug=True)
