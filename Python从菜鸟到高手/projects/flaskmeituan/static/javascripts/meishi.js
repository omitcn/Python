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

	var allshop = new Vue({
		el:'#shop',
		data:{
			shops:[]
		}
	})
	//  获取美食的分类
	$.ajax({
		url:'/sub_field',
		dataType:'json',
		type:'get',
		success:function(result)
		{
			new Vue({
				el:'#subfields',
				data:{

					subfields:result
				},
				methods:{
				    sub:function(e)
				    {
				    	var subId = parseInt(e.target.getAttribute('data-id'));
						$.ajax({
							url:'/meishi/click',
							dataType:'json',
							type:'post',
							data:{sub_id:subId},
							success:function(result)
							{
								allshop.shops = result
							}
						})				    	
				    }
				}
			})
		}
		,
		error:function(err)
		{
			console.log(err);
		}
	})

	$.ajax({
		url:'/district',
		dataType:'json',
		type:'post',
		success:function(result)
		{
			new Vue({
				el:'#district',
				data:{
					districts:result
				},
				methods:{
					onClick_District:function(e)
					{
				    	var areaId = parseInt(e.target.getAttribute('data-id'));
						$.ajax({
							url:'/district/click',
							dataType:'json',
							type:'post',
							data:{area_id:areaId},
							success:function(result)
							{
								allshop.shops = result
							}
						})				    	

					}
				}
			})  
		}
	})

	$.ajax({
		url:'/meishi/shop',
		dataType:'json',
		type:'post',
		success:function(result)
		{
			allshop.shops = result
		}
	})

	$('.tag-sort').click(function(){
		var sortType = $('.tag-sort').attr('data-id');
        if(sortType == '0')
        {
        	$('.tag-sort').attr('data-id','1');
        	$.ajax({
        		url:'/meishi/up',
        		dataType:'json',
        		type:'post',
        		success:function(result)
        		{
        			allshop.shops = result
        		}
        	})
        	

        }
        else
        {
        	$('.tag-sort').attr('data-id','0');
        	$.ajax({
        		url:'/meishi/down',
        		dataType:'json',
        		type:'post',
        		success:function(result)
        		{
        			allshop.shops = result
        		}
        	})
        }
	})
	
})