'''
@author：KongWeiKun
@file: re_test.py
@time: 17-9-29 下午4:43
@contact: 836242657@qq.com
'''
import re
q='''
<div id="comments-section">
        <div class="mod-hd">
            
        <a class="comment_btn j a_show_login" href="https://www.douban.com/register?reason=review" rel="nofollow">
            <span>我要写短评</span>
        </a>

            
            
    <h2>
        <i class="">十万个冷笑话2的短评</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/26759539/comments?status=P">全部 13929 条</a>
            ) </span>
    </h2>

        </div>
        <div class="mod-bd">
                
    <div class="tab-hd">
        <a id="hot-comments-tab" href="comments" data-id="hot" class="on">热门</a>&nbsp;/&nbsp;
        <a id="new-comments-tab" href="comments?sort=time" data-id="new">最新</a>&nbsp;/&nbsp;
        <a id="following-comments-tab" href="follows_comments" data-id="following" class="j a_show_login">好友</a>
    </div>

    <div class="tab-bd">
        <div id="hot-comments" class="tab">
            
    
        <div class="comment-item" data-cid="1230796249">
            
    
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">1413</span>
                <input value="1230796249" type="hidden">
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/pojian1987/" class="">破茧</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2017-08-17 14:38:39">
                    2017-08-17
                </span>
            </span>
        </h3>
        <p class=""> 大量经典动画乱入，但又不显得突兀。

大量广告强行插入，但又不显得讨厌。

大量槽点刚想骂娘，却发现这是笑点。

大量笑点全程密集，腹肌没痛膀胱痛。

总之，就是一句话：值得一看。
        </p>
    </div>

        </div>
        <div class="comment-item" data-cid="1229007635">
            
    
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">603</span>
                <input value="1229007635" type="hidden">
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/dreamfox/" class="">乌鸦火堂</a>
                    <span>看过</span>
                    <span class="allstar40 rating" title="推荐"></span>
                <span class="comment-time " title="2017-08-13 19:37:48">
                    2017-08-13
                </span>
            </span>
        </h3>
        <p class=""> 一如既往的脱线，其中穿插着十冷一贯的恶搞和情怀，交代世界观那段爆笑，最后大战那段也带出了该系列的创作动机：我们不玩驳杂的3D，或者说玩不起，就是用“梗和脑洞”，去汇成单纯的2D世界，单纯、搞笑。PS该系列也有着明显的受众划分，这种搞笑风格仅适用于同道中人，阿里巴巴那首歌情怀十足
        </p>
    </div>

        </div>
        <div class="comment-item" data-cid="1231378965">
            
    
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">124</span>
                <input value="1231378965" type="hidden">
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/82660297/" class="">啊啊反对</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2017-08-18 19:47:36">
                    2017-08-18
                </span>
            </span>
        </h3>
        <p class=""> 年轻的观众哟，你们看的是这个喜羊羊还是这个柯南，还是我们的青春呢？
        </p>
    </div>

        </div>
        <div class="comment-item" data-cid="1229306970">
            
    
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">160</span>
                <input value="1229306970" type="hidden">
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/2123968/" class="">静待花开</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2017-08-14 11:20:16">
                    2017-08-14
                </span>
            </span>
        </h3>
        <p class=""> 影片中致敬了很多经典电影和人物啊～用搞笑的方式面对操蛋的人生，脑洞大开的这个系列始终坚持自己的搞怪风格，真的很难得
        </p>
    </div>

        </div>
        <div class="comment-item" data-cid="1225658935">
            
    
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">122</span>
                <input value="1225658935" type="hidden">
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/lesc/" class="">苏筱兀</a>
                    <span>看过</span>
                    <span class="allstar40 rating" title="推荐"></span>
                <span class="comment-time " title="2017-08-06 18:32:13">
                    2017-08-06
                </span>
            </span>
        </h3>
        <p class=""> 实在无法数尽分分秒秒都存在的脑洞全开的奇葩桥段，还请各位观众自行走进电影院去观赏，感受一下这部足以让你笑出腹肌，笑到不能自理的脑洞电影！
        </p>
    </div>

        </div>



                
                &gt; <a href="comments?sort=new_score&amp;status=P">更多短评13929条</a>
        </div>
        <div id="new-comments" class="tab">
            <div id="normal">
            </div>
            <div class="fold-hd hide">
                <a class="qa" href="/help/opinion#t2-q0" target="_blank">为什么被折叠？</a>
                <a class="btn-unfold" href="#">有一些短评被折叠了</a>
                <div class="qa-tip">
                    评论被折叠，是因为发布这条评论的帐号行为异常。评论仍可以被展开阅读，对发布人的账号不造成其他影响。如果认为有问题，可以<a href="https://help.douban.com/help/ask?category=movie">联系</a>豆瓣电影。
                </div>
            </div>
            <div class="fold-bd">
            </div>
            <span id="total-num"></span>
        </div>
        <div id="following-comments" class="tab">
            
    


        <div class="comment-item">
            你关注的人还没写过短评
        </div>

        </div>
    </div>


            
            
        </div>
    </div>
'''

