"""
1. Client prepares HTTP Reqeust.

2. Send HTTP Request (From Client).

3. Server receives the request and looks for the data in the database.

4. Server sends the response back.

5. Client Receives and processes the response. 

Client              Server      Database


>>> import requests
>>> import requests
>>> r = requests.get("https://www.google.com")
>>> # get and post methods
>>> r. status_code
200
>>> #http status codes are 200 for OK, 403 for forbidden improper authentical or missing API key, 404 status code for not found
>>> r.headers
{'Date': 'Mon, 06 Apr 2020 02:45:27 GMT', 'Expires': '-1', 'Cache-Control': 'private, max-age=0', 'Content-Type': 'text/html; charset=ISO-8859-1', 'P3P': 'CP="This is not a P3P policy! See g.co/p3phelp for more info."', 'Content-Encoding': 'gzip', 'Server': 'gws', 'X-XSS-Protection': '0', 'X-Frame-Options': 'SAMEORIGIN', 'Set-Cookie': '1P_JAR=2020-04-06-02; expires=Wed, 06-May-2020 02:45:27 GMT; path=/; domain=.google.com; Secure, NID=201=LHhJ9YqRBCudrTlZ5aXJF2x3ieCzbHiSjg8R21nN6hokz7TGo54bwCPdwevk5Ic-HmbilDwx-1GFJ5FRI2kzpky14SRA_RpdGII8yc0KprPv0HaW9jfkoqVHDx4UCjIuqkMGQZlded15TO6pRYWtLQTE8LwrByC_gQ3XrpLBms0; expires=Tue, 06-Oct-2020 02:45:27 GMT; path=/; domain=.google.com; HttpOnly', 'Alt-Svc': 'quic=":443"; ma=2592000; v="46,43",h3-Q050=":443"; ma=2592000,h3-Q049=":443"; ma=2592000,h3-Q048=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,h3-T050=":443"; ma=2592000', 'Transfer-Encoding': 'chunked'}
>>> r.headers["Date"]
'Mon, 06 Apr 2020 02:45:27 GMT'
>>> r.text
'<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en-SG"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="XYq8pKhiTrVRZCmaBcZPlA==">(function(){window.google={kEI:\'x5eKXuWcLIuR9QOvroaICA\',kEXPI:\'0,202123,3,1151621,5662,731,223,3657,1447,207,3204,10,1051,175,364,542,893,4,60,817,383,246,5,623,337,50,9,60,274,554,115,105,40,103,5,116,175,116,5,79,419611,706743,1197715,309,125,329118,1294,12383,4855,32691,15248,867,28684,364,8824,8384,1325,3534,1361,283,9007,3029,4739,3118,4882,3033,1808,4020,978,7931,5297,2054,920,873,1217,2975,6430,7432,1571,2303,2883,21,317,3173,1344,1399,1379,520,399,2278,7,2796,887,706,1167,112,2212,202,328,149,1430,513,519,1140,277,55,48,820,3438,312,1136,3,2063,606,1839,184,1777,143,377,1947,244,503,1482,93,328,1284,16,2927,2247,473,1340,28,719,1039,603,1666,1,957,773,2072,7,817,4782,469,1565,6513,2663,641,2450,1114,1344,1226,1462,3934,1275,108,1714,1693,908,2,1473,2082,2132,261,4,12,5407,225,996,828,842,480,606,1349,3,346,200,30,157,813,183,562,120,373,1639,1906,356,84,266,149,189,3312,503,1,1538,8,439,28,130,1,70,247,914,589,273,121,1870,415,192,1345,1221,569,4,1118,410,17,126,178,314,4,20,43,239,353,1010,154,180,125,358,141,68,166,22,22,271,562,28,284,111,252,6,16,2,18,42,63,438,90,537,5,289,10,113,273,245,723,4,287,498,338,380,124,143,737,132,354,88,131,137,57,592,218,5830637,3277,1802617,6996022,549,333,444,1,2,80,1,900,896,1,8,1,2,2551,1,748,141,59,736,563,1,4265,1,1,1,1,137,1,1193,722,450,217,12,3,3,1,1,2,3,1,1,1,1,1,1,1,13,2,2,2,1,1,1,2,11,4,1,1,1,5,3,2,3,7,2,1,1,1,1,4,1,4,1,5,1,3,23962896,23,2641826\',kBL:\'-KLY\'};google.sn=\'webhp\';google.kHL=\'en-SG\';})();(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var c;a&&(!a.getAttribute||!(c=a.getAttribute("eid")));)a=a.parentNode;return c||google.kEI};google.getLEI=function(a){for(var c=null;a&&(!a.getAttribute||!(c=a.getAttribute("leid")));)a=a.parentNode;return c};google.ml=function(){return null};google.time=function(){return Date.now()};google.log=function(a,c,b,d,g){if(b=google.logUrl(a,c,b,d,g)){a=new Image;var e=google.lc,f=google.li;e[f]=a;a.onerror=a.onload=a.onabort=function(){delete e[f]};google.vel&&google.vel.lu&&google.vel.lu(b);a.src=b;google.li=f+1}};google.logUrl=function(a,c,b,d,g){var e="",f=google.ls||"";b||-1!=c.search("&ei=")||(e="&ei="+google.getEI(d),-1==c.search("&lei=")&&(d=google.getLEI(d))&&(e+="&lei="+d));d="";!b&&google.cshid&&-1==c.search("&cshid=")&&"slh"!=a&&(d="&cshid="+google.cshid);b=b||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+c+e+f+"&zx="+google.time()+d;/^http:/i.test(b)&&"https:"==window.location.protocol&&(google.ml(Error("a"),!1,{src:b,glmm:1}),b="");return b};}).call(this);(function(){google.y={};google.x=function(a,b){if(a)var c=a.id;else{do c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1};google.lm=[];google.plm=function(a){google.lm.push.apply(google.lm,a)};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};}).call(this);google.f={};(function(){\ndocument.documentElement.addEventListener("submit",function(b){var a;if(a=b.target){var c=a.getAttribute("data-submitfalse");a="1"==c||"q"==c&&!a.elements.q.value?!0:!1}else a=!1;a&&(b.preventDefault(),b.stopPropagation())},!0);document.documentElement.addEventListener("click",function(b){var a;a:{for(a=b.target;a&&a!=document.documentElement;a=a.parentElement)if("A"==a.tagName){a="1"==a.getAttribute("data-nohref");break a}a=!1}a&&b.preventDefault()},!0);}).call(this);\nvar a=window.location,b=a.href.indexOf("#");if(0<=b){var c=a.href.substring(b+1);/(^|&)q=/.test(c)&&-1==c.indexOf("#")&&a.replace("/search?"+c.replace(/(^|&)fp=[^&]*/g,"")+"&cad=h")};</script><style>#gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}.gbh{height:0;position:absolute;top:24px;width:100%}@media all{.gb1{height:22px;margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb4{color:#00c !important}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important}\n</style><style>body,td,a,p,.h{font-family:arial,sans-serif}body{margin:0;overflow-y:scroll}#gog{padding:3px 8px 0}td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#36c}.q{color:#00c}.ts td{padding:0}.ts{border-collapse:collapse}em{font-weight:bold;font-style:normal}.lst{height:25px;width:496px}.gsfi,.lst{font:18px arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;margin:3px 0 4px;margin-left:4px}input{font-family:inherit}body{background:#fff;color:#000}a{color:#11c;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl a{color:#36c}a:visited{color:#551a8b}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-left:13px;font-size:11px}.lsbb{background:#eee;border:solid 1px;border-color:#ccc #999 #999 #ccc;height:30px}.lsbb{display:block}.ftl,#fll a{display:inline-block;margin:0 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px repeat-x;border:none;color:#000;cursor:pointer;height:30px;margin:0;outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#ccc}.lst:focus{outline:none}</style><script nonce="XYq8pKhiTrVRZCmaBcZPlA=="></script></head><body bgcolor="#fff"><script nonce="XYq8pKhiTrVRZCmaBcZPlA==">(function(){var src=\'/images/nav_logo229.png\';var iesg=false;document.body.onload = function(){window.n && window.n();if (document.images){new Image().src=src;}\nif (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();}\n}\n})();</script><div id="mngb"> <div id=gbar><nobr><b class=gb1>Search</b> <a class=gb1 href="https://www.google.com.sg/imghp?hl=en&tab=wi">Images</a> <a class=gb1 href="https://maps.google.com.sg/maps?hl=en&tab=wl">Maps</a> <a class=gb1 href="https://play.google.com/?hl=en&tab=w8">Play</a> <a class=gb1 href="https://www.youtube.com/?gl=SG&tab=w1">YouTube</a> <a class=gb1 href="https://news.google.com.sg/nwshp?hl=en&tab=wn">News</a> <a class=gb1 href="https://mail.google.com/mail/?tab=wm">Gmail</a> <a class=gb1 href="https://drive.google.com/?tab=wo">Drive</a> <a class=gb1 style="text-decoration:none" href="https://www.google.com.sg/intl/en/about/products?tab=wh"><u>More</u> &raquo;</a></nobr></div><div id=guser width=100%><nobr><span id=gbn class=gbi></span><span id=gbf class=gbf></span><span id=gbe></span><a href="http://www.google.com.sg/history/optout?hl=en" class=gb4>Web History</a> | <a  href="/preferences?hl=en" class=gb4>Settings</a> | <a target=_top id=gb_70 href="https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/" class=gb4>Sign in</a></nobr></div><div class=gbh style=left:0></div><div class=gbh style=right:0></div> </div><center><br clear="all" id="lgpd"><div id="lga"><img alt="Google" height="92" src="/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png" style="padding:28px 0 14px" width="272" id="hplogo"><br><br></div><form action="/search" name="f"><table cellpadding="0" cellspacing="0"><tr valign="top"><td width="25%">&nbsp;</td><td align="center" nowrap=""><input name="ie" value="ISO-8859-1" type="hidden"><input value="en-SG" name="hl" type="hidden"><input name="source" type="hidden" value="hp"><input name="biw" type="hidden"><input name="bih" type="hidden"><div class="ds" style="height:32px;margin:4px 0"><input class="lst" style="margin:0;padding:5px 8px 0 6px;vertical-align:top;color:#000" autocomplete="off" value="" title="Google Search" maxlength="2048" name="q" size="57"></div><br style="line-height:0"><span class="ds"><span class="lsbb"><input class="lsb" value="Google Search" name="btnG" type="submit"></span></span><span class="ds"><span class="lsbb"><input class="lsb" id="tsuid1" value="I\'m Feeling Lucky" name="btnI" type="submit"><script nonce="XYq8pKhiTrVRZCmaBcZPlA==">(function(){var id=\'tsuid1\';document.getElementById(id).onclick = function(){if (this.form.q.value){this.checked = 1;if (this.form.iflsig)this.form.iflsig.disabled = false;}\nelse top.location=\'/doodles/\';};})();</script><input value="AINFCbYAAAAAXoql1ySuIzOIzpcplFGsPJxPSUw7t4B8" name="iflsig" type="hidden"></span></span></td><td class="fl sblc" align="left" nowrap="" width="25%"><a href="/advanced_search?hl=en-SG&amp;authuser=0">Advanced search</a></td></tr></table><input id="gbv" name="gbv" type="hidden" value="1"><script nonce="XYq8pKhiTrVRZCmaBcZPlA==">(function(){var a,b="1";if(document&&document.getElementById)if("undefined"!=typeof XMLHttpRequest)b="2";else if("undefined"!=typeof ActiveXObject){var c,d,e=["MSXML2.XMLHTTP.6.0","MSXML2.XMLHTTP.3.0","MSXML2.XMLHTTP","Microsoft.XMLHTTP"];for(c=0;d=e[c++];)try{new ActiveXObject(d),b="2"}catch(h){}}a=b;if("2"==a&&-1==location.search.indexOf("&gbv=2")){var f=google.gbvu,g=document.getElementById("gbv");g&&(g.value=a);f&&window.setTimeout(function(){location.href=f},0)};}).call(this);</script></form><div id="gac_scont"></div><div style="font-size:83%;min-height:3.5em"><br><div id="gws-output-pages-elements-homepage_additional_languages__als"><style>#gws-output-pages-elements-homepage_additional_languages__als{font-size:small;margin-bottom:24px}#SIvCob{display:inline-block;line-height:28px;}#SIvCob a{padding:0 3px;}.H6sW5{display:inline-block;margin:0 2px;white-space:nowrap}.z4hgWe{display:inline-block;margin:0 2px}</style><div id="SIvCob">Google offered in:  <a href="https://www.google.com/setprefs?sig=0_7xeVsIc0qU0Yq2U8kRIIhtanfV8%3D&amp;hl=zh-CN&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwilnO2T5NLoAhWLSH0KHS-XAYEQ2ZgBCAU">&#20013;&#25991;(&#31616;&#20307;)</a>    <a href="https://www.google.com/setprefs?sig=0_7xeVsIc0qU0Yq2U8kRIIhtanfV8%3D&amp;hl=ms&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwilnO2T5NLoAhWLSH0KHS-XAYEQ2ZgBCAY">Melayu</a>    <a href="https://www.google.com/setprefs?sig=0_7xeVsIc0qU0Yq2U8kRIIhtanfV8%3D&amp;hl=ta&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwilnO2T5NLoAhWLSH0KHS-XAYEQ2ZgBCAc">&#2980;&#2990;&#3007;&#2996;&#3021;</a>  </div></div></div><span id="footer"><div style="font-size:10pt"><div style="margin:19px auto;text-align:center" id="fll"><a href="/intl/en/ads/">Advertising\xa0Programs</a><a href="http://www.google.com.sg/intl/en/services/">Business Solutions</a><a href="/intl/en/about.html">About Google</a><a href="https://www.google.com/setprefdomain?prefdom=SG&amp;prev=https://www.google.com.sg/&amp;sig=K_BnX9x-tO2GX_AstrILeJcc9n7to%3D">Google.com.sg</a></div></div><p style="font-size:8pt;color:#767676">&copy; 2020 - <a href="/intl/en/policies/privacy/">Privacy</a> - <a href="/intl/en/policies/terms/">Terms</a></p></span></center><script nonce="XYq8pKhiTrVRZCmaBcZPlA==">(function(){window.google.cdo={height:0,width:0};(function(){var a=window.innerWidth,b=window.innerHeight;if(!a||!b){var c=window.document,d="CSS1Compat"==c.compatMode?c.documentElement:c.body;a=d.clientWidth;b=d.clientHeight}a&&b&&(a!=google.cdo.width||b!=google.cdo.height)&&google.log("","","/client_204?&atyp=i&biw="+a+"&bih="+b+"&ei="+google.kEI);}).call(this);})();(function(){var u=\'/xjs/_/js/k\\x3dxjs.hp.en.Z9GXM1WQNCo.O/m\\x3dsb_he,d/am\\x3dAAMCbAQ/d\\x3d1/rs\\x3dACT90oHzsANym_O9pyPQsJs2gvPdWWoEsQ\';\nsetTimeout(function(){var b=document;var a="SCRIPT";"application/xhtml+xml"===b.contentType&&(a=a.toLowerCase());a=b.createElement(a);a.src=u;google.timers&&google.timers.load&&google.tick&&google.tick("load","xjsls");document.body.appendChild(a)},0);})();(function(){window.google.xjsu=\'/xjs/_/js/k\\x3dxjs.hp.en.Z9GXM1WQNCo.O/m\\x3dsb_he,d/am\\x3dAAMCbAQ/d\\x3d1/rs\\x3dACT90oHzsANym_O9pyPQsJs2gvPdWWoEsQ\';})();function _DumpException(e){throw e;}\nfunction _F_installCss(c){}\n(function(){google.spjs=false;google.snet=true;google.em=[];google.emw=false;google.pdt=0;})();(function(){var pmc=\'{\\x22d\\x22:{},\\x22sb_he\\x22:{\\x22agen\\x22:true,\\x22cgen\\x22:true,\\x22client\\x22:\\x22heirloom-hp\\x22,\\x22dh\\x22:true,\\x22dhqt\\x22:true,\\x22ds\\x22:\\x22\\x22,\\x22ffql\\x22:\\x22en\\x22,\\x22fl\\x22:true,\\x22host\\x22:\\x22google.com\\x22,\\x22isbh\\x22:28,\\x22jsonp\\x22:true,\\x22msgs\\x22:{\\x22cibl\\x22:\\x22Clear Search\\x22,\\x22dym\\x22:\\x22Did you mean:\\x22,\\x22lcky\\x22:\\x22I\\\\u0026#39;m Feeling Lucky\\x22,\\x22lml\\x22:\\x22Learn more\\x22,\\x22oskt\\x22:\\x22Input tools\\x22,\\x22psrc\\x22:\\x22This search was removed from your \\\\u003Ca href\\x3d\\\\\\x22/history\\\\\\x22\\\\u003EWeb History\\\\u003C/a\\\\u003E\\x22,\\x22psrl\\x22:\\x22Remove\\x22,\\x22sbit\\x22:\\x22Search by image\\x22,\\x22srch\\x22:\\x22Google Search\\x22},\\x22ovr\\x22:{},\\x22pq\\x22:\\x22\\x22,\\x22refpd\\x22:true,\\x22rfs\\x22:[],\\x22sbpl\\x22:16,\\x22sbpr\\x22:16,\\x22scd\\x22:10,\\x22stok\\x22:\\x220Aan1xZVYDimQ21bUaFx9n2lMNk\\x22,\\x22uhde\\x22:false}}\';google.pmc=JSON.parse(pmc);})();</script>        </body></html>'

"""
"""

Example of Javascript Object Notation

{
response_code: 0,
results: [
{
category: "Entertainment: Music",
type: "multiple",
difficulty: "easy",
question: "Whose albums included &quot;Back in Black&quot; and &quot;Ballbreaker&quot;?",
correct_answer: "AC/DC",
incorrect_answers: [
"Iron Maiden",
"Black Sabbath",
"Metallica"
]
}
]
}

Javascript Object is the same as the Python Dictionary
It could also be a list, but usually dictionary like Object

https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple



#search Twitter APIs or even for Facebook.. useful for developers
#quiz API to get questions
import requests
r = requests.get("https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple")
r.status_code

r.text

type(r.text)

import json

question = json.loads(r.text)
question #converted to dictionary

type(question)

import pprint
pprint.pprint(question)

#Below is solution for pprint
{'response_code': 0,
 'results': [{'category': 'Entertainment: Music',
              'correct_answer': 'Robbie Williams',
              'difficulty': 'easy',
              'incorrect_answers': ['Justin Timberlake',
                                    'Harry Styles',
                                    'Gary Barlow'],
              'question': 'Which former boy-band star released hit solo single '
                          '&quot;Angels&quot; in 1997?',
              'type': 'multiple'}]}

question


question['results'][0]['incorrect_answers']


person={'Name': 'John', 'Age': 30}
person_json = json.dumps(person)
person_json

type(person_json)

#dictionary converted to string
"""