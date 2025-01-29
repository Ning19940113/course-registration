from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registrations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 创建数据库模型
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    school = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    day = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(100), nullable=False)
    remarks = db.Column(db.String(200), nullable=True)

# 创建数据库表
def create_db():
    with app.app_context():
        db.create_all()

# 表单处理
@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # 获取表单数据
        name = request.form["name"]
        school = request.form["school"]
        subject = request.form["subject"]
        day = request.form.getlist("day")  # 获取多选框
        time = request.form["time"]
        remarks = request.form["remarks"]

        # 存储数据到数据库
        new_registration = Registration(
            name=name,
            school=school,
            subject=subject,
            day=', '.join(day),  # 多选框数据合并成字符串
            time=time,
            remarks=remarks
        )
        db.session.add(new_registration)
        db.session.commit()

        return redirect(url_for('thank_you'))  # 提交后跳转到感谢页面
    return render_template("form.html")

# 感谢页面
@app.route("/thank_you")
def thank_you():
    return render_template("thank_you.html")

# 查看提交的记录
@app.route("/view_submissions")
def view_submissions():
    registrations = Registration.query.all()
    return render_template('view_submissions.html', registrations=registrations)

# 运行时创建数据库
if __name__ == "__main__":
    create_db()  # 手动创建数据库
    app.run(debug=True)
