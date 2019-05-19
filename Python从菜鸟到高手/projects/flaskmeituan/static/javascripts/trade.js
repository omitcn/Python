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
    $.ajax({
        url:'/personal',
        dataType: "json",
        type:'post',
        success: function (result) {
            
            new Vue({
                el:"#huser",
                data:{
                    username:result[0]['nickname'],
                    tel:result[0]['tel_number'],
                    pic:result[0]['pic_url']
                }
            })
        },
        error:function (err) {
            console.log("123");
        }
    })
    //获取订单信息
    var trade=new Vue({
        el:"#yui_3_16_0_1_1505369383117_860",
        data:{
            trades:[]
        },
        methods:{
            select:function($e){
                var val=$("#select").val();

                if (val=="0"){
                    $.ajax({
                        url:'/trade',
                        dataType:'json',
                        type:'post',
                        success:function (result) {
                            trade.trades=result;
                        }
                    })
                }else if(val=="1"){
                      $.ajax({//已付款
                        url:'/trade/paid',
                        dataType:'json',
                        type:'post',
                        success:function (result) {
                            trade.trades=result;
                        }
                    })
                }else if(val=="2"){//未付款
                     $.ajax({
                        url:'/trade/non-payment',
                        dataType:'json',
                        type:'post',
                        success:function (result) {
                            trade.trades=result;
                        }
                    })
                }
            }
        }
    })

    $.ajax({
        url:'/trade',
        dataType: "json",
        type:'post',
        success: function (result) {
            //alert(result[0]['nickname']);
            trade.trades=result;
        },
        error:function (err) {
            console.log("123");
        }
    })


    
    $(".J-nav__trigger").mouseenter(function () {
        $(".J-nav__list").show();
        $(".F-glob-caret-up").show();
        $(".F-glob-caret-down").hide();
    });
    $(".J-nav__trigger").mouseleave(function () {
        $(".J-nav__list").hide();
        $(".F-glob-caret-up").hide();
        $(".F-glob-caret-down").show();
    });
    $(".J-nav__list").mouseenter(function () {
        $(".J-nav__list").show();
        $(".F-glob-caret-up").show();
        $(".F-glob-caret-down").hide();
    });
    $(".J-nav__list").mouseleave(function () {
        $(".J-nav__list").hide();
        $(".F-glob-caret-up").hide();
        $(".F-glob-caret-down").show();
    });
    $("#yui_3_16_0_1_1505697438810_548").mouseenter(function () {
        $(".J-nav-level2").show();
    });
    $("#yui_3_16_0_1_1505697438810_548").mouseleave(function () {
        $(".J-nav-level2").hide();
    });
});


