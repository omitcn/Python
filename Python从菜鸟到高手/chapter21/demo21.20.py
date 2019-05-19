'''
--------《Python从菜鸟到高手》源代码------------

欧瑞科技版权所有
作者：李宁
如有任何技术问题，请加QQ技术讨论群：264268059    
或关注“极客起源”订阅号或“欧瑞科技”服务号或扫码关注订阅号和服务号，二维码在源代码根目录
如果QQ群已满，请访问https://geekori.com，在右侧查看最新的QQ群，同时可以扫码关注公众号

“欧瑞学院”是欧瑞科技旗下在线IT教育学院，包含大量IT前沿视频课程，
请访问http://geekori.com/edu或关注前面提到的订阅号和服务号，进入移动版的欧瑞学院

“极客题库”是欧瑞科技旗下在线题库，请扫描源代码根目录中的小程序码安装“极客题库”小程序

关于更多信息，请访问下面的页面
https://geekori.com/help/videocourse/readme.html



'''
from flask import Flask,request,render_template
from flask_wtf import FlaskForm
from wtforms import TextField,IntegerField,PasswordField,RadioField,TextAreaField,BooleanField,DateField,SubmitField,validators
app = Flask(__name__)
app.secret_key ='sdjsldj4323sdsdfssfdf43434'
class MyForm(FlaskForm):
    name = TextField('姓名',[validators.Required('请输入姓名')])
    email = TextField('Email',[validators.Required('请输入Email'),validators.email('请输入正确的Email地址')])
    ip = TextField('IP',[validators.Required('请输入IP地址'),validators.IPAddress(message='请输入正确的IP地址')])
    password1 = PasswordField('密码',[validators.Required('请输入密码')])
    password2 = PasswordField('确认密码',[validators.Required('请确认密码'),validators.EqualTo('password1','两次输入的密码不一致')] )
    
    value = TextField('电子邮件',[validators.Email('Email格式不正确'),validators.optional()])
    url = TextField('Url',[validators.URL(message='Url格式不正确'),validators.optional()])
    
    regexpValue = TextField('正则表达式',[validators.Regexp('^[a-z]{3}-[1-9]{3}$',message='格式错误，正确格式：abc-123'),validators.Optional()])
    submit = SubmitField('提交')    
@app.route('/',methods=['GET','POST'])
def contact():
    form = MyForm()
    ok = False
    if request.method == 'POST':
        if form.validate_on_submit() == False:
            print('error')
        else:
            print('校验成功')
            ok = True 
    return render_template('validate.txt',form = form, ok = ok)
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port='1234')