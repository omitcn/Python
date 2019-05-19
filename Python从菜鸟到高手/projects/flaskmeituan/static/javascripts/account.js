/*
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



*/
function getUrlParam(name)
{
    var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
    var r = window.location.search.substr(1).match(reg);  //匹配目标参数
    if (r!=null) return unescape(r[2]); return null; //返回参数值
}
$(document).ready(function () {
    $.ajax({
        url:'/account',
        dataType: "json",
        type:'post',
        success: function (result) {
            //alert(result[0]['nickname']);
            new Vue({
                el:"#huser",
                data:{
                    username:result[0]['nickname'],
                    
                }
            })
        },
        error:function (err) {
            console.log("123");
        }
    })
    $.ajax({
        url:"/account",
        dataType:"json",
        type:'post',
        success:function (result) {

            new Vue({
                el:'#content',
                data:{
                    users:result
                },
                methods:{
                    nick:function(e)
                    {
                        var nickname = prompt('输入您的姓名');
                        $.ajax({
                            url:'/account/nickname',
                            dataType:'json',
                            type:'post',
                            data:{username:nickname},
                            success:function(result)
                            {
                                window.location.href = "/toaccount"
                            }
                        })
                    },
                    pwd:function(e)
                    {
                        var password = prompt('输入您的密码');
                        $.ajax({
                            url:'/account/password',
                            dataType:'json',
                            type:'post',
                            data:{password:password},
                            success:function(result)
                            {
                                window.location.href = "/toaccount"
                            }
                        })
                    }   
                }
            })
        }
    });


});