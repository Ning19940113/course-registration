from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 首页，显示表单
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # 获取表单数据
        name = request.form['name']
        school = request.form['school']
        subject = request.form['subject']
        days = request.form.getlist('day')  # 获取多个选中的天
        time = request.form['time']
        remarks = request.form['remarks']
        
        # 处理数据，比如存储到数据库或打印
        print(f"Name: {name}, School: {school}, Subject: {subject}, Days: {days}, Time: {time}, Remarks: {remarks}")

        # 提交后重定向到感谢页面
        return redirect(url_for('thank_you'))

    # 显示表单页面
    return render_template('form.html')

# 感谢页面
@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
