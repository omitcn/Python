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
from wtforms import RadioField,SelectField,SelectMultipleField,SubmitField,validators
app = Flask(__name__)
app.secret_key ='sdjsldj4323sdsdfssfdf43434'

class ContactForm(FlaskForm):
    radio = RadioField('请选择一个',choices = [('值1','选项1'),('值2','选项2'),('值3','选项3')],
               validators = [validators.AnyOf(['值1','值2','值3'],'请选择一个值')])
    select = SelectField('请选择一个选项',choices=[('值1','选项1'),('值2','选项2'),('值3','选项3')],
                         validators = [validators.AnyOf(['值2'],'请选择第二项')])
    selectMultiple = SelectMultipleField('请选择多个选项',choices = [('值1','选项1'),('值2','选项2'),('值3','选项3')],
                                         validators=[validators.AnyOf([['值1','值2'],['值1','值3']],'只能选择前两项或第1项、第3项')])
    submit = SubmitField('提交')
@app.route('/', methods=['GET','POST'])
def contact():
    form = ContactForm()
    form.radio.data = '值3'
    form.selectMultiple.data = ['值1','值3']
    ok = False
    if request.method == 'POST':
        if form.validate_on_submit() == False:
            print('error')
        else:
            print('输入成功')
            print('radio',':',form.radio.data)
            print('select',':',form.select.data)
            print('selectMultiple',':',form.selectMultiple.data)
            ok = True
         
    return render_template('select.txt',form=form,ok=ok)
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port='1234')
