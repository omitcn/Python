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
$(document).ready(function(){
	var url = window.location.href;
	var id = url.replace(/.*\//,'');
	var arr=url.split('/');
	var shopId = arr[4]; // 店铺id

	$.ajax({
		url:'/combo',
		dataType:'json',
		type:'post',
		data:{cid:id},
		success:function(result)
		{
			new Vue({
				el:'#combo',
				data:{
					cms:result
				},
				methods:{
					sub:function()
					{
						var num = $('.J-cart-quantity').val()
						num = parseInt(num);
						if(num > 1)
						{
							$('.J-cart-quantity').val(num - 1);
						}
					},
					add:function()
					{
						var num = $('.J-cart-quantity').val()
						num = parseInt(num);
						$('.J-cart-quantity').val(num + 1);
					}
				}
			})
		}
	})

	$.ajax({
		url:'/shop/combo',
		dataType:'json',
		type:'post',
		data:{sid:shopId},
		success:function(result)
		{
			new Vue({
				el:'#shop-combo',
				data:{
					cas:result
				}
			})
		}
	})

	$.ajax({
		url:'/combo/content',
		dataType:'json',
		type:'post',
		data:{cid:id},
		success:function(result)
		{
			new Vue({
				el:'#sub-combo',
				data:{
					cname:result[0]["cname"],
					subs:result,
					snum:result.length + 1
				}
			})
		}
	})
    //  美团推荐
	$.ajax({
		url:'/combo/recommend',
		dataType:'json',
		type:'post',
		data:{sid:shopId},
		success:function(result)
		{
			new Vue({
				el:'#recommended',
				data:{
					rss:result
				}
			})
		}
	})

	// 获取商户图片
	$.ajax({
		url:'/combo/shoppic',
		dataType:'json',
		type:'post',
		data:{sid:shopId},
		success:function(result)
		{
			new Vue({
				el:'#anchor-bizinfo',
				data:{
					sname:result[0]["shop_name"],
					pics:result
				}
			})
		}
	})
})