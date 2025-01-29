from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registrations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 定义数据库模型
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    school = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    day = db.Column(db.String(100), nullable=False)  # 存储选中的星期，多个用逗号分隔
    time = db.Column(db.String(50), nullable=False)
    remarks = db.Column(db.String(255), nullable=True)

# 创建数据库
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 获取表单数据
        name = request.form.get('name')
        school = request.form.get('school')
        subject = request.form.get('subject')
        day = ', '.join(request.form.getlist('day'))  # 将选择的星期合并为逗号分隔字符串
        time = request.form.get('time')
        remarks = request.form.get('remarks')

        # 保存数据到数据库
        registration = Registration(
            name=name,
            school=school,
            subject=subject,
            day=day,
            time=time,
            remarks=remarks
        )
        db.session.add(registration)
        db.session.commit()

        # 返回感谢页面
        return render_template('thank_you.html', name=name, school=school, subject=subject, day=day, time=time, remarks=remarks)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