p='''
<div class="comment-item" data-cid="1229096241">
            
    
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">237</span>
                <input value="1229096241" type="hidden">
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/4370686/" class="">鲸鱼君</a>
                    <span>看过</span>
                    <span class="allstar40 rating" title="推荐"></span>
                <span class="comment-time " title="2017-08-13 22:10:59">
                    2017-08-13
                </span>
            </span>
        </h3>
        <p class=""> 《十万个冷笑话2》：比上一部好。星球大战的画风配上《同桌的你》的音乐，乱入的喜羊羊模仿柯南，河神跟女娲用微信视频……这个动画诠释了后现代解构主义的含义，玩的是颠覆和嫁接，虽然没有深度和意义，但这些超越脑洞制造出的笑点既能让人惊呼“卧槽什么鬼”，又会使宅男们乐不可支。★★★☆ 
        </p>
    </div>

</div>
'''
a='''

<!DOCTYPE html>
<html lang="zh-cmn-Hans" class="ua-linux ua-webkit">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="renderer" content="webkit">
    <meta name="referrer" content="always">
    <title>
        十万个冷笑话2 (豆瓣)
</title>
    
    <meta name="baidu-site-verification" content="cZdR4xxR7RxmM4zE" />
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
    
    <link rel="apple-touch-icon" href="https://img3.doubanio.com/f/movie/d59b2715fdea4968a450ee5f6c95c7d7a2030065/pics/movie/apple-touch-icon.png">
    <link href="https://img3.doubanio.com/f/shire/94213e812acbb00123f685909b4768bb304d16f3/css/douban.css" rel="stylesheet" type="text/css">
    <link href="https://img3.doubanio.com/f/shire/ae3f5a3e3085968370b1fc63afcecb22d3284848/css/separation/_all.css" rel="stylesheet" type="text/css">
    <link href="https://img3.doubanio.com/f/movie/3b4ee1d8b132cafb42c4e9f808c7526a41eee2db/css/movie/base/init.css" rel="stylesheet">
    <script type="text/javascript">var _head_start = new Date();</script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/movie/0495cb173e298c28593766009c7b0a953246c5b5/js/movie/lib/jquery.js"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/1efae2c2d48b407a9bed76b9dd5dd8de37a8dbe1/js/douban.js"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/0efdc63b77f895eaf85281fb0e44d435c6239a3f/js/separation/_all.js"></script>
    
    <meta name="keywords" content="十万个冷笑话2,十万个冷笑话2,十万个冷笑话2影评,剧情介绍,电影图片,预告片,影讯,在线购票,论坛">
    <meta name="description" content="十万个冷笑话2电影简介和剧情介绍,十万个冷笑话2影评、图片、预告片、影讯、论坛、在线购票">
    <meta name="mobile-agent" content="format=html5; url=http://m.douban.com/movie/subject/26759539/"/>
    <link rel="alternate" href="android-app://com.douban.movie/doubanmovie/subject/26759539/" />
    <link rel="stylesheet" href="https://img3.doubanio.com/dae/cdnlib/libs/LikeButton/1.0.5/style.min.css">
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/77323ae72a612bba8b65f845491513ff3329b1bb/js/do.js" data-cfg-autoload="false"></script>
    <script type="text/javascript">
      Do.add('dialog', {path: 'https://img3.doubanio.com/f/shire/3d185ca912c999ee7f464749201139ebf8eb6972/js/ui/dialog.js', type: 'js'});
      Do.add('dialog-css', {path: 'https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css', type: 'css'});
      Do.add('handlebarsjs', {path: 'https://img3.doubanio.com/f/movie/3d4f8e4a8918718256450eb6e57ec8e1f7a2e14b/js/movie/lib/handlebars.current.js', type: 'js'});
    </script>
    
  <script type='text/javascript'>
  var _vwo_code = (function() {
    var account_id = 249272,
      settings_tolerance = 0,
      library_tolerance = 2500,
      use_existing_jquery = false,
      // DO NOT EDIT BELOW THIS LINE
      f=false,d=document;return{use_existing_jquery:function(){return use_existing_jquery;},library_tolerance:function(){return library_tolerance;},finish:function(){if(!f){f=true;var a=d.getElementById('_vis_opt_path_hides');if(a)a.parentNode.removeChild(a);}},finished:function(){return f;},load:function(a){var b=d.createElement('script');b.src=a;b.type='text/javascript';b.innerText;b.onerror=function(){_vwo_code.finish();};d.getElementsByTagName('head')[0].appendChild(b);},init:function(){settings_timer=setTimeout('_vwo_code.finish()',settings_tolerance);var a=d.createElement('style'),b='body{opacity:0 !important;filter:alpha(opacity=0) !important;background:none !important;}',h=d.getElementsByTagName('head')[0];a.setAttribute('id','_vis_opt_path_hides');a.setAttribute('type','text/css');if(a.styleSheet)a.styleSheet.cssText=b;else a.appendChild(d.createTextNode(b));h.appendChild(a);this.load('//dev.visualwebsiteoptimizer.com/j.php?a='+account_id+'&u='+encodeURIComponent(d.URL)+'&r='+Math.random());return settings_timer;}};}());

  +function () {
    var bindEvent = function (el, type, handler) {
        var $ = window.jQuery || window.Zepto || window.$
       if ($ && $.fn && $.fn.on) {
           $(el).on(type, handler)
       } else if($ && $.fn && $.fn.bind) {
           $(el).bind(type, handler)
       } else if (el.addEventListener){
         el.addEventListener(type, handler, false);
       } else if (el.attachEvent){
         el.attachEvent("on" + type, handler);
       } else {
         el["on" + type] = handler;
       }
     }

    var _origin_load = _vwo_code.load
    _vwo_code.load = function () {
      var args = [].slice.call(arguments)
      bindEvent(window, 'load', function () {
        _origin_load.apply(_vwo_code, args)
      })
    }
  }()

  _vwo_settings_timer = _vwo_code.init();
  </script>


    <style type="text/css">
  
</style>
    <style type="text/css">img { max-width: 100%; }</style>
    <script type="text/javascript"></script>
    <link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/2f38f0e6a3170096.css">

    <link rel="shortcut icon" href="https://img3.doubanio.com/favicon.ico" type="image/x-icon">
</head>

<body>
  
    <script type="text/javascript">var _body_start = new Date();</script>

    
    



    <link href="//img3.doubanio.com/dae/accounts/resources/0b32f51/shire/bundle.css" rel="stylesheet" type="text/css">



<div id="db-global-nav" class="global-nav">
  <div class="bd">
    
<div class="top-nav-info">
  <a href="https://www.douban.com/accounts/login?source=movie" class="nav-login" rel="nofollow">登录</a>
  <a href="https://www.douban.com/accounts/register?source=movie" class="nav-register" rel="nofollow">注册</a>
</div>


    
<div class="top-nav-doubanapp">
  <a href="https://www.douban.com/doubanapp/app?channel=top-nav" class="lnk-doubanapp">下载豆瓣客户端</a>
  <div id="top-nav-appintro" class="more-items">
    <p class="appintro-title">豆瓣</p>
    <p class="slogan">我们的精神角落</p>
    <p class="qrcode">扫码直接下载</p>
    <div class="download">
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=iOS">iPhone</a>
      <span>·</span>
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=Android" class="download-android">Android</a>
    </div>
    <div id="doubanapp-tip">
      <a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 5.0 全新发布</a>
      <a href="javascript: void 0;" class="tip-close">×</a>
    </div>
  </div>
</div>

    


<div class="global-nav-items">
  <ul>
    <li class="">
      <a href="https://www.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-main&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣</a>
    </li>
    <li class="">
      <a href="https://book.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-book&quot;,&quot;uid&quot;:&quot;0&quot;}">读书</a>
    </li>
    <li class="on">
      <a href="https://movie.douban.com"  data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-movie&quot;,&quot;uid&quot;:&quot;0&quot;}">电影</a>
    </li>
    <li class="">
      <a href="https://music.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-music&quot;,&quot;uid&quot;:&quot;0&quot;}">音乐</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/location" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-location&quot;,&quot;uid&quot;:&quot;0&quot;}">同城</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/group" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-group&quot;,&quot;uid&quot;:&quot;0&quot;}">小组</a>
    </li>
    <li class="">
      <a href="https://read.douban.com&#47;?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-read&quot;,&quot;uid&quot;:&quot;0&quot;}">阅读</a>
    </li>
    <li class="">
      <a href="https://douban.fm&#47;?from_=shire_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-fm&quot;,&quot;uid&quot;:&quot;0&quot;}">FM</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/time&#47;?dt_time_source=douban-web_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-time&quot;,&quot;uid&quot;:&quot;0&quot;}">时间</a>
    </li>
    <li class="">
      <a href="https://dongxi.douban.com&#47;?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-commodity&quot;,&quot;uid&quot;:&quot;0&quot;}">东西</a>
    </li>
    <li class="">
      <a href="https://market.douban.com&#47;?utm_campaign=douban_top_nav&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-market&quot;,&quot;uid&quot;:&quot;0&quot;}">市集</a>
    </li>
    <li>
      <a href="#more" class="bn-more"><span>更多</span></a>
      <div class="more-items">
        <table cellpadding="0" cellspacing="0">
          <tbody>
            <tr>
              <td>
                <a href="https://ypy.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-ypy&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣摄影</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </li>
  </ul>
</div>

  </div>
</div>
<script>
  ;window._GLOBAL_NAV = {
    DOUBAN_URL: "https://www.douban.com",
    N_NEW_NOTIS: 0,
    N_NEW_DOUMAIL: 0
  };
</script>



    <script src="//img3.doubanio.com/dae/accounts/resources/0b32f51/shire/bundle.js" defer="defer"></script>




    



    <link href="//img3.doubanio.com/dae/accounts/resources/0b32f51/movie/bundle.css" rel="stylesheet" type="text/css">




<div id="db-nav-movie" class="nav">
  <div class="nav-wrap">
  <div class="nav-primary">
    <div class="nav-logo">
      <a href="https:&#47;&#47;movie.douban.com">豆瓣电影</a>
    </div>
    <div class="nav-search">
      <form action="https:&#47;&#47;movie.douban.com/subject_search" method="get">
        <fieldset>
          <legend>搜索：</legend>
          <label for="inp-query">
          </label>
          <div class="inp"><input id="inp-query" name="search_text" size="22" maxlength="60" placeholder="电影、影人、影院、电视剧" value=""></div>
          <div class="inp-btn"><input type="submit" value="搜索"></div>
          <input type="hidden" name="cat" value="1002" />
        </fieldset>
      </form>
    </div>
  </div>
  </div>
  <div class="nav-secondary">
    

<div class="nav-items">
  <ul>
    <li    ><a href="https://movie.douban.com/cinema/nowplaying/"
     >影讯&购票</a>
    </li>
    <li    ><a href="https://movie.douban.com/explore"
     >选电影</a>
    </li>
    <li    ><a href="https://movie.douban.com/tv/"
     >电视剧</a>
    </li>
    <li    ><a href="https://movie.douban.com/chart"
     >排行榜</a>
    </li>
    <li    ><a href="https://movie.douban.com/tag/"
     >分类</a>
    </li>
    <li    ><a href="https://movie.douban.com/review/best/"
     >影评</a>
    </li>
    <li    ><a href="https://movie.douban.com/annual2016/?source=navigation"
     >2016年度榜单</a>
    </li>
    <li    ><a href="https://movie.douban.com/standbyme/2016?source=navigation"
     >2016观影报告</a>
    </li>
  </ul>
</div>

  </div>
</div>

<script id="suggResult" type="text/x-jquery-tmpl">
  <li data-link="{{= url}}">
            <a href="{{= url}}" onclick="moreurl(this, {from:'movie_search_sugg', query:'{{= keyword }}', subject_id:'{{= id}}', i: '{{= index}}', type: '{{= type}}'})">
            <img src="{{= img}}" width="40" />
            <p>
                <em>{{= title}}</em>
                {{if year}}
                    <span>{{= year}}</span>
                {{/if}}
                {{if sub_title}}
                    <br /><span>{{= sub_title}}</span>
                {{/if}}
                {{if address}}
                    <br /><span>{{= address}}</span>
                {{/if}}
                {{if episode}}
                    {{if episode=="unknow"}}
                        <br /><span>集数未知</span>
                    {{else}}
                        <br /><span>共{{= episode}}集</span>
                    {{/if}}
                {{/if}}
            </p>
        </a>
        </li>
  </script>




    <script src="//img3.doubanio.com/dae/accounts/resources/0b32f51/movie/bundle.js" defer="defer"></script>





    
    <div id="wrapper">
        

        
    <div id="content">
        

    <div id="dale_movie_subject_top_icon"></div>
    <h1>
        <span property="v:itemreviewed">十万个冷笑话2</span>
            <span class="year">(2017)</span>
    </h1>

        <div class="grid-16-8 clearfix">
            

            
            <div class="article">
                
    

    





        <div class="indent clearfix">
            <div class="subjectwrap clearfix" xmlns:v="http://rdf.data-vocabulary.org/#" typeof="v:Movie">
                <div class="subject clearfix">
                    



<div id="mainpic" class="">
    <a class="nbgnbg" href="https://movie.douban.com/subject/26759539/photos?type=R" title="点击看更多海报">
        <img src="https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2492917402.webp" title="点击看更多海报" alt="十万个冷笑话2" rel="v:image" />
   </a>
</div>

                    


<div id="info">
        <span ><span class='pl'>导演</span>: <span class='attrs'><a href="/celebrity/1343619/" rel="v:directedBy">卢恒宇</a> / <a href="/celebrity/1345414/" rel="v:directedBy">李姝洁</a></span></span><br/>
        <span ><span class='pl'>编剧</span>: <span class='attrs'><a href="/celebrity/1343619/">卢恒宇</a> / <a href="/celebrity/1345414/">李姝洁</a> / <a href="/celebrity/1377973/">寒舞</a> / <a href="/celebrity/1377974/">隋佳林</a> / <a href="/celebrity/1377975/">高信影</a> / <a href="/celebrity/1321206/">赵聪</a></span></span><br/>
        <span class="actor"><span class='pl'>主演</span>: <span class='attrs'><a href="/celebrity/1334349/" rel="v:starring">山新</a> / <a href="/celebrity/1340968/" rel="v:starring">郝祥海</a> / <a href="/celebrity/1345414/" rel="v:starring">李姝洁</a> / <a href="/celebrity/1352712/" rel="v:starring">藤新</a> / <a href="/celebrity/1343032/" rel="v:starring">图特哈蒙</a> / <a href="/celebrity/1337468/" rel="v:starring">李佳怡</a> / <a href="/celebrity/1361154/" rel="v:starring">佟心竹</a> / <a href="/celebrity/1274213/" rel="v:starring">九孔</a> / <a href="/celebrity/1343619/" rel="v:starring">卢恒宇</a> / <a href="/celebrity/1334350/" rel="v:starring">宝木中阳</a></span></span><br/>
        <span class="pl">类型:</span> <span property="v:genre">喜剧</span> / <span property="v:genre">动画</span> / <span property="v:genre">奇幻</span><br/>
        
        <span class="pl">制片国家/地区:</span> 中国大陆<br/>
        <span class="pl">语言:</span> 汉语普通话<br/>
        <span class="pl">上映日期:</span> <span property="v:initialReleaseDate" content="2017-08-18(中国大陆)">2017-08-18(中国大陆)</span><br/>
        <span class="pl">片长:</span> <span property="v:runtime" content="101">101分钟</span><br/>
        <span class="pl">又名:</span> 十冷2 / One Hundred Thousand Bad Jokes II<br/>
        

</div>




                </div>
                    


<div id="interest_sectl">
    <div class="rating_wrap clearbox" rel="v:rating">
        <div class="clearfix">
          <div class="rating_logo ll">
              豆瓣评分
          </div>
          <div class="output-btn-wrap rr" style="display:none">
            <img src="https://img3.doubanio.com/f/movie/692e86756648f29457847c5cc5e161d6f6b8aaac/pics/movie/reference.png" />
            <a class="download-output-image" href="#">引用</a>
          </div>
          
          
        </div>
        


<div class="rating_self clearfix" typeof="v:Rating">
    <strong class="ll rating_num" property="v:average">7.6</strong>
    <span property="v:best" content="10.0"></span>
    <div class="rating_right ">
        <div class="ll bigstar bigstar40"></div>
        <div class="rating_sum">
                <a href="collections" class="rating_people"><span property="v:votes">26713</span>人评价</a>
        </div>
    </div>
</div>
<div class="ratings-on-weight">
    
        <div class="item">
        
        <span class="stars5 starstop" title="力荐">
            5星
        </span>
        <div class="power" style="width:32px"></div>
        <span class="rating_per">22.0%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars4 starstop" title="推荐">
            4星
        </span>
        <div class="power" style="width:64px"></div>
        <span class="rating_per">44.0%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars3 starstop" title="还行">
            3星
        </span>
        <div class="power" style="width:39px"></div>
        <span class="rating_per">27.1%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars2 starstop" title="较差">
            2星
        </span>
        <div class="power" style="width:7px"></div>
        <span class="rating_per">5.2%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars1 starstop" title="很差">
            1星
        </span>
        <div class="power" style="width:2px"></div>
        <span class="rating_per">1.7%</span>
        <br />
        </div>
</div>

    </div>
        <div class="rating_betterthan">
            好于 <a href="/typerank?type_name=喜剧&type=24&interval_id=80:70&action=">75% 喜剧片</a><br/>
            好于 <a href="/typerank?type_name=动画&type=25&interval_id=55:45&action=">53% 动画片</a><br/>
        </div>
</div>


                
            </div>
                




<div id="interest_sect_level" class="clearfix">
        
            <a href="https://www.douban.com/reason=collectwish&amp;ck=" rel="nofollow" class="j a_show_login colbutt ll" name="pbtn-26759539-wish">
                <span>想看</span>
            </a>
            <a href="https://www.douban.com/reason=collectcollect&amp;ck=" rel="nofollow" class="j a_show_login colbutt ll" name="pbtn-26759539-collect">
                <span>看过</span>
            </a>
        <div class="ll j a_stars">
            
    
    评价:
    <span id="rating"> <span id="stars" data-solid="https://img3.doubanio.com/f/shire/5a2327c04c0c231bced131ddf3f4467eb80c1c86/pics/rating_icons/star_onmouseover.png" data-hollow="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" data-solid-2x="https://img3.doubanio.com/f/shire/7258904022439076d57303c3b06ad195bf1dc41a/pics/rating_icons/star_onmouseover@2x.png" data-hollow-2x="https://img3.doubanio.com/f/shire/95cc2fa733221bb8edd28ad56a7145a5ad33383e/pics/rating_icons/star_hollow_hover@2x.png">

            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-26759539-1">
        <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star1" width="16" height="16"/></a>
            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-26759539-2">
        <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star2" width="16" height="16"/></a>
            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-26759539-3">
        <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star3" width="16" height="16"/></a>
            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-26759539-4">
        <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star4" width="16" height="16"/></a>
            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-26759539-5">
        <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star5" width="16" height="16"/></a>
    </span><span id="rateword" class="pl"></span>
    <input id="n_rating" type="hidden" value=""  />
    </span>

        </div>
    

</div>


            


















<div class="gtleft">
    <ul class="ul_subject_menu bicelink color_gray pt6 clearfix">
        
    
        
                <li> 
    <img src="https://img3.doubanio.com/f/shire/cc03d0fcf32b7ce3af7b160a0b85e5e66b47cc42/pics/short-comment.gif" />&nbsp;
        <a onclick="moreurl(this, {from:'mv_sbj_wr_cmnt_login'})" class="j a_show_login" href="https://www.douban.com/register?reason=review" rel="nofollow">写短评</a>
 </li>
                    <li> 
    
    <img src="https://img3.doubanio.com/f/shire/5bbf02b7b5ec12b23e214a580b6f9e481108488c/pics/add-review.gif" />&nbsp;
        <a onclick="moreurl(this, {from:'mv_sbj_wr_rv_login'})" class="j a_show_login" href="https://www.douban.com/register?reason=review" rel="nofollow">写影评</a>
 </li>
                    <li> 
    <img src="https://img3.doubanio.com/f/shire/61cc48ba7c40e0272d46bb93fe0dc514f3b71ec5/pics/add-doulist.gif" />&nbsp;
    <a href="/subject/26759539/questions/ask?from=subject_top">提问题</a>
 </li>
                <li> 
    



 </li>
                <li> 
   

   
    
    <span class="rec" id="电影-26759539">
    <a href= "#"
        data-type="电影"
        data-url="https://movie.douban.com/subject/26759539/"
        data-desc="电影《十万个冷笑话2》 (来自豆瓣) "
        data-title="电影《十万个冷笑话2》 (来自豆瓣) "
        data-pic="https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2492917402.jpeg"
        class="bn-sharing ">
        分享到
    </a> &nbsp;&nbsp;
    </span>

    <script>
        if (!window.DoubanShareMenuList) {
            window.DoubanShareMenuList = [];
        }
        var __cache_url = __cache_url || {};

        (function(u){
            if(__cache_url[u]) return;
            __cache_url[u] = true;
            window.DoubanShareIcons = 'https://img3.doubanio.com/f/shire/d15ffd71f3f10a7210448fec5a68eaec66e7f7d0/pics/ic_shares.png';

            var initShareButton = function() {
                $.ajax({url:u,dataType:'script',cache:true});
            };

            if (typeof Do == 'function' && 'ready' in Do) {
                Do(
                    'https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css',
                    'https://img3.doubanio.com/f/shire/3d185ca912c999ee7f464749201139ebf8eb6972/js/ui/dialog.js',
                    'https://img3.doubanio.com/f/movie/c4ab132ff4d3d64a83854c875ea79b8b541faf12/js/movie/lib/qrcode.min.js',
                    initShareButton
                );
            } else if(typeof Douban == 'object' && 'loader' in Douban) {
                Douban.loader.batch(
                    'https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css',
                    'https://img3.doubanio.com/f/shire/3d185ca912c999ee7f464749201139ebf8eb6972/js/ui/dialog.js',
                    'https://img3.doubanio.com/f/movie/c4ab132ff4d3d64a83854c875ea79b8b541faf12/js/movie/lib/qrcode.min.js'
                ).done(initShareButton);
            }

        })('https://img3.doubanio.com/f/movie/32be6727ed3ad8f6c4a417d8a086355c3e7d1d27/js/movie/lib/sharebutton.js');
    </script>


  </li>
            

    </ul>

    <script type="text/javascript">
        $(function(){
            $(".ul_subject_menu li.rec .bn-sharing").bind("click", function(){
                $.get("/blank?sbj_page_click=bn_sharing");
            });
        });
    </script>
</div>




                





<div class="rec-sec">
<span class="rec">
    <script id="movie-share" type="text/x-html-snippet">
        
    <form class="movie-share" action="/j/share" method="POST">
        <div class="clearfix form-bd">
            <div class="input-area">
                <textarea name="text" class="share-text" cols="72" data-mention-api="https://api.douban.com/shuo/in/complete?alt=xd&amp;callback=?"></textarea>
                <input type="hidden" name="target-id" value="26759539">
                <input type="hidden" name="target-type" value="0">
                <input type="hidden" name="title" value="十万个冷笑话2‎ (2017)">
                <input type="hidden" name="desc" value="导演 卢恒宇 主演 山新 / 郝祥海 / 中国大陆 / 7.6分(26713评价)">
                <input type="hidden" name="redir" value=""/>
                <div class="mentioned-highlighter"></div>
            </div>

            <div class="info-area">
                    <img class="media" src="https://img3.doubanio.com/view/movie_poster_cover/ipst/public/p2492917402.webp" />
                <strong>十万个冷笑话2‎ (2017)</strong>
                <p>导演 卢恒宇 主演 山新 / 郝祥海 / 中国大陆 / 7.6分(26713评价)</p>
                <p class="error server-error">&nbsp;</p>
            </div>
        </div>
        <div class="form-ft">
            <div class="form-ft-inner">
                



                <span class="avail-num-indicator">140</span>
                <span class="bn-flat">
                    <input type="submit" value="推荐" />
                </span>
            </div>
        </div>
    </form>
    
    <div id="suggest-mention-tmpl" style="display:none;">
        <ul>
            {{#users}}
            <li id="{{uid}}">
              <img src="{{avatar}}">{{{username}}}&nbsp;<span>({{{uid}}})</span>
            </li>
            {{/users}}
        </ul>
    </div>


    </script>

        
        <a href="/accounts/register?reason=recommend"  class="j a_show_login lnk-sharing" share-id="26759539" data-mode="plain" data-name="十万个冷笑话2‎ (2017)" data-type="movie" data-desc="导演 卢恒宇 主演 山新 / 郝祥海 / 中国大陆 / 7.6分(26713评价)" data-href="https://movie.douban.com/subject/26759539/" data-image="https://img3.doubanio.com/view/movie_poster_cover/ipst/public/p2492917402.webp" data-properties="{}" data-redir="" data-text="" data-apikey="" data-curl="" data-count="10" data-object_kind="1002" data-object_id="26759539" data-target_type="rec" data-target_action="0" data-action_props="{&#34;subject_url&#34;:&#34;https:\/\/movie.douban.com\/subject\/26759539\/&#34;,&#34;subject_title&#34;:&#34;十万个冷笑话2‎ (2017)&#34;}">推荐</a>
</span>


</div>






            <script type="text/javascript">
                $(function() {
                    $('.collect_btn', '#interest_sect_level').each(function() {
                        Douban.init_collect_btn(this);
                    });
                    $('html').delegate(".indent .rec-sec .lnk-sharing", "click", function() {
                        moreurl(this, {
                            from : 'mv_sbj_db_share'
                        });
                    });
                });
            </script>
        </div>
            


    <div id="collect_form_26759539"></div>


        


<div class="related-info" style="margin-bottom:-10px;">
    <a name="intro"></a>
    
        
            
            
    <h2>
        <i class="">十万个冷笑话2的剧情简介</i>
              · · · · · ·
    </h2>

            <div class="indent" id="link-report">
                    
                        <span property="v:summary" class="">
                                　　拥有着强大力量的创世神杖被四大神之一的埃及神拉（李璐 配音）盗走。为了令宇宙免于被毁灭的悲惨命运，希腊神宙斯（藤新 配音）派出了自己的女儿雅典娜（山新 配音）追踪神杖的下落。
                                    <br />
                                　　小金刚（皇贞季 配音）是自幼生长在孤儿院里的平凡少年，常年凭借着机灵的脑瓜靠着坑蒙拐骗赚钱度日，只为了有朝一日身患重病的青梅竹马小青（C小调 配音）能够康复。一次偶然中，小金刚得到了藏有创世神杖下落的藏宝图，随后遭到了雷神托尔（李姝洁 饰）的伏击，在争抢之中，藏宝图被破坏，就这样，小金刚成为了唯一一个知道创世神杖在哪里的凡人。就这样，小金刚、雅典娜、托尔，再加上一个来自东方的脱线河神（郝祥海 饰），一行四人踏上了寻找创世神杖的旅途。
                        </span>
                        <span class="pl"><a href="https://movie.douban.com/help/movie#t0-qs">&copy;豆瓣</a></span>
            </div>
</div>


    








<div id="celebrities" class="celebrities related-celebrities">

  
    <h2>
        <i class="">十万个冷笑话2的影人</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="/subject/26759539/celebrities">全部 17</a>
            ) </span>
    </h2>


  <ul class="celebrities-list from-subject __oneline">
      
    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1343619/" title="卢恒宇 " class="">
      <div class="avatar" style="background-image: url(https://img3.doubanio.com/img/celebrity/medium/1498213042.81.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1343619/" title="卢恒宇 " class="name">卢恒宇 </a></span>

      <span class="role" title="导演">导演</span>

    </div>
  </li>


      
    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1345414/" title="李姝洁 " class="">
      <div class="avatar" style="background-image: url(https://img3.doubanio.com/img/celebrity/medium/1498213287.65.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1345414/" title="李姝洁 " class="name">李姝洁 </a></span>

      <span class="role" title="导演">导演</span>

    </div>
  </li>


      
    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1334349/" title="山新 " class="">
      <div class="avatar" style="background-image: url(https://img3.doubanio.com/img/celebrity/medium/1398540567.14.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1334349/" title="山新 " class="name">山新 </a></span>

      <span class="role" title="饰 雅典娜">饰 雅典娜</span>

    </div>
  </li>


      
    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1340968/" title="郝祥海 " class="">
      <div class="avatar" style="background-image: url(https://img3.doubanio.com/img/celebrity/medium/1502784728.0.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1340968/" title="郝祥海 " class="name">郝祥海 </a></span>

      <span class="role" title="饰 河神">饰 河神</span>

    </div>
  </li>


      
    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1345414/" title="李姝洁 " class="">
      <div class="avatar" style="background-image: url(https://img3.doubanio.com/img/celebrity/medium/1498213287.65.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1345414/" title="李姝洁 " class="name">李姝洁 </a></span>

      <span class="role" title="饰 托尔">饰 托尔</span>

    </div>
  </li>


      
    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1352712/" title="藤新 " class="">
      <div class="avatar" style="background-image: url(https://img3.doubanio.com/img/celebrity/medium/1506003445.05.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1352712/" title="藤新 " class="name">藤新 </a></span>

      <span class="role" title="饰 宙斯">饰 宙斯</span>

    </div>
  </li>


  </ul>
</div>




    

<link rel="stylesheet" href="https://img3.doubanio.com/f/fanta/ba954f353fb7e2f830059e78c8e9e4791a96a4f6/components/dist/css/answer_entry.css">
<div id="author-wrapper" class="author-wrapper">
    <div class="loading"></div>
</div>
<script type="text/javascript">
    var answerObj = {
      ISALL: 'False',
      TYPE: 'movie',
      SUBJECT_ID: '26759539',
      USER_ID: 'None'
    }
</script>
<script type="text/javascript" src="https://img3.doubanio.com/f/movie/c7d6644d315d980333c64c04211e62e87a34dbcd/js/movie/lib/react.min.js"></script>
<script type="text/javascript" src="https://img3.doubanio.com/f/movie/d61288cc4105ce8dea909962536609eb73ea715a/js/movie/lib/react-dom.min.js"></script>
<script type="text/javascript" src="https://img3.doubanio.com/f/fanta/8cf39700a22a263dfd1bdd8fe01eda3b24857129/components/dist/answer_entry.js"></script> 

    









    
    <div id="related-pic" class="related-pic">
        
    
    
    <h2>
        <i class="">十万个冷笑话2的视频和图片</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/26759539/trailer#trailer">预告片15</a>&nbsp;|&nbsp;<a href="https://movie.douban.com/subject/26759539/all_photos">图片295</a>&nbsp;|&nbsp;<a href="https://movie.douban.com/subject/26759539/mupload">添加图片</a>
            ) </span>
    </h2>


        <ul class="related-pic-bd">
                <li>
                    <a class="related-pic-video" href="https://movie.douban.com/trailer/220136/#content">
                        <span></span>
                        <img src="https://img3.doubanio.com/img/trailer/medium/2495352736.jpg?" alt="预告片" />
                    </a>
                </li>
                <li>
                    <a href="https://movie.douban.com/photos/photo/2496482241/"><img src="https://img3.doubanio.com/view/photo/sqxs/public/p2496482241.webp" alt="图片" /></a>
                </li>
                <li>
                    <a href="https://movie.douban.com/photos/photo/2496902390/"><img src="https://img3.doubanio.com/view/photo/sqxs/public/p2496902390.webp" alt="图片" /></a>
                </li>
                <li>
                    <a href="https://movie.douban.com/photos/photo/2496298664/"><img src="https://img3.doubanio.com/view/photo/sqxs/public/p2496298664.webp" alt="图片" /></a>
                </li>
                <li>
                    <a href="https://movie.douban.com/photos/photo/2496796825/"><img src="https://img3.doubanio.com/view/photo/sqxs/public/p2496796825.webp" alt="图片" /></a>
                </li>
        </ul>
    </div>



    
    



<style type="text/css">
.award li { display: inline; margin-right: 5px }
.awards { margin-bottom: 20px }
.awards h2 { background: none; color: #000; font-size: 14px; padding-bottom: 5px; margin-bottom: 8px; border-bottom: 1px dashed #dddddd }
.awards .year { color: #666666; margin-left: -5px }
.mod { margin-bottom: 25px }
.mod .hd { margin-bottom: 10px }
.mod .hd h2 {margin:24px 0 3px 0}
</style>



    








    <div id="recommendations" class="">
        
        
    <h2>
        <i class="">喜欢这部电影的人也喜欢</i>
              · · · · · ·
    </h2>

        
    
    <div class="recommendations-bd">
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/25805054/?from=subject-page" >
                    <img src="https://img1.doubanio.com/view/movie_poster_cover/lpst/public/p2217523448.webp" alt="十万个冷笑话" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/25805054/?from=subject-page" class="" >十万个冷笑话</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/26811587/?from=subject-page" >
                    <img src="https://img1.doubanio.com/view/movie_poster_cover/lpst/public/p2490948849.webp" alt="大护法" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/26811587/?from=subject-page" class="" >大护法</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/27038183/?from=subject-page" >
                    <img src="https://img1.doubanio.com/view/movie_poster_cover/lpst/public/p2499793218.webp" alt="羞羞的铁拳" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/27038183/?from=subject-page" class="" >羞羞的铁拳</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/25662329/?from=subject-page" >
                    <img src="https://img1.doubanio.com/view/movie_poster_cover/lpst/public/p2315672647.webp" alt="疯狂动物城" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/25662329/?from=subject-page" class="" >疯狂动物城</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/26145033/?from=subject-page" >
                    <img src="https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2417949761.webp" alt="乐高蝙蝠侠大电影" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/26145033/?from=subject-page" class="" >乐高蝙蝠侠大电影</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/25812712/?from=subject-page" >
                    <img src="https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2469070974.webp" alt="神偷奶爸3" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/25812712/?from=subject-page" class="" >神偷奶爸3</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/11589036/?from=subject-page" >
                    <img src="https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2306653420.webp" alt="功夫熊猫3" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/11589036/?from=subject-page" class="" >功夫熊猫3</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1306249/?from=subject-page" >
                    <img src="https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p1946455272.webp" alt="唐伯虎点秋香" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1306249/?from=subject-page" class="" >唐伯虎点秋香</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/26354572/?from=subject-page" >
                    <img src="https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2411622136.webp" alt="欢乐好声音" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/26354572/?from=subject-page" class="" >欢乐好声音</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/4202982/?from=subject-page" >
                    <img src="https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2166640945.webp" alt="冰雪奇缘" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/4202982/?from=subject-page" class="" >冰雪奇缘</a>
            </dd>
        </dl>
    </div>

    </div>


        


<script type="text/x-handlebar-tmpl" id="comment-tmpl">
    <div class="dummy-fold">
        {{#each comments}}
        <div class="comment-item" data-cid="id">
            <div class="comment">
                <h3>
                    <span class="comment-vote">
                            <span class="votes">{{votes}}</span>
                        <input value="{{id}}" type="hidden"/>
                        <a href="javascript:;" class="j {{#if ../if_logined}}a_vote_comment{{else}}a_show_login{{/if}}">有用</a>
                    </span>
                    <span class="comment-info">
                        <a href="{{user.path}}" class="">{{user.name}}</a>
                        {{#if rating}}
                        <span class="allstar{{rating}}0 rating" title="{{rating_word}}"></span>
                        {{/if}}
                        <span>
                            {{time}}
                        </span>
                        <p> {{content}} </p>
                    </span>
            </div>
        </div>
        {{/each}}
    </div>
</script>












    

    <div id="comments-section">
        <div class="mod-hd">
            
        <a class="comment_btn j a_show_login" href="https://www.douban.com/register?reason=review" rel="nofollow">
            <span>我要写短评</span>
        </a>

            
            
    <h2>
        <i class="">十万个冷笑话2的短评</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/26759539/comments?status=P">全部 14478 条</a>
            ) </span>
    </h2>

        </div>
        <div class="mod-bd">
                
    <div class="tab-hd">
        <a id="hot-comments-tab" href="comments" data-id="hot" class="on">热门</a>&nbsp;/&nbsp;
        <a id="new-comments-tab" href="comments?sort=time" data-id="new">最新</a>&nbsp;/&nbsp;
        <a id="following-comments-tab" href="follows_comments" data-id="following"  class="j a_show_login">好友</a>
    </div>

    <div class="tab-bd">
        <div id="hot-comments" class="tab">
            
    
        <div class="comment-item" data-cid="1230796249">
            
    
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">1442</span>
                <input value="1230796249" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/pojian1987/" class="">破茧</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2017-08-17 14:38:39">
                    2017-08-17
                </span>
            </span>
        </h3>
        <p class=""> 大量经典动画乱入，但又不显得突兀。

大量广告强行插入，但又不显得讨厌。

大量槽点刚想骂娘，却发现这是笑点。

大量笑点全程密集，腹肌没痛膀胱痛。

总之，就是一句话：值得一看。
        </p>
    </div>

        </div>
        <div class="comment-item" data-cid="1229144122">
            
    
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">195</span>
                <input value="1229144122" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/53547561/" class="">智商二百五</a>
                    <span>看过</span>
                    <span class="allstar40 rating" title="推荐"></span>
                <span class="comment-time " title="2017-08-13 23:22:50">
                    2017-08-13
                </span>
            </span>
        </h3>
        <p class=""> 雷神·单身狗·表情包·托尔
        </p>
    </div>

        </div>
        <div class="comment-item" data-cid="1227527640">
            
    
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">102</span>
                <input value="1227527640" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/63898543/" class="">Citrus</a>
                    <span>看过</span>
                    <span class="allstar30 rating" title="还行"></span>
                <span class="comment-time " title="2017-08-10 19:31:31">
                    2017-08-10
                </span>
            </span>
        </h3>
        <p class=""> 时光机：你爸我从小在草原长大——原来是草原孤儿院啊喂！ps 结尾的脑洞真喜欢
        </p>
    </div>

        </div>
        <div class="comment-item" data-cid="1228420067">
            
    
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">132</span>
                <input value="1228420067" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/romanbaby/" class="">婴儿葛葛</a>
                    <span>看过</span>
                    <span class="allstar30 rating" title="还行"></span>
                <span class="comment-time " title="2017-08-12 17:01:56">
                    2017-08-12
                </span>
            </span>
        </h3>
        <p class=""> 结尾创意可能是近期看到的动画片里最好的
        </p>
    </div>

        </div>
        <div class="comment-item" data-cid="1229306970">
            
    
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">163</span>
                <input value="1229306970" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/2123968/" class="">静待花开</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2017-08-14 11:20:16">
                    2017-08-14
                </span>
            </span>
        </h3>
        <p class=""> 影片中致敬了很多经典电影和人物啊～用搞笑的方式面对操蛋的人生，脑洞大开的这个系列始终坚持自己的搞怪风格，真的很难得
        </p>
    </div>

        </div>



                
                &gt; <a href="comments?sort=new_score&status=P" >更多短评14478条</a>
        </div>
        <div id="new-comments" class="tab">
            <div id="normal">
            </div>
            <div class="fold-hd hide">
                <a class="qa" href="/help/opinion#t2-q0" target="_blank">为什么被折叠？</a>
                <a class="btn-unfold" href="#">有一些短评被折叠了</a>
                <div class="qa-tip">
                    评论被折叠，是因为发布这条评论的帐号行为异常。评论仍可以被展开阅读，对发布人的账号不造成其他影响。如果认为有问题，可以<a href="https://help.douban.com/help/ask?category=movie">联系</a>豆瓣电影。
                </div>
            </div>
            <div class="fold-bd">
            </div>
            <span id="total-num"></span>
        </div>
        <div id="following-comments" class="tab">
            
    


        <div class="comment-item">
            你关注的人还没写过短评
        </div>

        </div>
    </div>


            
            
        </div>
    </div>



    
    
        
            





<div id="askmatrix">
    <div class="mod-hd">
        <h2>
            关于《十万个冷笑话2》的问题
            · · · · · ·
            <span class="pl">
                (<a href='https://movie.douban.com/subject/26759539/questions/?from=subject'>
                    全部16个
                </a>)
            </span>
        </h2>


        
    
    <a class='j a_show_login comment_btn'
        href='https://movie.douban.com/subject/26759539/questions/ask/?from=subject'>我来提问</a>

    </div>

    <div class="mod-bd">
        <ul class="">
            <li class="">
                <span class="tit">
                    <a href="https://movie.douban.com/subject/26759539/questions/750923/?from=subject" class="">
                            为什么叫拉？
                    </a>
                </span>
                <span class="meta">
                    7人回答
                </span>
            </li>
            <li class="">
                <span class="tit">
                    <a href="https://movie.douban.com/subject/26759539/questions/750906/?from=subject" class="">
                            大家说说哪块情节让你们笑了？
                    </a>
                </span>
                <span class="meta">
                    16人回答
                </span>
            </li>
            <li class="">
                <span class="tit">
                    <a href="https://movie.douban.com/subject/26759539/questions/747631/?from=subject" class="">
                            为什么不直接取名叫《二十万个冷笑话》呢？
                    </a>
                </span>
                <span class="meta">
                    15人回答
                </span>
            </li>
            <li class="">
                <span class="tit">
                    <a href="https://movie.douban.com/subject/26759539/questions/750551/?from=subject" class="">
                            这算是前传吗？
                    </a>
                </span>
                <span class="meta">
                    7人回答
                </span>
            </li>
            <li class="">
                <span class="tit">
                    <a href="https://movie.douban.com/subject/26759539/questions/751057/?from=subject" class="">
                            最后降维有没有借鉴《头脑特工队》？
                    </a>
                </span>
                <span class="meta">
                    3人回答
                </span>
            </li>
        </ul>

        <p>&gt;
            <a href='https://movie.douban.com/subject/26759539/questions/?from=subject'>
                全部16个问题
            </a>
        </p>

    </div>
</div>



        

        

<link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/60f5fa5d8f2f04dc.css">

<section class="reviews mod movie-content">
    <header>
        <a href="new_review" rel="nofollow" class="create-review comment_btn" 
            data-isverify="False"
            data-verify-url="https://www.douban.com/accounts/phone/verify?redir=http://movie.douban.com/subject/26759539/new_review">
            <span>我要写影评</span>
        </a>
        <h2>
            十万个冷笑话2的影评 · · · · · ·
            <span class="pl">(<a href="reviews">全部 275 条</a>)</span>
        </h2>
    </header>


        


<div class="review-list">
  
  
      
  



  <div xmlns:v="http://rdf.data-vocabulary.org/#" typeof="v:Review" data-cid="8759742">
    <div class="main review-item" id="8759742">
        

  <header class="main-hd">
    <h3 class="title">
      <a href="https://movie.douban.com/review/8759742/" class="title-link">高度剧透，说说我还记得的十冷二的梗。我对十冷...</a>
      <div class="toggle_review right">        <a href="javascript:;" id="toggle-8759742"class="indicator unfold j" title="展开全文">        </a>
      </div>
    </h3>
    

<div class="header-more">
    <a class="author-avatar" href="https://www.douban.com/people/145002365/"><img width="48" height="48" src="https://img1.doubanio.com/icon/user_normal.jpg"></a>
    <a href="https://www.douban.com/people/145002365/" class="author">
      <span property="v:reviewer">苍云古齿剑</span>
    </a>    <span property="v:rating" class="allstar50 main-title-rating" title="力荐"></span>
  <span property="v:dtreviewed" content="2017-08-18"
      class="main-meta">2017-08-18 18:03:47</span>
</div>

  </header>

        <div class="main-bd">
          <div id="review_8759742_short" class="review-short">
            <div class="short-content">
                  <p class="main-title-tip">
                    这篇影评可能有剧透
                  </p>
                  <div class="toggle_review">
                    &gt;&nbsp;                    <a href="javascript:;" id="toggle-8759742-copy" class="unfold j" title="展开全文">                      没关系，可以显示全文                    </a>
                  </div>
            </div>
          </div>
          <div id="review_8759742_full" class="hidden">
            <div id="review_8759742_full_content" class="full-content"></div>
          </div>
        </div>
    </div>
  </div>

      
  



  <div xmlns:v="http://rdf.data-vocabulary.org/#" typeof="v:Review" data-cid="8766390">
    <div class="main review-item" id="8766390">
        

  <header class="main-hd">
    <h3 class="title">
      <a href="https://movie.douban.com/review/8766390/" class="title-link">挖掘十冷2的近100个剧情梗、BGM梗、广告梗、台词梗</a>
      <div class="toggle_review right">        <a href="javascript:;" id="toggle-8766390"class="indicator unfold j" title="展开全文">        </a>
      </div>
    </h3>
    

<div class="header-more">
    <a class="author-avatar" href="https://www.douban.com/people/MYfuneral/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u82413300-3.jpg"></a>
    <a href="https://www.douban.com/people/MYfuneral/" class="author">
      <span property="v:reviewer">般狐</span>
    </a>    <span property="v:rating" class="allstar40 main-title-rating" title="推荐"></span>
  <span property="v:dtreviewed" content="2017-08-21"
      class="main-meta">2017-08-21 15:51:22</span>
</div>

  </header>

        <div class="main-bd">
          <div id="review_8766390_short" class="review-short">
            <div class="short-content">
                  <p class="main-title-tip">
                    这篇影评可能有剧透
                  </p>
                  <div class="toggle_review">
                    &gt;&nbsp;                    <a href="javascript:;" id="toggle-8766390-copy" class="unfold j" title="展开全文">                      没关系，可以显示全文                    </a>
                  </div>
            </div>
          </div>
          <div id="review_8766390_full" class="hidden">
            <div id="review_8766390_full_content" class="full-content"></div>
          </div>
        </div>
    </div>
  </div>

      
  



  <div xmlns:v="http://rdf.data-vocabulary.org/#" typeof="v:Review" data-cid="8758419">
    <div class="main review-item" id="8758419">
        

  <header class="main-hd">
    <h3 class="title">
      <a href="https://movie.douban.com/review/8758419/" class="title-link">就是要逗你笑，越贱越好</a>
      <div class="toggle_review right">        <a href="javascript:;" id="toggle-8758419"class="indicator unfold j" title="展开全文">        </a>
      </div>
    </h3>
    

<div class="header-more">
    <a class="author-avatar" href="https://www.douban.com/people/48369193/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u48369193-6.jpg"></a>
    <a href="https://www.douban.com/people/48369193/" class="author">
      <span property="v:reviewer">二十二岛主</span>
    </a>    <span property="v:rating" class="allstar30 main-title-rating" title="还行"></span>
  <span property="v:dtreviewed" content="2017-08-18"
      class="main-meta">2017-08-18 00:13:47</span>
</div>

  </header>

        <div class="main-bd">
          <div id="review_8758419_short" class="review-short">
            <div class="short-content">
                  <p class="main-title-tip">
                    这篇影评可能有剧透
                  </p>
                  <div class="toggle_review">
                    &gt;&nbsp;                    <a href="javascript:;" id="toggle-8758419-copy" class="unfold j" title="展开全文">                      没关系，可以显示全文                    </a>
                  </div>
            </div>
          </div>
          <div id="review_8758419_full" class="hidden">
            <div id="review_8758419_full_content" class="full-content"></div>
          </div>
        </div>
    </div>
  </div>

      
  



  <div xmlns:v="http://rdf.data-vocabulary.org/#" typeof="v:Review" data-cid="8761273">
    <div class="main review-item" id="8761273">
        

  <header class="main-hd">
    <h3 class="title">
      <a href="https://movie.douban.com/review/8761273/" class="title-link">大杂烩</a>
      <div class="toggle_review right">        <a href="javascript:;" id="toggle-8761273"class="indicator unfold j" title="展开全文">        </a>
      </div>
    </h3>
    

<div class="header-more">
    <a class="author-avatar" href="https://www.douban.com/people/149237033/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u149237033-1.jpg"></a>
    <a href="https://www.douban.com/people/149237033/" class="author">
      <span property="v:reviewer">长安</span>
    </a>    <span property="v:rating" class="allstar30 main-title-rating" title="还行"></span>
  <span property="v:dtreviewed" content="2017-08-19"
      class="main-meta">2017-08-19 13:18:55</span>
</div>

  </header>

        <div class="main-bd">
          <div id="review_8761273_short" class="review-short">
            <div class="short-content">
                  《十万个冷笑话2》并没有对第一部就已经存在的问题做出真正的改变，而这一次的呈现虽然比之前作有着些许的提升，但那仍旧是在胡编乱造的尴尬剧情，生硬的包袱都只是让电影显得尤为低幼，而乱打情怀致敬牌的拼凑更是无法让人对这部电影本身产生多少感触。 一部动画电影最为重要...

                    <a class="pl" href="https://movie.douban.com/review/8761273/#comments">(46回应)</a>
                  <div class="more-info pl clearfix">
                    <span class="left">70有用 / 56没用</span>
                  </div>
            </div>
          </div>
          <div id="review_8761273_full" class="hidden">
            <div id="review_8761273_full_content" class="full-content"></div>
          </div>
        </div>
    </div>
  </div>

      
  



  <div xmlns:v="http://rdf.data-vocabulary.org/#" typeof="v:Review" data-cid="8752778">
    <div class="main review-item" id="8752778">
        

  <header class="main-hd">
    <h3 class="title">
      <a href="https://movie.douban.com/review/8752778/" class="title-link">在“我”的世界里 寻找快乐的意义</a>
      <div class="toggle_review right">        <a href="javascript:;" id="toggle-8752778"class="indicator unfold j" title="展开全文">        </a>
      </div>
    </h3>
    

<div class="header-more">
    <a class="author-avatar" href="https://www.douban.com/people/127665862/"><img width="48" height="48" src="https://img3.doubanio.com/icon/u127665862-5.jpg"></a>
    <a href="https://www.douban.com/people/127665862/" class="author">
      <span property="v:reviewer">如墨画卷</span>
    </a>    <span property="v:rating" class="allstar50 main-title-rating" title="力荐"></span>
  <span property="v:dtreviewed" content="2017-08-15"
      class="main-meta">2017-08-15 22:00:25</span>
</div>

  </header>

        <div class="main-bd">
          <div id="review_8752778_short" class="review-short">
            <div class="short-content">
                  <p class="main-title-tip">
                    这篇影评可能有剧透
                  </p>
                  <div class="toggle_review">
                    &gt;&nbsp;                    <a href="javascript:;" id="toggle-8752778-copy" class="unfold j" title="展开全文">                      没关系，可以显示全文                    </a>
                  </div>
            </div>
          </div>
          <div id="review_8752778_full" class="hidden">
            <div id="review_8752778_full_content" class="full-content"></div>
          </div>
        </div>
    </div>
  </div>





</div>










            <p class="pl" align="right">
                &gt;
                <a href="reviews">
                    更多影评275篇
                </a>
            </p>
</section>
    
<script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/1e25d5191146f38f.js"></script>

    <br/>
    <div class="section-discussion">
            
            <div class="mod-hd">
                    <a class="comment_btn j a_show_login" href="https://www.douban.com/register?reason=review" rel="nofollow"><span>添加新话题</span></a>
                
    <h2>
        讨论区
         &nbsp; &middot;&nbsp; &middot;&nbsp; &middot;&nbsp; &middot;&nbsp; &middot;&nbsp; &middot;
    </h2>

            </div>
            
  <table class="olt"><tr><td><td><td><td></tr>
        
        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/26759539/discussion/614973552/" title="说一些梗 冷门梗">说一些梗 冷门梗</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/165198127/">社会你熊老板er</a></td>
          <td class="pl"><span>82 回应</span></td>
          <td class="pl"><span>2017-10-02</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/26759539/discussion/614972880/" title="看《绝世高手》全程茫然的看这部片会感到搞笑吗">看《绝世高手》全程茫然的看这部片会感到搞笑吗</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/42177994/">再见渡洲</a></td>
          <td class="pl"><span>9 回应</span></td>
          <td class="pl"><span>2017-10-02</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/26759539/discussion/614960773/" title="立帖为证，十冷2正式上映不低于7.5分，赌20块钱话费。">立帖为证，十冷2正式上映不低于7.5分，赌20块钱话费。</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/64515288/">WillRious</a></td>
          <td class="pl"><span>183 回应</span></td>
          <td class="pl"><span>2017-10-02</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/26759539/discussion/614972021/" title="为什么叫拉？">为什么叫拉？</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/119123665/">term2000</a></td>
          <td class="pl"><span>51 回应</span></td>
          <td class="pl"><span>2017-10-02</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/26759539/discussion/614969784/" title="你们对剧情，真的，毫无要求吗？">你们对剧情，真的，毫无要求吗？</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/58703374/">炽天使-然</a></td>
          <td class="pl"><span>67 回应</span></td>
          <td class="pl"><span>2017-10-02</span></td>
        </tr>
  </table>

            <p class="pl" align="right">
                <a href="/subject/26759539/discussion/" rel="nofollow">
                    &gt; 去这部影片的讨论区（全部70条）
                </a>
            </p>
    </div>
    <script type="text/javascript">
        $(function(){if($.browser.msie && $.browser.version == 6.0){
            var $info = $('#info'),
                maxWidth = parseInt($info.css('max-width'));
            if($info.width() > maxWidth) {
                $info.width(maxWidth);
            }
        }});
    </script>


            </div>
            <div class="aside">
                


    









    <!-- douban ad begin -->
    <div id="dale_movie_subject_top_right"></div>
    <div id="dale_movie_subject_top_middle"></div>
    <!-- douban ad end -->

    



<style type="text/css">
    .m4 {margin-bottom:8px; padding-bottom:8px;}
    .movieOnline {background:#FFF6ED; padding:10px; margin-bottom:20px;}
    .movieOnline h2 {margin:0 0 5px;}
    .movieOnline .sitename {line-height:2em; width:160px;}
    .movieOnline td,.movieOnline td a:link,.movieOnline td a:visited{color:#666;}
    .movieOnline td a:hover {color:#fff;}
    .link-bt:link,
    .link-bt:visited,
    .link-bt:hover,
    .link-bt:active {margin:5px 0 0; padding:2px 8px; background:#a8c598; color:#fff; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; display:inline-block;}
</style>



    







    
    <div class="tags">
        
        
    <h2>
        <i class="">豆瓣成员常用的标签</i>
              · · · · · ·
    </h2>

        <div class="tags-body">
                <a href="/tag/搞笑" class="">搞笑</a>
                <a href="/tag/脑洞" class="">脑洞</a>
                <a href="/tag/国产动画" class="">国产动画</a>
                <a href="/tag/喜剧" class="">喜剧</a>
                <a href="/tag/国漫" class="">国漫</a>
                <a href="/tag/动画" class="">动画</a>
                <a href="/tag/2017" class="">2017</a>
                <a href="/tag/中国" class="">中国</a>
        </div>
    </div>


    <div id="dale_movie_subject_inner_middle"></div>
    <div id="dale_movie_subject_download_middle"></div>
        








<div id="subject-doulist">
    
    
    <h2>
        <i class="">以下豆列推荐</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/26759539/doulists">全部</a>
            ) </span>
    </h2>


    
    <ul>
            <li>
                <a href="https://www.douban.com/doulist/30299/" target="_blank">豆瓣电影【口碑榜】2017-09-22更新</a>
                <span>(影志)</span>
            </li>
            <li>
                <a href="https://www.douban.com/doulist/1295618/" target="_blank">【中国内地电影票房总排行】</a>
                <span>(荔枝超人)</span>
            </li>
            <li>
                <a href="https://www.douban.com/doulist/4286140/" target="_blank">国产动画片迎来了前所未有的春天！！！</a>
                <span>(武侠小王子)</span>
            </li>
            <li>
                <a href="https://www.douban.com/doulist/35918697/" target="_blank">正在上映</a>
                <span>(豆瓣电影)</span>
            </li>
            <li>
                <a href="https://www.douban.com/doulist/45651535/" target="_blank">烂片大全</a>
                <span>(liubinyan)</span>
            </li>
    </ul>

</div>

        








<div id="subject-others-interests">
    
    
    <h2>
        <i class="">谁在看这部电影</i>
              · · · · · ·
    </h2>

    
    <ul class="">
    </ul>

    
    <div class="subject-others-interests-ft">
        
            <a href="https://movie.douban.com/subject/26759539/collections">27824人看过</a>
                &nbsp;/&nbsp;
            <a href="https://movie.douban.com/subject/26759539/wishes">11730人想看</a>
    </div>

</div>



    
    

<!-- douban ad begin -->
<div id="dale_movie_subject_middle_right"></div>
<script type="text/javascript">
    (function (global) {
        if(!document.getElementsByClassName) {
            document.getElementsByClassName = function(className) {
                return this.querySelectorAll("." + className);
            };
            Element.prototype.getElementsByClassName = document.getElementsByClassName;

        }
        var articles = global.document.getElementsByClassName('article'),
            asides = global.document.getElementsByClassName('aside');

        if (articles.length > 0 && asides.length > 0 && articles[0].offsetHeight >= asides[0].offsetHeight) {
            (global.DoubanAdSlots = global.DoubanAdSlots || []).push('dale_movie_subject_middle_right');
        }
    })(this);
</script>
<!-- douban ad end -->



    <br/>

    
<p class="pl">订阅十万个冷笑话2的评论: <br/><span class="feed">
    <a href="https://movie.douban.com/feed/subject/26759539/reviews"> feed: rss 2.0</a></span></p>


            </div>
            <div class="extra">
                
    
<!-- douban ad begin -->
<div id="dale_movie_subject_bottom_super_banner"></div>
<script type="text/javascript">
    (function (global) {
        var body = global.document.body,
            html = global.document.documentElement;

        var height = Math.max(body.scrollHeight, body.offsetHeight, html.clientHeight, html.scrollHeight, html.offsetHeight);
        if (height >= 2000) {
            (global.DoubanAdSlots = global.DoubanAdSlots || []).push('dale_movie_subject_bottom_super_banner');
        }
    })(this);
</script>
<!-- douban ad end -->


            </div>
        </div>
    </div>

        
    <div id="footer">
            <div class="footer-extra"></div>
        
<span id="icp" class="fleft gray-link">
    &copy; 2005－2017 douban.com, all rights reserved 北京豆网科技有限公司
</span>

<a href="https://www.douban.com/hnypt/variformcyst.py" style="display: none;"></a>

<span class="fright">
    <a href="https://www.douban.com/about">关于豆瓣</a>
    · <a href="https://www.douban.com/jobs">在豆瓣工作</a>
    · <a href="https://www.douban.com/about?topic=contactus">联系我们</a>
    · <a href="https://www.douban.com/about?policy=disclaimer">免责声明</a>
    
    · <a href="https://help.douban.com/?app=movie" target="_blank">帮助中心</a>
    · <a href="https://www.douban.com/doubanapp/">移动应用</a>
    · <a href="https://www.douban.com/partner/">豆瓣广告</a>
</span>

    </div>

    </div>
    <script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/684220a8869faa38.js"></script>
        
        
    <link rel="stylesheet" type="text/css" href="https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css" />
    <link rel="stylesheet" type="text/css" href="https://img3.doubanio.com/f/movie/1d829b8605b9e81435b127cbf3d16563aaa51838/css/movie/mod/reg_login_pop.css" />
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/77323ae72a612bba8b65f845491513ff3329b1bb/js/do.js" data-cfg-autoload="false"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/3d185ca912c999ee7f464749201139ebf8eb6972/js/ui/dialog.js"></script>
    <script type="text/javascript">
        var HTTPS_DB='https://www.douban.com';
var account_pop={open:function(o,e){e?referrer="?referrer="+encodeURIComponent(e):referrer="?referrer="+window.location.href;var n="",i="",t=382;"reg"===o?(n="用户注册",i="https://accounts.douban.com/popup/login?source=movie#popup_register",t=480):"login"===o&&(n="用户登录",i="https://accounts.douban.com/popup/login?source=movie");var r=document.location.protocol+"//"+document.location.hostname,a=dui.Dialog({width:478,title:n,height:t,cls:"account_pop",isHideTitle:!0,modal:!0,content:"<iframe scrolling='no' frameborder='0' width='478' height='"+t+"' src='"+i+"' name='"+r+"'></iframe>"},!0),c=a.node;if(c.undelegate(),c.delegate(".dui-dialog-close","click",function(){var o=$("body");o.find("#login_msk").hide(),o.find(".account_pop").remove()}),$(window).width()<478){var u="";"reg"===o?u=HTTPS_DB+"/accounts/register"+referrer:"login"===o&&(u=HTTPS_DB+"/accounts/login"+referrer),window.location.href=u}else a.open();$(window).bind("message",function(o){"https://accounts.douban.com"===o.originalEvent.origin&&(c.find("iframe").css("height",o.originalEvent.data),c.height(o.originalEvent.data),a.update())})}};Douban&&Douban.init_show_login&&(Douban.init_show_login=function(o){var e=$(o);e.click(function(){var o=e.data("ref")||"";return account_pop.open("login",o),!1})}),Do(function(){$("body").delegate(".pop_register","click",function(o){o.preventDefault();var e=$(this).data("ref")||"";return account_pop.open("reg",e),!1}),$("body").delegate(".pop_login","click",function(o){o.preventDefault();var e=$(this).data("ref")||"";return account_pop.open("login",e),!1})});
    </script>

    
    
    
    




    
<script type="text/javascript">
    (function (global) {
        var newNode = global.document.createElement('script'),
            existingNode = global.document.getElementsByTagName('script')[0],
            adSource = '//erebor.douban.com/',
            userId = '',
            browserId = 'H0ak-4BoUEM',
            criteria = '7:郝祥海|7:动漫|7:奇幻|7:李姝洁|7:国产动画|7:九孔|7:卢恒宇|7:藤新|7:国产|7:宝木中阳|7:中国|7:李佳怡|7:国漫|7:脑洞|7:佟心竹|7:搞笑|7:喜剧|7:动画|7:2017|7:图特哈蒙|7:山新|3:/subject/26759539/?from=tag_all',
            preview = '',
            debug = false,
            adSlots = ['dale_movie_subject_top_icon', 'dale_movie_subject_top_right', 'dale_movie_subject_top_middle', 'dale_movie_subject_inner_middle', 'dale_movie_subject_download_middle'];

        global.DoubanAdRequest = {src: adSource, uid: userId, bid: browserId, crtr: criteria, prv: preview, debug: debug};
        global.DoubanAdSlots = (global.DoubanAdSlots || []).concat(adSlots);

        newNode.setAttribute('type', 'text/javascript');
        newNode.setAttribute('src', 'https://img3.doubanio.com/f/adjs/581c3c87bd224677f6207b2b3ba1e4a512cbb1dc/ad.release.js');
        newNode.setAttribute('async', true);
        existingNode.parentNode.insertBefore(newNode, existingNode);
    })(this);
</script>











    
  









<script type="text/javascript">
var _paq = _paq || [];
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
    var p=(('https:' == document.location.protocol) ? 'https' : 'http'), u=p+'://fundin.douban.com/';
    _paq.push(['setTrackerUrl', u+'piwik']);
    _paq.push(['setSiteId', '100001']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript';
    g.defer=true;
    g.async=true;
    g.src=p+'://img3.doubanio.com/dae/fundin/piwik.js';
    s.parentNode.insertBefore(g,s);
})();
</script>

<script type="text/javascript">
var setMethodWithNs = function(namespace) {
  var ns = namespace ? namespace + '.' : ''
    , fn = function(string) {
        if(!ns) {return string}
        return ns + string
      }
  return fn
}

var gaWithNamespace = function(fn, namespace) {
  var method = setMethodWithNs(namespace)
  fn.call(this, method)
}

var _gaq = _gaq || []
  , accounts = [
      { id: 'UA-7019765-1', namespace: 'douban' }
    , { id: 'UA-7019765-19', namespace: '' }
    ]
  , gaInit = function(account) {
      gaWithNamespace(function(method) {
        gaInitFn.call(this, method, account)
      }, account.namespace)
    }
  , gaInitFn = function(method, account) {
      _gaq.push([method('_setAccount'), account.id]);
      _gaq.push([method('_setSampleRate'), '5']);

      
  _gaq.push([method('_addOrganic'), 'google', 'q'])
  _gaq.push([method('_addOrganic'), 'baidu', 'wd'])
  _gaq.push([method('_addOrganic'), 'soso', 'w'])
  _gaq.push([method('_addOrganic'), 'youdao', 'q'])
  _gaq.push([method('_addOrganic'), 'so.360.cn', 'q'])
  _gaq.push([method('_addOrganic'), 'sogou', 'query'])
  if (account.namespace) {
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣'])
    _gaq.push([method('_addIgnoredOrganic'), 'douban'])
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣网'])
    _gaq.push([method('_addIgnoredOrganic'), 'www.douban.com'])
  }

      if (account.namespace === 'douban') {
        _gaq.push([method('_setDomainName'), '.douban.com'])
      }

        _gaq.push([method('_setCustomVar'), 1, 'responsive_view_mode', 'desktop', 3])

        _gaq.push([method('_setCustomVar'), 2, 'login_status', '0', 2]);

      _gaq.push([method('_trackPageview')])
    }

for(var i = 0, l = accounts.length; i < l; i++) {
  var account = accounts[i]
  gaInit(account)
}


;(function() {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
})()
</script>








      
    

    <!-- daisy4b-docker-->

  <script>_SPLITTEST=''</script>
</body>

</html>



'''
# pattern=re.compile(r'<span class="votes">(.*?)</span>.*?comment">(.*?)</a>.*?</span>.*?<span.*?class="">(.*?)</a>.*?<span>(.*?)</span>.*?title="(.*?)"></span>.*?title="(.*?)">.*?class=""> (.*?)\n',re.S)
pattern=re.compile('<div.*?typeof="v:Rating">.*?property="v:average">(.*?)</strong>.*?<div.*?class="comment-item".*?>.*?<p.*?class="">(.*?)</p>',re.S)
pattern1=re.compile('<span class="votes">(.*?)</span>.*?class="comment-time ".*?>(.*?)</span>',re.S)
pattern2=re.compile('<div.*?typeof="v:Rating">.*?property="v:average">(.*?)</strong>.*?<p class="">(.*?)</p>',re.S)
comment=re.findall(pattern2,a)
# print(comment)
for row in comment:
    print(row)