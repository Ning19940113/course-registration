from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据库（这里使用SQLite，文件保存在当前目录下）
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registrations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化数据库
db = SQLAlchemy(app)

# 创建数据库模型
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 自增ID
    name = db.Column(db.String(100), nullable=False)
    school = db.Column(db.String(200), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    day = db.Column(db.String(100), nullable=False)  # 存储为逗号分隔的字符串
    time = db.Column(db.String(50), nullable=False)
    remarks = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f"<Registration {self.name}, {self.school}, {self.subject}>"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        school = request.form.get('school')
        subject = request.form.get('subject')
        day = ', '.join(request.form.getlist('day'))  # 将选择的星期合并为逗号分隔字符串
        time = request.form.get('time')
        remarks = request.form.get('remarks')

        # 保存到数据库
        registration = Registration(
            name=name,
            school=school,
            subject=subject,
            day=day,
            time=time,
            remarks=remarks
        )
        db.session.add(registration)  # 添加数据
        db.session.commit()  # 提交事务

        return render_template('thank_you.html', name=name, school=school, subject=subject, day=day, time=time, remarks=remarks)

    return render_template('form.html')


# 感谢页面
@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
