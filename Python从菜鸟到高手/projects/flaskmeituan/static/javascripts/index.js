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

    //判断是否登录
    var user=new Vue({
        el: '#user',
        data: {
            username:"未登录"
        }
    })
    $.ajax({
        url:'/islogin',
        dataType: "text",
        type:'get',
        success: function (result) {
            user.username=result;
        },

        error:function (err) {
            console.log(err);
        }
    });

	//获取全部分类
	$.ajax({
	    url:'/field',
	    dataType: "json",
	    type:'get',
	    success: function (result) {
	        //alert(result);
	        new Vue({
	            el: '#field',
	            data: {
	                css:result
	            }
	        })
	    },
	    error:function (err) {
	        console.log("123");
	    }
	});

    $(document).on("mouseenter",".nav-li",function(){
        var index=$(this).index();
        var id=$(this).attr("data-id");

        $.ajax({
            url:'/sub_field',
            data:{fid:id},
            dataType: "json",
            type:'post',
            success: function (result) {
                //alert(result);
                new Vue({
                    el: '#meishi',
                    data: {
                        mss:result
                    }
                })
            },
            error:function (err) {
                console.log("123");
            }
        });
        $(".category-nav-detail-wrapper").addClass("active");
        $(".category-nav-detail").eq(index).addClass("active").siblings().removeClass("active");
    });
    $(document).on("mouseleave",".category-nav-detail",function(){
        var index=$(this).index();
        $(".category-nav-detail-wrapper").removeClass("active");
        $(".category-nav-detail").eq(index).removeClass("active").siblings().removeClass("active");
    });
});


