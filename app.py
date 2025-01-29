from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
# 创建 Mail 实例
mail = Mail(app)
def send_email(subject, recipient, body):
    try:
        msg = Message(subject=subject, recipients=[recipient], body=body)
        mail.send(msg)  # 发送邮件
        print("Email sent successfully!")  # 打印成功日志
    except Exception as e:
        print(f"Failed to send email: {str(e)}")  # 捕获异常并打印失败日志
# 创建Flask应用
app = Flask(__name__)

# 配置邮件服务
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = '405429005@qq.com'  # QQ邮箱
app.config['MAIL_PASSWORD'] = 'jhjznoiuozjhcbdf'  # QQ邮箱授权码
app.config['MAIL_DEFAULT_SENDER'] = '405429005@qq.com'

mail = Mail(app)

# 其他Flask应用配置和数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registrations.db'
db = SQLAlchemy(app)

# 创建数据库模型等其他代码...

# 发送邮件函数
def send_email(subject, recipient, body):
    msg = Message(subject, recipients=[recipient], body=body)
    mail.send(msg)

# 路由和视图函数...


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
        send_email(
        subject='Course Registration Confirmation',
        recipient='recipient@example.com',  # 这里填写管理员或用户邮箱
        body='Form submitted successfully!'
    )

        return render_template('thank_you.html')

if __name__ == '__main__':
    # 使用应用上下文创建数据库表
    with app.app_context():
        db.create_all()  # 创建数据库表
    app.run(host='0.0.0.0', port=5000, debug=True)

