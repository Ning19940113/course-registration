from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')  # 显示表单页面

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    grade = request.form['grade']
    
    # 获取多选科目
    subjects = request.form.getlist('subject')
    
    # 获取每个科目的意向上课时间
    subject_times = {}
    for subject in subjects:
        subject_time = request.form.get(subject + '-time')  # 动态生成的时间字段
        if subject_time:
            subject_times[subject] = subject_time
    
    # 获取具体上课时间
    day = request.form['day']
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    
    # 显示提交的数据
    return f"""
    报名成功！<br>
    学生姓名：{name} <br>
    年级：{grade} <br>
    科目：{', '.join(subjects)} <br>
    意向上课时间：{', '.join([f'{subject}: {subject_times.get(subject)}' for subject in subjects])} <br>
    上课时间：{day} {start_time} 到 {end_time}
    """

if __name__ == '__main__':
    app.run(debug=True)
