from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 显示表单页面
@app.route('/', methods=['GET'])
def form():
    return render_template('form.html')

# 处理表单提交
@app.route('/', methods=['POST'])
def submit_form():
    # 获取表单数据
    student_name = request.form['student_name']
    school_name = request.form['school_name']
    subject = request.form.getlist('subject')  # 获取选中的科目
    class_time = request.form.getlist('class_time')  # 获取选择的时间段
    
    # 这里可以添加代码来存储表单数据，如保存到数据库或打印到控制台
    print("Student Name:", student_name)
    print("School Name:", school_name)
    print("Selected Subjects:", subject)
    print("Selected Class Times:", class_time)

    # 重定向到感谢页面
    return redirect(url_for('thank_you'))


# 显示感谢页面
@app.route('/thank_you', methods=['GET'])
def thank_you():
    return render_template('thank_you.html')


if __name__ == '__main__':
    app.run(debug=True)
