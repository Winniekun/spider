'''
@author：KongWeiKun
@file: re_test.py
@time: 17-9-29 下午4:43
@contact: 836242657@qq.com
'''
import re
q='''

<!DOCTYPE html>
<html lang="zh-cmn-Hans" class="ua-linux ua-webkit">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="renderer" content="webkit">
    <meta name="referrer" content="always">
    <title>寻梦环游记 短评</title>
    
    <meta name="baidu-site-verification" content="cZdR4xxR7RxmM4zE" />
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
    
    <meta name="keywords" content="寻梦环游记,Coco,影讯,排片,放映时间,电影票价,在线购票"/>
    <meta name="description" content="寻梦环游记短评" />
    <meta name="mobile-agent" content="format=html5; url=http://m.douban.com/movie/subject/20495023/comments"/>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/77323ae72a612bba8b65f845491513ff3329b1bb/js/do.js" data-cfg-autoload="false"></script>

    <link rel="apple-touch-icon" href="https://img3.doubanio.com/f/movie/d59b2715fdea4968a450ee5f6c95c7d7a2030065/pics/movie/apple-touch-icon.png">
    <link href="https://img3.doubanio.com/f/shire/da18e98a294047dd92298000fe2080b38efda2ae/css/douban.css" rel="stylesheet" type="text/css">
    <link href="https://img3.doubanio.com/f/shire/ae3f5a3e3085968370b1fc63afcecb22d3284848/css/separation/_all.css" rel="stylesheet" type="text/css">
    <link href="https://img3.doubanio.com/f/movie/8864d3756094f5272d3c93e30ee2e324665855b0/css/movie/base/init.css" rel="stylesheet">
    <script type="text/javascript">var _head_start = new Date();</script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/movie/0495cb173e298c28593766009c7b0a953246c5b5/js/movie/lib/jquery.js"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/1efae2c2d48b407a9bed76b9dd5dd8de37a8dbe1/js/douban.js"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/0efdc63b77f895eaf85281fb0e44d435c6239a3f/js/separation/_all.js"></script>
    
    <style type="text/css"></style>
    <style type="text/css">img { max-width: 100%; }</style>
    <script type="text/javascript"></script>
    <link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/13a836970108bf09.css">

    <link rel="shortcut icon" href="https://img3.doubanio.com/favicon.ico" type="image/x-icon">
</head>

<body>
  
    <script type="text/javascript">var _body_start = new Date();</script>

    
    



    <link href="//img3.doubanio.com/dae/accounts/resources/321e246/shire/bundle.css" rel="stylesheet" type="text/css">



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
      <a href="https://time.douban.com&#47;?dt_time_source=douban-web_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-time&quot;,&quot;uid&quot;:&quot;0&quot;}">时间</a>
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



    <script src="//img3.doubanio.com/dae/accounts/resources/321e246/shire/bundle.js" defer="defer"></script>




    



    <link href="//img3.doubanio.com/dae/accounts/resources/321e246/movie/bundle.css" rel="stylesheet" type="text/css">




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
          <div class="inp"><input id="inp-query" name="search_text" size="22" maxlength="60" placeholder="搜索电影、电视剧、综艺、影人" value=""></div>
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




    <script src="//img3.doubanio.com/dae/accounts/resources/321e246/movie/bundle.js" defer="defer"></script>





    
    <div id="wrapper">
        

        
    <div id="content">
        
    <h1>寻梦环游记 短评</h1>

        <div class="grid-16-8 clearfix">
            
            
            <div class="article">
                
    



<div class="clearfix Comments-hd">
    <ul class="fleft CommentTabs">
            <li class="is-active">
                <span>看过(88810)</span>
            </li>

            <li>
                <a href="?status=F">想看(1316)</a>
            </li>
    </ul>
    <div class="fright">
        <a href="javascript:;" class="comment_btn j a_show_login" name="cbtn-20495023">我来写短评</a>
    </div>
</div>

    
    <div class="title_line clearfix color_gray">
        <div class="fleft Comments-sortby">
                <span>热门</span>
                <a href="?sort=time&status=P">最新</a>
            <a href="follows_comments?status=P" class="j a_show_login">好友</a>
        </div>
    </div>

    <div class="comment-filter">
        <label>
            <input type="radio" name="sort" value=""  checked="checked"><span class="filter-name">全部</span><span class="comment-percent"></span>
        </label>
        <label>
            <input type="radio" name="sort" value="h" ><span class="filter-name">好评</span><span class="comment-percent">94%</span>
        </label>
        <label>
            <input type="radio" name="sort" value="m" ><span class="filter-name">一般</span><span class="comment-percent">4%</span>
        </label>
        <label>
            <input type="radio" name="sort" value="l" ><span class="filter-name">差评</span><span class="comment-percent">2%</span>
        </label>
    </div>

    <div class="mod-bd" id="comments">
        







    
        
        <div class="comment-item" data-cid="1274216591">
            
    
        <div class="avatar">
            <a title="西楼尘" href="https://www.douban.com/people/xilouchen/">
                <img src="https://img3.doubanio.com/icon/u49290419-14.jpg" class="" />
            </a>
        </div>
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">9939</span>
                <input value="1274216591" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/xilouchen/" class="">西楼尘</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2017-11-20 23:01:54">
                    2017-11-20
                </span>
            </span>
        </h3>
        <p class=""> 供奉的遗像是牵引家人回家的通道，驻留的记忆是保持亡灵存续的神力，热闹的音乐是唤醒思念启封的药引。我为你写了首歌，穿越浩瀚的岁月烟尘，捱过冰冷的孤独冬季，横跨漫长的天人之路，在你老去的时候，唱给你听。这瑰丽的灯火万家，摇曳的烛光千盏，不如你梳着麻花辫坐在床头时，眼里闪烁的星光璀璨。
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1272459662">
            
    
        <div class="avatar">
            <a title="nek" href="https://www.douban.com/people/qrzf/">
                <img src="https://img3.doubanio.com/icon/u3202333-183.jpg" class="" />
            </a>
        </div>
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">8715</span>
                <input value="1272459662" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/qrzf/" class="">nek</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2017-11-17 16:21:08">
                    2017-11-17
                </span>
            </span>
        </h3>
        <p class=""> 邻座的女孩哭倒在我怀里啊电影多么美妙！
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1273977139">
            
    
        <div class="avatar">
            <a title="帝月" href="https://www.douban.com/people/steve647/">
                <img src="https://img3.doubanio.com/icon/u46841511-13.jpg" class="" />
            </a>
        </div>
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">7822</span>
                <input value="1273977139" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/steve647/" class="">帝月</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2017-11-20 13:30:34">
                    2017-11-20
                </span>
            </span>
        </h3>
        <p class=""> 广州试片会。主持人在现场透露：Coco原本涉及到亡灵题材，是不能引进的。但是在过审时，当场看哭了所有广电审查人员，so破例让过了。。。
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1274629886">
            
    
        <div class="avatar">
            <a title="小歪" href="https://www.douban.com/people/35552430/">
                <img src="https://img3.doubanio.com/icon/u35552430-6.jpg" class="" />
            </a>
        </div>
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">3938</span>
                <input value="1274629886" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/35552430/" class="">小歪</a>
                    <span>看过</span>
                    <span class="allstar30 rating" title="还行"></span>
                <span class="comment-time " title="2017-11-21 22:14:18">
                    2017-11-21
                </span>
            </span>
        </h3>
        <p class=""> 无后同性恋们的一场极大的噩梦。
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1271992746">
            
    
        <div class="avatar">
            <a title="Juillet.🌳" href="https://www.douban.com/people/vip_fiona/">
                <img src="https://img3.doubanio.com/icon/u1520402-410.jpg" class="" />
            </a>
        </div>
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">5116</span>
                <input value="1271992746" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/vip_fiona/" class="">Juillet.🌳</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2017-11-16 16:09:05">
                    2017-11-16
                </span>
            </span>
        </h3>
        <p class=""> 我们是人类的一分子，而人类是充满激情的。医学、法律、商业、科技，这些都是崇高的追求，足以支撑人的一生。但音乐、诗歌、梦想、情感，这些才是我们活着的意义。
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1265348886">
            
    
        <div class="avatar">
            <a title="小九儿" href="https://www.douban.com/people/cloudy20011128/">
                <img src="https://img3.doubanio.com/icon/u1763584-26.jpg" class="" />
            </a>
        </div>
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">3291</span>
                <input value="1265348886" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/cloudy20011128/" class="">小九儿</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2017-11-02 07:28:41">
                    2017-11-02
                </span>
            </span>
        </h3>
        <p class=""> 11月1日亡灵节当天，墨西哥城的影院里，隔壁座儿的小男孩画着鬼脸儿穿着骷髅服，老奶奶抱着万寿菊，举家一起看coco。生活与动画交叠而映，感慨又感动，炫目又泪目。这才叫文化输出，好羡慕，好嫉妒。（ps：盖尔加西亚~不枉爱了你十余年）（pps：开场前送了20分钟冰雪奇缘番外 ，以为走错片场）
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1268390428">
            
    
        <div class="avatar">
            <a title="朽木立夏" href="https://www.douban.com/people/lassiedusky/">
                <img src="https://img1.doubanio.com/icon/u3270510-27.jpg" class="" />
            </a>
        </div>
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">3214</span>
                <input value="1268390428" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/lassiedusky/" class="">朽木立夏</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2017-11-16 21:07:36">
                    2017-11-16
                </span>
            </span>
        </h3>
        <p class=""> 第一次觉得死后世界通往人间的万寿菊之桥和七夕鹊桥是一样的原理，爱不分种类是共通的，相见是因为想念，存在是因为记忆的力量。而只有墨西哥人能有欢乐的能力把悼念先人的节日过得如此五彩斑斓。欢迎有女儿的爸爸来影院哭一哭。亡灵节海关大厅井井有条，效率极佳!拒绝寂静的死后世界，我们要喧嚣!
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1274054952">
            
    
        <div class="avatar">
            <a title="虎哥" href="https://www.douban.com/people/57460299/">
                <img src="https://img3.doubanio.com/icon/u57460299-2.jpg" class="" />
            </a>
        </div>
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">2727</span>
                <input value="1274054952" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/57460299/" class="">虎哥</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2017-11-20 16:38:20">
                    2017-11-20
                </span>
            </span>
        </h3>
        <p class=""> 满分。毕竟我已经很久没有看个电影哭得像个小孩子了 似乎大家又要说起那句老话：电影是绝佳的造梦机器。那些回不去的家乡 没能守护的家人也只有在梦里相见。
                
                <a class="source-icon" href="https://www.douban.com/doubanapp/" target="_blank"><img src="https://img3.doubanio.com/f/shire/c541f3cbc321589b29d7c7b6d00e620243f224d9/pics/comment/iphone.png" title="发自iPhone" alt="iPhone" rel="v:image"/></a>
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1272178186">
            
    
        <div class="avatar">
            <a title="影志" href="https://www.douban.com/people/tjz230/">
                <img src="https://img1.doubanio.com/icon/u1005928-127.jpg" class="" />
            </a>
        </div>
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">2049</span>
                <input value="1272178186" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/tjz230/" class="">影志</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2017-11-16 23:21:45">
                    2017-11-16
                </span>
            </span>
        </h3>
        <p class=""> 皮克斯保持原创的又一巅峰，回忆与遗忘的情感核心，在家庭、音乐、梦想、冒险的故事线下饱满溢出银幕，最后只能以泪洗面。2017年度最佳电影！
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1272156627">
            
    
        <div class="avatar">
            <a title="阿德" href="https://www.douban.com/people/joearde/">
                <img src="https://img3.doubanio.com/icon/u1015534-35.jpg" class="" />
            </a>
        </div>
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">1932</span>
                <input value="1272156627" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/joearde/" class="">阿德</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2017-11-16 22:42:52">
                    2017-11-16
                </span>
            </span>
        </h3>
        <p class=""> 不得不服皮克斯，一边和你探讨梦想、成功、家庭的意义；一边用各种充满想象力的情节、画面、音乐，让你叹为观止；这样的电影，怎能不爱。（家长指导：6岁以上推荐看，虽然有亡灵情节，但这可是一个关于爱的故事。）
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1276245008">
            
    
        <div class="avatar">
            <a title="桃桃淘电影" href="https://www.douban.com/people/qijiuzhiyue/">
                <img src="https://img3.doubanio.com/icon/u1032989-50.jpg" class="" />
            </a>
        </div>
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">1397</span>
                <input value="1276245008" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/qijiuzhiyue/" class="">桃桃淘电影</a>
                    <span>看过</span>
                    <span class="allstar40 rating" title="推荐"></span>
                <span class="comment-time " title="2017-11-25 14:25:22">
                    2017-11-25
                </span>
            </span>
        </h3>
        <p class=""> 亲情催泪弹。所以，动画会不会好看，除了技术，更重要的还是如何讲好故事，把感情放进去，借作品把情感传递开，包括这部以及头脑特工队等很多能成功，皆是如此。不过，有些人似乎总是搞不懂这件事。
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1275659165">
            
    
        <div class="avatar">
            <a title="Kirara酱" href="https://www.douban.com/people/crab802/">
                <img src="https://img1.doubanio.com/icon/u1301195-38.jpg" class="" />
            </a>
        </div>
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">1652</span>
                <input value="1275659165" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/crab802/" class="">Kirara酱</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2017-11-24 09:56:06">
                    2017-11-24
                </span>
            </span>
        </h3>
        <p class=""> 人有三次死亡。第一次是生物学的死亡；第二次是社会宣布你死亡；第三次是最后一个记得你的人离开这个世界。
想念上个月去世的外婆，想念老爸，想念所有离我而去的人们。
后悔没带纸，平复了半天情绪最后离开放映厅。。。
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1275992287">
            
    
        <div class="avatar">
            <a title="王大根" href="https://www.douban.com/people/diewithme/">
                <img src="https://img3.doubanio.com/icon/u4640303-132.jpg" class="" />
            </a>
        </div>
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">1065</span>
                <input value="1275992287" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/diewithme/" class="">王大根</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2017-11-24 22:54:47">
                    2017-11-24
                </span>
            </span>
        </h3>
        <p class=""> 死后世界还是这么三六九等，穷逼死了还是穷逼，那还不如被快点遗忘消失掉啊！
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1276176310">
            
    
        <div class="avatar">
            <a title="萨库拉" href="https://www.douban.com/people/iisakura/">
                <img src="https://img1.doubanio.com/icon/u4193588-7.jpg" class="" />
            </a>
        </div>
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">702</span>
                <input value="1276176310" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/iisakura/" class="">萨库拉</a>
                    <span>看过</span>
                    <span class="allstar30 rating" title="还行"></span>
                <span class="comment-time " title="2017-11-25 11:40:38">
                    2017-11-25
                </span>
            </span>
        </h3>
        <p class=""> 准备好的纸巾完全没用上。可能作为一个伦理冷感的人，大家庭不是我的点。而且皮克斯的剧本愈发磕磕绊绊，第二幕冒险和最后的反转毫无新意，价值观非常保守，“被人记住”其实是为“传宗接代”代言，最后也在梦想和家庭之间和了把稀泥。
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1242791408">
            
    
        <div class="avatar">
            <a title="羚羊的灵魂" href="https://www.douban.com/people/clzleo/">
                <img src="https://img1.doubanio.com/icon/u59237362-8.jpg" class="" />
            </a>
        </div>
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">663</span>
                <input value="1242791408" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/clzleo/" class="">羚羊的灵魂</a>
                    <span>看过</span>
                    <span class="allstar40 rating" title="推荐"></span>
                <span class="comment-time " title="2017-11-13 11:48:24">
                    2017-11-13
                </span>
            </span>
        </h3>
        <p class=""> 麻烦说比头脑特工队好的适可而止，coco这烂大街的设定真的被头脑完爆。只是一些观众更吃coco这种温情又煽情的故事罢了
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1276891984">
            
    
        <div class="avatar">
            <a title="张小北" href="https://www.douban.com/people/xzfd/">
                <img src="https://img1.doubanio.com/icon/u2279829-7.jpg" class="" />
            </a>
        </div>
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">902</span>
                <input value="1276891984" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/xzfd/" class="">张小北</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2017-11-26 16:28:02">
                    2017-11-26
                </span>
            </span>
        </h3>
        <p class=""> 不算皮克斯史上最佳，但在今年这个格外寒冷的冬天，它足够温暖。
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1276982139">
            
    
        <div class="avatar">
            <a title="shininglove" href="https://www.douban.com/people/2849243/">
                <img src="https://img1.doubanio.com/icon/u2849243-58.jpg" class="" />
            </a>
        </div>
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">710</span>
                <input value="1276982139" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/2849243/" class="">shininglove</a>
                    <span>看过</span>
                    <span class="allstar40 rating" title="推荐"></span>
                <span class="comment-time " title="2017-11-26 19:25:14">
                    2017-11-26
                </span>
            </span>
        </h3>
        <p class=""> 老人不图儿女为家做多大贡献呀，一辈子不容易就图个团团圆圆。皮克斯替蔡国庆唱了回春晚。
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1272146051">
            
    
        <div class="avatar">
            <a title="Luc" href="https://www.douban.com/people/LucFrance/">
                <img src="https://img3.doubanio.com/icon/u1978083-1.jpg" class="" />
            </a>
        </div>
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">652</span>
                <input value="1272146051" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/LucFrance/" class="">Luc</a>
                    <span>看过</span>
                    <span class="allstar40 rating" title="推荐"></span>
                <span class="comment-time " title="2017-11-16 22:23:49">
                    2017-11-16
                </span>
            </span>
        </h3>
        <p class=""> 一个基于文化传统的完整世界观，挖掘了死亡与回忆的意义。绚烂热闹的亡灵界令人神往，皮克斯技术上的优势再度体现的淋漓尽致。故事上更像《飞屋》和《头脑》的墨西哥音乐MV版，家族的温情对应的是偶像的坍塌，成长的叛逆与梦想总有归宿。亡灵们的骷髅梗真是个百试不爽的笑点宝库阿。
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1276642957">
            
    
        <div class="avatar">
            <a title="Rilkelee" href="https://www.douban.com/people/rilkelee/">
                <img src="https://img3.doubanio.com/icon/u44617262-20.jpg" class="" />
            </a>
        </div>
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">484</span>
                <input value="1276642957" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/rilkelee/" class="">Rilkelee</a>
                    <span>看过</span>
                    <span class="allstar30 rating" title="还行"></span>
                <span class="comment-time " title="2017-11-26 02:28:17">
                    2017-11-26
                </span>
            </span>
        </h3>
        <p class=""> 漫天好评太夸张了吧。。。Pixar的叙事与价值观内核真是愈发俗套保守了，这还真是个全世界都要回归家庭本位的年代咩。。。
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1274196290">
            
    
        <div class="avatar">
            <a title="季霖" href="https://www.douban.com/people/joincaroline/">
                <img src="https://img3.doubanio.com/icon/u150204750-1.jpg" class="" />
            </a>
        </div>
    <div class="comment">
        <h3>
            
            <span class="comment-vote">
                <span class="votes">550</span>
                <input value="1274196290" type="hidden"/>
                <a href="javascript:;" class="j a_show_login">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/joincaroline/" class="">季霖</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2017-11-20 22:24:22">
                    2017-11-20
                </span>
            </span>
        </h3>
        <p class=""> 看着看着就哭了，哭了有至少三次。片头叙事的载体与手法很巧妙，时空流畅地穿梭于缤纷色彩中。配乐动听，Dolby带来演唱会般的体验。纯真美好的梦想无比激昂，安稳温暖的亲情格外芬芳。我们都会离开这个世界，可是，有了一片金色花瓣的祝福，我们不会孤单。想唱就唱，唱得响亮；想哭就哭，泪过启航
        </p>
    </div>

        </div>




    <div class="comments-footer-tips">
        * 影片上映之前的、与影片无关的或包含人身攻击等内容的短评都将有可能被折叠，且评分不计入豆瓣评分。<br/>
        * 短评的排序是将豆瓣成员的投票加权平均计算后的结果，通过算法的调校，更好地反映短评内容的价值。<br/>
    </div>


        <div id="paginator" class="center">
                <span class="first"><< 首页</span>
                <span class="prev">< 前页</span>
                <a href="?start=20&amp;limit=20&amp;sort=new_score&amp;status=P&amp;percent_type=" data-page="" class="next">后页 ></a>
        </div>





        
        
    </div>

            </div>
            <div class="aside">
                

    
<p class="pl2">&gt; <a href="https://movie.douban.com/subject/20495023/">去 寻梦环游记 的页面</a></p>

    <div class="indent">
        









<div class="movie-summary">
        <div class="movie-pic"><a  href="https://movie.douban.com/subject/20495023/" ><img alt="寻梦环游记 Coco" title="寻梦环游记 Coco" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2503997609.webp" rel="v:image" width="100px"></a></div>
    <span class="attrs">
        
            
        <p>
            <span class="pl">导演:</span>
                <a  href="https://movie.douban.com/celebrity/1022678/">李·昂克里奇</a> / <a  href="https://movie.douban.com/celebrity/1370425/">阿德里安·莫利纳</a>
        </p>

        
            
        <p>
            <span class="pl">主演:</span>
                <a  href="https://movie.douban.com/celebrity/1370411/">安东尼·冈萨雷斯</a> / <a  href="https://movie.douban.com/celebrity/1041009/">盖尔·加西亚·贝纳尔</a> / <a  href="https://movie.douban.com/celebrity/1036383/">本杰明·布拉特</a> / <a  href="https://movie.douban.com/celebrity/1056068/">阿兰纳·乌巴奇</a> / <a  href="https://movie.douban.com/celebrity/1329603/">芮妮·维克托</a> / <a  href="https://movie.douban.com/celebrity/1077191/">杰米·卡米尔</a> / <a  href="https://movie.douban.com/celebrity/1014115/">阿方索·阿雷奥</a> / <a  href="https://movie.douban.com/celebrity/1383503/">赫伯特·西古恩萨</a> / <a  href="https://movie.douban.com/celebrity/1009632/">加布里埃尔·伊格莱西亚斯</a> / <a  href="https://movie.douban.com/celebrity/1077918/">隆巴多·博伊尔</a> / <a  href="https://movie.douban.com/celebrity/1133060/">安娜·奥菲丽亚·莫吉亚</a> / <a  href="https://movie.douban.com/celebrity/1263061/">娜塔丽·科尔多瓦</a> / <a  href="https://movie.douban.com/celebrity/1122108/">赛琳娜·露娜</a> / <a  href="https://movie.douban.com/celebrity/1031917/">爱德华·詹姆斯·奥莫斯</a> / <a  href="https://movie.douban.com/celebrity/1309727/">索菲亚·伊斯皮诺萨</a> / <a  href="https://movie.douban.com/celebrity/1384451/">卡拉·梅迪纳</a> / <a  href="https://movie.douban.com/celebrity/1134178/">黛娅娜·欧特里</a> / <a  href="https://movie.douban.com/celebrity/1009958/">路易斯·瓦尔德斯</a> / <a  href="https://movie.douban.com/celebrity/1383505/">布兰卡·阿拉切利</a> / <a  href="https://movie.douban.com/celebrity/1384452/">萨尔瓦多·雷耶斯</a> / <a  href="https://movie.douban.com/celebrity/1010603/">切奇·马林</a> / <a  href="https://movie.douban.com/celebrity/1383504/">奥克塔维·索利斯</a> / <a  href="https://movie.douban.com/celebrity/1002680/">约翰·拉岑贝格</a>
        </p>

        
            
        <p>
            <span class="pl">类型:</span>
                喜剧, 动画, 冒险, 音乐, 家庭
        </p>

        
            
        <p>
            <span class="pl">地区:</span>
                美国
        </p>

        
            
        <p>
            <span class="pl">片长:</span>
                105分钟
        </p>

        
            
        <p>
            <span class="pl">上映:</span>
                2017-10-20(莫雷利亚电影节), 2017-11-22(美国), 2017-11-24(中国大陆)
        </p>

        <a  class="trail_link" data-trailer-id="223639" href="https://movie.douban.com/trailer/223639/#content" >预告片</a>
    </span>
</div>



    </div>
    <div id="dale_movie_subject_comments_bottom_right"></div>

            </div>
            <div class="extra">
                
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
    <script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/436c5b1e44b70215.js"></script>
        
        
    <link rel="stylesheet" type="text/css" href="https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css" />
    <link rel="stylesheet" type="text/css" href="https://img3.doubanio.com/f/movie/1d829b8605b9e81435b127cbf3d16563aaa51838/css/movie/mod/reg_login_pop.css" />
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/77323ae72a612bba8b65f845491513ff3329b1bb/js/do.js" data-cfg-autoload="false"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/4ea3216519a6183c7bcd4f7d1a6d4fd57ce1a244/js/ui/dialog.js"></script>
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
            browserId = 'y1ihsym9qH0',
            criteria = '3:/subject/20495023/comments?start=0&amp;limit=20&amp;sort=new_score&amp;status=P&amp;percent_type=',
            preview = '',
            debug = false,
            adSlots = ['dale_movie_subject_comments_bottom_right'];

        global.DoubanAdRequest = {src: adSource, uid: userId, bid: browserId, crtr: criteria, prv: preview, debug: debug};
        global.DoubanAdSlots = (global.DoubanAdSlots || []).concat(adSlots);

        newNode.setAttribute('type', 'text/javascript');
        newNode.setAttribute('src', 'https://img3.doubanio.com/f/adjs/5a274edd066a1fca36439233b6aa5f8ebce75685/ad.release.js');
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
pattern=re.compile('<div class="comment-item".*?>.*?<div class="comment">.*?<p class="">(.*?)</p>',re.S)
comment=re.findall(pattern,q)
# print(comment)
for row in comment:
    print(row)