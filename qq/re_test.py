'''
@author：KongWeiKun
@file: re_test.py
@time: 17-11-21 下午5:45
@contact: 836242657@qq.com
'''
import re
p='''























	 
		
			
				
			
		
	




	











	

<!DOCTYPE HTML>
<html lang="zh-cn" class="skin-light">
<head>
<noscript><meta http-equiv="refresh" content="0; url=//qzs.qq.com/qzone/v6/troubleshooter/noscript.html" /></noscript>
<meta charset="UTF-8" />
<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
<title>http:// [http://836242657.qzone.qq.com]</title>
<meta name="keywords" content="QQ空间,黄钻,免费装扮,开心农场,QQ农场,QQ牧场" />



	<meta name="description" content="http://photo.store.qq.com/http_imgload.cgi?/rurl2=fdada5" />

<link rel="apple-touch-icon" href="//qzonestyle.gtimg.cn/qzone/v8/index/touch-icon-ipad-retina.png">
<link rel="apple-touch-icon" sizes="76x76" href="//qzonestyle.gtimg.cn/qzone/v8/index/touch-icon-ipad.png">
<link rel="apple-touch-icon" sizes="120x120" href="//qzonestyle.gtimg.cn/qzone/v8/index/touch-icon-iphone-retina.png">
<link rel="apple-touch-icon" sizes="152x152" href="//qzonestyle.gtimg.cn/qzone/v8/index/touch-icon-ipad-retina.png">
<link rel="icon" sizes="any" mask href="//qzonestyle.gtimg.cn/qzone/v8/img/Qzone.svg">
<meta name="theme-color" content="#FFC028">

<script type="text/javascript">
	window.diyitems_1_url = ''
	
		window.g_cdn_proto = 'https:'
	

	
    	var g_domain = "qq.com";
    
    document.domain=g_domain;
    window.g_isFrameWorkTestEnv = "0";
    window.g_point0=Date.now(); 
    var _s_=new Date(),
	g_T={},
	siDomain="qzonestyle.gtimg.cn",
	imgcacheDomain="qzs."+g_domain,
	
	g_iUin=836242657,
	g_iLoginUin=836242657;
	
	

g_T.fwp=[_s_];


//引入配置文件

window.g_dms = {
            'u.qzone.qq.com' : 1,
            'base.s2.qzone.qq.com' : 1,
            'base.s8.qzone.qq.com' : 1,
            'base.qzone.qq.com' : 1,
            'r.qzone.qq.com' : 1,
            'rsh.qzone.qq.com' : 1,
            'ic2.cnc.qzone.qq.com' : 1,
            'ic2.edu.qzone.qq.com':1,
            'ic2.qzone.qq.com':1,
            'ic2.s1.qzone.qq.com':1,
            'ic2.s11.qzone.qq.com' : 1,
            'ic2.s12.qzone.qq.com':1,
            'ic2.s2.qzone.qq.com' : 1,
            'ic2.s21.qzone.qq.com' : 1,
            'ic2.s5.qzone.qq.com':1,
            'ic2.s51.qzone.qq.com':1,
            'ic2.s6.qzone.qq.com':1,
            'ic2.s7.qzone.qq.com':1,
            'ic2.s8.qzone.qq.com' : 1,
            'ic2.qzone.qq.com' : 1,
            'xalist.photo.qzone.qq.com' :1,
            'hzalist.photo.qzone.qq.com' :1,
            'alist.photo.qzone.qq.com' :1,
            'shalist.photo.qzone.qq.com' :1,
            'plist.photo.qzone.qq.com':1,
            'xaplist.photo.qzone.qq.com':1,
            'hzplist.photo.qzone.qq.com':1,
            'gzplist.photo.qzone.qq.com':1,
            'shplist.photo.qzone.qq.com':1,
            'photo.qzone.qq.com':1,
            'xa.photo.qzone.qq.com':1,
            'hz.photo.qzone.qq.com':1,
            'gz.photo.qzone.qq.com':1,
            'shanghai.photo.qzone.qq.com':1,
            'app.photo.qzone.qq.com':1,
            'b.qzone.qq.com':1,
            'b1.cnc.qzone.qq.com':1,
            'b1.edu.qzone.qq.com':1,
            'b1.qzone.qq.com':1,
            'b11.cnc.qzone.qq.com':1,
            'b11.edu.qzone.qq.com':1,
            'b11.qzone.qq.com':1,
            'b1.ctc.qzone.qq.com':1,
            'b11.ctc.qzone.qq.com':1,
            'b.ctc.qzone.qq.com':1,
            'b.edu.qzone.qq.com':1,
            'fav.qzone.qq.com' : 1,
            'sns.qzone.qq.com' : 1,
            'm.qzone.qq.com' : 1,
            'snsapp.qzone.qq.com' : 1,
            'taotao.qzone.qq.com' : 1,
            'w.qzone.qq.com' : 1,
            'g.qzone.qq.com' : 1
        };
 
 
window.g_sdms = {
    'taotao.qq.com' : 1,
    'taotao.qzone.qq.com' : 1,
    'b.qzone.qq.com' : 1,
    'pageapp.qzone.qq.com' : 1,
    'b11.qzone.qq.com' : 1,
    'b1.qzone.qq.com' : 1,
    'br.qzone.qq.com' : 1,
    'm.qzone.qq.com' : 1,
    'base.qzone.qq.com' : 1,
    'w.qzone.qq.com' : 1,
    'g.qzone.qq.com' : 1,
    'r.qzone.qq.com' : 1,
    'ic2.qzone.qq.com' : 1,
    'boss.qzone.qq.com' : 1,
    'mall.qzone.qq.com' : 1,
    'statistic.qzone.qq.com' : 1,
    'fav.qzone.qq.com' : 1,
    'snsapp.qzone.qq.com' : 1,
    'vip.qzone.qq.com' : 1,
    'route.store.qq.com' : 1,
            'drift.qzone.qq.com' : 1,
            'p1.qzone.qq.com' : 1,
            'p2.qzone.qq.com' : 1,
            'xalist.photo.qzone.qq.com' :1,
            'hzalist.photo.qzone.qq.com' :1,
            'alist.photo.qzone.qq.com' :1,
            'shalist.photo.qzone.qq.com' :1,
            'plist.photo.qzone.qq.com':1,
            'xaplist.photo.qzone.qq.com':1,
            'hzplist.photo.qzone.qq.com':1,
            'gzplist.photo.qzone.qq.com':1,
            'shplist.photo.qzone.qq.com':1,
            'photo.qzone.qq.com':1,
            'xa.photo.qzone.qq.com':1,
            'hz.photo.qzone.qq.com':1,
            'gz.photo.qzone.qq.com':1,
            'shanghai.photo.qzone.qq.com':1,
            'tj.photo.qzone.qq.com':1,
            'app.photo.qzone.qq.com':1,
            'memo.qq.com' : 1,
            'analy.qq.com' : 1,
            'analy.qzone.qq.com' : 1,
            'page.qq.com' : 1,
            'rsh.qzone.qq.com' : 1,
            'search.qzone.qq.com' : 1,
            'flower.qzone.qq.com' : 1,
            'sz.ic2.qzone.qq.com' : 1,//通过qqtips到PC空间时，ic2域名统一走深圳
            'up.photo.qq.com' : 1
};

window.g_cgidomain = location.host.replace('.qzone.qq.com','') || 'h5';



    window.g_proto = 'https:';


!function(e){var n,i,t,o={maxBatchReportCount:6,interval:3e3,reportInterface:"//h5.qzone.qq.com/wspeed.qq.com/w.cgi?"},r={},a=navigator.userAgent;navigator.appVersion;if(r.adjustBehaviors=function(){},window.ActiveXObject||window.msIsStaticHTML){if(r.ie=6,(window.XMLHttpRequest||a.indexOf("MSIE 7.0")>-1)&&(r.ie=7),(window.XDomainRequest||a.indexOf("Trident/4.0")>-1)&&(r.ie=8),a.indexOf("Trident/5.0")>-1&&(r.ie=9),a.indexOf("Trident/6.0")>-1&&(r.ie=10),a.indexOf("Trident/7.0")>-1&&(r.ie=11),r.isBeta=navigator.appMinorVersion&&navigator.appMinorVersion.toLowerCase().indexOf("beta")>-1,r.ie<7)try{document.execCommand("BackgroundImageCache",!1,!0)}catch(s){}t=function(e){return function(n,i){var t;return"string"==typeof n?e(n,i):(t=Array.prototype.slice.call(arguments,2),e(function(){n.apply(null,t)},i))}}}else document.getBoxObjectFor||"undefined"!=typeof window.mozInnerScreenX?(n=/(?:Firefox|GranParadiso|Iceweasel|Minefield).(\d+\.\d+)/i,r.firefox=parseFloat((n.exec(a)||n.exec("Firefox/3.3"))[1],10)):navigator.taintEnabled?window.opera?r.opera=parseFloat(window.opera.version(),10):r.ie=6:(i=/AppleWebKit.(\d+\.\d+)/i.exec(a),r.webkit=i?parseFloat(i[1],10):document.evaluate?document.querySelector?525:420:419,(i=/Chrome.(\d+\.\d+)/i.exec(a))||window.chrome?r.chrome=i?parseFloat(i[1],10):"2.0":((i=/Version.(\d+\.\d+)/i.exec(a))||window.safariHandler)&&(r.safari=i?parseFloat(i[1],10):"3.3"),r.air=a.indexOf("AdobeAIR")>-1?1:0,r.isiPod=a.indexOf("iPod")>-1,r.isiPad=a.indexOf("iPad")>-1,r.isiPhone=a.indexOf("iPhone")>-1);(r.macs=a.indexOf("Mac OS X")>-1)||(r.windows=(i=/Windows.+?(\d+\.\d+)/i.exec(a),i&&parseFloat(i[1],10)),r.linux=a.indexOf("Linux")>-1,r.android=a.indexOf("Android")>-1),r.iOS=a.indexOf("iPhone OS")>-1,!r.iOS&&(i=/OS (\d+(?:_\d+)*) like Mac OS X/i.exec(a),r.iOS=!(!i||!i[1]));var d=function(){var e=[],n=!1,i=new Image;return i.onload=i.onerror=function(){n=!1,e.length&&(n=!0,i.src=e.shift())},function(t){e.push(t),n||(n=!0,i.src=e.shift())}}(),c=function(e){return null===e?"null":void 0===e?"undefined":Object.prototype.toString.call(e).slice(8,-1).toLowerCase()},u=function(e){e.indexOf("://")<1&&(e=location.protocol+"//"+location.host+(0==e.indexOf("/")?"":location.pathname.substr(0,location.pathname.lastIndexOf("/")+1))+e);var n=e.split("://");if("array"==c(n)&&n.length>1&&/^[a-zA-Z]+$/.test(n[0])){this.protocol=n[0].toLowerCase();var i=n[1].split("/");if("array"==c(i)){this.host=i[0],this.pathname="/"+i.slice(1).join("/").replace(/(\?|\#).+/i,""),this.href=e;var t=n[1].lastIndexOf("?"),o=n[1].lastIndexOf("#");return this.search=t>=0?n[1].substring(t):"",this.hash=o>=0?n[1].substring(o):"",this.search.length>0&&this.hash.length>0&&(o<t?this.search="":this.search=n[1].substring(t,o)),this}return null}return null},f=[],l=function(){var e="unknown";return e="",e=r.windows?"window_"+r.windows:r.macs?"macos_"+r.macs:r.isiPad?"ipad":"unknown_os",e+=r.chrome?"_chrome_"+r.chrome:r.ie?"_ie_"+r.ie:r.firefox?"_ff_"+r.firefox:"_unknown_br"},h=function(e){e.frequency||(0===e.resultcode?e.frequency=20:e.frequency=1);var n={appid:e.appid||"1000372",releaseversion:l(),stime:e.stime||11e3,commandid:e.commandid||"",apn:"wifi",resultcode:e.resultcode||0,touin:window.g_iLoginUin||"0",frequency:e.frequency||1,r:Math.random()};n.frequency>1&&Math.random()*n.frequency>1||(n.commandid=m(n.commandid),f.push(n),x())},p=function(e){return/^(?:ht|f)tp(?:s)?\:\/\/(?:[\w\-\.]+)\.\w+/i.test(e)},m=function(e){if(!e)return"";if(!p(e))return e;var n=u(e),i=(n.host||"unknown").replace(".qzone.qq.com","/p").replace(".qq.com","/q").replace("qzonestyle.gtimg.cn","cdn").replace("qzs.qq.com","cdn"),t=n.pathname.split("/");return i+"/"+t[t.length-1]},w=function(){var e,n=[];if(!f.length)return"";var i=0;for(n.push("key=appid,releaseversion,stime,commandid,resultcode,touin,frequency");(e=f.shift())&&(n.push(i+1+"_1="+e.appid),n.push(i+1+"_2="+e.releaseversion),n.push(i+1+"_3="+e.stime),n.push(i+1+"_4="+e.commandid),n.push(i+1+"_5="+e.resultcode),n.push(i+1+"_6="+e.touin),n.push(i+1+"_7="+e.frequency),i++,!(i>=h.maxBatchReportCount)););return n.join("&")},x=function(){if(1!=h._isSending){h._isSending=!0;var e=o.reportInterface;setTimeout(function(){var n=w();n&&n.length&&d(e+n),h._isSending=!1,f.length&&x()},o.interval)}};h.getVersion=l,window.haboStat=h}(window);

(function() {
        var reportNum = 0;
        var beforeLoad = 1;
        var needReport = window.g_iLoginUin%100 == 43;

		var getReportResult = function(){
			var result;
            var pathName = location.pathname;
                
            if(!pathName){
            	pathName = '/'
			}
		
            var frags = pathName.split('/');
            var appid = window.g_app_identifier.toLowerCase();
            if(window.g_isDirectApp){
                if(appid == 'mood' || appid=='311' || appid=='photo' || appid=='4' || appid=='share' || appid=='202' || appid=='blog' || appid=='2'){//说说和相册的appid有点特别，要修正一下
                    if(frags[1]==appid){
                        frags[2] && (frags[2] ='num')
					}else if(frags[2]==appid){
                        frags[3] && (frags[3] = 'num')
                        frags[4] && (frags[4] = 'num')

                    }else{
						frags[4] && (frags[4] = 'num')
                        frags[5] && (frags[5] = 'num')
					}
                }
            }
            if(frags && frags.length>0){
                pathName = frags.join('/');
            }
			result = (location.host + pathName).replace(/\d{5,30}/,'num').replace(/\/+$/ig,'');
			return result;
		};

        var onErrorOcurred = function(event) {
            if(needReport && reportNum == 0) {
                reportNum = 1;
                
                var result = getReportResult();

                // 堆栈信息
                var errorObj = event.error || {};
                var stack = errorObj.stack || '';

                var xhr = new XMLHttpRequest();
                xhr.withCredentials = true;
				var url = '//h5.qzone.qq.com/log/post/error/' + result+'?from=pcqzone&qua='+window.haboStat.getVersion();
                xhr.open('post', url, true);
                xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                var errMsg = event.message + ";url:" + location.href + "\n stack: " + stack + ";";
                errMsg += "scriptURI:" + event.filename + ";";
                errMsg += "lineNumber:" + event.lineno + ";";
                errMsg += "columnNumber:" + event.colno + ";";
                errMsg += "beforeLoad:" + beforeLoad + ";";
                xhr.send(errMsg);
            }
        };

        var onWindowLoaded = function(evt){
            
            beforeLoad = 0;
            // reportNum为0（即成功）才上报，失败上报会在上报错误时在Node端过滤后上报
            // 先灰度下
             needReport && !reportNum && window.haboStat && window.haboStat({
				appid	: 1000416,
				commandid : getReportResult(),
                stime : 1000, 
                resultcode : 0, //这里只上报成功
                touin : window.g_iLoginUin || 0,
                frequency :  1
            });
        
        }

        if(window.addEventListener){
             window.addEventListener('error', function(e){
                onErrorOcurred(e);
                });
             window.listenError = true;
            window.addEventListener('load', function(e){
                onWindowLoaded(e);
            });
        }else if(window.attachEvent){
            window.attachEvent('onerror', function(e){
                onErrorOcurred(e);
            })
            window.listenError = true;
            window.attachEvent('onload', function(e){
                onWindowLoaded(e);
            });
        }
       
        
}());




document.namespaces&&document.namespaces.add&&(document.namespaces.add('qz', location.protocol + '//qzone.qq.com/'),document.namespaces.add('x', location.protocol+'//qzone.qq.com/'));

	var QZFL={},
		QZFF_M_img_ribr=[];
	QZFL.event={
		getEvent : function(evt){
			var evt=window.event||evt,c,cnt;
			if(!evt&&window.Event){
				c=arguments.callee;
				cnt=0;
				while(c){
					if((evt=c.arguments[0])&&typeof(evt.srcElement)!="undefined"){
						break;
					}else if(cnt>9){
						break;
					}
					c=c.caller;
					++cnt;
				}
			}
			return evt;
		},
		getTarget : function(evt){
			var e=QZFL.event.getEvent(evt);
			if(e){
				return e.srcElement||e.target;
			}
			return null;
		}
	};
	QZFL.object = {
		getType: function(o){return o === null ? 'null' : (o === undefined ? 'undefined' : Object.prototype.toString.call(o).slice(8,-1).toLowerCase());}
	};
	QZFL.media={
		reduceImgByRule:function(ew,eh,opts,cb){
			QZFF_M_img_ribr.push(QZFL.event.getTarget());
		},
		adjustImageSize:function(w,h,s,cb,ecb){
			var op = {trueSrc:s,callback:function(o, type, ew, eh, p){(QZFL.object.getType(cb) == "function") && cb(o, ew, eh, null, p.ow, p.oh,p);},errCallback:ecb};
			QZFL.media.reduceImage(0, w, h, op);
		},
		reduceImage:function(type, ew, eh, opts){
			var rd = function(o, t, ew, eh, p, cb){
				var rl, k;
				if(p.rate==1){
					p.direction[0] = ( ew>eh ? 'height' : 'width');
					p.direction[1] = ( ew>eh ? 'width' : 'height');
				}
				rl = ( p.direction[t] == "width" ? ew : eh );
				t ? ( ( ( rl>p.shortSize ) ? ( rl = p.shortSize ) : 1 ) && ( p.k = p.shortSize/rl ) ) : ( ( ( rl>p.longSize ) ? ( rl = p.longSize ) : 1 ) && ( p.k = p.longSize/rl ) );
				o.setAttribute(p.direction[t],rl);
				(QZFL.object.getType(cb) == "function") && cb(o, t, ew, eh, p);
			};
			opts = opts || {};
			opts.img = (opts.img && (typeof(opts.img.nodeName) != 'undefined' || typeof(opts.img.nodeType) != 'undefined')  ? opts.img : QZFL.event.getTarget());
			opts.img.onload=null;
			opts.trueSrc && (opts.img.src = opts.trueSrc);
			if(opts.img){
				if( ! ( opts.direction && opts.rate && opts.longSize && opts.shortSize ) ){
					r = QZFL.media.getImageInfo(function(o,p){
						if(!o||!p){
							return;
						}
						rd(opts.img, type, ew, eh, p, opts.callback)
					},opts);
				}else{
					rd(opts.img, type, ew, eh, opts, opts.callback)
				}
			}
		},
		getImageInfo:function(callback, opts){
			var gif = function(img,cb,opts){
				if(img){
					var _w = opts.ow || img.width, _h = opts.oh || img.height, r,ls,ss,d;
					if(_w && _h){
						if(_w >=_h){
							ls = _w;
							ss = _h;
							d = ["width","height"];
						}else{
							ls = _h;
							ss = _w;
							d = ["height","width"];
						}
						r = {
							direction:d,
							rate : ls/ ss,
							longSize :ls,
							shortSize :ss
						};
						r.ow = _w;
						r.oh = _h;
					}
					(QZFL.object.getType(cb) == "function") && cb(img,r,opts);
				}
			};
			opts = opts || {};
			if(QZFL.object.getType(opts.trueSrc)== "string"){
				var _i = new Image();
				_i.onload = (function(ele, cb, p){
					return function(){
						gif( ele, cb, p );
						ele = ele.onerror =  ele.onload = null;
					};
				})(_i, callback, opts);

				_i.onerror =  (function(ele, cb, p){
					return function(){
						if (typeof(p.errCallback) == 'function') {
							p.errCallback();
						}
						ele = ele.onerror =  ele.onload = null;
					};
				})(_i, callback, opts);

				_i.src = opts.trueSrc;
			}else if(opts.img && opts.img.nodeType == 1){
				gif(opts.img, callback, opts );
			}
		}
	};


	function restXHTML(s){
		return s.replace(/&amp;|&lt;|&gt;|&apos;|&#0?39;|&quot;/g,function(a){
			switch (a){
				case "&amp;":return "&";
				case "&lt;":return"<";
				case "&gt;":return ">";
				case "&apos;":
				case "&#39;":
				case "&#039;":return "\x27";
				case "&quot;":return "\x22";
			}
		});
	}


	




window.g_isGrayRelease = true;




</script>

	
	<link href="//qzonestyle.gtimg.cn/aoi/skin/2.css?max_age=19830212&d=20160530165317" rel="stylesheet"/>
<link href="//qzonestyle.gtimg.cn/aoi/icenter-171109154112.css?max_age=31536000" rel="stylesheet"/>
<link href="//qzonestyle.gtimg.cn/aoi/icenter-poster-comment-170109104014.css?max_age=31536000" rel="stylesheet"/>







	
		<style id="mainJSBg" type="text/css">
				
			.background-container{
				background-repeat:no-repeat;
				
				background-position:center top;
				
				background-attachment:scroll;
				
				background-image:url(//i.gtimg.cn/qzone/space_item/orig/3/72019_top.jpg);
			}
			
			
				
				.bg-body{
					background-image:url(//i.gtimg.cn/qzone/space_item/orig/3/72019_bg.jpg); background-repeat:repeat;}
			
			
			
		</style>
	



<style id="mainJSTitleBar" type="text/css">
	.layout-head-inner {
		height:190px;
		
		
		
		}
</style>





<style type="text/css">

</style>
<style type="text/css" id="dynamicStyle">
.ownermode{display:;}
.clientmode{display:none;}
.editmode{display:none;}
.customoff{display:;}
.alphamode{display:none;}
</style>






<link rel="alternate" type="application/rss+xml" title="RSS news feed" href="http://feeds.qzone.qq.com/cgi-bin/cgi_rss_out?uin=836242657" />



	<link rel="Shortcut Icon" href="//qzonestyle.gtimg.cn/aoi/img/logo/favicon.ico?max_age=31536000" type="image/x-icon" />



	<!--[if IE]><base href="//qzs.qq.com/"></base><![endif]-->
	<!--[if !(IE)]><!--><base href="//qzs.qq.com/" /><!--<![endif]-->




<!--[if IE]>
<script type="text/javascript">
    function toAbsURL(s) { 
     var l = location, h, p, f, i; 
     if (/^\w+:/.test(s)) { 
       return s; 
     } 
     h = l.protocol + '//' + l.host + (l.port!=''?(':' + l.port):''); 
     if (s.indexOf('/') == 0) { 
       return h + s; 
     } 
     p = l.pathname.replace(/\/[^\/]*$/, ''); 
     f = s.match(/\.\.\//g); 
     if (f) { 
       s = s.substring(f.length * 3); 
       for (i = f.length; i--;) { 
         p = p.substring(0, p.lastIndexOf('/')); 
       } 
     } 
     return h + p + '/' + s; 
   }


    var base = document.getElementsByTagName('base')[0];
    base.href = toAbsURL(base.href);
</script>
<![endif]-->
</head>

<script type="text/javascript">
    if(window.g_iLoginUin % 10 == 3) {
        var ua = navigator.userAgent || '';
        var uinArray = /uin=o0*(\S+);/.exec(document.cookie || '');
        var pathArray = /^\/[^\/]+?\/[^\/]+/.exec(location.pathname || '');

        var qua = '',
            apn = 'WIFI',
            uin = uinArray && uinArray[1];;

        var collector = [],
            collectorTime = 2000,//2000ms时间间隔内的请求合并上报
            collectorTimer;
        window.reportHaboGlobal = function(code, appid, command) {
            command = command || '';
            if (command[0] === '/') {
                command = 'hybrid' + command + (pathArray && pathArray[0]);;
            }

            var data = {
                releaseversion: qua,
                apn: apn,
                touin: uin,
                key: 'appid,commandid,resultcode'
            };
            collector.push([appid || '1000361', command, code]);
            var url = location.protocol === 'https:' ? 'https://h5.qzone.qq.com/wspeed.qq.com/w.cgi' : 'http://wspeed.qq.com/w.cgi';

            collectorTimer && clearTimeout(collectorTimer);
            collectorTimer = setTimeout(report, collectorTime);
            function report() {
                var params = [];
                for (var key in data) {
                    if (data.hasOwnProperty(key)) {
                        params.push(key + '=' + encodeURIComponent(data[key]));
                    }
                }
                if (collector && collector.length) {
                    var i = 0;
                    while (collector.length) {
                        if (params.join('&').length > 1000) {
                            break;
                        }
                        var c = collector.shift();
                        params.push([i + 1, 1].join('_') + '=' + c[0]);
                        params.push([i + 1, 2].join('_') + '=' + c[1]);
                        params.push([i + 1, 3].join('_') + '=' + c[2]);
                        i++;
                    }
                }
                params.push('rv=' + Math.random());
                new Image().src = url + '?' + params.join('&');
                i > 0 && collector.length && setTimeout(report, 1000);
            }
        };
        var toUrlParam = function(data) {
            var arr = [];
            for (var key in data) {
                if (data.hasOwnProperty(key)) {
                    if(data[key] !== '' && data[key] !== undefined) {
                        arr.push(encodeURIComponent(key) + '=' + encodeURIComponent(data[key]));
                    }
                }
            }
            return arr.join('&');
        };
        var send = function(data, callback, onTimeout) {
            try {
                onTimeout && setTimeout(function() {
                    callback = null;
                    onTimeout && onTimeout();
                }, 3000);
                data = toUrlParam(data);
                var url = '//h5.qzone.qq.com/log/post/script/error/' + command;
                var xhr = window.XMLHttpRequest ? new XMLHttpRequest() : {};
                if ('withCredentials' in xhr) {
                    xhr.open('post', url, true);
                    xhr.withCredentials = true;
                    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                    xhr.onreadystatechange = function(){
                        if (xhr.readyState == 4 && xhr.status == 200) {
                            var o = JSON.parse(xhr.responseText);
                            onTimeout = null;
                            callback && callback(o);
                        }
                    };
                    try{xhr.send(data);}catch(e){};
                } else if ('XDomainRequest' in window) {
                    var xdr = new XDomainRequest();
                    xdr.open('post', url);
                    xdr.onload = function() {
                        var o;
                        window.JSON ? (o = JSON.parse(xdr.responseText)) : eval('o = ' + xdr.responseText);
                        onTimeout = null;
                        callback && callback(o);
                    };
                    setTimeout(function() {
                        try{xdr.send(data);}catch(e){};
                    }, 0);
                }
            } catch(e) {}
        };

        var appid = '1000416',
            maxJsErrorCount = parseInt(''),
            maxJsErrorCount = isNaN(maxJsErrorCount) ? 5 : maxJsErrorCount,
            jsErrorCount = 0,
            command = 'hybrid/pcweb',
            reportHabo = 1,
            queue = [],
            isReporting = false,
            hasReportPv = false;
        var report = function() {
            var data = queue.shift();
            if (!data) {
                isReporting = false;
                return;
            }
            isReporting = true;
            data.reportHabo = reportHabo;
            reportHabo = 0;
            send(data, function(o) {
                if (o && o.code == 0 && o.data && o.data.result != 1) {
                    reportHabo = data.reportHabo;
                }
                setTimeout(report, 1000);
            }, function() {
                report();
            });
        };
        window.reportJsError = function(data) {
            reportPv();
            if (jsErrorCount++ >= maxJsErrorCount) {return;}
            queue.push(data);
            !isReporting && report();
        };
        var filterError = function(data) {
            if(data.scriptUrl.indexOf('main_page_cgi') > -1 || data.scriptUrl.indexOf('cgi_emotion_list.fcg') > -1) {
                return true;
            }

            return false;
        };
        var onError = function(event) {
            var data = {
                appid: appid,
                error: event.message,
                stack: event.error && event.error.stack || '',
                url: location.href,
                scriptUrl: event.filename,
                lineNumber: event.lineno,
                columnNumber: event.colno
            };
            var fn = window.beforeJsErrorReport;
            if (typeof fn === 'function' && false === fn(data)) {
                return;
            }
            if(filterError(data)) {
                return;
            }
            window.reportJsError(data);
        };
        var reportPv = function() {
            if (hasReportPv) {return;}
            window.reportHaboGlobal && reportHaboGlobal(0, appid, command);
            hasReportPv = true;
        };

        if (window.addEventListener) {
            window.addEventListener('error', onError);
        } else if (window.attachEvent) {
            window.attachEvent('onerror', onError);
        } else {
            window.onerror = onError;
        }
    }
</script>


     
    <body  class="os-mac bg-body  date-20171123">

<div style="position:absolute;top:-200px;">
    <a href="http://rc.qzone.qq.com/im?visitor=blind" tabindex="1" class="blind" accesskey="o">用读屏软件的朋友从这里进入QQ空间读屏版</a>
    <a href="http://qzs.qq.com/qzone/v6/accessibility/help.html" tabindex="2" accesskey="0">QQ空间无障碍使用帮助，请点击这里</a>
    <a href="http://support.qq.com/write.shtml?fid=811" tabindex="3" target="_blank">使用QQ空间遇到问题，点击这里反馈</a>
    <a href="//user.qzone.qq.com/836242657#pageContent" tabindex="4" accesskey="8">跳到内容区</a>
</div>
<div class="layout-invisible">
    <span id="trs_tip" style="background-color:#FFF2D1;padding:10px;">如果您看到这个提示，说明QQ空间无法正常打开，请尝试<a href="//user.qzone.qq.com/troubleshooter#style" title="空间小助手"><strong>使用空间小助手修复</strong></a></span>
</div>













<div class="top-fix-bar">
	<div class="top-fix-inner" >
        <div class="top-fix-container" id="QZ_Toolbar_Container">
            <div class="top-fix-wrap">
                
                <a class="logo" href="//qzone.qq.com/" title="QQ空间">QQ空间</a>
                
                <ul class="top-nav">
                    <li class="nav-list" id="tb_ic_li">
                        <div class="nav-list-inner">
                            <a id="aIcenter" class="nav-hover" href="//user.qzone.qq.com/836242657/infocenter?via=toolbar" accesskey="1"><i class="ui-icon icon-icenter"></i><span>个人中心</span></a>
                        </div>
                    </li>
                    <li class="nav-list" id="tb_index_li">
                        <div class="nav-list-inner">
                            <a id="aMainPage" href="//user.qzone.qq.com/836242657/main" class="homepage-link a-link " accesskey="z"><i class="ui-icon icon-homepage"></i><span>我的主页</span><i class="drop-down-arrow"></i></a>
                        </div>
                        
                        <div class="nav-drop-down" id="tb_menu_panel" style="display:none;">
                            <div class="side-area">
                                <div class="homepage-link">
                                    <a class="link-icon" href="//user.qzone.qq.com/836242657/main"><i class="icon-homepage"></i></a>
                                    <a class="link-text" href="//user.qzone.qq.com/836242657/main">主页</a>
                                </div>
                            </div>
                            <div class="main-area">
                                <div class="main-application">
                                    <ul class="main-application-list clearfix" id="tb_menu_list">
                                        <li class="menu_item_2">
                                            <a href="javascript:;"><i class="icon-blog"></i></a>
                                            <a class="app-name">日志</a>
                                        </li>
                                        <li class="menu_item_4">
                                            <a  href="javascript:;"><i class="icon-album"></i></a>
                                            <a class="app-name">相册</a>
                                        </li>
                                        <li class="menu_item_311">
                                            <a  href="javascript:;"><i class="icon-say"></i></a>
                                            <a class="app-name">说说</a>
                                        </li>
                                        <li class="menu_item_202">
                                            <a  href="javascript:;"><i class="icon-share"></i></a>
                                            <a class="app-name">分享</a>
                                        </li>
                                        <li class="menu_item_847">
                                            <a  href="javascript:;"><i class="icon-video"></i></a>
                                            <a class="app-name">视频</a>
                                        </li>
                                        <li class="menu_item_305">
                                            <a  href="javascript:;"><i class="icon-music"></i></a>
                                            <a class="app-name">音乐</a>
                                        </li>
                                        <li class="menu_item_334">
                                            <a  href="javascript:;"><i class="icon-message-book"></i></a>
                                            <a class="app-name">留言板</a>
                                        </li>
                                        <li class="menu_item_1">
                                            <a  href="javascript:;"><i class="icon-personal"></i></a>
                                            <a class="app-name">个人档</a>
                                        </li>
                                         <li class="menu_item_907">
                                             <a  href="javascript:;"><i class="icon-collect"></i></a>
                                             <a class="app-name">收藏</a>
                                         </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </li>

					<li class="nav-list" id="tb_friend_li">
						<div class="nav-list-inner">
							<a  id="aMyFriends" href="//user.qzone.qq.com/836242657/myhome/friends/index" class="friends-link a-link"><i class="ui-icon icon-friend"></i><span>好友</span><i class="drop-down-arrow"></i></a>
						</div>
						
						<div class="nav-drop-down friends-drop-down" id="friends-drop-down" style="display: none;">
							<div class="side-area">
								<div class="friends-link">
									<a href="javascript:" class="link-icon"><i class="icon-friends"></i></a>
									<a href="javascript:" class="link-text">寻找好友</a>
								</div>

								<div class="friends-relation">
									<a href="javascript:" class="link-icon"><i class="icon-relation"></i></a>
									<a href="javascript:" class="link-text">亲密度</a>
								</div>

								
							</div>
							<div class="main-area">        
								<div class="mod-friends-topbar">
									<div class="inner">
										<div class="hd">
											<h3>最近联络的好友</h3>
											<div class="friends-search-topbar ">
												<input type="text" placeholder="搜索好友" id="friend_search_input"><button><i class="ui-icon sp-top-search"></i></button>
											</div>
											
											<div class="friends-results-topbar" style="display:none">
												<ul class="results-list-topbar qz-scrollbar" id="search_friend_result"></ul>
												<p class="null" style="display:none">没有找到相关用户</p>
											</div>
										</div>
										<div class="bd">
											<ul class="friends-list-topbar clearfix" id="friends-list-topbar"></ul>
										</div>
										<div class="ft"></div>
									</div>
								</div>
							</div>
						</div>
					</li>


                    <li class="nav-list" id="tb_app_li">
                        <div class="nav-list-inner">
                            <a id="aAppstore" href="//user.qzone.qq.com/836242657/appstore" class="application-link a-link"><i class="ui-icon icon-application"></i><span>游戏</span><i class="drop-down-arrow"></i></a>
                        </div>
                        
                        <div class="nav-drop-down application-drop-down" id="tb_app_wall" style="display:none;">
                            <div class="side-area">
                                <div class="application-shop">
                                    <a class="link-icon" href="//user.qzone.qq.com/836242657/apppoints?via=QZ.APPWALL.APPCENTER"><i class="icon-shop"></i></a>
                                    <a class="link-text" href="//user.qzone.qq.com/836242657/apppoints?via=QZ.APPWALL.APPCENTER">积分商城</a>
                                </div>
                            </div>
                            <div class="main-area">
                                <div class="main-application">
                                    <ul id="tb_recent_app_list" class="main-application-list clearfix"></ul>
                                </div>
                                <div class="publicity-msg" style="display: none;">
                                    <a id="tb_qboss_text_ad" href="javascript:;" target="_blank"></a>
                                </div>
                            </div>
                        </div>
                    </li>
					
                    <li class="nav-list" id="tb_dress_li">
                        <div class="nav-list-inner">
                            <a  id="aMall" class="dress-up-link a-link" href="//rc.qzone.qq.com/onekeydressup"><i class="ui-icon icon-dress-up"></i><span>装扮</span><i class="drop-down-arrow"></i></a>
                        </div>
                        
                        <div class="nav-drop-down dress-drop-down" id="tb_dress_panel" style="display:none;"></div>
                    </li>
					
                </ul>

                
                <div class="user-info">
                    <a class="user-home" href="//user.qzone.qq.com/836242657/main">
                        <img class="user-avatar" src="//qlogo2.store.qq.com/qzone/836242657/836242657/30?1372472103" alt="您的头像">
                        <span class="user-name textoverflow">K.</span>
                    </a>
					<a id="tb_logout" class="logout-new" href="javascript:;" title="退出"><i class="ui-icon icon-logout"></i></a>                    
                    <div id="tb_setting_li" class="user-setting">
                        <i id="tb_setting_i" class="drop-down-arrow"></i>
                        <div class="user-drop-down" id="tb_setting_panel" style="display:none;">
                            <b class="white-line"></b>
                            <div class="drop-down-setting">
                                <a type="info" href="javascript:;">修改资料</a>
                                <a type="dress" href="javascript:;">主页排版</a>
                                <a type="set" href="javascript:;">空间设置</a>
                                <a type="auth" href="javascript:;">权限设置</a>
                            </div>
                            
			                     <a target="_blank" class="online-service" href="http://service.qq.com/special_auto/qzone.html" id="aHelpCenter">帮助中心</a>
                            
                            <a href="http://support.qq.com/discuss/46_1.shtml" target="_blank" title="意见反馈">意见反馈</a>
                            <a href="http://guanjia.qq.com/user/?ADTAG=media.outenter.qzone" target="_blank" title="安全防护" id="securityDefence" onclick="TCISD && TCISD.hotClick('toolbar.houseKeeper', 'user.qzone.qq.com')">安全防护</a>
                        </div>
                    </div>
                    <a href="http://pay.qq.com/ipay/index.shtml?c=xxjzgw,xxjzghh&amp;ch=self&amp;aid=zone.tbarshuang" id="tb_vip_li" target="_blank" class="vip-setting" ><i class="ui-icon icon-vip"></i></a>
				</div>

                
                <!-- 顶部搜索框 默认放出 2014-04-22 markqin -->
                <div class="top-search">
                    <div class="search-box">
                        <input class="search-input" type="text" placeholder="用户/游戏/动态"><!--搜索框默认态-->
                        <a href="javascript:;" class="search-button"><i class="ui-icon icon-search"></i></a>
                    </div>
                    <div class="search-drop-down" id="search_smart_panel_navigation_bar" style="display:none">
                        <div id="search_smart_search_loading" class="waiting-box" style="display:none">
                            <img src="//qzonestyle.gtimg.cn/aoi/img/loading2.gif" alt="等待图标" />
                        </div>
                        <div id="search_smart_search_list">
                            <div class="result-box r-modle j-default-result-list" style="display:none">
                                <a href="//user.qzone.qq.com/UIN/infocenter?qz_referrer=special&clickReport=searchSpecial" class="result-list">
                                    <div class="avatar"><i class="ui-icon icon-ts-special"></i></div>
                                    <div class="result-details">
                                        <p class="info">特别关心</p>
                                    </div>
                                </a>
                                <a href="//user.qzone.qq.com/UIN/myhome/friends/ofpmd?clickReport=searchMaybeKnow" class="result-list">
                                    <div class="avatar"><i class="ui-icon icon-ts-qq"></i></div>
                                    <div class="result-details">
                                        <p class="info">可能认识的人</p>
                                    </div>
                                </a>
                                <a href="//user.qzone.qq.com/UIN/myhome/217?clickReport=searchAuthenQzone" class="result-list">
                                    <div class="avatar"><i class="ui-icon icon-ts-approve"></i></div>
                                    <div class="result-details">
                                        <p class="info">认证空间</p>
                                    </div>
                                </a>
                                <a href="//rc.qzone.qq.com/appstore?via=qzonesearchbar&clickReport=searchApp" class="result-list">
                                    <div class="avatar"><i class="ui-icon icon-ts-app"></i></div>
                                    <div class="result-details">
                                        <p class="info">游戏应用</p>
                                    </div>
                                </a>
                            </div>
                            <div class="smart-result-list" style="display:none"></div>
                        </div>
                        <a id="search_smart_search_more" class="search-for-friends" style="display:none" href="javascript:;">
                            <span>查看更多</span><i class="more-icon"></i>
                        </a>
                    </div>
                </div>

                
                <div class="music-container" id="tb_music_li">
                    <div class="music-panel">
                        <a class="music-play" href="javascript:;"><i class="ui-icon ico-music-stop"></i></a>
                        <b class="music-dynamic"><i class="ui-icon ico-music-dynamic"></i></b>
                    </div>
                    
                    <div id="tb_music_panel" class="music-drop-down" style="display:none;">
                        <div class="drop-down-container">
                            <div class="background-music">
                                <i class="icon-qq-music"></i>
                                <b>我的背景音乐</b>
                                <div class="setting-box">
                                    <a href="javascript:;" class="music-setting">设置</a>
                                </div>
                            </div>
                            <div class="music-list">
                                <div class="music-scroll-container">
                                    <div style="top:0" class="music-choose">
                                    </div>
                                </div>
                                <b class="scroll-bar-container">
                                    <b style="top:0" class="scroll-bar"></b>
                                </b>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="vip-drop-down" id="tb_vip_panel" style="display:none;">
                    <b class="white-line"></b>
                    <div class="drop-down-setting">
                        
						<a id="aPayBySelf" href="http://pay.qq.com/ipay/index.shtml?c=xxjzgw,xxjzghh&amp;ch=self&amp;aid=zone.tbarshuang" target="_blank">开通黄钻</a>
						<a id="aPayByYear" href="http://pay.qq.com/ipay/index.shtml?c=xxjzgw,xxjzghh&amp;ch=self&aid=zone.tbarshuangnf&paytime=year" target="_blank">开年费黄钻</a>
                        

                        <a id="aPayByFriend" href="javascript:;">向好友索取</a>
                        <a id="aPayToFriend" target="_blank" href="http://pay.qq.com/ipay/index.shtml?c=xxjzgw,xxjzghh&amp;ch=send&aid=zone.tbar.send&ADTAG=pay.service.qzone.send&u=0">赠送给好友</a>
                        <a id="aVipHome" target="_blank" href="http://vip.qzone.com/?login=qq">黄钻官网</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="background-container" id="layBackground">
    
    
    
    <div class="layout-head ">
        <div class="layout-head-inner" id="headContainer">
            
            <div class="head-info">
                <h1 class="head-title" id="top_head_title"><span class="title-text ui-mr5">http://</span>
                    
<a href="javascript:;" 
	id="qz-head-level" 
	class="qz-level-flag" 
	onclick="window.QZONE && QZONE.FP.toApp('/qzscore');window.TCISD &amp;&amp; window.TCISD.hotClick('point_ic_image', 'flower.qzone.qq.com');return false;" 
	href="javascript:;"
>
	<span 
		class="qz_qzone_lv qz_qzone_lv_3 qz_qzone_no_2" 
		title="当前空间等级：25级；积分：3330分" 
	><span class="no"><b class="d2"></b><b class="d5"></b></span></span>
</a>


                     
                        <span class="qz-app-flag wing-fly"><i class="ui-icon icon-qzphone"></i></span>  
                     
                </h1>
                <div class="head-description">
                    <span class="description-text" id="QZ_Space_Desc">http://photo.store.qq.com/http_imgload.cgi?/rurl2=fdada5</span>
                </div>
            </div>
            <div class="head-detail">
                <div class="head-detail-name">
                    <span class="user-name textoverflow">K.</span>
                    
                    
                    
                     
                            <span class="user-vip-info">
                                
                                
                                
                            </span>
                     
                </div>
                












    
    <div class="head-detail-info clearfix"><!-- 未开通黄钻的用户成长信息不可见 -->
        <div class="detail-info-level">
            <a id="diamon" data-year="" data-super="0" class="f_user_vip qz_ichotclick " target="_blank" href="http://pay.qq.com/ipay/index.shtml?n=12&c=xxjzgw,xxjzghh&aid=info.nickname&ch=qdqb,kj" style="cursor:pointer;">
            <i class="qz_vip_icon_l qz_vip_icon_l_gray_1"></i></a>
        </div>
        <div class="detail-info-con">
           

            
                <div class="qz-progress-bar  qz-progress-bar-gray">
                    <div class="progress-bar-info">
                        <span class="txt-value">成长值<b class="count">1</b></span><span class="txt-speed">成长速度<b class="count">-10点/天</b></span>
                    </div>
                    <div class="progress-bar-panel">
                        
                        
                        <div class="progress-bar-count" style="width:0%"><span class="count">0%</span></div>
                    </div>
                </div>
            
            
        </div>
        


<div class="user-vip-info">
    
        
            
                <a class="qz-btn-vip qz-btn-vip-fee" title="续费黄钻" href="http://pay.qq.com/ipay/index.shtml?n=3&c=xxjzgw,xxjzghh&aid=info.nickname&ch=qdqb,kj" target="_blank"></a>
            
        
    

    
     
    
</div>
    </div>

            </div>
            
            <!--挂件-->
            <div class="layout-shop-item" id="QZ_Shop_Items_Container">
                







	
		
			
		
	


	
		
	






	
		
	



	








	
		
		
		
		
			
			
			
			
			
			<div class="shop-item" id="menuContainer" style="width: px; height: 32px; left: 150px; top: 192px; "><div class="head-nav"><ul class="head-nav-menu"><li class="menu_item_N1"><span class="arr"></span><a href="javascript:;" title="主页" tabindex="1" accesskey="z">主页</a></li><li class="menu_item_2"><span class="arr"></span><a href="javascript:;" title="日志" tabindex="1" accesskey="r">日志</a></li><li class="menu_item_4"><span class="arr"></span><a href="javascript:;" title="相册" tabindex="1" accesskey="4">相册</a></li><li class="menu_item_334"><span class="arr"></span><a href="javascript:;" title="留言板" tabindex="1">留言板</a></li><li class="menu_item_311"><span class="arr"></span><a href="javascript:;" title="说说" tabindex="1" accesskey="6">说说</a></li><li class="menu_item_1"><span class="arr"></span><a href="javascript:;" title="个人档" tabindex="1" accesskey="1">个人档</a></li><li class="menu_item_305"><span class="arr"></span><a href="javascript:;" title="音乐" tabindex="1">音乐</a></li><li class="menu_item_more"><span class="arr"></span><a href="javascript:;" title="更多" tabindex="1">更多</a></li></ul></div></div>
		
	


            </div>
            

    <div class="actions profile-hd-actions" id="like_button_pannel">
        
            
            
        

        

        

        <span class="btn-head btn-head-like">
            <a href="javascript:;" class="lnk-left" id="view_like_list" title="0">
                <s class="ui-icon sp-btn-like"></s>
                <span class="txt good-num">0</span>
                <span class="txt message-num none"></span>
            </a>
        </span>
    </div>

        </div>
    </div>

    <div class="layout-nav">
        <div class="layout-nav-inner">
            <div class="head-avatar">
                <a id="QM_OwnerInfo_ModifyIcon" title="修改头像" href="javascript:;">
                    <div class="head-dress"></div>
                    <img src="//qlogo2.store.qq.com/qzone/836242657/836242657/100?1372472103" class="user-avatar" id="QM_OwnerInfo_Icon" />
                </a>
            </div>
        </div>
    </div>
    <div class="layout-background">
    
    <div class="layout-body">
        
        <div id="pageContent" class="layout-page clearfix">
            
            <div id="main_feed_container" class="col-main ">
                <div class="col-main-feed">
                    <div id="QM_Mood_Poster_Container" data-version="20131111">

	

<div id="QM_Mood_Poster_Inner" class="qz-poster bg b-test">
	<div class="qz-inputer bor2">
		<div id="qz_poster_editor_v4_container" class="textarea c_tx2" contenteditable="true" accesskey="q"></div>
	</div>
	<!-- attach -->
	<div class="qz-poster-attach-side">
		<div class="attach">
			<div class="item bor3 bg4 item-pic">
				<a href="javascript:void(0);" onclick="return false;" class="pic">
					<i class="icon icon-pic"></i>
					<span class="txt">照片</span>
				</a>
			</div>
		
			<div class="item bor3 bg4 item-other">
				<a href="javascript:void(0);" onclick="return false;" class="other">
					<i class="icon icon-other"></i>
					<span class="txt">其他</span>
				</a>
			</div>
		</div>
		<!-- attach -->
		<div class="other-attach-drop none">
						
		</div>
		<!-- other-drop -->
	</div>
	<!-- attach-side -->
	<div class="attachbar-holder" id="qz_poster_attachbar_v4_container" ></div>
	<div class="qz-poster-pops-holder">
		<!-- 浮层占位 -->
	</div>
	<!-- pop-holder -->
	<div class="qz-poster-status-holder" id="qz_poster_v4_resource_container">
		<!-- 附件占位 -->
	</div>
	<!-- status_holder -->
	<div class="qz-poster-ft">
		<div class="qz-poster-attach" id="qz_poster_fun_attachbar_v4_container">
			<a href="javascript:void(0);" class="emot"> <i class="icon icon-emot"></i>
				<span class="txt">表情</span>
			</a>
			<a href="javascript:void(0)" class="at"> <i class="icon icon-at"></i>
				<span class="txt">好友</span>
			</a>
			<a href="javascript:void(0)" class="topic"><i class="icon icon-topic"></i>
				<span class="txt">话题</span>
			</a>
		</div>
		<div class="qz-poster-sync">
			<div class="sync-nuts">
				<a class="sync-qq evt_click" data-hottag="moodposter.syncqq" href="javascript:void(0);" onclick="return false;" title="同步QQ">
					<i class="icon icon-qq"></i>
					<span class="txt">同步QQ</span>
				</a>
				<a class="sync-weibo evt_click" data-hottag="moodposter.syncweibo" href="javascript:void(0)" onclick="return false;" title="同步微博">
					<i class="icon icon-weibo"></i>
					<span class="txt">同步微博</span>
				</a>
				<a class="sync-timing evt_click none" data-hottag="moodposter.timer" href="javascript:void(0);" onclick="return false;" title="发表为定时说说">
					<i class="icon icon-timing"></i>
					<span class="txt">定时说说</span>
				</a>
				<div class="set-audience" data-hottag="moodposter.secret">
					<span class="dividor c_tx3">|</span><span class="private-label c_tx3">可见范围：</span>
					<a href="javascript:void(0);" class="audience c_tx3" role="button" aria-haspop="true">
						<span class="text-place">所有人</span>
						<b class="ui_trigbox ui_trigbox_b">
							<b class="ui_trig c_tx3"></b>
							<b class="ui_trig ui_trig_up bor_bg"></b>
						</b>
					</a>
				</div>
			</div>
		</div>
		<div class="op evt_click" data-hottag="MOODPOSTER.POST">
			<a href="javascript:void(0);" onclick="return false;" id="moodPosterButton"  class="btn-post btn gb_bt">
			<i class="icon icon-loading"></i>
			<span class="txt">发表</span>
			</a>
		</div>
	</div>
</div>
</div>

	







<div style="display:none" data-isfest="0"></div>


                    
                    <div id="feed_friend" >
                        <div class="fn-feed-control-v2 clearfix">
                            <div class="control-inner">
                                <div class="feed-control-tab">
                                    <a id='feed_tab_hover' class="item-on item-on-slt" href="javascript:;">
                                        <span id="feed_hover_text">全部动态</span>
                                        <i class="ui-icon icon-feed-down"></i>
                                    </a>
                                    <div class="qz-bubble tab-bubble" style="display:none;" id='friend_feed_control'>
                                        <div class="bubble-i">
                                            <div class="op-list" >
                                                <a id='feed_tab_all' class="item item-slt" href="javascript:;">全部动态</a>
                                                <a id='feed_tab_photo' class="item" href="javascript:;">相册</a>
                                                <a id='feed_tab_blog' class="item" href="javascript:;">日志</a>
                                                <a id='feed_tab_renzheng' class="item none" href="javascript:;">认证空间</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="feed-control-tab-op">
                                    <a id="feed_friend_refresh" title="刷新动态" href="javascript:;" class="item-left"><i class="ui-icon  icon-refresh-v9"></i></a>
                                    <span class="line"></span>
                                    <a id="feed_friend_set" title="动态设置" href="javascript:;" class="item-right"><i class="ui-icon  icon-set-v9"></i></a>
                                </div>
                            </div>
                        </div>
                        <div class="fn-feed-container">
                            <div class="feed  feed-v9">
                                <div class="feed_inner">
                                    <ul id="feed_friend_list">                                                                                                                                                                                                                                                                                         <li class="f-single f-s-s" id="fct_3418791386_311_0_1511369547_0_1"><div class="f-single-head f-aside"><div class="f-adorn-top"></div>    <div class="user-pto"><a href="http://user.qzone.qq.com/3418791386" target="_blank" class="user-avatar q_namecard f-s-a" link="nameCard_3418791386" data-clicklog="avatar"><img src="https://qlogo3.store.qq.com/qzone/3418791386/3418791386/50?1499690974"></a></div><div class="user-op"><a href="javascript:;" class="arrow-down" data-cmd="qz_opr_more" data-moreoperate="1"><i class="fui-icon icon-arrow-down"></i></a>        </div><div class="user-info"><div class="f-nick"><a target="_blank" href="http://user.qzone.qq.com/3418791386"  data-clicklog="nick" class="f-name q_namecard " link="nameCard_3418791386">可里老师/tpPython</a>  </div><div class="info-detail"><span  class=" ui-mr8 state" > 00:52</span><a href="javascript:;" data-cmd="qz_sign" class="f-sign-show state" title="我也要设置"></a></div></div></div><div class="f-single-content f-wrap"><div class="f-item f-s-i" id="feed_3418791386_311_0_1511369547_0_1" data-feedsflag="" data-iswupfeed="1" data-key="da9dc6cb4bab155a2d3a0400" data-specialtype="" data-extend-info="0_0_0_0_0_0_0|08009c0002000001|0000000000000000" data-functype="func_friend_feed" data-hasfollowed="1"><div class="f-info">T仔，萌萌哒<img src="http://qzonestyle.gtimg.cn/qzone/em/e6104.gif" title=""/><img src="http://qzonestyle.gtimg.cn/qzone/em/e6104.gif" title=""/> </div><div class="qz_summary wupfeed" id="hex_3418791386_311_0_1511369547_0_1"><i class="none" name="feed_data"  data-bitmap="08009c0002000001" data-yybitmap="0000000000000000" data-vipstarbitmap="0000000000000000" data-fkey="da9dc6cb4bab155a2d3a0400" data-tid="da9dc6cb4bab155a2d3a0400" data-uin="3418791386" data-origfkey="" data-origtid="da9dc6cb4bab155a2d3a0400" data-origuin="3418791386" data-subid="" data-totweet="" data-issignin="" data-source="" data-retweetcount="0" data-stat="exNDgYmCtviI7hAd3TJBd4!O4d4uS1a3pVDklE8lWNCj50DyxoqJXfX8H4IQQpJVlUW1/tZKR4EQp4YhVjgVcUGemGONSqg9pVDklE8lWNCj50DyxoqJXeqM6mXA759OQCBp!TIziyc6yqdgxo4hJk!nrTr2sBbal3dC6lZmCjjRMOZn7NewHEtvJA37tBgSMzAkbzg1AwLebTZGkpc85XI6RXAL45Fr_"   data-topicid="3418791386_da9dc6cb4bab155a2d3a0400__1"    data-feedstype="100"  data-abstime="1511369547"   data-iswupfeed="1"  data-platformid="50"  data-accessright="1"></i><div class="f-ct "><div class="f-ct-txtimg fui-txtimg   fui-imgbox-row-wrap"><div class="txt-box ">                                    </div><div class="img-box img-box-row row-two"><a  class="img-item  "data-cmd="qz_popup" href="https://user.qzone.qq.com/3418791386/311/"   class="  qz_ichotclick   with-sign img-two  " data-topicid="3418791386_da9dc6cb4bab155a2d3a0400__1" data-pickey="da9dc6cb4bab155a2d3a0400,,V102Cd9k2LLK0Q,NDR02p3GyzCrFVpvbGEK8gAAAAAAAAA!" data-clicklog="pic" data-originurl="||" hotclickPath="0_appid_311_v8.pic_count_2.pic_0" hotdomain="icv6act.qzone.qq.com" data-version="2" data-param="da9dc6cb4bab155a2d3a0400|3418791386|0" data-src="/qzone/photo/zone/icenter_popup.html" data-width="392" data-height="255" data-type="popup" data-title="" data-config=""><img src="http://a3.qpic.cn/psb?/V102Cd9k2LLK0Q/dBrkGdru.7MMFBchp.caUX3CkW9p56Xq0Cu9Zxk8YrY!/m/dPIAAAAAAAAA&amp;ek=1&amp;kp=1&amp;pt=0&amp;bo=oAEPAaABDwEDACU!&amp;vuin=836242657&amp;tm=1511402400&amp;sce=60-3-3&amp;rf=0-0"  style="margin-left:-74px;margin-top:0px;height:279px;width:428px;"height='224' style="margin-left:-59px;"/></a><a  class="img-item  "data-cmd="qz_popup" href="https://user.qzone.qq.com/3418791386/311/"   class="  qz_ichotclick   img-two  " data-topicid="3418791386_da9dc6cb4bab155a2d3a0400__1" data-pickey="da9dc6cb4bab155a2d3a0400,,V102Cd9k2LLK0Q,NDR02p3GyzGrFVqEiqkQ8gAAAAAAAAA!" data-clicklog="pic" data-originurl="||" hotclickPath="0_appid_311_v8.pic_count_2.pic_1" hotdomain="icv6act.qzone.qq.com" data-version="2" data-param="da9dc6cb4bab155a2d3a0400|3418791386|1" data-src="/qzone/photo/zone/icenter_popup.html" data-width="392" data-height="392" data-type="popup" data-title="" data-config=""><img src="http://a3.qpic.cn/psb?/V102Cd9k2LLK0Q/7CGrl6qdMpVQrEyzMShrhgam36W*1HmbrwbqQwnf5xc!/m/dPIAAAAAAAAA&amp;ek=1&amp;kp=1&amp;pt=0&amp;bo=gAKAAoACgAIRADc!&amp;t=5&amp;vuin=836242657&amp;tm=1511402400&amp;sce=60-3-3&amp;rf=0-0"  style="margin-left:0px;margin-top:0px;height:279px;width:279px;"width='200' /></a></div></div></div></div></div></div><div class="f-single-foot"><div class="f-op-detail f-detail content-line"><p class="op-list"><a class="item qz_retweet_btn " href="javascript:;" data-cmd="qz_popup" data-version="4" data-isnewtype="1" data-type="ForwardingBox" data-src="/qzone/app/controls/forwardingBox/forwardingBoxFacade.js" data-clicklog="retweet" ><i class="fui-icon icon-op-share"></i></a><span class="item-line"></span>&nbsp;<a href="javascript:;" data-version="6.3" data-cmd="qz_reply" data-link="1" data-clicklog="comment"  class=" qz_btn_reply item "><i class="fui-icon icon-op-comment"></i></a>&nbsp;<span class="item-line"></span><a class="item qz_like_btn_v3 " data-islike="0" data-likecnt="9" data-showcount="9" data-unikey="http://user.qzone.qq.com/3418791386/mood/da9dc6cb4bab155a2d3a0400" data-curkey="http://user.qzone.qq.com/3418791386/mood/da9dc6cb4bab155a2d3a0400" data-clicklog="like" href="javascript:;"><i class="fui-icon icon-op-praise"></i></a></p><a href="javascript:;" class="state qz_feed_plugin" data-role="Visitor" data-config="311|da9dc6cb4bab155a2d3a0400|3418791386" data-clicklog="visitor">浏览178次</a></div>        <div class="f-ang-t"></div><div class="f-like-list f-like _likeInfo" likeinfo="9"><div class="icon-btn"><a href="javascript:;" data-islike="0" data-likecnt="9" data-showcount="9" data-unikey="http://user.qzone.qq.com/3418791386/mood/da9dc6cb4bab155a2d3a0400" data-curkey="http://user.qzone.qq.com/3418791386/mood/da9dc6cb4bab155a2d3a0400" data-clicklog="like" class="praise qz_like_prase"><i class="fui-icon icon-list-praise"></i></a><div class="bubble" style="display:none;"><div class="bd">+1</div><b class="arrow arrow-down"></b></div></div><div class="user-list"><a href="http://user.qzone.qq.com/66535967" class="item q_namecard" target="_blank" link="nameCard_66535967 des_66535967">(_ℳ ｒ肖_)</a>、<a href="http://user.qzone.qq.com/364996814" class="item q_namecard" target="_blank" link="nameCard_364996814 des_364996814">君安</a>、<a href="http://user.qzone.qq.com/523298028" class="item q_namecard" target="_blank" link="nameCard_523298028 des_523298028">Life Is One Big Illusion</a>、<a href="http://user.qzone.qq.com/986504086" class="item q_namecard" target="_blank" link="nameCard_986504086 des_986504086">漩 。</a>、<a href="http://user.qzone.qq.com/1207999021" class="item q_namecard" target="_blank" link="nameCard_1207999021 des_1207999021">游戏</a>、<a href="http://user.qzone.qq.com/1356062343" class="item q_namecard" target="_blank" link="nameCard_1356062343 des_1356062343">。贪欲</a>、<a href="http://user.qzone.qq.com/2576142644" class="item q_namecard" target="_blank" link="nameCard_2576142644 des_2576142644">爱哭的咸鱼猫</a>、<a href="http://user.qzone.qq.com/2769077078" class="item q_namecard" target="_blank" link="nameCard_2769077078 des_2769077078">Let me shine ——Melody</a>、<a href="http://user.qzone.qq.com/3219354564" class="item q_namecard" target="_blank" link="nameCard_3219354564 des_3219354564">琳果儿</a>共<span class="f-like-cnt">9</span>人觉得很赞</div></div><div class="mod-comments" style="padding:0"><div class="mod-commnets-poster feedClickCmd comment_default_inputentry" data-cmd="qz_reply" data-version="6" data-action="http://taotao.qq.com/cgi-bin/emotion_cgi_re_feeds" data-param="t1_source=&amp;t1_uin=3418791386&amp;t1_tid=da9dc6cb4bab155a2d3a0400&amp;signin=0&amp;sceneid=100" data-charset="utf-8" data-maxLength="" data-tuin="3418791386" data-config="1|1|1|1,b52,with_fwd,同时转发;0|1,taotaoact.qzone.qq.com,@InputReply|1,taotaoact.qzone.qq.com,@ClickReply|1,taotaoact.qzone.qq.com,commentPresentClick"  data-tid="" ><div class="comments-poster-bd comments-poster-default"><div class="comments-box" data-clicklog="comment"><div class="textinput textinput-default bor2" contenteditable="true" alt="replybtn" placeholder="评论"><a class="c_tx3" href="javascript:void(0);" alt="replybtn">评论</a></div><div class="mod-insert-img"><a href="javascript:;" data-cmd="qz_quick_upload_img" class="btn-insert-img bg"><i class="icon-camera-16"></i></a></div></div></div></div></div>    </div></li>                                                                                                                                                                                                                                                                                                                                                                                                                                   <li class="f-single f-s-s" id="fct_1983710849_311_0_1511367590_0_1"><div class="f-single-head f-aside"><div class="f-adorn-top"></div>    <div class="user-pto"><a href="http://user.qzone.qq.com/1983710849" target="_blank" class="user-avatar q_namecard f-s-a" link="nameCard_1983710849" data-clicklog="avatar"><img src="https://qlogo2.store.qq.com/qzone/1983710849/1983710849/50?1511325872"></a></div><div class="user-op"><a href="javascript:;" class="arrow-down" data-cmd="qz_opr_more" data-moreoperate="1"><i class="fui-icon icon-arrow-down"></i></a>        </div><div class="user-info"><div class="f-nick"><a target="_blank" href="http://user.qzone.qq.com/1983710849"  data-clicklog="nick" class="f-name q_namecard " link="nameCard_1983710849">林柏栎</a>  </div><div class="info-detail"><span  class=" ui-mr8 state" > 00:19</span><a href="javascript:;" data-cmd="qz_sign" class="f-sign-show state" title="我也要设置"></a></div></div></div><div class="f-single-content f-wrap"><div class="f-item f-s-i" id="feed_1983710849_311_0_1511367590_0_1" data-feedsflag="" data-iswupfeed="1" data-key="81063d76a6a3155afc4e0b00" data-specialtype="" data-extend-info="0_0_0_0_0_0_0|08808d800202c001|1018000056ac1004" data-functype="func_friend_feed" data-hasfollowed="1"><div class="f-info">哈哈<img src="http://qzonestyle.gtimg.cn/qzone/em/e277.png"  title=""/></div><div class="qz_summary wupfeed" id="hex_1983710849_311_0_1511367590_0_1"><i class="none" name="feed_data"  data-bitmap="08808d800202c001" data-yybitmap="1018000056ac1004" data-vipstarbitmap="0000000048000100" data-fkey="81063d76a6a3155afc4e0b00" data-tid="81063d76a6a3155afc4e0b00" data-uin="1983710849" data-origfkey="" data-origtid="81063d76a6a3155afc4e0b00" data-origuin="1983710849" data-subid="" data-totweet="" data-issignin="" data-source="" data-retweetcount="0" data-stat="HsHAijm8fXdFjOubEFwwXDECtJvNON0RaVxppVwIU2Zd5GKHW4MrmMbpk93xxkc2PeVoGhwZR/6VFxwDPAqGTHqyj6fc5qgmSgWAoxFcxyZoSKUmY6vrlLkodo7wqWtBe/S9CK5LtuDY!ch7pm1KiTg/aZ9SfUqQMU!u4iGmYL8t8Wr2GtXACGKvwAtjR!40_"   data-topicid="1983710849_81063d76a6a3155afc4e0b00__1"    data-feedstype="100"  data-abstime="1511367590"   data-iswupfeed="1"  data-platformid="52"  data-accessright="1"></i><div class="f-ct "><div class="f-ct-txtimg fui-txtimg   fui-imgbox-row-wrap"><div class="txt-box ">                                    </div><div class="img-box img-box-row row-two"><a  class="img-item  "data-cmd="qz_popup" href="https://user.qzone.qq.com/1983710849/311/"   class="  qz_ichotclick   img-two  " data-topicid="1983710849_81063d76a6a3155afc4e0b00__1" data-pickey="81063d76a6a3155afc4e0b00,http://b243.photo.store.qq.com/psb?/V10hFhZT47VRtr/75rUiRFDZt8NtGSt5l6UsK5B1.*P*j9IuuTDpDfs20Y!/b/dPMAAAAAAAAA&amp;bo=GwLAAwAAAAARAO0!" data-clicklog="pic" data-originurl="||" hotclickPath="0_appid_311_v8.pic_count_4.pic_0" hotdomain="icv6act.qzone.qq.com" data-version="2" data-param="81063d76a6a3155afc4e0b00|1983710849|0" data-src="/qzone/photo/zone/icenter_popup.html" data-width="539" data-height="960" data-type="popup" data-title="" data-config=""><img src="http://a4.qpic.cn/psb?/V10hFhZT47VRtr/75rUiRFDZt8NtGSt5l6UsK5B1.*P*j9IuuTDpDfs20Y!/m/dPMAAAAAAAAA&amp;ek=1&amp;kp=1&amp;pt=0&amp;bo=GwLAAwAAAAARAO0!&amp;t=5&amp;vuin=836242657&amp;tm=1511402400&amp;sce=60-3-3&amp;rf=0-0"  style="margin-left:0px;margin-top:-109px;height:496px;width:279px;"height='200' /></a><a  class="img-item  "data-cmd="qz_popup" href="https://user.qzone.qq.com/1983710849/311/"   class="  qz_ichotclick   img-two  " data-topicid="1983710849_81063d76a6a3155afc4e0b00__1" data-pickey="81063d76a6a3155afc4e0b00,http://b242.photo.store.qq.com/psb?/V10hFhZT47VRtr/lgMaWTOwiV*3U4vg7engxjxiSuBMyc5osml4e0cFaFc!/b/dPIAAAAAAAAA&amp;bo=KgM4BAAAAAARACI!" data-clicklog="pic" data-originurl="||" hotclickPath="0_appid_311_v8.pic_count_4.pic_1" hotdomain="icv6act.qzone.qq.com" data-version="2" data-param="81063d76a6a3155afc4e0b00|1983710849|1" data-src="/qzone/photo/zone/icenter_popup.html" data-width="810" data-height="1080" data-type="popup" data-title="" data-config=""><img src="http://a3.qpic.cn/psb?/V10hFhZT47VRtr/lgMaWTOwiV*3U4vg7engxjxiSuBMyc5osml4e0cFaFc!/m/dPIAAAAAAAAA&amp;ek=1&amp;kp=1&amp;pt=0&amp;bo=KgM4BAAAAAARACI!&amp;t=5&amp;vuin=836242657&amp;tm=1511402400&amp;sce=60-3-3&amp;rf=0-0"  style="margin-left:0px;margin-top:0px;height:371px;width:279px;"height='200' /></a><a  class="img-item  "data-cmd="qz_popup" href="https://user.qzone.qq.com/1983710849/311/"   class="  qz_ichotclick   img-two  " data-topicid="1983710849_81063d76a6a3155afc4e0b00__1" data-pickey="81063d76a6a3155afc4e0b00,http://b242.photo.store.qq.com/psb?/V10hFhZT47VRtr/1O.k259JGr.ZtqoL40wtLhgoJOUFg8nI4MD8bmj9Ym8!/b/dPIAAAAAAAAA&amp;bo=KgM4BAAAAAARACI!" data-clicklog="pic" data-originurl="||" hotclickPath="0_appid_311_v8.pic_count_4.pic_2" hotdomain="icv6act.qzone.qq.com" data-version="2" data-param="81063d76a6a3155afc4e0b00|1983710849|2" data-src="/qzone/photo/zone/icenter_popup.html" data-width="810" data-height="1080" data-type="popup" data-title="" data-config=""><img src="http://a3.qpic.cn/psb?/V10hFhZT47VRtr/1O.k259JGr.ZtqoL40wtLhgoJOUFg8nI4MD8bmj9Ym8!/m/dPIAAAAAAAAA&amp;ek=1&amp;kp=1&amp;pt=0&amp;bo=KgM4BAAAAAARACI!&amp;t=5&amp;vuin=836242657&amp;tm=1511402400&amp;sce=60-3-3&amp;rf=0-0"  style="margin-left:0px;margin-top:-46px;height:371px;width:279px;"height='200' /></a><a  class="img-item  "data-cmd="qz_popup" href="https://user.qzone.qq.com/1983710849/311/"   class="  qz_ichotclick   img-two  " data-topicid="1983710849_81063d76a6a3155afc4e0b00__1" data-pickey="81063d76a6a3155afc4e0b00,http://b318.photo.store.qq.com/psb?/V10hFhZT47VRtr/7TH.Heq4ay9SkU0qHwLlAlNDKuHodPsjrBvQTMvSGQY!/b/dD4BAAAAAAAA&amp;bo=OAQqAwAAAAARACI!" data-clicklog="pic" data-originurl="||" hotclickPath="0_appid_311_v8.pic_count_4.pic_3" hotdomain="icv6act.qzone.qq.com" data-version="2" data-param="81063d76a6a3155afc4e0b00|1983710849|3" data-src="/qzone/photo/zone/icenter_popup.html" data-width="1080" data-height="810" data-type="popup" data-title="" data-config=""><img src="http://a3.qpic.cn/psb?/V10hFhZT47VRtr/7TH.Heq4ay9SkU0qHwLlAlNDKuHodPsjrBvQTMvSGQY!/m/dD4BAAAAAAAA&amp;ek=1&amp;kp=1&amp;pt=0&amp;bo=OAQqAwAAAAARACI!&amp;t=5&amp;vuin=836242657&amp;tm=1511402400&amp;sce=60-3-3&amp;rf=0-0"  style="margin-left:-4px;margin-top:0px;height:279px;width:371px;"height='224' style="margin-left:-36px;"/></a></div></div><div class="f-reprint">        <p class="item">        <i class="fui-icon icon-print-phone"></i><span class="ui-mr8 state">来自&nbsp;<a href="http://z.qzone.com?from=androidgrzxpl" target="_blank"  class=" phone-style state">小米 5C (4G)</a>&nbsp;</span>        </p>                            </div>    </div></div></div></div><div class="f-single-foot"><div class="f-op-detail f-detail content-line"><p class="op-list"><a class="item qz_retweet_btn " href="javascript:;" data-cmd="qz_popup" data-version="4" data-isnewtype="1" data-type="ForwardingBox" data-src="/qzone/app/controls/forwardingBox/forwardingBoxFacade.js" data-clicklog="retweet" ><i class="fui-icon icon-op-share"></i></a><span class="item-line"></span>&nbsp;<a href="javascript:;" data-version="6.3" data-cmd="qz_reply" data-link="1" data-clicklog="comment"  class=" qz_btn_reply item "><i class="fui-icon icon-op-comment"></i></a>&nbsp;<span class="item-line"></span><a class="item qz_like_btn_v3 " data-islike="0" data-likecnt="29" data-showcount="20" data-unikey="http://user.qzone.qq.com/1983710849/mood/81063d76a6a3155afc4e0b00" data-curkey="http://user.qzone.qq.com/1983710849/mood/81063d76a6a3155afc4e0b00" data-clicklog="like" href="javascript:;"><i class="fui-icon icon-op-praise"></i></a></p><a href="javascript:;" class="state qz_feed_plugin" data-role="Visitor" data-config="311|81063d76a6a3155afc4e0b00|1983710849" data-clicklog="visitor">浏览196次</a></div>        <div class="f-ang-t"></div><div class="f-like-list f-like _likeInfo" likeinfo="29"><div class="icon-btn"><a href="javascript:;" data-islike="0" data-likecnt="29" data-showcount="29" data-unikey="http://user.qzone.qq.com/1983710849/mood/81063d76a6a3155afc4e0b00" data-curkey="http://user.qzone.qq.com/1983710849/mood/81063d76a6a3155afc4e0b00" data-clicklog="like" class="praise qz_like_prase"><i class="fui-icon icon-list-praise"></i></a><div class="bubble" style="display:none;"><div class="bd">+1</div><b class="arrow arrow-down"></b></div></div><div class="user-list"><a href="http://user.qzone.qq.com/947118418" class="item q_namecard" target="_blank" link="nameCard_947118418 des_947118418">苗幼林</a>、<a href="http://user.qzone.qq.com/1983710849" class="item q_namecard" target="_blank" link="nameCard_1983710849 des_1983710849">林柏栎</a>、<a href="http://user.qzone.qq.com/3072966990" class="item q_namecard" target="_blank" link="nameCard_3072966990 des_3072966990">徐佳庆</a>、<a href="http://user.qzone.qq.com/11670089" class="item q_namecard" target="_blank" link="nameCard_11670089 des_11670089">Sunny_Rain</a>、<a href="http://user.qzone.qq.com/192497410" class="item q_namecard" target="_blank" link="nameCard_192497410 des_192497410">赵琦</a>、<a href="http://user.qzone.qq.com/307417019" class="item q_namecard" target="_blank" link="nameCard_307417019 des_307417019">w<img src="http://qzonestyle.gtimg.cn/qzone/em/e328522.gif" title=""/>R</a>、<a href="http://user.qzone.qq.com/473618849" class="item q_namecard" target="_blank" link="nameCard_473618849 des_473618849">西南樵夫</a>、<a href="http://user.qzone.qq.com/583392448" class="item q_namecard" target="_blank" link="nameCard_583392448 des_583392448">看一看世界的繁华~</a>、<a href="http://user.qzone.qq.com/634224930" class="item q_namecard" target="_blank" link="nameCard_634224930 des_634224930">清风</a>、<a href="http://user.qzone.qq.com/742553611" class="item q_namecard" target="_blank" link="nameCard_742553611 des_742553611"><img src="http://qzonestyle.gtimg.cn/qzone/em/e328014.gif" title=""/>.<img src="http://qzonestyle.gtimg.cn/qzone/em/e328176.gif" title=""/></a>、<a href="http://user.qzone.qq.com/752291671" class="item q_namecard" target="_blank" link="nameCard_752291671 des_752291671">Corgi</a>、<a href="http://user.qzone.qq.com/786596597" class="item q_namecard" target="_blank" link="nameCard_786596597 des_786596597">超越自我的人生极限</a>、<a href="http://user.qzone.qq.com/836396917" class="item q_namecard" target="_blank" link="nameCard_836396917 des_836396917">A curious cat</a>、<a href="http://user.qzone.qq.com/971219273" class="item q_namecard" target="_blank" link="nameCard_971219273 des_971219273">故人 *</a>、<a href="http://user.qzone.qq.com/1002119625" class="item q_namecard" target="_blank" link="nameCard_1002119625 des_1002119625"><img src="http://qzonestyle.gtimg.cn/qzone/em/e327811.gif" title=""/></a>、<a href="http://user.qzone.qq.com/1098181515" class="item q_namecard" target="_blank" link="nameCard_1098181515 des_1098181515">一颗菠菠萝<img src="http://qzonestyle.gtimg.cn/qzone/em/e327821.gif" title=""/></a>、<a href="http://user.qzone.qq.com/1127066808" class="item q_namecard" target="_blank" link="nameCard_1127066808 des_1127066808">Cong</a>、<a href="http://user.qzone.qq.com/1147933424" class="item q_namecard" target="_blank" link="nameCard_1147933424 des_1147933424">binEncoder</a>、<a href="http://user.qzone.qq.com/1411832579" class="item q_namecard" target="_blank" link="nameCard_1411832579 des_1411832579">吸烟伤肺゛想你伤心ゞ</a>、<a href="http://user.qzone.qq.com/1432898176" class="item q_namecard" target="_blank" link="nameCard_1432898176 des_1432898176">千羽</a>等<span class="f-like-cnt">29</span>人觉得很赞</div></div><div class="mod-comments" style="padding:0"><div class="comments-list "><ul><li class="comments-item bor3" data-type="commentroot" data-tid="1" data-uin="1983710849" data-nick="林柏栎" data-who="1"><div class="comments-item-bd"><div class="single-reply"><div class="ui-avatar"><a href="http://user.qzone.qq.com/1983710849" target="_blank"><img class="q_namecard" link="nameCard_1983710849 des_1983710849" alt="林柏栎" src="http://qlogo2.store.qq.com/qzone/1983710849/1983710849/30?1511325872" /></a></div><div class="comments-content"><a class="nickname name c_tx q_namecard"  link="nameCard_1983710849" target="_blank" href="http://user.qzone.qq.com/1983710849">林柏栎</a>&nbsp; : <a class="nickname name c_tx  q_namecard"  link="nameCard_192497410" target="_blank" href="http://user.qzone.qq.com/192497410">@赵琦</a>&nbsp;谢谢啊，兄弟<div class="comments-op"><span  class=" ui-mr10 state" > 00:21</span><a class="act-reply none" href="javascript:;" data-cmd="qz_reply" data-version="6.4" data-action="http://taotao.qq.com/cgi-bin/emotion_cgi_re_feeds" data-param="t1_source=&amp;t1_uin=1983710849&amp;t1_tid=81063d76a6a3155afc4e0b00&amp;t2_uin=1983710849&amp;t2_tid=1&amp;subdotype=55702&amp;signin=0&amp;sceneid=100" data-charset="utf-8" data-tuin="" data-config="1|1|1|0|1,taotaoact.qzone.qq.com,@InputReply|1,taotaoact.qzone.qq.com,@ClickReply|1,taotaoact.qzone.qq.com,commentPresentClick"><b class="hide-clip">回复</b></a></div></div></div></div></li><li class="comments-item bor3" data-type="commentroot" data-tid="2" data-uin="1983710849" data-nick="林柏栎" data-who="1"><div class="comments-item-bd"><div class="single-reply"><div class="ui-avatar"><a href="http://user.qzone.qq.com/1983710849" target="_blank"><img class="q_namecard" link="nameCard_1983710849 des_1983710849" alt="林柏栎" src="http://qlogo2.store.qq.com/qzone/1983710849/1983710849/30?1511325872" /></a></div><div class="comments-content"><a class="nickname name c_tx q_namecard"  link="nameCard_1983710849" target="_blank" href="http://user.qzone.qq.com/1983710849">林柏栎</a>&nbsp; : <a class="nickname name c_tx  q_namecard"  link="nameCard_742553611" target="_blank" href="http://user.qzone.qq.com/742553611">@<img src="http://qzonestyle.gtimg.cn/qzone/em/e328014.gif" title=""/>.<img src="http://qzonestyle.gtimg.cn/qzone/em/e328176.gif" title=""/></a>&nbsp;<img src="http://qzonestyle.gtimg.cn/qzone/em/e106.png"  title=""/><div class="comments-op"><span  class=" ui-mr10 state" > 00:23</span><a class="act-reply none" href="javascript:;" data-cmd="qz_reply" data-version="6.4" data-action="http://taotao.qq.com/cgi-bin/emotion_cgi_re_feeds" data-param="t1_source=&amp;t1_uin=1983710849&amp;t1_tid=81063d76a6a3155afc4e0b00&amp;t2_uin=1983710849&amp;t2_tid=2&amp;subdotype=55702&amp;signin=0&amp;sceneid=100" data-charset="utf-8" data-tuin="" data-config="1|1|1|0|1,taotaoact.qzone.qq.com,@InputReply|1,taotaoact.qzone.qq.com,@ClickReply|1,taotaoact.qzone.qq.com,commentPresentClick"><b class="hide-clip">回复</b></a></div></div></div><div class="comments-list mod-comments-sub"><ul><li class="comments-item bor3" data-type="replyroot" data-tid="1" data-uin="742553611" data-nick="[em]e328014[/em].[em]e328176[/em]" data-who="1"><div class="comments-item-bd"><div class="single-reply"><div class="ui-avatar"><a href="http://user.qzone.qq.com/742553611" target="_blank"><img class="q_namecard" link="nameCard_742553611 des_742553611" alt="[em]e328014[/em].[em]e328176[/em]" src="http://qlogo4.store.qq.com/qzone/742553611/742553611/30" /></a></div><div class="comments-content"><a class="nickname name c_tx q_namecard"  link="nameCard_742553611" target="_blank" href="http://user.qzone.qq.com/742553611"><img src="http://qzonestyle.gtimg.cn/qzone/em/e328014.gif" title=""/>.<img src="http://qzonestyle.gtimg.cn/qzone/em/e328176.gif" title=""/></a>&nbsp;回复<a class="nickname name c_tx q_namecard"  link="nameCard_1983710849" target="_blank" href="http://user.qzone.qq.com/1983710849">林柏栎</a>&nbsp; : 美美哒<div class="comments-op"><span  class=" ui-mr10 state" > 00:25</span><a class="act-reply none" href="javascript:;" data-cmd="qz_reply" data-version="6.4" data-action="http://taotao.qq.com/cgi-bin/emotion_cgi_re_feeds" data-param="t1_source=&amp;t1_uin=1983710849&amp;t1_tid=81063d76a6a3155afc4e0b00&amp;t2_uin=1983710849&amp;t2_tid=2&amp;subdotype=55702&amp;signin=0&amp;sceneid=100" data-charset="utf-8" data-tuin="" data-config="1|1|1|0|1,taotaoact.qzone.qq.com,@InputReply|1,taotaoact.qzone.qq.com,@ClickReply|1,taotaoact.qzone.qq.com,commentPresentClick"><b class="hide-clip">回复</b></a></div></div></div></div></li><li class="comments-item bor3" data-type="replyroot" data-tid="2" data-uin="1983710849" data-nick="林柏栎" data-who="1"><div class="comments-item-bd"><div class="single-reply"><div class="ui-avatar"><a href="http://user.qzone.qq.com/1983710849" target="_blank"><img class="q_namecard" link="nameCard_1983710849 des_1983710849" alt="林柏栎" src="http://qlogo2.store.qq.com/qzone/1983710849/1983710849/30?1511325872" /></a></div><div class="comments-content"><a class="nickname name c_tx q_namecard"  link="nameCard_1983710849" target="_blank" href="http://user.qzone.qq.com/1983710849">林柏栎</a>&nbsp;回复<a class="nickname name c_tx q_namecard"  link="nameCard_742553611" target="_blank" href="http://user.qzone.qq.com/742553611"><img src="http://qzonestyle.gtimg.cn/qzone/em/e328014.gif" title=""/>.<img src="http://qzonestyle.gtimg.cn/qzone/em/e328176.gif" title=""/></a>&nbsp; : 比心<img src="http://qzonestyle.gtimg.cn/qzone/em/e166.png"  title=""/><div class="comments-op"><span  class=" ui-mr10 state" > 00:26</span><a class="act-reply none" href="javascript:;" data-cmd="qz_reply" data-version="6.4" data-action="http://taotao.qq.com/cgi-bin/emotion_cgi_re_feeds" data-param="t1_source=&amp;t1_uin=1983710849&amp;t1_tid=81063d76a6a3155afc4e0b00&amp;t2_uin=1983710849&amp;t2_tid=2&amp;subdotype=55702&amp;signin=0&amp;sceneid=100" data-charset="utf-8" data-tuin="" data-config="1|1|1|0|1,taotaoact.qzone.qq.com,@InputReply|1,taotaoact.qzone.qq.com,@ClickReply|1,taotaoact.qzone.qq.com,commentPresentClick"><b class="hide-clip">回复</b></a></div></div></div></div></li></ul></div></div></li><li class="comments-item bor3" data-type="commentroot" data-tid="3" data-uin="1791407456" data-nick="杨夫人" data-who="1"><div class="comments-item-bd"><div class="single-reply"><div class="ui-avatar"><a href="http://user.qzone.qq.com/1791407456" target="_blank"><img class="q_namecard" link="nameCard_1791407456 des_1791407456" alt="杨夫人" src="http://qlogo1.store.qq.com/qzone/1791407456/1791407456/30" /></a></div><div class="comments-content"><a class="nickname name c_tx q_namecard"  link="nameCard_1791407456" target="_blank" href="http://user.qzone.qq.com/1791407456">杨夫人</a>&nbsp; : 好看<img src="http://qzonestyle.gtimg.cn/qzone/em/e102.png"  title=""/><div class="comments-op"><span  class=" ui-mr10 state" > 06:48</span><a class="act-reply none" href="javascript:;" data-cmd="qz_reply" data-version="6.4" data-action="http://taotao.qq.com/cgi-bin/emotion_cgi_re_feeds" data-param="t1_source=&amp;t1_uin=1983710849&amp;t1_tid=81063d76a6a3155afc4e0b00&amp;t2_uin=1791407456&amp;t2_tid=3&amp;subdotype=55702&amp;signin=0&amp;sceneid=100" data-charset="utf-8" data-tuin="" data-config="1|1|1|0|1,taotaoact.qzone.qq.com,@InputReply|1,taotaoact.qzone.qq.com,@ClickReply|1,taotaoact.qzone.qq.com,commentPresentClick"><b class="hide-clip">回复</b></a></div></div></div></div></li><li class="comments-item bor3" data-type="commentroot" data-tid="4" data-uin="2638182618" data-nick="Black Galaxy" data-who="1"><div class="comments-item-bd"><div class="single-reply"><div class="ui-avatar"><a href="http://user.qzone.qq.com/2638182618" target="_blank"><img class="q_namecard" link="nameCard_2638182618 des_2638182618" alt="Black Galaxy" src="http://qlogo3.store.qq.com/qzone/2638182618/2638182618/30" /></a></div><div class="comments-content"><a class="nickname name c_tx q_namecard"  link="nameCard_2638182618" target="_blank" href="http://user.qzone.qq.com/2638182618">Black Galaxy</a>&nbsp; : 后面那个熊，是不是菜菜<div class="comments-op"><span  class=" ui-mr10 state" > 09:23</span><a class="act-reply none" href="javascript:;" data-cmd="qz_reply" data-version="6.4" data-action="http://taotao.qq.com/cgi-bin/emotion_cgi_re_feeds" data-param="t1_source=&amp;t1_uin=1983710849&amp;t1_tid=81063d76a6a3155afc4e0b00&amp;t2_uin=2638182618&amp;t2_tid=4&amp;subdotype=55702&amp;signin=0&amp;sceneid=100" data-charset="utf-8" data-tuin="" data-config="1|1|1|0|1,taotaoact.qzone.qq.com,@InputReply|1,taotaoact.qzone.qq.com,@ClickReply|1,taotaoact.qzone.qq.com,commentPresentClick"><b class="hide-clip">回复</b></a></div></div></div></div></li></ul></div><div class="mod-commnets-poster feedClickCmd comment_default_inputentry" data-cmd="qz_reply" data-version="6" data-action="http://taotao.qq.com/cgi-bin/emotion_cgi_re_feeds" data-param="t1_source=&amp;t1_uin=1983710849&amp;t1_tid=81063d76a6a3155afc4e0b00&amp;signin=0&amp;sceneid=100" data-charset="utf-8" data-maxLength="" data-tuin="1983710849" data-config="1|1|1|1,b52,with_fwd,同时转发;0|1,taotaoact.qzone.qq.com,@InputReply|1,taotaoact.qzone.qq.com,@ClickReply|1,taotaoact.qzone.qq.com,commentPresentClick"  data-tid="" ><div class="comments-poster-bd comments-poster-default"><div class="comments-box" data-clicklog="comment"><div class="textinput textinput-default bor2" contenteditable="true" alt="replybtn" placeholder="评论"><a class="c_tx3" href="javascript:void(0);" alt="replybtn">评论</a></div><div class="mod-insert-img"><a href="javascript:;" data-cmd="qz_quick_upload_img" class="btn-insert-img bg"><i class="icon-camera-16"></i></a></div></div></div></div></div>    </div></li>                                                                                                                                                             <li class="f-single f-s-s" id="fct_2184558967_311_5_1511365243_0_1"><div class="f-single-head f-aside"><div class="f-adorn-top"></div>    <div class="user-pto"><a href="http://user.qzone.qq.com/2184558967" target="_blank" class="user-avatar q_namecard f-s-a" link="nameCard_2184558967" data-clicklog="avatar"><img src="https://qlogo4.store.qq.com/qzone/2184558967/2184558967/50?1490883485"></a></div><div class="user-op"><a href="javascript:;" class="arrow-down" data-cmd="qz_opr_more" data-moreoperate="1"><i class="fui-icon icon-arrow-down"></i></a>        </div><div class="user-info"><div class="f-nick"><a target="_blank" href="http://user.qzone.qq.com/2184558967"  data-clicklog="nick" class="f-name q_namecard " link="nameCard_2184558967">沈旭</a>  </div><div class="info-detail"><span  class=" ui-mr8 state" >昨天 23:40</span><a href="javascript:;" data-cmd="qz_sign" class="f-sign-show state" title="我也要设置"></a></div></div></div><div class="f-single-content f-wrap"><div class="f-item f-s-i" id="feed_2184558967_311_5_1511365243_0_1" data-feedsflag="" data-iswupfeed="1" data-key="77b935827b9a155a6bb40a00" data-specialtype="" data-extend-info="0_0_0_0_0_0_0|08009c8002024201|0000000000000000" data-functype="func_friend_feed" data-hasfollowed="1"><div class="f-info">来吧来吧，抓住机会哟</div><div class="qz_summary wupfeed" id="hex_2184558967_311_5_1511365243_0_1"><i class="none" name="feed_data"  data-bitmap="08009c8002024201" data-yybitmap="0000000000000000" data-vipstarbitmap="0000000000000000" data-fkey="77b935827b9a155a6bb40a00" data-tid="77b935827b9a155a6bb40a00" data-uin="2184558967" data-origfkey="" data-origtid="4e440a57638f155a7d440300" data-origuin="1460290638" data-subid="" data-totweet="" data-issignin="" data-source="" data-retweetcount="0" data-stat="Ntmd6rNYrZCivTwTmTL2nQbvtWYjDFUif2dKsU!1E3R2cFqQ9fZaTsNNjtNqQpxnyrR50qOpZ1AbwPLktiu6Sa3Q!MInfrQBSgWAoxFcxyZoSKUmY6vrlNATfFdedQFdZpjw//ON/tk17CYErck7PNg6ls!SWjCyet1QHDabw26jLtZY7fOQcM!0AY9hipb0zZSVcHRdzwHy8w1gH3SnZ39nSrFPtRN0dnBakPX2Wk7DTY7TakKcZ5FR6heX!WEEunnsuim3hm8_"   data-topicid="2184558967_77b935827b9a155a6bb40a00__1"    data-feedstype="100"  data-abstime="1511365243"   data-iswupfeed="1"  data-platformid="52"  data-accessright="1"></i><div class="f-ct "><div class="f-ct-txtimg fui-txtimg  fui-txtimg fui-txtimg-bg  fui-imgbox-row-wrap"><div class="txt-box  qz_info_cut">                                    <a class="nickname name c_tx  q_namecard"  link="nameCard_1460290638" target="_blank" href="http://user.qzone.qq.com/1460290638">西南交通大学彝文化协会</a>&nbsp;<span  class=" state" >：</span>终于来了，彝协小哥哥小姐姐们为大家精心准备的书签来了，明后天可现场领书签哟<img src="http://qzonestyle.gtimg.cn/qzone/em/e400837.gif" title=""/><img src="http://qzonestyle.gtimg.cn/qzone/em/e400837.gif" title=""/><br/>时间：周四周五，中午和下午<br/>地点：二食堂、四食堂门口<br/>精美的书签在向你招手<img src="http://qzonestyle.gtimg.cn/qzone/em/e400846.gif" title=""/><img src="http://qzonestyle.gtimg.cn/qzone/em/e400846.gif" title=""/><br/> <a href="javascript:;" data-cmd="qz_toggle" data-pos="2">展开全文</a><img src="http://qzonestyle.gtimg.cn/qzone_v6/img/feed/loading.gif" class="load_img none"></div><div class="txt-box qz_info_complete none"></div><div class="img-box img-box-row row-three"><a  class="img-item  "data-cmd="qz_popup" href="https://user.qzone.qq.com/1460290638/311/"   class="  qz_ichotclick   img-three  " data-topicid="2184558967_77b935827b9a155a6bb40a00__1" data-pickey="77b935827b9a155a6bb40a00,http://b347.photo.store.qq.com/psb?/V13Uz9Av0QdwLU/gOmK3X06X7mgMHleZBXj5GhBVB0z0QcSanRqL1EGtgI!/b/dFsBAAAAAAAA&amp;bo=SQbkCAAAAAARAJQ!" data-clicklog="pic" data-originurl="||" hotclickPath="0_appid_311_v8.pic_count_9.pic_0" hotdomain="icv6act.qzone.qq.com" data-version="2" data-param="77b935827b9a155a6bb40a00|2184558967|0" data-src="/qzone/photo/zone/icenter_popup.html" data-width="1609" data-height="2276" data-type="popup" data-title="" data-config=""><img src="http://a4.qpic.cn/psb?/V13Uz9Av0QdwLU/gOmK3X06X7mgMHleZBXj5GhBVB0z0QcSanRqL1EGtgI!/m/dFsBAAAAAAAA&amp;ek=1&amp;kp=1&amp;pt=0&amp;bo=SQbkCAAAAAARAJQ!&amp;t=5&amp;vuin=836242657&amp;tm=1511402400&amp;sce=60-4-3&amp;rf=0-0"  style="margin-left:0px;margin-top:-38px;height:260px;width:185px;"/></a><a  class="img-item  "data-cmd="qz_popup" href="https://user.qzone.qq.com/1460290638/311/"   class="  qz_ichotclick   img-three  " data-topicid="2184558967_77b935827b9a155a6bb40a00__1" data-pickey="77b935827b9a155a6bb40a00,http://b243.photo.store.qq.com/psb?/V13Uz9Av0QdwLU/iAwmmBXtfvgujAp0vEO1exUuA8tQ6qwbvD27IUHG3c4!/b/dPMAAAAAAAAA&amp;bo=SQbkCAAAAAARAJQ!" data-clicklog="pic" data-originurl="||" hotclickPath="0_appid_311_v8.pic_count_9.pic_1" hotdomain="icv6act.qzone.qq.com" data-version="2" data-param="77b935827b9a155a6bb40a00|2184558967|1" data-src="/qzone/photo/zone/icenter_popup.html" data-width="1609" data-height="2276" data-type="popup" data-title="" data-config=""><img src="http://a4.qpic.cn/psb?/V13Uz9Av0QdwLU/iAwmmBXtfvgujAp0vEO1exUuA8tQ6qwbvD27IUHG3c4!/m/dPMAAAAAAAAA&amp;ek=1&amp;kp=1&amp;pt=0&amp;bo=SQbkCAAAAAARAJQ!&amp;t=5&amp;vuin=836242657&amp;tm=1511402400&amp;sce=60-4-3&amp;rf=0-0"  style="margin-left:0px;margin-top:-38px;height:260px;width:185px;"/></a><a  class="img-item  "data-cmd="qz_popup" href="https://user.qzone.qq.com/1460290638/311/"   class="  qz_ichotclick   img-three  " data-topicid="2184558967_77b935827b9a155a6bb40a00__1" data-pickey="77b935827b9a155a6bb40a00,http://b243.photo.store.qq.com/psb?/V13Uz9Av0QdwLU/P3nj6Seo2bFUygSMAMlfo6W9KVYRNjqO3Z.Po8eDYAI!/b/dPMAAAAAAAAA&amp;bo=SQbkCAAAAAARAJQ!" data-clicklog="pic" data-originurl="||" hotclickPath="0_appid_311_v8.pic_count_9.pic_2" hotdomain="icv6act.qzone.qq.com" data-version="2" data-param="77b935827b9a155a6bb40a00|2184558967|2" data-src="/qzone/photo/zone/icenter_popup.html" data-width="1609" data-height="2276" data-type="popup" data-title="" data-config=""><img src="http://a4.qpic.cn/psb?/V13Uz9Av0QdwLU/P3nj6Seo2bFUygSMAMlfo6W9KVYRNjqO3Z.Po8eDYAI!/m/dPMAAAAAAAAA&amp;ek=1&amp;kp=1&amp;pt=0&amp;bo=SQbkCAAAAAARAJQ!&amp;t=5&amp;vuin=836242657&amp;tm=1511402400&amp;sce=60-4-3&amp;rf=0-0"  style="margin-left:0px;margin-top:-38px;height:260px;width:185px;"/></a><a  class="img-item  "data-cmd="qz_popup" href="https://user.qzone.qq.com/1460290638/311/"   class="  qz_ichotclick   img-three  " data-topicid="2184558967_77b935827b9a155a6bb40a00__1" data-pickey="77b935827b9a155a6bb40a00,http://b347.photo.store.qq.com/psb?/V13Uz9Av0QdwLU/qQUB7jKsW4vIFlrkePmyGxE45sUwiyYiH24xMrJkdDk!/b/dFsBAAAAAAAA&amp;bo=SQbkCAAAAAARAJQ!" data-clicklog="pic" data-originurl="||" hotclickPath="0_appid_311_v8.pic_count_9.pic_3" hotdomain="icv6act.qzone.qq.com" data-version="2" data-param="77b935827b9a155a6bb40a00|2184558967|3" data-src="/qzone/photo/zone/icenter_popup.html" data-width="1609" data-height="2276" data-type="popup" data-title="" data-config=""><img src="http://a4.qpic.cn/psb?/V13Uz9Av0QdwLU/qQUB7jKsW4vIFlrkePmyGxE45sUwiyYiH24xMrJkdDk!/m/dFsBAAAAAAAA&amp;ek=1&amp;kp=1&amp;pt=0&amp;bo=SQbkCAAAAAARAJQ!&amp;t=5&amp;vuin=836242657&amp;tm=1511402400&amp;sce=60-4-3&amp;rf=0-0"  style="margin-left:0px;margin-top:-64px;height:260px;width:185px;"/></a><a  class="img-item  "data-cmd="qz_popup" href="https://user.qzone.qq.com/1460290638/311/"   class="  qz_ichotclick   img-three  " data-topicid="2184558967_77b935827b9a155a6bb40a00__1" data-pickey="77b935827b9a155a6bb40a00,http://b242.photo.store.qq.com/psb?/V13Uz9Av0QdwLU/tnL4eS80hhz.MELqcfFNJhv6pAmkMTW2poCez8.LaW0!/b/dPIAAAAAAAAA&amp;bo=SQbkCAAAAAARAJQ!" data-clicklog="pic" data-originurl="||" hotclickPath="0_appid_311_v8.pic_count_9.pic_4" hotdomain="icv6act.qzone.qq.com" data-version="2" data-param="77b935827b9a155a6bb40a00|2184558967|4" data-src="/qzone/photo/zone/icenter_popup.html" data-width="1609" data-height="2276" data-type="popup" data-title="" data-config=""><img src="http://a3.qpic.cn/psb?/V13Uz9Av0QdwLU/tnL4eS80hhz.MELqcfFNJhv6pAmkMTW2poCez8.LaW0!/m/dPIAAAAAAAAA&amp;ek=1&amp;kp=1&amp;pt=0&amp;bo=SQbkCAAAAAARAJQ!&amp;t=5&amp;vuin=836242657&amp;tm=1511402400&amp;sce=60-4-3&amp;rf=0-0"  style="margin-left:0px;margin-top:-38px;height:260px;width:185px;"/></a><a  class="img-item  "data-cmd="qz_popup" href="https://user.qzone.qq.com/1460290638/311/"   class="  qz_ichotclick   img-three  " data-topicid="2184558967_77b935827b9a155a6bb40a00__1" data-pickey="77b935827b9a155a6bb40a00,http://b319.photo.store.qq.com/psb?/V13Uz9Av0QdwLU/Q.9JgZicXr.ZALoI34Awfz9yzhZpIffirJeuqHXpF.g!/b/dD8BAAAAAAAA&amp;bo=SQbkCAAAAAARAJQ!" data-clicklog="pic" data-originurl="||" hotclickPath="0_appid_311_v8.pic_count_9.pic_5" hotdomain="icv6act.qzone.qq.com" data-version="2" data-param="77b935827b9a155a6bb40a00|2184558967|5" data-src="/qzone/photo/zone/icenter_popup.html" data-width="1609" data-height="2276" data-type="popup" data-title="" data-config=""><img src="http://a4.qpic.cn/psb?/V13Uz9Av0QdwLU/Q.9JgZicXr.ZALoI34Awfz9yzhZpIffirJeuqHXpF.g!/m/dD8BAAAAAAAA&amp;ek=1&amp;kp=1&amp;pt=0&amp;bo=SQbkCAAAAAARAJQ!&amp;t=5&amp;vuin=836242657&amp;tm=1511402400&amp;sce=60-4-3&amp;rf=0-0"  style="margin-left:0px;margin-top:-58px;height:260px;width:185px;"/></a><a  class="img-item  "data-cmd="qz_popup" href="https://user.qzone.qq.com/1460290638/311/"   class="  qz_ichotclick   img-three  " data-topicid="2184558967_77b935827b9a155a6bb40a00__1" data-pickey="77b935827b9a155a6bb40a00,http://b319.photo.store.qq.com/psb?/V13Uz9Av0QdwLU/7kxLsP*AN1dcuQsKY.obJR.U5W5ZAclEoq5mPmIFJBo!/b/dD8BAAAAAAAA&amp;bo=SQbkCAAAAAARAJQ!" data-clicklog="pic" data-originurl="||" hotclickPath="0_appid_311_v8.pic_count_9.pic_6" hotdomain="icv6act.qzone.qq.com" data-version="2" data-param="77b935827b9a155a6bb40a00|2184558967|6" data-src="/qzone/photo/zone/icenter_popup.html" data-width="1609" data-height="2276" data-type="popup" data-title="" data-config=""><img src="http://a4.qpic.cn/psb?/V13Uz9Av0QdwLU/7kxLsP*AN1dcuQsKY.obJR.U5W5ZAclEoq5mPmIFJBo!/m/dD8BAAAAAAAA&amp;ek=1&amp;kp=1&amp;pt=0&amp;bo=SQbkCAAAAAARAJQ!&amp;t=5&amp;vuin=836242657&amp;tm=1511402400&amp;sce=60-4-3&amp;rf=0-0"  style="margin-left:0px;margin-top:-64px;height:260px;width:185px;"/></a><a  class="img-item  "data-cmd="qz_popup" href="https://user.qzone.qq.com/1460290638/311/"   class="  qz_ichotclick   img-three  " data-topicid="2184558967_77b935827b9a155a6bb40a00__1" data-pickey="77b935827b9a155a6bb40a00,http://b242.photo.store.qq.com/psb?/V13Uz9Av0QdwLU/QglxfahYu5F2ROWE1LBcbXOhdUiiKsS.4J4Q8Jhkr6Q!/b/dPIAAAAAAAAA&amp;bo=HALkAgAAAAARAM8!" data-clicklog="pic" data-originurl="||" hotclickPath="0_appid_311_v8.pic_count_9.pic_7" hotdomain="icv6act.qzone.qq.com" data-version="2" data-param="77b935827b9a155a6bb40a00|2184558967|7" data-src="/qzone/photo/zone/icenter_popup.html" data-width="540" data-height="740" data-type="popup" data-title="" data-config=""><img src="http://a3.qpic.cn/psb?/V13Uz9Av0QdwLU/QglxfahYu5F2ROWE1LBcbXOhdUiiKsS.4J4Q8Jhkr6Q!/m/dPIAAAAAAAAA&amp;ek=1&amp;kp=1&amp;pt=0&amp;bo=HALkAgAAAAARAM8!&amp;t=5&amp;vuin=836242657&amp;tm=1511402400&amp;sce=60-4-3&amp;rf=0-0"  style="margin-left:0px;margin-top:-34px;height:253px;width:185px;"/></a><a  class="img-item  "data-cmd="qz_popup" href="https://user.qzone.qq.com/1460290638/311/"   class="  qz_ichotclick   img-three  " data-topicid="2184558967_77b935827b9a155a6bb40a00__1" data-pickey="77b935827b9a155a6bb40a00,http://b242.photo.store.qq.com/psb?/V13Uz9Av0QdwLU/NViZNzvcLc9OFh3Hry4x61kkstbUF7WxP1W96CBVJc8!/b/dPIAAAAAAAAA&amp;bo=AgECAQAAAAARADc!" data-clicklog="pic" data-originurl="||" hotclickPath="0_appid_311_v8.pic_count_9.pic_8" hotdomain="icv6act.qzone.qq.com" data-version="2" data-param="77b935827b9a155a6bb40a00|2184558967|8" data-src="/qzone/photo/zone/icenter_popup.html" data-width="258" data-height="258" data-type="popup" data-title="" data-config=""><img src="http://a3.qpic.cn/psb?/V13Uz9Av0QdwLU/NViZNzvcLc9OFh3Hry4x61kkstbUF7WxP1W96CBVJc8!/m/dPIAAAAAAAAA&amp;ek=1&amp;kp=1&amp;pt=0&amp;bo=AgECAQAAAAARADc!&amp;t=5&amp;vuin=836242657&amp;tm=1511402400&amp;sce=60-4-3&amp;rf=0-0"  style="margin-left:0px;margin-top:0px;height:185px;width:185px;"/></a></div></div></div></div></div></div><div class="f-single-foot"><div class="f-op-detail f-detail content-line"><p class="op-list"><a class="item qz_retweet_btn " href="javascript:;" data-cmd="qz_popup" data-version="4" data-isnewtype="1" data-type="ForwardingBox" data-src="/qzone/app/controls/forwardingBox/forwardingBoxFacade.js" data-clicklog="retweet" ><i class="fui-icon icon-op-share"></i></a><span class="item-line"></span>&nbsp;<a href="javascript:;" data-version="6.3" data-cmd="qz_reply" data-link="1" data-clicklog="comment"  class=" qz_btn_reply item "><i class="fui-icon icon-op-comment"></i></a>&nbsp;<span class="item-line"></span><a class="item qz_like_btn_v3 " data-islike="0" data-likecnt="15" data-showcount="0" data-unikey="http://user.qzone.qq.com/1460290638/mood/4e440a57638f155a7d440300" data-curkey="http://user.qzone.qq.com/2184558967/mood/77b935827b9a155a6bb40a00" data-clicklog="like" href="javascript:;"><i class="fui-icon icon-op-praise"></i></a></p><a href="javascript:;" class="state qz_feed_plugin" data-role="Visitor" data-config="311|77b935827b9a155a6bb40a00|2184558967" data-clicklog="visitor">浏览29次</a></div>        <div class="f-ang-t"></div><div class="f-like-list f-like _likeInfo" likeinfo="15"><div class="icon-btn"><a href="javascript:;" data-islike="0" data-likecnt="15" data-showcount="15" data-unikey="http://user.qzone.qq.com/1460290638/mood/4e440a57638f155a7d440300" data-curkey="http://user.qzone.qq.com/2184558967/mood/77b935827b9a155a6bb40a00" data-clicklog="like" class="praise qz_like_prase"><i class="fui-icon icon-list-praise"></i></a><div class="bubble" style="display:none;"><div class="bd">+1</div><b class="arrow arrow-down"></b></div></div><div class="user-list"><span class="f-like-cnt">15人觉得很赞</span></div></div><div class="mod-comments" style="padding:0"><div class="comments-list "><ul><li class="comments-item bor3" data-type="commentroot" data-tid="1" data-uin="779036067" data-nick="~~~~~~~~~~~~·" data-who="1"><div class="comments-item-bd"><div class="single-reply"><div class="ui-avatar"><a href="http://user.qzone.qq.com/779036067" target="_blank"><img class="q_namecard" link="nameCard_779036067 des_779036067" alt="~~~~~~~~~~~~·" src="http://qlogo4.store.qq.com/qzone/779036067/779036067/30" /></a></div><div class="comments-content"><a class="nickname name c_tx q_namecard"  link="nameCard_779036067" target="_blank" href="http://user.qzone.qq.com/779036067">~~~~~~~~~~~~·</a>&nbsp; : <img src="http://qzonestyle.gtimg.cn/qzone/em/e144.png"  title=""/><img src="http://qzonestyle.gtimg.cn/qzone/em/e144.png"  title=""/><div class="comments-op"><span  class=" ui-mr10 state" >昨天 23:48</span><a class="act-reply none" href="javascript:;" data-cmd="qz_reply" data-version="6.4" data-action="http://taotao.qq.com/cgi-bin/emotion_cgi_re_feeds" data-param="t1_source=&amp;t1_uin=2184558967&amp;t1_tid=77b935827b9a155a6bb40a00&amp;t2_uin=779036067&amp;t2_tid=1&amp;subdotype=55702&amp;signin=0&amp;sceneid=100" data-charset="utf-8" data-tuin="" data-config="1|1|1|0|1,taotaoact.qzone.qq.com,@InputReply|1,taotaoact.qzone.qq.com,@ClickReply|1,taotaoact.qzone.qq.com,commentPresentClick"><b class="hide-clip">回复</b></a></div></div></div></div></li></ul></div><div class="mod-commnets-poster feedClickCmd comment_default_inputentry" data-cmd="qz_reply" data-version="6" data-action="http://taotao.qq.com/cgi-bin/emotion_cgi_re_feeds" data-param="t1_source=&amp;t1_uin=2184558967&amp;t1_tid=77b935827b9a155a6bb40a00&amp;signin=0&amp;sceneid=100" data-charset="utf-8" data-maxLength="" data-tuin="2184558967" data-config="1|1|1|1,b52,with_fwd,同时转发;0|1,taotaoact.qzone.qq.com,@InputReply|1,taotaoact.qzone.qq.com,@ClickReply|1,taotaoact.qzone.qq.com,commentPresentClick"  data-tid="" ><div class="comments-poster-bd comments-poster-default"><div class="comments-box" data-clicklog="comment"><div class="textinput textinput-default bor2" contenteditable="true" alt="replybtn" placeholder="评论"><a class="c_tx3" href="javascript:void(0);" alt="replybtn">评论</a></div><div class="mod-insert-img"><a href="javascript:;" data-cmd="qz_quick_upload_img" class="btn-insert-img bg"><i class="icon-camera-16"></i></a></div></div></div></div></div>    </div></li>                                                                                                                                                 <li class="f-single f-s-s" id="fct_2987533319_202_2_1511363351_0_1"><div class="f-single-head f-aside"><div class="f-adorn-top"></div>    <div class="user-pto"><a href="http://user.qzone.qq.com/2987533319" target="_blank" class="user-avatar q_namecard f-s-a" link="nameCard_2987533319" data-clicklog="avatar"><img src="https://qlogo4.store.qq.com/qzone/2987533319/2987533319/50?1502999741"></a></div><div class="user-op"><a href="javascript:;" class="arrow-down" data-cmd="qz_opr_more" data-moreoperate="1"><i class="fui-icon icon-arrow-down"></i></a>        </div><div class="user-info"><div class="f-nick"><a target="_blank" href="http://user.qzone.qq.com/2987533319"  data-clicklog="nick" class="f-name q_namecard " link="nameCard_2987533319">皮永飞</a>  </div><div class="info-detail"><span  class=" ui-mr8 state" >昨天 23:09</span><a href="javascript:;" data-cmd="qz_sign" class="f-sign-show state" title="我也要设置"></a></div></div></div><div class="f-single-content f-wrap"><div class="f-item f-s-i" id="feed_2987533319_202_2_1511363351_0_1" data-feedsflag="" data-iswupfeed="1" data-key="bfddgdbbfb" data-specialtype="" data-extend-info="0_0_0_0_0_0_0|08009c8002004001|0000000000000000" data-functype="func_friend_feed" data-hasfollowed="1"><div class="f-info">哇哦，西柚车队也有微信公众号了，赞赞\(≧▽≦)/</div><div class="qz_summary wupfeed" id="hex_2987533319_202_2_1511363351_0_1"><i class="none" name="feed_data"  data-bitmap="08009c8002004001" data-yybitmap="0000000000000000" data-vipstarbitmap="0000000040000000" data-fkey="bfddgdbbfb" data-tid="1511363351" data-uin="2987533319" data-origfkey="" data-origtid="" data-origuin="3044456550" data-subid="" data-totweet="" data-issignin="" data-source="" data-retweetcount="3" data-stat="vvCs9YFze4FGZdZ2i2OOxvhECR8!C4sUa1fh26U!kKiBV95NDAYoy18Y8YHmSI4We4!vadXnHesdWcbZpyP6oq65mXtvBXGqXXz84MDJmuDFy2pe0jHMeAr/WHnzfjCWe0EKb99vj7SwMmJY4T4HgOhjk5JP5JhzWiZaGh/3xEQ_"   data-topicid="2987533319_1511363351"    data-feedstype="100"  data-abstime="1511363351"   data-iswupfeed="1"  data-platformid="50"  data-accessright="1"></i><div class="f-ct" ><div class="fui-left-right f-ct-txtimg f-ct-imgtxt f-ct-fixed "><div class="img-box"><a href="http://mp.weixin.qq.com/s/UoCfy-hp1FrPCoT9vafpVw" target="_blank" title="点击查看" data-clicklog="pic_jump"  ><img src="http://qqadapt.qpic.cn/adapt/0/dd309142-6204-0df0-ebb4-bcc562fa8da1/200?pt=0&ek=1&kp=1&sce=60-4-3"  style="margin-left:-30px;height:120px;"/></a></div><?# 判断feeds正文内容是否只有url类型，没有text类型?><div class="txt-box one-line"><h4 style="word-break:break-all;" class="txt-box-title t-fixed"><a href="http://mp.weixin.qq.com/s/UoCfy-hp1FrPCoT9vafpVw" target="_blank"  class=" c_tx">http://mp.weixin.qq.com/s/UoCfy-hp1FrPCoT9vafpVw</a>&nbsp;</h4><a href="http://mp.weixin.qq.com/s/UoCfy-hp1FrPCoT9vafpVw" target="_blank"  class=" f-name info state ellipsis-two"></a>&nbsp;</div></div></div></div></div></div><div class="f-single-foot"><div class="f-op-detail f-detail content-line"><p class="op-list"><a class="item qz_retweet_btn " href="javascript:;" data-cmd="qz_popup" data-version="4" data-isnewtype="1" data-type="ForwardingBox" data-src="/qzone/app/controls/forwardingBox/forwardingBoxFacade.js" data-clicklog="retweet" ><i class="fui-icon icon-op-share"></i></a><span class="item-line"></span>&nbsp;<a href="javascript:;" data-version="6.3" data-cmd="qz_reply" data-link="1" data-clicklog="comment"  class=" qz_btn_reply item "><i class="fui-icon icon-op-comment"></i></a>&nbsp;<span class="item-line"></span><a class="item qz_like_btn_v3 " data-islike="0" data-likecnt="28" data-showcount="1" data-unikey="http://mp.weixin.qq.com/s/UoCfy-hp1FrPCoT9vafpVw" data-curkey="002987533319001511363351" data-clicklog="like" href="javascript:;"><i class="fui-icon icon-op-praise"></i></a></p><a href="javascript:;" class="state qz_feed_plugin" data-role="Visitor" data-config="202|1511363351|2987533319" data-clicklog="visitor">浏览229次</a></div>        <div class="f-ang-t"></div><div class="f-like-list f-like _likeInfo" likeinfo="28"><div class="icon-btn"><a href="javascript:;" data-islike="0" data-likecnt="28" data-showcount="28" data-unikey="http://mp.weixin.qq.com/s/UoCfy-hp1FrPCoT9vafpVw" data-curkey="002987533319001511363351" data-clicklog="like" class="praise qz_like_prase"><i class="fui-icon icon-list-praise"></i></a><div class="bubble" style="display:none;"><div class="bd">+1</div><b class="arrow arrow-down"></b></div></div><div class="user-list"><a href="http://user.qzone.qq.com/947118418" class="item q_namecard" target="_blank" link="nameCard_947118418 des_947118418">苗幼林</a>等<span class="f-like-cnt">28</span>人觉得很赞</div></div><div class="mod-comments" style="padding:0"><div class="comments-list "><ul><li class="comments-item bor3" data-type="commentroot" data-tid="1511363783" data-uin="1593032586" data-nick="夏代有工的玉" data-who="1"><div class="comments-item-bd"><div class="single-reply"><div class="ui-avatar"><a href="http://user.qzone.qq.com/1593032586" target="_blank"><img class="q_namecard" link="nameCard_1593032586 des_1593032586" alt="夏代有工的玉" src="http://qlogo3.store.qq.com/qzone/1593032586/1593032586/30" /></a></div><div class="comments-content"><a class="nickname name c_tx q_namecard"  link="nameCard_1593032586" target="_blank" href="http://user.qzone.qq.com/1593032586">夏代有工的玉</a>&nbsp; : 关注一波儿<div class="comments-op"><span  class=" ui-mr10 state" >昨天 23:16</span><a class="act-reply none" href="javascript:;" data-cmd="qz_reply" data-version="6.4" data-action="http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshareaddcomment" data-param="2987533319&#39;&#39;1511363351&#39;&#39;1511363783&#39;&#39;1593032586&#39;&#39;&#39;&#39;&#39;&#39;100" data-charset="utf-8" data-tuin="" data-config="1|1|0|0|0|0|0"><b class="hide-clip">回复</b></a></div></div></div><div class="comments-list mod-comments-sub"><ul><li class="comments-item bor3" data-type="replyroot" data-tid="1511363974" data-uin="2987533319" data-nick="皮永飞" data-who="1"><div class="comments-item-bd"><div class="single-reply"><div class="ui-avatar"><a href="http://user.qzone.qq.com/2987533319" target="_blank"><img class="q_namecard" link="nameCard_2987533319 des_2987533319" alt="皮永飞" src="http://qlogo4.store.qq.com/qzone/2987533319/2987533319/30?1502999741" /></a></div><div class="comments-content"><a class="nickname name c_tx q_namecard"  link="nameCard_2987533319" target="_blank" href="http://user.qzone.qq.com/2987533319">皮永飞</a>&nbsp;回复<a class="nickname name c_tx q_namecard"  link="nameCard_1593032586" target="_blank" href="http://user.qzone.qq.com/1593032586">夏代有工的玉</a>&nbsp; : 谢谢支持.<div class="comments-op"><span  class=" ui-mr10 state" >昨天 23:19</span><a class="act-reply none" href="javascript:;" data-cmd="qz_reply" data-version="6.4" data-action="http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshareaddcomment" data-param="2987533319&#39;&#39;1511363351&#39;&#39;1511363783&#39;&#39;1593032586&#39;&#39;&#39;&#39;&#39;&#39;100" data-charset="utf-8" data-tuin="" data-config="1|1|0|0|0|0|0"><b class="hide-clip">回复</b></a></div></div></div></div></li></ul></div></div></li></ul></div><div class="mod-commnets-poster feedClickCmd comment_default_inputentry" data-cmd="qz_reply" data-version="6" data-action="http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshareaddcomment" data-param="2987533319&#39;&#39;1511363351&#39;&#39;-1&#39;&#39;0&#39;&#39;&#39;&#39;&#39;&#39;100" data-charset="utf-8" data-maxLength="" data-tuin="2987533319" data-config="1|1|0|0|0|0|0"  data-tid="" ><div class="comments-poster-bd comments-poster-default"><div class="comments-box" data-clicklog="comment"><div class="textinput textinput-default bor2" contenteditable="true" alt="replybtn" placeholder="评论"><a class="c_tx3" href="javascript:void(0);" alt="replybtn">评论</a></div><div class="mod-insert-img"><a href="javascript:;" data-cmd="qz_quick_upload_img" class="btn-insert-img bg"><i class="icon-camera-16"></i></a></div></div></div></div></div>    </div></li>                                                                                                                                               <li class="f-single f-s-s" id="fct_1042609362_311_0_1511361602_0_1"><div class="f-single-head f-aside"><div class="f-adorn-top"></div>    <div class="user-pto"><a href="http://user.qzone.qq.com/1042609362" target="_blank" class="user-avatar q_namecard f-s-a" link="nameCard_1042609362" data-clicklog="avatar"><img src="https://qlogo3.store.qq.com/qzone/1042609362/1042609362/50?1480896531"></a></div><div class="user-op"><a href="javascript:;" class="arrow-down" data-cmd="qz_opr_more" data-moreoperate="1"><i class="fui-icon icon-arrow-down"></i></a>        </div><div class="user-info"><div class="f-nick"><a target="_blank" href="http://user.qzone.qq.com/1042609362"  data-clicklog="nick" class="f-name q_namecard " link="nameCard_1042609362">宋雪</a>  </div><div class="info-detail"><span  class=" ui-mr8 state" >昨天 22:40</span><a href="javascript:;" data-cmd="qz_sign" class="f-sign-show state" title="我也要设置"></a></div></div></div><div class="f-single-content f-wrap"><div class="f-item f-s-i" id="feed_1042609362_311_0_1511361602_0_1" data-feedsflag="" data-iswupfeed="1" data-key="d2f4243e428c155a572b0200" data-specialtype="" data-extend-info="0_0_0_0_0_0_0|08d594800202c101|0000000000000001" data-functype="func_friend_feed" data-hasfollowed="1"><div class="f-info">打了7分钟的电话，有6分半都是我在说，我爸心里是不是在想，是不是当初抱错了？话这么多<img src="http://qzonestyle.gtimg.cn/qzone/em/e400824.gif" title=""/><img src="http://qzonestyle.gtimg.cn/qzone/em/e400824.gif" title=""/><img src="http://qzonestyle.gtimg.cn/qzone/em/e400824.gif" title=""/><img src="http://qzonestyle.gtimg.cn/qzone/em/e400905.gif" title=""/><img src="http://qzonestyle.gtimg.cn/qzone/em/e400905.gif" title=""/><img src="http://qzonestyle.gtimg.cn/qzone/em/e400905.gif" title=""/><img src="http://qzonestyle.gtimg.cn/qzone/em/e400905.gif" title=""/></div><div class="qz_summary wupfeed" id="hex_1042609362_311_0_1511361602_0_1"><i class="none" name="feed_data"  data-bitmap="08d594800202c101" data-yybitmap="0000000000000001" data-vipstarbitmap="0000000040000000" data-fkey="d2f4243e428c155a572b0200" data-tid="d2f4243e428c155a572b0200" data-uin="1042609362" data-origfkey="" data-origtid="d2f4243e428c155a572b0200" data-origuin="1042609362" data-subid="" data-totweet="" data-issignin="" data-source="" data-retweetcount="0" data-stat="exNDgYmCtvh99ZDrytoWlkGo4tOi0oVK3SQ/dwEf0cgxg0GbsjOSaSxUaapUI0FXwd9TcN7TxzJ9c/1sFt/lTLe1Y9U2mVUr3SQ/dwEf0cgxg0GbsjOSaW7FzuWSNzadQCBp!TIziyeQ5ldoD!kiYifSF76V!bVgvR/rSnjBH2zSZaVFEgvENIJjJvdOSOT!MzAkbzg1AwJL4IdJ3zDPZRXi1DDZK5ON_"   data-topicid="1042609362_d2f4243e428c155a572b0200__1"    data-feedstype="100"  data-abstime="1511361602"   data-iswupfeed="1"  data-platformid="54"  data-accessright="1"></i></div></div></div><div class="f-single-foot"><div class="f-op-detail f-detail content-line"><p class="op-list"><a class="item qz_retweet_btn " href="javascript:;" data-cmd="qz_popup" data-version="4" data-isnewtype="1" data-type="ForwardingBox" data-src="/qzone/app/controls/forwardingBox/forwardingBoxFacade.js" data-clicklog="retweet" ><i class="fui-icon icon-op-share"></i></a><span class="item-line"></span>&nbsp;<a href="javascript:;" data-version="6.3" data-cmd="qz_reply" data-link="1" data-clicklog="comment"  class=" qz_btn_reply item "><i class="fui-icon icon-op-comment"></i></a>&nbsp;<span class="item-line"></span><a class="item qz_like_btn_v3 " data-islike="0" data-likecnt="16" data-showcount="16" data-unikey="http://user.qzone.qq.com/1042609362/mood/d2f4243e428c155a572b0200" data-curkey="http://user.qzone.qq.com/1042609362/mood/d2f4243e428c155a572b0200" data-clicklog="like" href="javascript:;"><i class="fui-icon icon-op-praise"></i></a></p><a href="javascript:;" class="state qz_feed_plugin" data-role="Visitor" data-config="311|d2f4243e428c155a572b0200|1042609362" data-clicklog="visitor">浏览176次</a></div>        <div class="f-ang-t"></div><div class="f-like-list f-like _likeInfo" likeinfo="16"><div class="icon-btn"><a href="javascript:;" data-islike="0" data-likecnt="16" data-showcount="16" data-unikey="http://user.qzone.qq.com/1042609362/mood/d2f4243e428c155a572b0200" data-curkey="http://user.qzone.qq.com/1042609362/mood/d2f4243e428c155a572b0200" data-clicklog="like" class="praise qz_like_prase"><i class="fui-icon icon-list-praise"></i></a><div class="bubble" style="display:none;"><div class="bd">+1</div><b class="arrow arrow-down"></b></div></div><div class="user-list"><a href="http://user.qzone.qq.com/397612783" class="item q_namecard" target="_blank" link="nameCard_397612783 des_397612783">完全民事行为能力人</a>、<a href="http://user.qzone.qq.com/676893174" class="item q_namecard" target="_blank" link="nameCard_676893174 des_676893174">桔子宝宝<img src="http://qzonestyle.gtimg.cn/qzone/em/e258182.gif" title=""/></a>、<a href="http://user.qzone.qq.com/945256136" class="item q_namecard" target="_blank" link="nameCard_945256136 des_945256136">一生太短。</a>、<a href="http://user.qzone.qq.com/1043456495" class="item q_namecard" target="_blank" link="nameCard_1043456495 des_1043456495">小可爱</a>、<a href="http://user.qzone.qq.com/1097784302" class="item q_namecard" target="_blank" link="nameCard_1097784302 des_1097784302">木</a>、<a href="http://user.qzone.qq.com/1097827997" class="item q_namecard" target="_blank" link="nameCard_1097827997 des_1097827997">Ansel</a>、<a href="http://user.qzone.qq.com/1164316683" class="item q_namecard" target="_blank" link="nameCard_1164316683 des_1164316683">手心向上</a>、<a href="http://user.qzone.qq.com/1342864826" class="item q_namecard" target="_blank" link="nameCard_1342864826 des_1342864826">╭L</a>、<a href="http://user.qzone.qq.com/1455802755" class="item q_namecard" target="_blank" link="nameCard_1455802755 des_1455802755">逗逗逗</a>、<a href="http://user.qzone.qq.com/1622592223" class="item q_namecard" target="_blank" link="nameCard_1622592223 des_1622592223">chen</a>、<a href="http://user.qzone.qq.com/1643387601" class="item q_namecard" target="_blank" link="nameCard_1643387601 des_1643387601">从前的人   多认真</a>、<a href="http://user.qzone.qq.com/1711287586" class="item q_namecard" target="_blank" link="nameCard_1711287586 des_1711287586">星光@</a>、<a href="http://user.qzone.qq.com/2447379367" class="item q_namecard" target="_blank" link="nameCard_2447379367 des_2447379367">Ying</a>、<a href="http://user.qzone.qq.com/2461444500" class="item q_namecard" target="_blank" link="nameCard_2461444500 des_2461444500">︷冰茉冷薇℉</a>、<a href="http://user.qzone.qq.com/2471792080" class="item q_namecard" target="_blank" link="nameCard_2471792080 des_2471792080">焰君·沉默</a>、<a href="http://user.qzone.qq.com/2717327797" class="item q_namecard" target="_blank" link="nameCard_2717327797 des_2717327797">叶玲</a>共<span class="f-like-cnt">16</span>人觉得很赞</div></div><div class="mod-comments" style="padding:0"><div class="mod-commnets-poster feedClickCmd comment_default_inputentry" data-cmd="qz_reply" data-version="6" data-action="http://taotao.qq.com/cgi-bin/emotion_cgi_re_feeds" data-param="t1_source=&amp;t1_uin=1042609362&amp;t1_tid=d2f4243e428c155a572b0200&amp;signin=0&amp;sceneid=100" data-charset="utf-8" data-maxLength="" data-tuin="1042609362" data-config="1|1|1|1,b52,with_fwd,同时转发;0|1,taotaoact.qzone.qq.com,@InputReply|1,taotaoact.qzone.qq.com,@ClickReply|1,taotaoact.qzone.qq.com,commentPresentClick"  data-tid="" ><div class="comments-poster-bd comments-poster-default"><div class="comments-box" data-clicklog="comment"><div class="textinput textinput-default bor2" contenteditable="true" alt="replybtn" placeholder="评论"><a class="c_tx3" href="javascript:void(0);" alt="replybtn">评论</a></div><div class="mod-insert-img"><a href="javascript:;" data-cmd="qz_quick_upload_img" class="btn-insert-img bg"><i class="icon-camera-16"></i></a></div></div></div></div></div>    </div></li>                                                                                                                                           <li class="f-single f-s-s f-single-biz" id="fct_20050606_5000_1_1511400387_0_1"><div class="f-single-top"><span>广告</span><a href="javascript:;" class="arrow-down adFeedsItem" data-cmd="qz_opr_more"><i class="fui-icon icon-arrow-down"></i></a><div class="qz-bubble" style="display: none;">            <div class="bubble-i op-list">                <a href="javascript:;" class="item hot-close"><i class="fui-icon icon-hide"></i>关闭</a>            </div>            <b class="bubble-trig ui-trigbox ui-trigbox-t">                <b class="ui-trig"></b>                <b class="ui-trig ui-trig-up"></b>            </b>        </div></div><div class="f-single-content f-wrap"><div class="f-info">      <a class="report-qboss" href="http://rc.qzone.qq.com/1105695953?via=QZ.SEVENTH.FEED&app_custom=essence " target="_blank" data-traceinfo="2386_199455_578_1_0_0" >一人一宠，刀刀暴击，兄弟今晚我们血战皇城！>>></a>    </div>    <div class="f-ct">            <div class="fui-txtimg">                <div class="img-box"><a class="report-qboss" href="http://rc.qzone.qq.com/1105695953?via=QZ.SEVENTH.FEED&app_custom=essence " target="_blank" data-traceinfo="2386_199455_578_1_0_0" ><img src="http://qzonestyle.gtimg.cn/qzone/space_item/boss_pic/2386_2017_11/1511343086245_208912.jpg" style="width:560px"/></a>                </div>                <div class="detail-box clearfix">                    <p class="state tip">                    <b style="color: #5d7895;">1942613</b>个网友在玩</p>                    <div class="fixed-right">                        <a class="fixed-btn" href="http://rc.qzone.qq.com/1105695953?via=QZ.SEVENTH.FEED&app_custom=essence " target="_blank" data-traceinfo="2386_199455_578_1_0_0" class="fixed-btn report-qboss">开始游戏                        </a>                    </div>                </div>            </div>        </div></div></li></ul>
                                    <div style="visibility:hidden;" id="feed_friend_tips"></div>
                                    <img style="width:1px;height:1px;" src="about:blank" onerror="window.FIRST_PAGE_FEEDS_TIME=new Date();" />
                                    <script type="text/javascript">
                                        window.FIRST_PAGE_FEEDS_TIME2=new Date();
                                        setTimeout(function(){window.FIRST_PAGE_FEEDS_TIME3=new Date();}, 0);
                                    </script>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div id="feed_me" class="none">
                        <div class="fn-feed-control-v2 clearfix">
                            <div class="control-inner">
                                <div class="feed-control-tab" id="me_feed_control">
                                    <a title="查看我的空间动态" class="item-on item-on-slt" id="feed_tab_my" href="javascript:;">我的空间动态<span id="tab_menu_my_cnt" class="sn-count none">0</span><i class="dot dot-tl"></i><i class="dot dot-tr"></i><i class="dot dot-bl"></i><i class="dot dot-br"></i></a>
                                </div>
                                <div class="feed-control-tab-op">
                                    <label class="feed-choose-item" for="feed_me_filter_friend"><i class="ui-icon qz-checkbox-on"></i><input id="feed_me_filter_friend" class="none" type="checkbox" checked="checked">显示非好友评论</label>
                                    <a id="feed_me_refresh" title="刷新动态" href="javascript:;" class="item-left"><i class="ui-icon  icon-refresh-v9"></i></a>
                                </div>
                            </div>
                        </div>
                        <div class="fn-feed-container">
                            <div class="feed  feed-v9">
                                <div class="feed_inner"><div style="display:none;" id="feed_me_update" class="tipsbox bg2"></div><ul id="feed_me_list"></ul><div id="feed_me_tips" style="visibility:hidden;"></div></div>
                            </div>
                        </div>
                    </div>

                    
                    <div id="feed_mv" class="none">
                        <div class="fn-feed-control-v2 clearfix">
                            <div class="control-inner">
                                <div class="feed-control-tab" id="mv_feed_control">
                                    <a title="查看直播广场" class="item-on item-on-slt" id="feed_tab_mv" href="javascript:;">直播广场<i class="dot dot-tl"></i><i class="dot dot-tr"></i><i class="dot dot-bl"></i><i class="dot dot-br"></i></a>
                                </div>
                                <div class="feed-control-tab-op">
                                    <a id="feed_mv_refresh" title="刷新动态" href="javascript:;" class="item-left"><i class="ui-icon  icon-refresh-v9"></i></a>
                                </div>
                            </div>
                        </div>
                        <div class="fn-feed-content">
                            <div class="fn-feed-slide">
                                <div class="slide-wrapper">
                                    <div class="slide-content">
                                        <ul style="position: relative;width: 766px;height: 252px;">
                                            <!-- slide content -->
                                        </ul>
                                    </div>
                                   <div class="slide-btn" style="cursor:pointer">
                                        <a class="prev" href="javascript:void(0);">
                                            <i class="ui-icon icon-prev"></i>
                                        </a>
                                        <a class="next" href="javascript:void(0);">
                                            <i class="ui-icon icon-next"></i>
                                        </a>
                                        <div class="hd">
                                            <ul>
                                                <!-- slide btn -->
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="fn-feed-title clearfix">
                                <div class="feed-control-tab">
                                    <span><!-- 直播广场 --></span></div>
                                <div class="feed-control-tab-op">
                                    <label class="feed-live-star">
                                        <i class="ui-icon icon-star"></i>
                                        <span class="j-balance"></span>
                                        <a href="//h5.qzone.qq.com/vip/paycoin" target="_blank"> 充值</a>
                                    </label>
                                </div>
                            </div>
                            <div class="fn-feed-list">
                                <ul class="item-list clearfix" id="feed_mv_list">
                                    <!-- feed -->
                                </ul>
                            </div>
                        </div>
                    </div>

                    
                    <div id="feed_sdc" class="none">
                        <div class="fn-feed-control-v2 clearfix">
                            <div class="control-inner">
                                <div class="feed-control-tab">
                                    <a id="yearAll" href="javascript:;" class="item-on item-on-slt" data-year="2016">全部</a>
                                    <span class="line"></span>
                                    <a id="year2016" href="javascript:;" class="item-on">2016</a>
                                    <span class="line"></span>
                                    <a id="year2015" href="javascript:;" class="item-on">2015</a>
                                    <span class="line"></span>
                                    <a id="year2014" href="javascript:;" class="item-on">2014</a>
                                </div>
                                <div class="feed-control-tab-op">
                                    <a href="javascript:;" title="刷新动态" class="item-left"><i class="ui-icon  icon-refresh-v9"></i></a>
                                    <span class="line"></span>
                                    <a href="javascript:;" title="动态设置" class="item-right"><i class="ui-icon  icon-set-v9"></i></a>
                                </div>
                            </div>
                        </div>
                        <div class="fn-feed-container beforeyear-pop">
                            <div class="feed  feed-v9">
                                <div class="feed_inner">
                                    <ul id="feed_sdc_list_2016" class="feed_sdc_list"></ul>
                                    <ul id="feed_sdc_list_2015" class="feed_sdc_list"></ul>
                                    <ul id="feed_sdc_list_2014" class="feed_sdc_list"></ul>
                                    <div id="feed_sdc_tips" style="visibility:hidden;" class="f-more-label"></div> 
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="col-main-sidebar">
                    
                    <div id="QM_Container_31">
                        <div id="QM_100004_Title" class="hd none"></div>
                        <div id="QM_100004_Body" class="bd">
                            <div class="fn-checkin-btn">
    <div class="checkin-btn m11d23">
        <div class="ck-time">
            <span class="ck-week">周四</span>
            <span class="ck-day">11.23</span>
        </div>
        <a href="javascript:void(0);" id="checkin_button" onclick="QM&&QM.checkin&&QM.checkin.clickCheckinButton();return false;" class="ck-btn">签到<span class="ck-clip"></span></a>
        <div class="ck-count">
            <span class="ck-count-bg icenter-font">o</span>
            <span class="ck-count-num">7</span>
            <span class="ck-count-word">Days</span>
        </div>
        <span class="ck-flag c_tx4"></span>
        <div class="ck-new-flag"></div>
    </div>
</div>


                        </div>
                        <div id="QM_100004_Bottom" class="ft none"></div>
                    </div>
                    
                    
                        <div id="QM_Container_100005" class="icenter-right-mod icenter-right-ad">
                            <div id="QM_100005_Title" class="hd none">
                                <h3>精彩生活</h3>
                            </div>
                            <div id="QM_100005_Body" class="bd" style="height:120px;">
                                

<div class="gdtads_box">
<div class="gdtads_img" id="gdtLifeCnt">
<a href="http://c.gdt.qq.com/gdt_click.fcg?viewid=vLJaZSeeHYb5oxcsIR!fBdDWnGBGtnitvU!cqCzhAM0UY8n20hLwyNocxZyQ6zzOh5ujnaXQmoz_EHXQJ39RP5UhFC24jO47EYenot4buH67SfbqV7Ddq3KdHFCKs77Pu9Ho1cL5QYzFVdi6esoxvA&jtype=0&via=06000101310DD4CF&i=1&os=0" target="_blank" id="gdtLifelink" class="gdtads_img_link"><img src="http://pgdt.gtimg.cn/gdt/0/DAAAaWTADcAB4AAdBZcHheCo00XEPv.jpg/0?ck=936b9503b4ab1661e18b03f76cc501a5" id="gdtLifeImg" alt="" /></a>
<div class="change_box _js_next" style="display: none;" id="gdtLifeNext">
<a href="javascript:;" onclick="return false;"><i class="icon_change"></i></a>
</div>
<div class="gdtads_loading" id="gdtLifeLoading" style="display: none">Loading...</div>
<img src="http://v.gdt.qq.com/gdt_stats.fcg?viewid=vLJaZSeeHYb5oxcsIR!fBdDWnGBGtnitvU!cqCzhAM0UY8n20hLwyNocxZyQ6zzOh5ujnaXQmoz_EHXQJ39RP5UhFC24jO47EYenot4buH67SfbqV7Ddq3KdHFCKs77Pu9Ho1cL5QYzFVdi6esoxvA&i=1&os=0" style="width:1px;height: 1px; visibility: hidden;" />
<input type="hidden" id="gdtLifealist" value="" />
</div>
</div>


<input type="hidden" id="gdtLifeHtml" value="1" />
<input type="hidden" id="gdtLifecn" value="" />
<input type="hidden" id="gdtLifeexptime" value="" />
<input type="hidden" id="gdtLifeordlist" value="" />

<!--[if !IE]>|xGv00|a99ae7a130aa7e7004caa47c0fffc884<![endif]-->

                            </div>
                            <div id="QM_100005_Bottom" class="ft none">
                                
                            </div>
                        </div>
                    
					
                    <div id="QM_Container_100002" class="icenter-right-mod">
                        <div id="QM_100002_Title" class="hd">
                            <h3>大家都在看</h3>
                        </div>
                        <div id="QM_100002_Body" class="bd">
                            <div class="fn_hotTopic_v5">
                                <ol>
                                    <li class="topic_item" key="http://rc.qzone.qq.com/1106193011?via=QZ.ISWATCHING&app_custom=essence" feedkey="" data-url="http://rc.qzone.qq.com/1106193011?via=QZ.ISWATCHING&amp;app_custom=essence&amp;referer=hot_topic" qbosskey="2129_199345_439_1_100586_113861"><a class="topic_avatar" target="_blank" href="http://rc.qzone.qq.com/1106193011?via=QZ.ISWATCHING&amp;app_custom=essence&amp;referer=hot_topic"><img src="http://qzonestyle.gtimg.cn/qzone/space_item/boss_pic/2129_2017_11/1511333280496_795008.jpg" alt=""></a><div class="topic_main"><div class="topic_title"><a target="_blank" class="c_tx2 title_txt topic_text" href="http://rc.qzone.qq.com/1106193011?via=QZ.ISWATCHING&amp;app_custom=essence&amp;referer=hot_topic">这个最强职业，一个技能能秒全屏？</a></div><div class="topic_op"><a href="javascript:;" class="topic_op_link"><i class="ui_icon icon_hottopic_praise"></i><span class="act_text c_tx">赞</span></a> <span class="topic_op_num bor2"><span class="act_count">1696</span><b class="ui_trigbox ui_trigbox_l"><b class="ui_trig bor2"></b><b class="ui_trig ui_trig_up bor_bg"></b></b></span></div></div></li><li class="topic_item" key="http://user.qzone.qq.com/3255016169/mood/e99a03c2d28a015add240d00.1" feedkey="" data-url="http://user.qzone.qq.com/3255016169/mood/e99a03c2d28a015add240d00.1?referer=hot_topic" qbosskey="2129_199149_563_1_100612_113729"><a class="topic_avatar" target="_blank" href="http://user.qzone.qq.com/3255016169/mood/e99a03c2d28a015add240d00.1?referer=hot_topic"><img src="http://qzonestyle.gtimg.cn/qzone/space_item/boss_pic/2129_2017_11/1511248699854_266749.png" alt=""></a><div class="topic_main"><div class="topic_title"><a target="_blank" class="c_tx2 title_txt topic_text" href="http://user.qzone.qq.com/3255016169/mood/e99a03c2d28a015add240d00.1?referer=hot_topic">杨洋，时光深处的你，美好如初见！</a></div><div class="topic_op"><a href="javascript:;" class="topic_op_link"><i class="ui_icon icon_hottopic_praise"></i><span class="act_text c_tx">赞</span></a> <span class="topic_op_num bor2"><span class="act_count">8</span><b class="ui_trigbox ui_trigbox_l"><b class="ui_trig bor2"></b><b class="ui_trig ui_trig_up bor_bg"></b></b></span></div></div></li>
                                    
                                        

<li class="topic_item" 

data-gdt="http://analy.qq.com/cgi-bin/apptrace?appid_via=100631368_1A000101310DD4CF&platform=1&action=200"

data-url="http://c.gdt.qq.com/gdt_click.fcg?viewid=BXkkiCKzz_X5oxcsIR!fBRHSr0dSX2Vkwxu1Z!5NjPtMS_I5V9GVVcgCUb9CLtNtOlFCA5pbPDzJ3PRqHrpwcNGwPnsL05pjcqeyEbM6HfFV!0pcopa0V0A6Q8pTUnHCHP4f2jSVMTI&jtype=0&via=1A000101310DD4CF&i=1&os=0"
>
<a class="topic_avatar" target="_blank" href="http://c.gdt.qq.com/gdt_click.fcg?viewid=BXkkiCKzz_X5oxcsIR!fBRHSr0dSX2Vkwxu1Z!5NjPtMS_I5V9GVVcgCUb9CLtNtOlFCA5pbPDzJ3PRqHrpwcNGwPnsL05pjcqeyEbM6HfFV!0pcopa0V0A6Q8pTUnHCHP4f2jSVMTI&jtype=0&via=1A000101310DD4CF&i=1&os=0">
<img src="http://pgdt.gtimg.cn/gdt/0/transformer_10212651923126594853_67.jpg/0?ck=2cd83f96b821ed4391da9fc4e936069e" alt="">
</a>
<div class="topic_main">
<div class="topic_title"><a target="_blank" class="c_tx2 title_txt topic_text" href="http://c.gdt.qq.com/gdt_click.fcg?viewid=BXkkiCKzz_X5oxcsIR!fBRHSr0dSX2Vkwxu1Z!5NjPtMS_I5V9GVVcgCUb9CLtNtOlFCA5pbPDzJ3PRqHrpwcNGwPnsL05pjcqeyEbM6HfFV!0pcopa0V0A6Q8pTUnHCHP4f2jSVMTI&jtype=0&via=1A000101310DD4CF&i=1&os=0">做一回加勒比海盗</a>
</div>
<div class="topic_op" >
<a href="http://c.gdt.qq.com/gdt_click.fcg?viewid=BXkkiCKzz_X5oxcsIR!fBRHSr0dSX2Vkwxu1Z!5NjPtMS_I5V9GVVcgCUb9CLtNtOlFCA5pbPDzJ3PRqHrpwcNGwPnsL05pjcqeyEbM6HfFV!0pcopa0V0A6Q8pTUnHCHP4f2jSVMTI&jtype=0&via=1A000101310DD4CF&i=1&os=0" target="_blank" class="topic_op_link"><i class="ui_icon icon_hottopic_prefer"></i><span class="act_text c_tx">去看看</span></a>
<span class="topic_op_num bor2">
<span class="act_count">71</span>
<b class="ui_trigbox ui_trigbox_l"><b class="ui_trig bor2"></b><b class="ui_trig ui_trig_up bor_bg"></b></b>
</span>
</div>
</div>
<img src="http://v.gdt.qq.com/gdt_stats.fcg?viewid=BXkkiCKzz_X5oxcsIR!fBRHSr0dSX2Vkwxu1Z!5NjPtMS_I5V9GVVcgCUb9CLtNtOlFCA5pbPDzJ3PRqHrpwcNGwPnsL05pjcqeyEbM6HfFV!0pcopa0V0A6Q8pTUnHCHP4f2jSVMTI&i=1&os=0" width="1" height="1" style="visibility: hidden;" />

<img src="http://analy.qq.com/cgi-bin/apptrace?appid_via=100631368_1A000101310DD4CF&platform=1&action=100" width="1" height="1"  style="visibility: hidden;" />

</li>

<!--[if !IE]>|xGv00|3f78282c7313db1fc5aad9ed0a5be80f<![endif]-->

                                    
                                </ol>
                            </div>
                        </div>
                        <div id="QM_100002_Bottom" class="ft">
                            
                            <a href="javascript:;" class="p_prev prev-page unclick" title="上一页"><i></i></a>
                            <a href="javascript:;" class="p_next next-page" title="下一页"><i></i></a>
                        </div>
                    </div>
                    
                    
                    <div id="QM_Container_3" class="icenter-right-mod" style="display:none">
                        <div id="QM_3_Title" class="hd"><p>
								<a class="title" href="javascript:">谁看过我</a>
								<b class="divide-line">|</b>
								<a href="javascript:;" id="visitYou">我看过谁</a></p></div>
                        <div id="QM_3_Body" class="bd">
                        </div>
                        <div id="QM_3_Bottom" class="ft">
							<div id="QM_3_pager"></div>
							<div id="QM_3_info"></div>
                        </div>
                    </div>
                    
                    
                    <div id="QM_Container_333" class="icenter-right-mod">
                        <div id="QM_333_Title" class="hd">
                            <h3>礼物</h3>
                        </div>
                        <div id="QM_333_Body" class="bd">
                            <div class="bd" id="qm_333_gift_list">
	<div class="gift-bd">
		<ul class="send-gift-list">
			
				<li isHighActive="0" isFestival="0" isVisitor="0" isBirth="1" uin="871073013" nick="软工 6刘李" source="0" year="1909" month="11" day="28"  lunarflag="0" is_super="0" is_year="0" vip_level="0"  gender="1" age="108" birthday="1909-11-28"  relate_days="5" btntext="0" >
					<div class="user-info">

						<a href="http://user.qzone.qq.com/871073013" class="user-avatar" target="_blank"><img src="http://qlogo2.store.qq.com/qzone/871073013/871073013/50"></a>

				        <div class="info-details">
				            <p>
				            	<a href="http://user.qzone.qq.com/871073013" title="软工 6刘李" target="_blank" class="user-name textoverflow">软工 6刘李</a>
				            	
				            </p>
				            <p>
								
									<span class="user-desc c_tx3">5后天生日</span>
								
				            </p>
				        </div>
				        <!-- 关闭按钮 -->
				        <a class="close-button" title="3天内不再显示此人" uin="871073013" data-hottag="ISD.QZONEGIFT.QZONEINFOCENTER.CENTER-closeuin" href="javascript:;">×</a>
				    </div>

				    
						<a class="button bgr2 c_tx_2">
							
							<i class="icon-cake"></i><b class="c_tx2">生日快乐</b>
							
						</a>
					
				</li>
			
				<li isHighActive="0" isFestival="0" isVisitor="0" isBirth="1" uin="12976735" nick="英语老师" source="0" year="2015" month="11" day="30"  lunarflag="0" is_super="0" is_year="0" vip_level="0"  gender="1" age="2" birthday="2015-11-30"  relate_days="7" btntext="0" >
					<div class="user-info">

						<a href="http://user.qzone.qq.com/12976735" class="user-avatar" target="_blank"><img src="http://qlogo2.store.qq.com/qzone/12976735/12976735/50"></a>

				        <div class="info-details">
				            <p>
				            	<a href="http://user.qzone.qq.com/12976735" title="英语老师" target="_blank" class="user-name textoverflow">英语老师</a>
				            	
				            </p>
				            <p>
								
									<span class="user-desc c_tx3">7后天生日</span>
								
				            </p>
				        </div>
				        <!-- 关闭按钮 -->
				        <a class="close-button" title="3天内不再显示此人" uin="12976735" data-hottag="ISD.QZONEGIFT.QZONEINFOCENTER.CENTER-closeuin" href="javascript:;">×</a>
				    </div>

				    
						<a class="button bgr2 c_tx_2">
							
							<i class="icon-cake"></i><b class="c_tx2">生日快乐</b>
							
						</a>
					
				</li>
			
				<li isHighActive="0" isFestival="0" isVisitor="1" isBirth="0" uin="694986479" nick="严振威" source="0" year="0" month="0" day="0"  lunarflag="0" is_super="0" is_year="0" vip_level="0"  gender="0" age="0"  relate_days="0" btntext="0" >
					<div class="user-info">

						<a href="http://user.qzone.qq.com/694986479" class="user-avatar" target="_blank"><img src="http://qlogo2.store.qq.com/qzone/694986479/694986479/50"></a>

				        <div class="info-details">
				            <p>
				            	<a href="http://user.qzone.qq.com/694986479" title="严振威" target="_blank" class="user-name textoverflow">严振威</a>
				            	
				            </p>
				            <p>
								
									<span class="user-desc c_tx3">近期看过你</span>
								
				            </p>
				        </div>
				        <!-- 关闭按钮 -->
				        <a class="close-button" title="3天内不再显示此人" uin="694986479" data-hottag="ISD.QZONEGIFT.QZONEINFOCENTER.CENTER-closeuin" href="javascript:;">×</a>
				    </div>

				    
						
						<a class="button bgr2 c_tx_2">
							<i class="icon-visitor"></i><b class="c_tx2">感谢来访</b>
						</a>
					
				</li>
			
		</ul>
	</div>
</div>
                        </div>
                        <div id="QM_333_Bottom" class="ft">
                            <div class="gift-ft">
	
		<a href="javascript:void(0)" class="prev-page" data-hottag="ISD.QZONEINFOCENTER.CENTER-pre_group">
			<i></i>
		</a>
		<a href="javascript:void(0)" class="next-page" data-hottag="ISD.QZONEINFOCENTER.CENTER-next_group">
			<i></i>
		</a>
	

	<a href="javascript:void(0)" class="send-all" data-birthnum="2" data-hottag="ISD.QZONEGIFT.QZONEINFOCENTER.CENTER-more_gift">给更多好友送礼</a>
</div>
                        </div>
                    </div>
                    
                    <div id="QM_Container_100003_anchor" data-friend-num="316" class="icenter-right-mod none"></div>
                    
                    
                    
                    <div id="QM_Container_100014" class="icenter-right-mod before-year none"></div>
                    
                    <div id="QM_Container_100012" class="collet_box fn_fnrecm icenter-right-mod icenter-right-photo" style="visibility:hidden;">
                        <div id="QM_100012_Title" class="box_hd">
                        </div>
                        <div id="QM_100012_Body" class="box_bd">
                        </div>
                        <div id="QM_100012_Bottom" class="box_ft">
                        </div>
                    </div>
                </div>
            </div>
            
            <div id="care_friend_container" class="col-main none">
                <div class="col-main-feed">
                    <div class="fn-feed-control-v2 clearfix">
                        <div class="control-inner">
                            <div class="feed-control-tab">
                                <a id="care_menu_all" href="javascript:;" class="item-on item-on-slt">
                                    <span id="care_menu_nick">关心的好友</span>
                                    <i class="ui-icon icon-feed-down"></i>
                                </a>
                                <span class="line"></span>
                                
                                <div class="scrollbar" id="care_menu_cnt" style="display:none;">
                                    <div class="fn-single-select">
                                        <ul id="care_menu_list" class="avatar-list"></ul>
                                    </div>
                                </div>
    							<span title="您可能关心的好友动态" class="item"  style="font-weight:bold;display:none" id="may_care_title">您可能关心的好友动态</span>
                            </div>
                            <div class="feed-control-tab-op">
                                <a title="刷新动态" id="feed_care_refresh" href="javascript:;" class="item-left"><i class="ui-icon  icon-refresh-v9"></i></a>
                            </div>
                        </div>
                    </div>
                    <div class="fn-feed-container">
                        <div class="feed  feed-v9">
                            <div class="feed_inner">
                                <div style="display:none;" id="feed_care_update" class="tipsbox bg2"></div>
                                <ul id="feed_care_list"></ul>
                                <div id="feed_care_tips" style="visibility:hidden;"></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-main-sidebar">
                    <div class="icenter-right-mod mod-add-care" id="spcare_addspecial">
                        <div class="hd">
                            <a href="javascript:;" class="btn-add-care-big" id="add_care_btn"><i class="ui-icon icon-care-red-b"></i>添加特别关心</a>
                        </div>
                        <div class="bd"></div>
                    </div>

                    <div class="icenter-right-mod mod-special-counter" id="spcare_careme" style="display:none">
	                    <div class="hd">
	                        <h3>关心我的</h3>
	                    </div>
	                    <div class="bd">
	                        <div class="box_bd qz-grid" >
	                            <div class="special-counter qz-left bg5">
	                                <div class="in-hd qz-grid bg6">
	                                    <s class="qz-left ui_icon sp-sc-heart"></s><s class="qz-right ui_icon sp-sc-heart"></s>
	                                </div>
	                                <div class="in-bd"><strong class="sc-counter c_tx3" id="sp_careme_count">-</strong></div>
	                            </div>
	                            <div class="qz-main c_tx2" id="sp_careme_desc" title="为保护用户隐私，此处将不展示具体好友。">
									<p><a href="javascript:" id="sp_careme_action"></a></p>
	                            </div>
	                        </div>
	                    </div>
	                </div>


					
					<div class="icenter-right-mod mod-my-cared-list" id="my_care_list_con" style="display:none">
						<div class="hd">
							<h3>我关心的 <span id="carelist_count_new"></span></h3>
						</div>
						<div class="bd">
							<ul id="my_care_list"></ul>
						</div>
						<div class="ft">
							<a href="javascript:" class="prev-page unclick" title="上一页"><i></i></a>
							<a href="javascript:" class="next-page unclick" title="下一页" ><i></i></a>
						</div>
					</div>
					
					
					
                </div>
            </div>
            <div id="app_right_container" class="col-main none"></div>
            
            <div id="leftMenu" class="col-menu">
                


<div class="mod-side-nav mod-side-nav-message" data-version="20171113" >
    <div class="inner">
        <div class="bd">
            
            <ul id="tab_menu_list" class="sn-list">
                <li type="friend">
                    <a id="tab_menu_friend" href="javascript:;" class="qz-grid">
                        <div class="qz-left"><i class="ui-icon sp-friend-feed"></i></div>
                        <div class="qz-right"><span class="sn-count none" id="tab_menu_friend_cnt">0</span></div>
                        <div class="qz-main"><span class="sn-title">好友动态</span></div>
                    </a>
                </li>
                
                <li type="care">
                    <a id="tab_menu_care" href="javascript:;" class="qz-grid" accesskey="t">
                        <div class="qz-left"><i class="ui-icon sp-close-feed"></i></div>
                        <div class="qz-right"><span class="sn-count none" id="tab_menu_care_cnt">0</span></div>
                        <div class="qz-main"><span class="sn-title">特别关心</span></div>
                    </a>
                </li>
                
                
                <li type="me">
                    <a id="tab_menu_me" href="javascript:;" class="qz-grid" accesskey="y">
                        <div class="qz-left"><i class="ui-icon sp-at"></i></div>
                        <div class="qz-right"><span class="sn-count none" id="tab_menu_me_cnt">0</span></div>
                        <div class="qz-main"><span class="sn-title">与我相关</span></div>
                    </a>
                </li>
                
                
                <li type="mv">
                    <a id="tab_menu_mv" href="javascript:;" class="qz-grid" accesskey="m" style="display:none;">
                        <div class="qz-left"><i class="ui-icon sp-video"></i></div>
                        <div class="qz-right"><span class="sn-count none" id="tab_menu_mv_cnt">0</span></div>
                        <div class="qz-main"><span class="sn-title">直播广场</span></div>
                    </a>
                </li>


                <li type="sdc">
                    <a id="tab_menu_sdc" href="javascript:;" class="qz-grid">
                        <div class="qz-left"><i class="ui-icon sp-past-years"></i></div>
                        <div class="qz-main"><span class="sn-title">那年今日</span></div>
                    </a>
                </li>

                
                
                
                
                
                <li type="class" class="ke_gray">
                    <a id="tab_menu_class" href="javascript:;" class="qz-grid txclass" data-url="https://ke.qq.com/index_new.html?source=qzone&from=152">
                        <div class="qz-left"><i class="ui-icon sp-classroom"></i></div>
                        <div class="qz-main"><span class="sn-title">腾讯课堂</span></div>
                    </a>
                </li>

                <li type="app">
                    <a id="tab_menu_app" href="javascript:;" class="qz-grid">
                        <div class="qz-left"><i class="ui-icon sp-app-center"></i></div>
                        <div class="qz-right"><span class="sn-count none" id="tab_menu_app_cnt">0</span></div>
                        <div class="qz-main"><span class="sn-title">游戏应用</span></div>
                    </a>                   
                </li>

                  
            </ul>

            <a id="tab_switch" title="展开" class="qz-grid more-toggle more-toggle-hide" href="javascript:;"  data = '______'>
                <i class="ui-icon sp-nav-l-down"></i>
            </a>

            <ul id="tab_hide_list" class="sn-list none">
                
                    <li type="fav">
                         <a id="tab_menu_fav" href="javascript:;" class="qz-grid">
                            <div class="qz-left"><i class="ui-icon sp-fav"></i></div>
                            <div class="qz-main"><span class="sn-title">我的收藏</span></div>
                        </a>                    
                    </li>
                
            </ul>
        </div>
    </div>
</div>
<div class="mod-side-nav mod-side-nav-recently-used" data-applist4="0">
    <div class="inner" id="applist_html">
        <div class="hd"></div>
        <div class="bd">
            <ul class="sn-list" id="tab_applist_show">
                            

                

                 
                    <li>
                        <a href="http://rc.qzone.qq.com/1101328322?via=QZ.LEFT.XIAOLABA&amp;app_custom=essence" data-bosstrace="2156_199230_3_1_0_0" onclick="TCISD && TCISD.hotClick('applist.leftposition.guangbo','applist.qzone.qq.com');" class="qz-grid" target="_blank">
                            <div class="qz-left"><i class="ui-icon sp-popularize sparkle"></i></div>
                            <div class="qz-main"><span class="sn-title">炫舞豪礼风暴!</span></div>
                        </a>
                    </li>
                

                <li>
                    <a href="//game.qzone.qq.com/?via=QZONE.CENTER" class="qz-grid qz-gamecenter">
                        <div class="qz-left"><i class="ui-icon sp-gamecenter"></i></div>
                        <div class="qz-main"><span class="sn-title">游戏应用中心</span></div>
                    </a>
                </li>

                
                
    
               
         
            
            
        
        
        
            
        
            
        
            
        
            
               
        
            <li data-recommend="0" data-xiaoyouxi="0" data-apptype="0" data-newicon="0">
                <a class="qz-grid j-to-app" title="" data-index = "" data-id="362" data-via="" data-traceinfo="" href="javascript:;">
                <div class="qz-left">
                    
                        <img alt="Q宠大乐斗" src="//i.gtimg.cn/open/app_icon/00/00/03/62/362_16.png">
                    
                </div>
                
                    
                
                <div class="qz-main">
                    <span class="sn-title">
                        Q宠大乐斗
                    </span>
                </div>
                </a> 
                
            </li>
        
    
               
         
            
            
        
        
        
            
        
            
        
            
        
            
               
        
            <li data-recommend="0" data-xiaoyouxi="0" data-apptype="0" data-newicon="0">
                <a class="qz-grid j-to-app" title="" data-index = "" data-id="25227" data-via="" data-traceinfo="" href="javascript:;">
                <div class="qz-left">
                    
                        <img alt="捕鱼假日" src="//i.gtimg.cn/open/app_icon/00/02/52/27/25227_16.png">
                    
                </div>
                
                    
                
                <div class="qz-main">
                    <span class="sn-title">
                        捕鱼假日
                    </span>
                </div>
                </a> 
                
            </li>
        
    
               
         
            
            
        
        
        
            
        
            
        
            
        
            
               
        
            <li data-recommend="0" data-xiaoyouxi="0" data-apptype="0" data-newicon="0">
                <a class="qz-grid j-to-app" title="" data-index = "" data-id="346" data-via="" data-traceinfo="" href="javascript:;">
                <div class="qz-left">
                    
                        <img alt="3366小游戏" src="//i.gtimg.cn/open/app_icon/00/00/03/46/346_16.png">
                    
                </div>
                
                    
                
                <div class="qz-main">
                    <span class="sn-title">
                        3366小游戏
                    </span>
                </div>
                </a> 
                
            </li>
        
    


                <li class="sn-other">
                    <a href="//rc.qzone.qq.com/appstore/allapp?via=QZONE.CENTER">我的全部游戏应用&gt;&gt;</a>
                </li>

                
                
                    <li class="sn-line">
                        <sapn>热门游戏</sapn>
                    </li>
                    
    
               
        
            
        
        
        
            
        
            
        
            
        
            
               
        
            <li data-recommend="0" data-xiaoyouxi="0" data-apptype="0" data-newicon="0">
                <a class="qz-grid j-to-app" title="" data-index = "" data-id="1106151934" data-via="QZ.MYAPP.HOT" data-traceinfo="2544_199346_848_1_0_0" href="javascript:;">
                <div class="qz-left">
                    
                        <img alt="传奇荣耀" src="//i.gtimg.cn/open/app_icon/06/15/19/34/1106151934_16.png">
                    
                </div>
                
                    
                
                <div class="qz-main">
                    <span class="sn-title">
                        传奇荣耀
                    </span>
                </div>
                </a> 
                
            </li>
        
    
               
        
            
        
        
        
            
        
            
        
            
        
            
               
        
            <li data-recommend="1" data-xiaoyouxi="0" data-apptype="0" data-newicon="0">
                <a class="qz-grid j-to-app" title="" data-index = "" data-id="1101328322" data-via="QZ.MYAPP.HOT" data-traceinfo="2544_199347_848_1_0_0" href="javascript:;">
                <div class="qz-left">
                    
                        <img alt="炫舞时代" src="//i.gtimg.cn/open/app_icon/01/32/83/22/1101328322_16.png">
                    
                </div>
                
                    
                        <div class="qz-right"><i class="ui_icon icon_app_recommend"></i></div>
                    
                
                <div class="qz-main">
                    <span class="sn-title">
                        炫舞时代
                    </span>
                </div>
                </a> 
                
            </li>
        
    
               
        
            
        
        
        
            
        
            
        
            
        
            
               
        
            <li data-recommend="0" data-xiaoyouxi="0" data-apptype="0" data-newicon="0">
                <a class="qz-grid j-to-app" title="" data-index = "" data-id="1106193011" data-via="QZ.MYAPP.HOT" data-traceinfo="2544_199344_848_1_0_0" href="javascript:;">
                <div class="qz-left">
                    
                        <img alt="龙神契约" src="//i.gtimg.cn/open/app_icon/06/19/30/11/1106193011_16.png">
                    
                </div>
                
                    
                
                <div class="qz-main">
                    <span class="sn-title">
                        龙神契约
                    </span>
                </div>
                </a> 
                
            </li>
        
    

                

                
                
                    <li class="sn-line">
                        <sapn>新品抢先</sapn>
                    </li>
                    
    
               
        
            
        
        
        
            
        
            
        
            
        
            
               
        
            <li data-recommend="0" data-xiaoyouxi="0" data-apptype="0" data-newicon="1">
                <a class="qz-grid j-to-app" title="" data-index = "" data-id="1106170555" data-via="QZ.MYAPP.NEW" data-traceinfo="2545_198902_848_1_0_0" href="javascript:;">
                <div class="qz-left">
                    
                        <img alt="刺秦秘史" src="//i.gtimg.cn/open/app_icon/06/17/05/55/1106170555_16.png">
                    
                </div>
                
                    
                        <div class="qz-right"><i class="ui_icon icon_app_new_cn"></i></div>
                    
                
                <div class="qz-main">
                    <span class="sn-title">
                        刺秦秘史
                    </span>
                </div>
                </a> 
                
            </li>
        
    

                

                
                
                
                
                
            </ul>

            
                <a id="tab_applist_switch" title="展开" class="qz-grid more-toggle more-toggle-hide" href="javascript:;">
                   <i class="ui-icon sp-nav-l-down"></i>
                </a>
                
                <ul class="sn-list none" id="tab_applist_hide">
                    
                    <li class="sn-line">
                        <sapn>休闲娱乐</sapn>
                    </li>
                    
    
               
        
            
        
        
        
            
        
            
        
            
        
            
               
        
            <li data-recommend="0" data-xiaoyouxi="0" data-apptype="0" data-newicon="0">
                <a class="qz-grid j-to-app" title="" data-index = "" data-id="1105526422" data-via="QZ.MYAPP.CASUAL" data-traceinfo="2546_199324_848_1_0_0" href="javascript:;">
                <div class="qz-left">
                    
                        <img alt="星球大乱斗" src="//i.gtimg.cn/open/app_icon/05/52/64/22/1105526422_16.png">
                    
                </div>
                
                    
                
                <div class="qz-main">
                    <span class="sn-title">
                        星球大乱斗
                    </span>
                </div>
                </a> 
                
            </li>
        
    
               
        
            
        
        
        
            
        
            
        
            
        
            
               
        
            <li data-recommend="0" data-xiaoyouxi="0" data-apptype="0" data-newicon="0">
                <a class="qz-grid j-to-app" title="" data-index = "" data-id="1105974527" data-via="QZ.MYAPP.CASUAL" data-traceinfo="2546_199323_848_1_0_0" href="javascript:;">
                <div class="qz-left">
                    
                        <img alt="超神狙击" src="//i.gtimg.cn/open/app_icon/05/97/45/27/1105974527_16.png">
                    
                </div>
                
                    
                
                <div class="qz-main">
                    <span class="sn-title">
                        超神狙击
                    </span>
                </div>
                </a> 
                
            </li>
        
    
               
         
            
            
        
        
        
            
        
            
        
            
        
            
               
        
            <li data-recommend="0" data-xiaoyouxi="0" data-apptype="0" data-newicon="0">
                <a class="qz-grid j-to-app" title="" data-index = "" data-id="363" data-via="QZ.MYAPP.CASUAL" data-traceinfo="2546_199325_848_1_0_0" href="javascript:;">
                <div class="qz-left">
                    
                        <img alt="欢乐斗地主" src="//i.gtimg.cn/open/app_icon/00/00/03/63/363_16.png">
                    
                </div>
                
                    
                
                <div class="qz-main">
                    <span class="sn-title">
                        欢乐斗地主
                    </span>
                </div>
                </a> 
                
            </li>
        
    

                    
                    
                </ul>
            

            <ul class="sn-list" id="tab_otherlist_show">
                
                <li>
                    <a class="qz-grid sn-act" href="javascript:;" id="aPointMall" data-id="-10004">
                       <div class="qz-left"><i class="ui-icon sp-shop"></i></div>
                       <div class="qz-main"><span class="sn-title">积分兑换实物</span></div>
                    </a>
                </li>
                
                <li>
                    <a class="qz-grid sn-act" href="javascript:;" id="aMyGift" data-id="-10001">
                        <div class="qz-left"><i class="ui-icon sp-gift"></i></div>
                        <div class="qz-main"><span class="sn-title">每日抽奖</span></div>
                    </a>
                </li>
            </ul>

        </div>
    </div>
</div> 
                
                <div class="collet_box fn_paipai" id="QM_Container_11">
                    <div id="QM_Container_100006">
                        <div class="box_bd" id="QM_100006_Body"></div>
                    </div>
                </div>
            </div>
        </div>
        
        <div id="pageApp" class="layout-app mod_wrap none">
            <div class="mod_wrap_inner">
                <div class="mod_wrap_bd">
                    <div class="mod_wrap_iframe" id="app_container" style="min-height:435px;"></div>
                </div>
            </div>
        </div>
        <div id="page3rdApp" class="layout-app none" style="min-height:750px;"></div>
    </div>
    <div class="layout-copyright">
	<p><a href="http://z.qzone.com/" onclick="TCISD && TCISD.hotClick('bottomqzoneapp', 'user.qzone.com')" target="_blank">空间手机版</a> | <a href="http://vip.qzone.com/" onclick="TCISD && TCISD.hotClick('threefromendofpage', 'guangxi.vip.qzone.com', 'main')" target="_blank">黄钻贵族</a> | <a href="http://user.qzone.qq.com/20050606" target="_blank">官方Qzone</a> | <a href="http://connect.qq.com/" target="_blank">QQ互联</a> | <a href="http://page.opensns.qq.com/" target="_blank">认证服务</a> | <a href="http://blog.qq.com/" target="_blank">腾讯博客</a> | <a href="http://service.qq.com/special_auto/qzone.html" target="_blank">腾讯客服</a> | <a href="http://qzone.qq.com/web/tk.html" target="_blank">QQ空间服务协议</a> | <a href="http://wiki.open.qq.com/wiki/Tencent_Open_Platform_Complaint_Guidelines" target="_blank">Complaint Guidelines</a> | <a href="http://www.qq.com/culture.shtml" target="_blank">粤网文[2017]6138-1456号</a></p>
	<p>Copyright &copy; 2005 - 2017 Tencent.<a href="http://www.tencent.com/en-us/le/copyrightstatement.shtml" target="_blank">All Rights Reserved.</a></p>
	<p>腾讯公司 <a href="http://www.tencent.com/zh-cn/le/copyrightstatement.shtml" target="_blank">版权所有</a></p>
</div>
    </div>
    
    
</div>
<div class="fix-layout">    <div class="gb-operation-area" id="_returnTop_layout_inner">        <a href="javascript:;" id="goto_top_btn" class="gb-operation-button return-top">            <i class="gb-operation-icon" title="返回顶部"></i>            <span class="gb-operation-text">顶部</span>        </a>    </div></div>
<div id="QZ_Float_Items_Container" class="lay-shop-item-fixed"></div>
<div class="ui-tooltip" style="display:none;" id="g_reply_tips">
	<div class="inner">
		<div class="bd">回复</div>
		<b class="arrow arrow-down"></b>
	</div>
</div>
<div class="ui-tooltip" style="display:none;" id="g_delete_tips">
    <div class="inner">
        <div class="bd">删除</div>
        <b class="arrow arrow-down"></b>
    </div>
</div>
<script type="text/javascript">
g_T.fwp[4] = new Date();var g_V={qz:'_v8_2.1.65',jq:'2.0.3',sea:'2.1.1',core_ic:'50108',fp:'60628',ic:'50215',popcss:'?d=140918103710',delay:'-170302163216',req:'61221',ci:'_20131225'};
var g_ISP={p:"255",
i:"-3",
f:"1",
c:'10.238.7.239'},
g_type="M",
g_Set="",
g_ICSet="",
g_SPrefix="",
g_SPrefix_Server="",
g_DPrefix="",
g_dns_name="",
g_UserBitmap="18c19da00002e201",
g_LoginBitmap="18c19da00002e201",
g_UserunimBitmap="0808008888000341",
g_LoginUnimBitmap="0808008888000341",
g_UserVipStarBitmap="0000120008000000",
g_LoginVipStarBitmap="0000120008000000",
g_Bitmap_3rd="0000000000000840",
g_IZone_Flag=+"1",
g_diyTitle="",
g_SceneID=9,
g_neatstyle=0,
g_7DDressNo=0,
g_StyleID="2",
g_fullMode=99,
g_Mode="ofp",
g_version=8,
g_isFriend=0,
g_NowTime=1511403987,
g_StaticFlag="0",
g_isDirectApp=0,
ownermode=(g_iLoginUin==g_iUin),
ownerProfileSummary=["K.",
					1,
					19,
					"@@",
					"http:\/\/",
					"http:\/\/photo.store.qq.com\/http_imgload.cgi?\/rurl2=fdada5",
					"1997-12-2",
					"0000000000000001"],
g_isOFP="1",
g_isHideTitle="0",
g_icLayout="0",
g_isFromPengYou="", 
g_isBrandQzone="",
g_isFamousQzone="",
g_xwMode="",
g_needDec=1,
g_isFastPav=1,
g_scenarioidle="1024",
g_isBGScroll=0,
g_Dressup={items:[{type:1,itemno:72019,posx:0,posy:0,posz:0,height:0,width:0,flag:31},{type:19,itemno:1,posx:0,posy:0,posz:0,height:120,width:0,flag:0},{type:13,itemno:1,posx:50,posy:50,posz:0,height:0,width:0,flag:1},{type:347,itemno:94914,posx:720,posy:152,posz:0,height:0,width:0,flag:0} ],windows:[]},
g_isLite=0,
g_yPos=+'',
g_portraitTime=+'1372472103',
g_loginPortraitTime = + '1372472103', 
g_firstLoginTime=+'1511403625',
g_isLikable=+'1',
g_likedNumber=+'0',
g_likeable_today=+"1",
g_supportWebp=+'1',
g_OSClass="os-mac",
g_applistWallNum = parseInt("0" || "0",10), 
g_isStarVip = +"0",
g_isStarVipYear = +"0",
g_iStarVipLevel = +"0",


g_iEmoji=[],
g_PreData={app:{
			     ret:0,
			     data:{},
			     flag:1
    },
	flower:{
			ret:0,
			score:+"3330",
			gardener:+"25"
	},
	hat:{
			ret:-1,
	        id:+""
	},
	hotbar:{
		ret:-2
	},
	qbossData:{
		
	},
	potential:{flag:+''}, 
	homeAddr:{"hco":"","hp":"","hc":""},
	qq_friendNum:"316"
},
g_app_identifier='', 
qlogoDomain="store.qq.com",
g_starstamp_pic = +'1507871637',
g_starstamp_emotion = +'1507871637',
g_ic_fpfeedsType='friend',
g_Data={
	feedsPart1: {result:'',message:'',main:{needFold:'',icServerTime:'1511403988',icView:'1',daylist:'',uinlist:'',hasMoreFeeds_0:true,hasMoreFeeds_1:true,hasMoreFeeds_100:true,foldAllHostBTNClass:'',foldAllHostBTNTitle:'',foldAllHostFeedDisplay:'',friend_more:'',host_more:'',aboutHostFeeds_new_cnt:'0',replyHostFeeds_new_cnt:'0',host_pav_offset:'',get_visitorfeed:'1',myFeeds_new_cnt:'0',friendFeeds_new_cnt:'0',friendFeeds_newblog_cnt:'',friendFeeds_newphoto_cnt:'',newfeeds_uinlist:'',newfeeds_uinlist_more:'',newfeeds_special_cnt:'0',newfeeds_friend_cnt:'0',newfeeds_follow_cnt:'0',newfeeds_group_cnt:'',tips:'',js_showtips:'',lastaccesstime:'',lastAccessRelateTime:'',begintime:'1511361602',dayspac:'1',hidedNameList:[],QzoneFeedsKey:'',hsFlag:'',aisortNextTime:'',aisortBeginTime:'',aisortEndTime:'',aisortOffset:'',blacklist:'28943223,179100235,237643951,253405482,296131666,327403691,361334669,370718670,448578993,499087308,525062703,528335091,528837221,543464184,564792703,578132406,627319651,735966092,742120137,745603555,745938768,761573702,781276709,794805521,854299287,904577395,932717213,940790848,1003825976,1015905285,1031016814,1041004215,1055200926,1059199268,1131170145,1145695208,1160125859,1176468163,1181396334,1193647891,1196067277,1203377468,1214548479,1223789272,1262282608,1322069581,1351538788,1379158310,1420185269,1422119445,1464827646,1475913389,1538927186,1600593882,1603394427,1607868169,1634351866,1634586466,1637375943,1656499605,1693206037,1696845270,1732668921,2440736807,2474011758,2542900572,2584778797,2714779220,2739549811,2774716434,2796186530,2802596484,2836490541,3024139947,3077279122,3137209690,3495385490',pagenum:'2',externparam:'basetime=1511361602&pagenum=2&dayvalue=1&getadvlast=1&hasgetadv=&lastentertime=1511403625&LastAdvPos=0&UnReadCount=0&UnReadSum=0&LastIsADV=1&UpdatedFollowUins=&UpdatedFollowCount=0&LastRecomBrandID='}},
	feedsPart2: {host_data:[undefined],        about_data:[                                undefined        ],friend_data:[undefined],        firstpage_data:[                                {                        ver:'1',                        appid:'311',                        typeid:'0',                        key:'da9dc6cb4bab155a2d3a0400',                        flag:'0',                        dataonly:'0',                        feedno:'0',                        title:'',                        summary:'',                        appiconid:'311',                        clscFold:'icenter_list_extend',                        abstime:'1511369547',                        feedstime:' 00:52',                        userHome:'http://user.qzone.qq.com/3418791386',                        namecardLink:'nameCard_3418791386',                        ouin:'',                        uin:'3418791386',                        opuin:'3418791386',                        foldFeed:'',                        foldFeedTitle:'',                        showEbtn:'',                        scope:'0',                        hideExtend:'',                        nickname:'可里老师\/tpPython',                        remark:'',score:'',                        type:'',                        vip:'vip_0',                        bitmap:'08009c0002000001',     yybitmap:'0000000000000000',                        info_user_name:'',                        logimg:'http://qlogo3.store.qq.com/qzone/3418791386/3418791386/50?1499690974',                        bor:'',                        lastFeedBor:'',                        list_bor2:'',                        info_user_display:'',                        upernum:'',                        oprType:'0',                        moreflag:'',                        otherflag:'0_0_0_0_0_0_0',                        sameuser:{},                        uper_isfriend:[],                        uperlist:[],mergeData:[undefined]                },                                {                        ver:'1',                        appid:'311',                        typeid:'0',                        key:'81063d76a6a3155afc4e0b00',                        flag:'0',                        dataonly:'0',                        feedno:'1',                        title:'',                        summary:'',                        appiconid:'311',                        clscFold:'icenter_list_extend',                        abstime:'1511367590',                        feedstime:' 00:19',                        userHome:'http://user.qzone.qq.com/1983710849',                        namecardLink:'nameCard_1983710849',                        ouin:'',                        uin:'1983710849',                        opuin:'1983710849',                        foldFeed:'',                        foldFeedTitle:'',                        showEbtn:'',                        scope:'0',                        hideExtend:'',                        nickname:'林柏栎',                        remark:'',score:'',                        type:'',                        vip:'vip_0',                        bitmap:'08808d800202c001',     yybitmap:'1018000056ac1004',                        info_user_name:'',                        logimg:'http://qlogo2.store.qq.com/qzone/1983710849/1983710849/50?1511325872',                        bor:'',                        lastFeedBor:'',                        list_bor2:'',                        info_user_display:'',                        upernum:'',                        oprType:'0',                        moreflag:'',                        otherflag:'0_0_0_0_0_0_0',                        sameuser:{},                        uper_isfriend:[],                        uperlist:[],mergeData:[undefined]                },                                {                        ver:'1',                        appid:'311',                        typeid:'5',                        key:'77b935827b9a155a6bb40a00',                        flag:'0',                        dataonly:'0',                        feedno:'2',                        title:'',                        summary:'',                        appiconid:'311',                        clscFold:'icenter_list_extend',                        abstime:'1511365243',                        feedstime:'昨天 23:40',                        userHome:'http://user.qzone.qq.com/2184558967',                        namecardLink:'nameCard_2184558967',                        ouin:'',                        uin:'2184558967',                        opuin:'2184558967',                        foldFeed:'',                        foldFeedTitle:'',                        showEbtn:'',                        scope:'0',                        hideExtend:'',                        nickname:'沈旭',                        remark:'',score:'',                        type:'',                        vip:'vip_0',                        bitmap:'08009c8002024201',     yybitmap:'0000000000000000',                        info_user_name:'',                        logimg:'http://qlogo4.store.qq.com/qzone/2184558967/2184558967/50?1490883485',                        bor:'',                        lastFeedBor:'',                        list_bor2:'',                        info_user_display:'',                        upernum:'',                        oprType:'0',                        moreflag:'',                        otherflag:'0_0_0_0_0_0_0',                        sameuser:{},                        uper_isfriend:[],                        uperlist:[],mergeData:[undefined]                },                                {                        ver:'1',                        appid:'202',                        typeid:'2',                        key:'bfddgdbbfb',                        flag:'0',                        dataonly:'0',                        feedno:'3',                        title:'',                        summary:'',                        appiconid:'202',                        clscFold:'icenter_list_extend',                        abstime:'1511363351',                        feedstime:'昨天 23:09',                        userHome:'http://user.qzone.qq.com/2987533319',                        namecardLink:'nameCard_2987533319',                        ouin:'',                        uin:'2987533319',                        opuin:'2987533319',                        foldFeed:'',                        foldFeedTitle:'',                        showEbtn:'',                        scope:'0',                        hideExtend:'',                        nickname:'皮永飞',                        remark:'',score:'',                        type:'',                        vip:'vip_0',                        bitmap:'08009c8002004001',     yybitmap:'0000000000000000',                        info_user_name:'',                        logimg:'http://qlogo4.store.qq.com/qzone/2987533319/2987533319/50?1502999741',                        bor:'',                        lastFeedBor:'',                        list_bor2:'',                        info_user_display:'',                        upernum:'',                        oprType:'0',                        moreflag:'',                        otherflag:'0_0_0_0_0_0_0',                        sameuser:{},                        uper_isfriend:[],                        uperlist:[],mergeData:[undefined]                },                                {                        ver:'1',                        appid:'311',                        typeid:'0',                        key:'d2f4243e428c155a572b0200',                        flag:'0',                        dataonly:'0',                        feedno:'4',                        title:'',                        summary:'',                        appiconid:'311',                        clscFold:'icenter_list_extend',                        abstime:'1511361602',                        feedstime:'昨天 22:40',                        userHome:'http://user.qzone.qq.com/1042609362',                        namecardLink:'nameCard_1042609362',                        ouin:'',                        uin:'1042609362',                        opuin:'1042609362',                        foldFeed:'',                        foldFeedTitle:'',                        showEbtn:'',                        scope:'0',                        hideExtend:'',                        nickname:'宋雪',                        remark:'',score:'',                        type:'',                        vip:'vip_0',                        bitmap:'08d594800202c101',     yybitmap:'0000000000000001',                        info_user_name:'',                        logimg:'http://qlogo3.store.qq.com/qzone/1042609362/1042609362/50?1480896531',                        bor:'',                        lastFeedBor:'',                        list_bor2:'',                        info_user_display:'',                        upernum:'',                        oprType:'0',                        moreflag:'',                        otherflag:'0_0_0_0_0_0_0',                        sameuser:{},                        uper_isfriend:[],                        uperlist:[],mergeData:[undefined]                },                                {                        ver:'1',                        appid:'5000',                        typeid:'1',                        key:'20050606_1511403987',                        flag:'0',                        dataonly:'0',                        feedno:'5',                        title:'',                        summary:'',                        appiconid:'5000',                        clscFold:'icenter_list_extend',                        abstime:'1511400387',                        feedstime:' 09:26',                        userHome:'http://user.qzone.qq.com/20050606',                        namecardLink:'nameCard_20050606',                        ouin:'',                        uin:'20050606',                        opuin:'20050606',                        foldFeed:'',                        foldFeedTitle:'',                        showEbtn:'',                        scope:'0',                        hideExtend:'',                        nickname:'官方Qzone',                        remark:'',score:'',                        type:'',                        vip:'novip',                        bitmap:'989d9de00513c081',     yybitmap:'100008000000000b',                        info_user_name:'',                        logimg:'http://qlogo3.store.qq.com/qzone/20050606/20050606/50?1450773587',                        bor:'',                        lastFeedBor:'',                        list_bor2:'',                        info_user_display:'',                        upernum:'',                        oprType:'0',                        moreflag:'',                        otherflag:'1_0_0_0_0_0_1',                        sameuser:{},                        uper_isfriend:[],                        uperlist:[],mergeData:[undefined]                },                                undefined        ]},
	feeds:{
		type:'friend',
		hostFeedsFilter:'',
		view:'1'
	}
},
g_moreModules=["v8/dress/otherview_v8","v8/core/state"],
G_Param={};
G_Param.qz_referrer='';
if(''=='special'){
	document.getElementById('tab_menu_care').parentNode.className = 'current';
}else{
	if(g_ic_fpfeedsType=="friend"){
		document.getElementById('tab_menu_friend').parentNode.className = 'current';
	}else{
		document.getElementById('tab_menu_me').parentNode.className = 'current';
	}
}
g_weather={};

g_weather['save']={
	'country':'中国',
	'province':'浙江',
	'city':'杭州',
	'temp':'11',
	'weather':'晴',
	'day':'1',
	'pm2d5':''
	};

var g_blog_loc_prefix='';
var g_BLOG_LOCATION_PREFIX='b', g_BLOG_LOCATION_LOGIN_PREFIX='b';



(function(){
	var ua = {}, agent = navigator.userAgent;
	if (window.ActiveXObject || window.msIsStaticHTML){
		ua.ie = 6;
		(window.XMLHttpRequest || (agent.indexOf('MSIE 7.0') > -1)) && (ua.ie = 7); 
		(window.XDomainRequest || (agent.indexOf('Trident/4.0') > -1)) && (ua.ie = 8); 
		(agent.indexOf('Trident/5.0') > -1) && (ua.ie = 9); 
		(agent.indexOf('Trident/6.0') > -1) && (ua.ie = 10); 
		(agent.indexOf('Trident/7.0') > -1) && (ua.ie = 11);

		if(ua.ie == 6 || ua.ie == 7 || ua.ie == 8){
			g_V.jq='1.10.2';
		}
	}
})();

(navigator.appVersion.indexOf("QQBrowser/7")>-1) && (function(){
	try{
		var styleTest = '';
		var lastCpuTime,checkInterval = 1000,checkCount=15,threadCPUData=[],
			qqbrowser = window.external.qqbrowser,
			systemInfo = eval('('+ qqbrowser.perfCounter.systemInfo +')'),
			memoryu = eval('('+ qqbrowser.perfCounter.memoryUsage +')'),
			memorya =  memoryu.Process.CommittedSize,
			memoryb,
			cpuNumber = systemInfo.LogicProcessors,
			intervalUS = checkInterval*1000;

		if(!cpuNumber){
			return;
		}

		function calcCpuUsage(){
			var cpuTime = eval('('+ qqbrowser.perfCounter.cpuTime +')');
			if(lastCpuTime){
				var delSystemTime = (cpuTime.system - lastCpuTime.system);
				threadCPUData.push(100 * (cpuTime.thread - lastCpuTime.thread) / intervalUS);
			}
			lastCpuTime = cpuTime;
		}
		function avg(arr){
			var h=0;
			for(var i=0,len=arr.length;i<len;i++){
				h+=arr[i];
			}
			return h/checkCount;
		}
		var _i=0,
		timer = setInterval(function(){
			if(_i<checkCount){
				calcCpuUsage();
				_i++;
			}else{
				clearTimeout(timer);
				setTimeout(function(){
					memoryu = eval('('+ qqbrowser.perfCounter.memoryUsage +')');
					memoryb =  memoryu.Process.CommittedSize;
					if(window.TCISD && window.TCISD.createTimeStat){
						var apiStat = TCISD.createTimeStat("apiTimeStat", [7820, 109, 6]);
						apiStat.setZero(0);
						G_Param.threadCPUUsage = avg(threadCPUData);
						G_Param.threadMemoryUsage = memoryb-memorya;
						apiStat.mark(1,G_Param.threadCPUUsage*1000);
						apiStat.mark(2,G_Param.threadMemoryUsage);
						apiStat.report();
					}
				},10000);
			}
		},checkInterval);
	}catch(err){}
})();


</script>

<script type="text/javascript" src="https://qzonestyle.gtimg.cn/ac/qzone/qzfl/qzfl_v8_2.1.65.js" ></script>
<script type="text/javascript" src="https://qzonestyle.gtimg.cn/ac/lib/seajs/sea-2.1.1.js" ></script>
<script type="text/javascript" src="https://qzonestyle.gtimg.cn/c/=/qzone/v8/core/seajs_config.js,/qzone/v8/engine/plugin-combo.js,/qzone/v8/core/ic.js?max_age=31536001&amp;d=50108" ></script>

<script>
    (function(){
        // if(window.location.protocol!='https:' || window.g_cdn_proto !='https'){
        //     return;
        // }
        var newSiDomain = 'h5.qzone.qq.com/proxy/domain/qzonestyle.gtimg.cn';
        var cookieflag = document.cookie.indexOf('blabla')>-1;
        if(cookieflag && (/(?:^user\.(s\d\.)?|\d{5,}\.|rc\.)qzone\.qq\.com/.test(location.host))){
            newSiDomain = location.host+'/q/qzs';
        }
        (function(v,b,e,i,s){
            var arJs=[];
            if(!window.QZFL || !QZFL.lang){
                arJs.push(b,s,'/ac/qzone/qzfl/qzfl',g_V.qz,'.js',e);    
            }
            if(!window.seajs){
                arJs.push(b,s,'/ac/lib/seajs/sea-'+g_V.sea+'.js',e);    
            }
            
            if(arJs.length){
                
                
                if(s.indexOf('h5.qzone.qq.com')>-1){
                    window.g_script_retry = 'h5.qzone.qq.com';
                }else{
                    window.g_script_retry = 'user.qzone.qq.com';
                }
                arJs.push(b,s,'/c/=/qzone/v8/core/seajs_config.js,/qzone/v8/engine/plugin-combo.js,/qzone/v8/core/ic.js?max_age=31536001&amp;d='+g_V.core_ic,e);
                document.write(arJs.join(''));    
            }
        })(g_V,'<script type="text/javascript" charset="utf-8" src="'+(window.g_cdn_proto || window.location.protocol)+'//','"><\/script>',imgcacheDomain,newSiDomain);
    })();
    
</script>

<script type="text/javascript">
(function(){
    
   if(!window.QZFL){
        return;
   }
   var sslInfo = QZFL.cookie.get('x-stgw-ssl-info');
   if(!sslInfo){
        return;
   }
    var frags = sslInfo.split('|');
    var isSessionReused = frags[4] == 'r';
    var connectionNum = parseInt(frags[3] || '0',10);
    if(window.g_iLoginUin%10 !=3){
        //不用全部看
        return;
    }

    if(connectionNum==1 && !ua.chrome){
        window.haboStat({
            commandid : 'first_screen_ssl_session_reused',
            stime : 1000, 
            resultcode : isSessionReused ? 0 : 1,
            touin : window.g_iLoginUin || 0,
            frequency :  1
        });
    }
    
})();


(function(){var _i=new Image(),_r=Math.random(),_re = new RegExp("(?:^|;+|\\s+)_qz_fix=([^;]*)"),m=document.cookie.match(_re),_v=!m ?"":m[1],_ph='//pinghot.qq.com/pingd?dm=homeact.qzone.qq.com.hot&url=/troubleshooter&tt=-&hottag=guanjia.qzonestyle.',_phe='&hotx=9999&hoty=9999&rand='+_r;_i.onerror=function(){var _t=new Image();if(_v>0){document.getElementById('trs_tip').innerHTML='如果您看到这个提示，说明QQ空间仍然无法正常打开，请您返回空间小助手，进行<a href="http://user.qzone.qq.com/troubleshooter#secondfix" title="空间小助手"><strong>深度修复</strong></a>';_t.src=_ph+'badagain'+_phe;}else{_t.src=_ph+'bad'+_phe;}var _d = document.createElement("div");_d.innerHTML = '<iframe frameborder="0" style="width:1px;height:1px;" src="http://user.qzone.qq.com/troubleshooter?traytip"></iframe>';document.body.appendChild(_d);};_i.onload=function(){if(_v==2){var _t=new Image();_t.src=_ph+'fixed'+_phe;}};_i.src='//'+siDomain+'/ac/qzone_v5/client/year_vip_icon.png?i='+_r;})();
QZFL.event.onDomReady(function(){
    g_T.fwp[3] = new Date();
});
    
    

    var fsimg = document.getElementById("full_background_img");
    if(fsimg){
        window.adjust_full_screen_skin = function(){
            var bg = document.getElementById('full_background'),
                    bg_img=document.getElementById('full_background_img'),
                    cw = QZFL.dom.getClientWidth(),
                    ch = QZFL.dom.getClientHeight(),
                    iw = bg_img.width,
                    ih = bg_img.height;

                bg.style.width=cw+"px";
                bg.style.height=ch+"px";

                if (cw / ch > iw / ih) {
                    var new_h = cw * ih / iw,
                        imgTop = (ch - new_h) / 2;
                    bg_img.style.width=cw + "px";
                    bg_img.style.height=new_h + "px";
                    bg_img.style.top="";
                    bg_img.style.left="";
                }else {
                    var new_w = ch * iw / ih,
                        imgLeft = (cw - new_w) / 2;
                    bg_img.style.width=new_w + "px";
                    bg_img.style.height=ch + "px";
                    bg_img.style.left=imgLeft + "px";
                    bg_img.style.top="";
                }
        };
        if (!QZONE.shop || !QZONE.shop.initDressUp) {
            var url = fsimg.getAttribute("data-src");
            fsimg.onload = adjust_full_screen_skin;
            fsimg.src = url;
        }
    }
    
    var mc = document.getElementById('menuContainer');
    var oldGuideMap = {
        N2: "myhome",
        3: "305",
        5: "4",
        6: "306",
        7: "1",
        8: "3",
        10: "311",
        11: "323",
        13: "338",
        14: "myhome",
        15: "yellowgrade",
        17: "333",
        18: "340"
    };
    var isDefaultMenu = '1' == 1,
        isCustom = '1' & 2 > 0,
        isMobile = (window.ua && (ua.isiPhone || ua.isiPad)),
        lst;
    window.getHotTagPrefix = function(){
            var env = window.g_app_identifier != "" ? 'app' : (window.g_isOFP == "0" ? 'home' : 'center');

            return env + 'click' +  (window.ownermode ? "-host" : "-guest");
        };
    window.custom_menu_swf = function(id) {
        if(QZFL.userAgent.chrome || QZFL.userAgent.safari){
            var _cbi = document.getElementById('_chrome_bug_input');
            if(!_cbi){
                var _laybg = document.getElementById('layBackground');
                QZFL.dom.createElementIn("input",_laybg,false,{id:"_chrome_bug_input",type:'text',style:"border:1px;width:1px;position:absolute;left:-10px;"});
                _cbi =  document.getElementById('_chrome_bug_input');
            }
            _cbi.focus();
        }
        
        if (id != 'close') {
            id = (!isCustom && !isDefaultMenu && !isMobile) ? (oldGuideMap[id] || id) : id;
            if(id == "-1" || id == "N1"){
                id = "main";
            }
            if (id == '5' || id == '7') {
                id = oldGuideMap[id];
            }
            var _p = getHotTagPrefix();
            window.TCISD && TCISD.hotClick("menu_v8."+_p+".appid_"+id, "8.qzone.qq.com");
            if(id == '219'){
                if(QZONE.music && typeof(QZONE.music.switchPage)=="function"){
                    QZONE.music.switchPage();
                }
            }else{
                if(QZONE.FrontPage && QZONE.FrontPage.toApp) {
                    QZONE.FrontPage.toApp("/" + id);  
                }              
            }
        }
        return false;
    };
    if (!QZONE.shop || !QZONE.shop.initDressUp) {
        mc && QZFL.event.delegate(mc, 'li', 'click', function (e) {
            QZFL.event.preventDefault(e);
            this.className = this.className.replace(/_\-1/, '_N1');
            var appid = this.className.match(/menu_item_([A-Z0-9\-]*)/i);
            appid && appid[1] && custom_menu_swf(appid[1]);
            if (lst) {
                QZFL.css.removeClassName(lst, 'cur');
            }
            lst = this;
            QZFL.css.addClassName(lst, 'cur');
        });
        mc && mc.setAttribute('reged', '1');
    }

(function(){try{if(parent!=self && (parent.document.domain!=document.domain || (document.referrer && !/^http(s)?:\/\/[.\w-]+\.qq\.com\//i.test(document.referrer)))){throw new Error("can't be iframed");}}catch(e){window.open(location.href, "_top");}})();
    /**
     * β 增加新接口 获取通过URL传递的参数值
     * @param {String} name 参数的名称
     */
    var getParameter = function(url, name){
        var r = new RegExp("(\\?|#|&)" + name + "=([^&#]*)(&|#|$)"),
            m = url.match(r);
        return (!m ? "" : m[2]);
    };
    //上报用iframe嵌套qzone的用户
    var qq = getParameter(location.href, 'qzoneInIframe');
    if(qq) {
        TCISD.stringStat(1000100, {
                bid: 108146,
                rc: 'QQ:' + qq
        }, {
            reportRate: 1
        });
    }
    var clickReport = getParameter(location.href, 'clickReport');
    if(window.TCISD && window.TCISD.pv) {
        TCISD.pv('user.qzone.qq.com', clickReport);
    }






</script>

</body>



<script type="text/javascript">
window.g_qzonetoken = (function(){ try{return "9f4aa1450729ebe32a60b5b8077abdba7679b0d9d36d8266ba05ea2d03c1108558792d5ba2ba72e18c95";} catch(e) {var xhr = new XMLHttpRequest();xhr.withCredentials = true;xhr.open('post', '//h5.qzone.qq.com/log/post/error/qzonetoken', true);xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');xhr.send(e);}})();

/**
 * 框架机模调上报
 */
var reportMd = function (code, type, delay) {
	//使用模调测速
	var url = "//h5.qzone.qq.com/report/md?"
		+ "fromId=204971707&toId=211006088&interfaceId=111900240"
		+ (typeof code == 'undefined' ? '' : ("&code=" + code))
		+ (typeof type == 'undefined' ? '' : ("&type=" + type))
		+ (typeof delay == 'undefined' ? '' : ("&delay=" + Math.min(delay, 10 * 1000)))
		+ '&r=' + Math.random();
	var img = new Image();
	img.src = url;
};

reportMd(0, 0, 1);

</script>


</html>

'''
pattern=re.compile(r'window\.g_qzonetoken = \(function\(\)\{ try\{return "(.*?)";\}')
s=re.search(pattern,p)
print(s)
# file='./cookies.txt'
# # cookies=open(file)
# # cookiess={}
# # for row in cookies:
# #     arr=row.strip().strip(';').split('=')
# #     cookiess.setdefault(arr[0],arr[1])
# # print(cookiess)