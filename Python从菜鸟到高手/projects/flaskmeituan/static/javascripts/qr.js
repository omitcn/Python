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
$(document).ready(function () {
    var url = window.location.href;
    var id=url.split("#");
    //alert(id[1]);
    //生成二维码
    new Vue({
       el: '#main',
       data: {
            url:"http://paysdk.weixin.qq.com/example/qrcode.php?data="+id[1]
          }
       })
        
    run();
    
});

function run() {
    setInterval(function(){
        setInterval(chat(),2000);
    },2000)
}
function chat() {

    $.ajax({ //获取订单状态是否成功
        url:'/pay/order',
        dataType: "text",
        type:'post',
        success: function (result) {

            if(result=='SUCCESS'){
                $.ajax({ 
                    url:'/update',
                    dataType: "text",
                    type:'post',
                    success:function (result) {
                        if(result=="1"){
                            alert("购买成功！");
                            window.location.href='/'
                        }

                    },
                    error:function(e){
                    	console.dir(e);
                    	alert(e);
                    }
                })
            }

        },
        error:function (err) {
            console.log("123");
        }
    })
}
function getUrlParam(name)
{
    var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
    var r = window.location.search.substr(1).match(reg);  //匹配目标参数
    if (r!=null) return unescape(r[2]); return null; //返回参数值
}
