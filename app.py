from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# 创建Flask应用
app = Flask(__name__)

# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # 使用SQLite数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 禁止SQLAlchemy追踪数据库修改
db = SQLAlchemy(app)  # 创建SQLAlchemy实例

# 创建数据库模型
class RegistrationForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(100), nullable=False)  # 学生姓名
    grade = db.Column(db.String(50), nullable=False)  # 年级
    subjects = db.Column(db.String(200), nullable=False)  # 所选科目
    time_slots = db.Column(db.String(200), nullable=False)  # 所选时间段
    school = db.Column(db.String(100), nullable=True)  # 学校（可选）

    def __repr__(self):
        return f'<RegistrationForm {self.name}>'

# 初始化数据库
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # 获取表单数据
    name = request.form['name']
    grade = request.form['grade']
    subjects = ', '.join(request.form.getlist('subjects'))  # 获取多个选项
    time_slots = ', '.join(request.form.getlist('time_slots'))  # 获取多个选项
    school = request.form['school']

    # 创建新的表单提交记录
    new_submission = RegistrationForm(
        name=name,
        grade=grade,
        subjects=subjects,
        time_slots=time_slots,
        school=school
    )

    # 添加到数据库并提交
    db.session.add(new_submission)
    db.session.commit()

    return render_template('thank_you.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
