<!DOCTYPE html>


<html>
  <head>
    <meta charset="utf-8"><script type="text/javascript">(window.NREUM||(NREUM={})).init={ajax:{deny_list:["bam-cell.nr-data.net"]}};(window.NREUM||(NREUM={})).loader_config={xpid:"UAQDVFVRGwEAXVlbBAg=",licenseKey:"8d5fb92f6e",applicationID:"2098939"};window.NREUM||(NREUM={}),__nr_require=function(t,e,n){function r(n){if(!e[n]){var i=e[n]={exports:{}};t[n][0].call(i.exports,function(e){var i=t[n][1][e];return r(i||e)},i,i.exports)}return e[n].exports}if("function"==typeof __nr_require)return __nr_require;for(var i=0;i<n.length;i++)r(n[i]);return r}({1:[function(t,e,n){function r(t){try{s.console&&console.log(t)}catch(e){}}var i,o=t("ee"),a=t(28),s={};try{i=localStorage.getItem("__nr_flags").split(","),console&&"function"==typeof console.log&&(s.console=!0,i.indexOf("dev")!==-1&&(s.dev=!0),i.indexOf("nr_dev")!==-1&&(s.nrDev=!0))}catch(c){}s.nrDev&&o.on("internal-error",function(t){r(t.stack)}),s.dev&&o.on("fn-err",function(t,e,n){r(n.stack)}),s.dev&&(r("NR AGENT IN DEVELOPMENT MODE"),r("flags: "+a(s,function(t,e){return t}).join(", ")))},{}],2:[function(t,e,n){function r(t,e,n,r,s){try{p?p-=1:i(s||new UncaughtException(t,e,n),!0)}catch(f){try{o("ierr",[f,c.now(),!0])}catch(d){}}return"function"==typeof u&&u.apply(this,a(arguments))}function UncaughtException(t,e,n){this.message=t||"Uncaught error with no additional information",this.sourceURL=e,this.line=n}function i(t,e){var n=e?null:c.now();o("err",[t,n])}var o=t("handle"),a=t(29),s=t("ee"),c=t("loader"),f=t("gos"),u=window.onerror,d=!1,l="nr@seenError";if(!c.disabled){var p=0;c.features.err=!0,t(1),window.onerror=r;try{throw new Error}catch(h){"stack"in h&&(t(10),t(9),"addEventListener"in window&&t(6),c.xhrWrappable&&t(11),d=!0)}s.on("fn-start",function(t,e,n){d&&(p+=1)}),s.on("fn-err",function(t,e,n){d&&!n[l]&&(f(n,l,function(){return!0}),this.thrown=!0,i(n))}),s.on("fn-end",function(){d&&!this.thrown&&p>0&&(p-=1)}),s.on("internal-error",function(t){o("ierr",[t,c.now(),!0])})}},{}],3:[function(t,e,n){var r=t("loader");r.disabled||(r.features.ins=!0)},{}],4:[function(t,e,n){function r(){var t=new PerformanceObserver(function(t,e){var n=t.getEntries();s(v,[n])});try{t.observe({entryTypes:["resource"]})}catch(e){}}function i(t){if(s(v,[window.performance.getEntriesByType(w)]),window.performance["c"+l])try{window.performance[h](m,i,!1)}catch(t){}else try{window.performance[h]("webkit"+m,i,!1)}catch(t){}}function o(t){}if(window.performance&&window.performance.timing&&window.performance.getEntriesByType){var a=t("ee"),s=t("handle"),c=t(10),f=t(9),u=t(5),d=t(19),l="learResourceTimings",p="addEventListener",h="removeEventListener",m="resourcetimingbufferfull",v="bstResource",w="resource",g="-start",y="-end",x="fn"+g,b="fn"+y,E="bstTimer",R="pushState",S=t("loader");if(!S.disabled){S.features.stn=!0,t(8),"addEventListener"in window&&t(6);var O=NREUM.o.EV;a.on(x,function(t,e){var n=t[0];n instanceof O&&(this.bstStart=S.now())}),a.on(b,function(t,e){var n=t[0];n instanceof O&&s("bst",[n,e,this.bstStart,S.now()])}),c.on(x,function(t,e,n){this.bstStart=S.now(),this.bstType=n}),c.on(b,function(t,e){s(E,[e,this.bstStart,S.now(),this.bstType])}),f.on(x,function(){this.bstStart=S.now()}),f.on(b,function(t,e){s(E,[e,this.bstStart,S.now(),"requestAnimationFrame"])}),a.on(R+g,function(t){this.time=S.now(),this.startPath=location.pathname+location.hash}),a.on(R+y,function(t){s("bstHist",[location.pathname+location.hash,this.startPath,this.time])}),u()?(s(v,[window.performance.getEntriesByType("resource")]),r()):p in window.performance&&(window.performance["c"+l]?window.performance[p](m,i,d(!1)):window.performance[p]("webkit"+m,i,d(!1))),document[p]("scroll",o,d(!1)),document[p]("keypress",o,d(!1)),document[p]("click",o,d(!1))}}},{}],5:[function(t,e,n){e.exports=function(){return"PerformanceObserver"in window&&"function"==typeof window.PerformanceObserver}},{}],6:[function(t,e,n){function r(t){for(var e=t;e&&!e.hasOwnProperty(u);)e=Object.getPrototypeOf(e);e&&i(e)}function i(t){s.inPlace(t,[u,d],"-",o)}function o(t,e){return t[1]}var a=t("ee").get("events"),s=t("wrap-function")(a,!0),c=t("gos"),f=XMLHttpRequest,u="addEventListener",d="removeEventListener";e.exports=a,"getPrototypeOf"in Object?(r(document),r(window),r(f.prototype)):f.prototype.hasOwnProperty(u)&&(i(window),i(f.prototype)),a.on(u+"-start",function(t,e){var n=t[1];if(null!==n&&("function"==typeof n||"object"==typeof n)){var r=c(n,"nr@wrapped",function(){function t(){if("function"==typeof n.handleEvent)return n.handleEvent.apply(n,arguments)}var e={object:t,"function":n}[typeof n];return e?s(e,"fn-",null,e.name||"anonymous"):n});this.wrapped=t[1]=r}}),a.on(d+"-start",function(t){t[1]=this.wrapped||t[1]})},{}],7:[function(t,e,n){function r(t,e,n){var r=t[e];"function"==typeof r&&(t[e]=function(){var t=o(arguments),e={};i.emit(n+"before-start",[t],e);var a;e[m]&&e[m].dt&&(a=e[m].dt);var s=r.apply(this,t);return i.emit(n+"start",[t,a],s),s.then(function(t){return i.emit(n+"end",[null,t],s),t},function(t){throw i.emit(n+"end",[t],s),t})})}var i=t("ee").get("fetch"),o=t(29),a=t(28);e.exports=i;var s=window,c="fetch-",f=c+"body-",u=["arrayBuffer","blob","json","text","formData"],d=s.Request,l=s.Response,p=s.fetch,h="prototype",m="nr@context";d&&l&&p&&(a(u,function(t,e){r(d[h],e,f),r(l[h],e,f)}),r(s,"fetch",c),i.on(c+"end",function(t,e){var n=this;if(e){var r=e.headers.get("content-length");null!==r&&(n.rxSize=r),i.emit(c+"done",[null,e],n)}else i.emit(c+"done",[t],n)}))},{}],8:[function(t,e,n){var r=t("ee").get("history"),i=t("wrap-function")(r);e.exports=r;var o=window.history&&window.history.constructor&&window.history.constructor.prototype,a=window.history;o&&o.pushState&&o.replaceState&&(a=o),i.inPlace(a,["pushState","replaceState"],"-")},{}],9:[function(t,e,n){var r=t("ee").get("raf"),i=t("wrap-function")(r),o="equestAnimationFrame";e.exports=r,i.inPlace(window,["r"+o,"mozR"+o,"webkitR"+o,"msR"+o],"raf-"),r.on("raf-start",function(t){t[0]=i(t[0],"fn-")})},{}],10:[function(t,e,n){function r(t,e,n){t[0]=a(t[0],"fn-",null,n)}function i(t,e,n){this.method=n,this.timerDuration=isNaN(t[1])?0:+t[1],t[0]=a(t[0],"fn-",this,n)}var o=t("ee").get("timer"),a=t("wrap-function")(o),s="setTimeout",c="setInterval",f="clearTimeout",u="-start",d="-";e.exports=o,a.inPlace(window,[s,"setImmediate"],s+d),a.inPlace(window,[c],c+d),a.inPlace(window,[f,"clearImmediate"],f+d),o.on(c+u,r),o.on(s+u,i)},{}],11:[function(t,e,n){function r(t,e){d.inPlace(e,["onreadystatechange"],"fn-",s)}function i(){var t=this,e=u.context(t);t.readyState>3&&!e.resolved&&(e.resolved=!0,u.emit("xhr-resolved",[],t)),d.inPlace(t,y,"fn-",s)}function o(t){x.push(t),m&&(E?E.then(a):w?w(a):(R=-R,S.data=R))}function a(){for(var t=0;t<x.length;t++)r([],x[t]);x.length&&(x=[])}function s(t,e){return e}function c(t,e){for(var n in t)e[n]=t[n];return e}t(6);var f=t("ee"),u=f.get("xhr"),d=t("wrap-function")(u),l=t(19),p=NREUM.o,h=p.XHR,m=p.MO,v=p.PR,w=p.SI,g="readystatechange",y=["onload","onerror","onabort","onloadstart","onloadend","onprogress","ontimeout"],x=[];e.exports=u;var b=window.XMLHttpRequest=function(t){var e=new h(t);try{u.emit("new-xhr",[e],e),e.addEventListener(g,i,l(!1))}catch(n){try{u.emit("internal-error",[n])}catch(r){}}return e};if(c(h,b),b.prototype=h.prototype,d.inPlace(b.prototype,["open","send"],"-xhr-",s),u.on("send-xhr-start",function(t,e){r(t,e),o(e)}),u.on("open-xhr-start",r),m){var E=v&&v.resolve();if(!w&&!v){var R=1,S=document.createTextNode(R);new m(a).observe(S,{characterData:!0})}}else f.on("fn-end",function(t){t[0]&&t[0].type===g||a()})},{}],12:[function(t,e,n){function r(t){if(!s(t))return null;var e=window.NREUM;if(!e.loader_config)return null;var n=(e.loader_config.accountID||"").toString()||null,r=(e.loader_config.agentID||"").toString()||null,f=(e.loader_config.trustKey||"").toString()||null;if(!n||!r)return null;var h=p.generateSpanId(),m=p.generateTraceId(),v=Date.now(),w={spanId:h,traceId:m,timestamp:v};return(t.sameOrigin||c(t)&&l())&&(w.traceContextParentHeader=i(h,m),w.traceContextStateHeader=o(h,v,n,r,f)),(t.sameOrigin&&!u()||!t.sameOrigin&&c(t)&&d())&&(w.newrelicHeader=a(h,m,v,n,r,f)),w}function i(t,e){return"00-"+e+"-"+t+"-01"}function o(t,e,n,r,i){var o=0,a="",s=1,c="",f="";return i+"@nr="+o+"-"+s+"-"+n+"-"+r+"-"+t+"-"+a+"-"+c+"-"+f+"-"+e}function a(t,e,n,r,i,o){var a="btoa"in window&&"function"==typeof window.btoa;if(!a)return null;var s={v:[0,1],d:{ty:"Browser",ac:r,ap:i,id:t,tr:e,ti:n}};return o&&r!==o&&(s.d.tk=o),btoa(JSON.stringify(s))}function s(t){return f()&&c(t)}function c(t){var e=!1,n={};if("init"in NREUM&&"distributed_tracing"in NREUM.init&&(n=NREUM.init.distributed_tracing),t.sameOrigin)e=!0;else if(n.allowed_origins instanceof Array)for(var r=0;r<n.allowed_origins.length;r++){var i=h(n.allowed_origins[r]);if(t.hostname===i.hostname&&t.protocol===i.protocol&&t.port===i.port){e=!0;break}}return e}function f(){return"init"in NREUM&&"distributed_tracing"in NREUM.init&&!!NREUM.init.distributed_tracing.enabled}function u(){return"init"in NREUM&&"distributed_tracing"in NREUM.init&&!!NREUM.init.distributed_tracing.exclude_newrelic_header}function d(){return"init"in NREUM&&"distributed_tracing"in NREUM.init&&NREUM.init.distributed_tracing.cors_use_newrelic_header!==!1}function l(){return"init"in NREUM&&"distributed_tracing"in NREUM.init&&!!NREUM.init.distributed_tracing.cors_use_tracecontext_headers}var p=t(25),h=t(14);e.exports={generateTracePayload:r,shouldGenerateTrace:s}},{}],13:[function(t,e,n){function r(t){var e=this.params,n=this.metrics;if(!this.ended){this.ended=!0;for(var r=0;r<l;r++)t.removeEventListener(d[r],this.listener,!1);return e.protocol&&"data"===e.protocol?void g("Ajax/DataUrl/Excluded"):void(e.aborted||(n.duration=a.now()-this.startTime,this.loadCaptureCalled||4!==t.readyState?null==e.status&&(e.status=0):o(this,t),n.cbTime=this.cbTime,s("xhr",[e,n,this.startTime,this.endTime,"xhr"],this)))}}function i(t,e){var n=c(e),r=t.params;r.hostname=n.hostname,r.port=n.port,r.protocol=n.protocol,r.host=n.hostname+":"+n.port,r.pathname=n.pathname,t.parsedOrigin=n,t.sameOrigin=n.sameOrigin}function o(t,e){t.params.status=e.status;var n=v(e,t.lastSize);if(n&&(t.metrics.rxSize=n),t.sameOrigin){var r=e.getResponseHeader("X-NewRelic-App-Data");r&&(t.params.cat=r.split(", ").pop())}t.loadCaptureCalled=!0}var a=t("loader");if(a.xhrWrappable&&!a.disabled){var s=t("handle"),c=t(14),f=t(12).generateTracePayload,u=t("ee"),d=["load","error","abort","timeout"],l=d.length,p=t("id"),h=t(20),m=t(18),v=t(15),w=t(19),g=t(21).recordSupportability,y=NREUM.o.REQ,x=window.XMLHttpRequest;a.features.xhr=!0,t(11),t(7),u.on("new-xhr",function(t){var e=this;e.totalCbs=0,e.called=0,e.cbTime=0,e.end=r,e.ended=!1,e.xhrGuids={},e.lastSize=null,e.loadCaptureCalled=!1,e.params=this.params||{},e.metrics=this.metrics||{},t.addEventListener("load",function(n){o(e,t)},w(!1)),h&&(h>34||h<10)||t.addEventListener("progress",function(t){e.lastSize=t.loaded},w(!1))}),u.on("open-xhr-start",function(t){this.params={method:t[0]},i(this,t[1]),this.metrics={}}),u.on("open-xhr-end",function(t,e){"loader_config"in NREUM&&"xpid"in NREUM.loader_config&&this.sameOrigin&&e.setRequestHeader("X-NewRelic-ID",NREUM.loader_config.xpid);var n=f(this.parsedOrigin);if(n){var r=!1;n.newrelicHeader&&(e.setRequestHeader("newrelic",n.newrelicHeader),r=!0),n.traceContextParentHeader&&(e.setRequestHeader("traceparent",n.traceContextParentHeader),n.traceContextStateHeader&&e.setRequestHeader("tracestate",n.traceContextStateHeader),r=!0),r&&(this.dt=n)}}),u.on("send-xhr-start",function(t,e){var n=this.metrics,r=t[0],i=this;if(n&&r){var o=m(r);o&&(n.txSize=o)}this.startTime=a.now(),this.listener=function(t){try{"abort"!==t.type||i.loadCaptureCalled||(i.params.aborted=!0),("load"!==t.type||i.called===i.totalCbs&&(i.onloadCalled||"function"!=typeof e.onload))&&i.end(e)}catch(n){try{u.emit("internal-error",[n])}catch(r){}}};for(var s=0;s<l;s++)e.addEventListener(d[s],this.listener,w(!1))}),u.on("xhr-cb-time",function(t,e,n){this.cbTime+=t,e?this.onloadCalled=!0:this.called+=1,this.called!==this.totalCbs||!this.onloadCalled&&"function"==typeof n.onload||this.end(n)}),u.on("xhr-load-added",function(t,e){var n=""+p(t)+!!e;this.xhrGuids&&!this.xhrGuids[n]&&(this.xhrGuids[n]=!0,this.totalCbs+=1)}),u.on("xhr-load-removed",function(t,e){var n=""+p(t)+!!e;this.xhrGuids&&this.xhrGuids[n]&&(delete this.xhrGuids[n],this.totalCbs-=1)}),u.on("xhr-resolved",function(){this.endTime=a.now()}),u.on("addEventListener-end",function(t,e){e instanceof x&&"load"===t[0]&&u.emit("xhr-load-added",[t[1],t[2]],e)}),u.on("removeEventListener-end",function(t,e){e instanceof x&&"load"===t[0]&&u.emit("xhr-load-removed",[t[1],t[2]],e)}),u.on("fn-start",function(t,e,n){e instanceof x&&("onload"===n&&(this.onload=!0),("load"===(t[0]&&t[0].type)||this.onload)&&(this.xhrCbStart=a.now()))}),u.on("fn-end",function(t,e){this.xhrCbStart&&u.emit("xhr-cb-time",[a.now()-this.xhrCbStart,this.onload,e],e)}),u.on("fetch-before-start",function(t){function e(t,e){var n=!1;return e.newrelicHeader&&(t.set("newrelic",e.newrelicHeader),n=!0),e.traceContextParentHeader&&(t.set("traceparent",e.traceContextParentHeader),e.traceContextStateHeader&&t.set("tracestate",e.traceContextStateHeader),n=!0),n}var n,r=t[1]||{};"string"==typeof t[0]?n=t[0]:t[0]&&t[0].url?n=t[0].url:window.URL&&t[0]&&t[0]instanceof URL&&(n=t[0].href),n&&(this.parsedOrigin=c(n),this.sameOrigin=this.parsedOrigin.sameOrigin);var i=f(this.parsedOrigin);if(i&&(i.newrelicHeader||i.traceContextParentHeader))if("string"==typeof t[0]||window.URL&&t[0]&&t[0]instanceof URL){var o={};for(var a in r)o[a]=r[a];o.headers=new Headers(r.headers||{}),e(o.headers,i)&&(this.dt=i),t.length>1?t[1]=o:t.push(o)}else t[0]&&t[0].headers&&e(t[0].headers,i)&&(this.dt=i)}),u.on("fetch-start",function(t,e){this.params={},this.metrics={},this.startTime=a.now(),this.dt=e,t.length>=1&&(this.target=t[0]),t.length>=2&&(this.opts=t[1]);var n,r=this.opts||{},o=this.target;if("string"==typeof o?n=o:"object"==typeof o&&o instanceof y?n=o.url:window.URL&&"object"==typeof o&&o instanceof URL&&(n=o.href),i(this,n),"data"!==this.params.protocol){var s=(""+(o&&o instanceof y&&o.method||r.method||"GET")).toUpperCase();this.params.method=s,this.txSize=m(r.body)||0}}),u.on("fetch-done",function(t,e){if(this.endTime=a.now(),this.params||(this.params={}),"data"===this.params.protocol)return void g("Ajax/DataUrl/Excluded");this.params.status=e?e.status:0;var n;"string"==typeof this.rxSize&&this.rxSize.length>0&&(n=+this.rxSize);var r={txSize:this.txSize,rxSize:n,duration:a.now()-this.startTime};s("xhr",[this.params,r,this.startTime,this.endTime,"fetch"],this)})}},{}],14:[function(t,e,n){var r={};e.exports=function(t){if(t in r)return r[t];if(0===(t||"").indexOf("data:"))return{protocol:"data"};var e=document.createElement("a"),n=window.location,i={};e.href=t,i.port=e.port;var o=e.href.split("://");!i.port&&o[1]&&(i.port=o[1].split("/")[0].split("@").pop().split(":")[1]),i.port&&"0"!==i.port||(i.port="https"===o[0]?"443":"80"),i.hostname=e.hostname||n.hostname,i.pathname=e.pathname,i.protocol=o[0],"/"!==i.pathname.charAt(0)&&(i.pathname="/"+i.pathname);var a=!e.protocol||":"===e.protocol||e.protocol===n.protocol,s=e.hostname===document.domain&&e.port===n.port;return i.sameOrigin=a&&(!e.hostname||s),"/"===i.pathname&&(r[t]=i),i}},{}],15:[function(t,e,n){function r(t,e){var n=t.responseType;return"json"===n&&null!==e?e:"arraybuffer"===n||"blob"===n||"json"===n?i(t.response):"text"===n||""===n||void 0===n?i(t.responseText):void 0}var i=t(18);e.exports=r},{}],16:[function(t,e,n){function r(){}function i(t,e,n,r){return function(){return u.recordSupportability("API/"+e+"/called"),o(t+e,[f.now()].concat(s(arguments)),n?null:this,r),n?void 0:this}}var o=t("handle"),a=t(28),s=t(29),c=t("ee").get("tracer"),f=t("loader"),u=t(21),d=NREUM;"undefined"==typeof window.newrelic&&(newrelic=d);var l=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],p="api-",h=p+"ixn-";a(l,function(t,e){d[e]=i(p,e,!0,"api")}),d.addPageAction=i(p,"addPageAction",!0),d.setCurrentRouteName=i(p,"routeName",!0),e.exports=newrelic,d.interaction=function(){return(new r).get()};var m=r.prototype={createTracer:function(t,e){var n={},r=this,i="function"==typeof e;return o(h+"tracer",[f.now(),t,n],r),function(){if(c.emit((i?"":"no-")+"fn-start",[f.now(),r,i],n),i)try{return e.apply(this,arguments)}catch(t){throw c.emit("fn-err",[arguments,this,t],n),t}finally{c.emit("fn-end",[f.now()],n)}}}};a("actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(t,e){m[e]=i(h,e)}),newrelic.noticeError=function(t,e){"string"==typeof t&&(t=new Error(t)),u.recordSupportability("API/noticeError/called"),o("err",[t,f.now(),!1,e])}},{}],17:[function(t,e,n){function r(t){if(NREUM.init){for(var e=NREUM.init,n=t.split("."),r=0;r<n.length-1;r++)if(e=e[n[r]],"object"!=typeof e)return;return e=e[n[n.length-1]]}}e.exports={getConfiguration:r}},{}],18:[function(t,e,n){e.exports=function(t){if("string"==typeof t&&t.length)return t.length;if("object"==typeof t){if("undefined"!=typeof ArrayBuffer&&t instanceof ArrayBuffer&&t.byteLength)return t.byteLength;if("undefined"!=typeof Blob&&t instanceof Blob&&t.size)return t.size;if(!("undefined"!=typeof FormData&&t instanceof FormData))try{return JSON.stringify(t).length}catch(e){return}}}},{}],19:[function(t,e,n){var r=!1;try{var i=Object.defineProperty({},"passive",{get:function(){r=!0}});window.addEventListener("testPassive",null,i),window.removeEventListener("testPassive",null,i)}catch(o){}e.exports=function(t){return r?{passive:!0,capture:!!t}:!!t}},{}],20:[function(t,e,n){var r=0,i=navigator.userAgent.match(/Firefox[\/\s](\d+\.\d+)/);i&&(r=+i[1]),e.exports=r},{}],21:[function(t,e,n){function r(t,e){var n=[a,t,{name:t},e];return o("storeMetric",n,null,"api"),n}function i(t,e){var n=[s,t,{name:t},e];return o("storeEventMetrics",n,null,"api"),n}var o=t("handle"),a="sm",s="cm";e.exports={constants:{SUPPORTABILITY_METRIC:a,CUSTOM_METRIC:s},recordSupportability:r,recordCustom:i}},{}],22:[function(t,e,n){function r(){return s.exists&&performance.now?Math.round(performance.now()):(o=Math.max((new Date).getTime(),o))-a}function i(){return o}var o=(new Date).getTime(),a=o,s=t(30);e.exports=r,e.exports.offset=a,e.exports.getLastTimestamp=i},{}],23:[function(t,e,n){function r(t){return!(!t||!t.protocol||"file:"===t.protocol)}e.exports=r},{}],24:[function(t,e,n){function r(t,e){var n=t.getEntries();n.forEach(function(t){"first-paint"===t.name?p("timing",["fp",Math.floor(t.startTime)]):"first-contentful-paint"===t.name&&p("timing",["fcp",Math.floor(t.startTime)])})}function i(t,e){var n=t.getEntries();if(n.length>0){var r=n[n.length-1];if(f&&f<r.startTime)return;var i=[r],o=a({});o&&i.push(o),p("lcp",i)}}function o(t){t.getEntries().forEach(function(t){t.hadRecentInput||p("cls",[t])})}function a(t){var e=navigator.connection||navigator.mozConnection||navigator.webkitConnection;if(e)return e.type&&(t["net-type"]=e.type),e.effectiveType&&(t["net-etype"]=e.effectiveType),e.rtt&&(t["net-rtt"]=e.rtt),e.downlink&&(t["net-dlink"]=e.downlink),t}function s(t){if(t instanceof w&&!y){var e=Math.round(t.timeStamp),n={type:t.type};a(n),e<=h.now()?n.fid=h.now()-e:e>h.offset&&e<=Date.now()?(e-=h.offset,n.fid=h.now()-e):e=h.now(),y=!0,p("timing",["fi",e,n])}}function c(t){"hidden"===t&&(f=h.now(),p("pageHide",[f]))}if(!("init"in NREUM&&"page_view_timing"in NREUM.init&&"enabled"in NREUM.init.page_view_timing&&NREUM.init.page_view_timing.enabled===!1)){var f,u,d,l,p=t("handle"),h=t("loader"),m=t(27),v=t(19),w=NREUM.o.EV;if("PerformanceObserver"in window&&"function"==typeof window.PerformanceObserver){u=new PerformanceObserver(r);try{u.observe({entryTypes:["paint"]})}catch(g){}d=new PerformanceObserver(i);try{d.observe({entryTypes:["largest-contentful-paint"]})}catch(g){}l=new PerformanceObserver(o);try{l.observe({type:"layout-shift",buffered:!0})}catch(g){}}if("addEventListener"in document){var y=!1,x=["click","keydown","mousedown","pointerdown","touchstart"];x.forEach(function(t){document.addEventListener(t,s,v(!1))})}m(c)}},{}],25:[function(t,e,n){function r(){function t(){return e?15&e[n++]:16*Math.random()|0}var e=null,n=0,r=window.crypto||window.msCrypto;r&&r.getRandomValues&&(e=r.getRandomValues(new Uint8Array(31)));for(var i,o="xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx",a="",s=0;s<o.length;s++)i=o[s],"x"===i?a+=t().toString(16):"y"===i?(i=3&t()|8,a+=i.toString(16)):a+=i;return a}function i(){return a(16)}function o(){return a(32)}function a(t){function e(){return n?15&n[r++]:16*Math.random()|0}var n=null,r=0,i=window.crypto||window.msCrypto;i&&i.getRandomValues&&Uint8Array&&(n=i.getRandomValues(new Uint8Array(31)));for(var o=[],a=0;a<t;a++)o.push(e().toString(16));return o.join("")}e.exports={generateUuid:r,generateSpanId:i,generateTraceId:o}},{}],26:[function(t,e,n){function r(t,e){if(!i)return!1;if(t!==i)return!1;if(!e)return!0;if(!o)return!1;for(var n=o.split("."),r=e.split("."),a=0;a<r.length;a++)if(r[a]!==n[a])return!1;return!0}var i=null,o=null,a=/Version\/(\S+)\s+Safari/;if(navigator.userAgent){var s=navigator.userAgent,c=s.match(a);c&&s.indexOf("Chrome")===-1&&s.indexOf("Chromium")===-1&&(i="Safari",o=c[1])}e.exports={agent:i,version:o,match:r}},{}],27:[function(t,e,n){function r(t){function e(){t(s&&document[s]?document[s]:document[o]?"hidden":"visible")}"addEventListener"in document&&a&&document.addEventListener(a,e,i(!1))}var i=t(19);e.exports=r;var o,a,s;"undefined"!=typeof document.hidden?(o="hidden",a="visibilitychange",s="visibilityState"):"undefined"!=typeof document.msHidden?(o="msHidden",a="msvisibilitychange"):"undefined"!=typeof document.webkitHidden&&(o="webkitHidden",a="webkitvisibilitychange",s="webkitVisibilityState")},{}],28:[function(t,e,n){function r(t,e){var n=[],r="",o=0;for(r in t)i.call(t,r)&&(n[o]=e(r,t[r]),o+=1);return n}var i=Object.prototype.hasOwnProperty;e.exports=r},{}],29:[function(t,e,n){function r(t,e,n){e||(e=0),"undefined"==typeof n&&(n=t?t.length:0);for(var r=-1,i=n-e||0,o=Array(i<0?0:i);++r<i;)o[r]=t[e+r];return o}e.exports=r},{}],30:[function(t,e,n){e.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],ee:[function(t,e,n){function r(){}function i(t){function e(t){return t&&t instanceof r?t:t?f(t,c,a):a()}function n(n,r,i,o,a){if(a!==!1&&(a=!0),!p.aborted||o){t&&a&&t(n,r,i);for(var s=e(i),c=m(n),f=c.length,u=0;u<f;u++)c[u].apply(s,r);var l=d[y[n]];return l&&l.push([x,n,r,s]),s}}function o(t,e){g[t]=m(t).concat(e)}function h(t,e){var n=g[t];if(n)for(var r=0;r<n.length;r++)n[r]===e&&n.splice(r,1)}function m(t){return g[t]||[]}function v(t){return l[t]=l[t]||i(n)}function w(t,e){p.aborted||u(t,function(t,n){e=e||"feature",y[n]=e,e in d||(d[e]=[])})}var g={},y={},x={on:o,addEventListener:o,removeEventListener:h,emit:n,get:v,listeners:m,context:e,buffer:w,abort:s,aborted:!1};return x}function o(t){return f(t,c,a)}function a(){return new r}function s(){(d.api||d.feature)&&(p.aborted=!0,d=p.backlog={})}var c="nr@context",f=t("gos"),u=t(28),d={},l={},p=e.exports=i();e.exports.getOrSetContext=o,p.backlog=d},{}],gos:[function(t,e,n){function r(t,e,n){if(i.call(t,e))return t[e];var r=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(t,e,{value:r,writable:!0,enumerable:!1}),r}catch(o){}return t[e]=r,r}var i=Object.prototype.hasOwnProperty;e.exports=r},{}],handle:[function(t,e,n){function r(t,e,n,r){i.buffer([t],r),i.emit(t,e,n)}var i=t("ee").get("handle");e.exports=r,r.ee=i},{}],id:[function(t,e,n){function r(t){var e=typeof t;return!t||"object"!==e&&"function"!==e?-1:t===window?0:a(t,o,function(){return i++})}var i=1,o="nr@id",a=t("gos");e.exports=r},{}],loader:[function(t,e,n){function r(){if(!T++){var t=O.info=NREUM.info,e=v.getElementsByTagName("script")[0];if(setTimeout(f.abort,3e4),!(t&&t.licenseKey&&t.applicationID&&e))return f.abort();c(R,function(e,n){t[e]||(t[e]=n)});var n=a();s("mark",["onload",n+O.offset],null,"api"),s("timing",["load",n]);var r=v.createElement("script");0===t.agent.indexOf("http://")||0===t.agent.indexOf("https://")?r.src=t.agent:r.src=h+"://"+t.agent,e.parentNode.insertBefore(r,e)}}function i(){"complete"===v.readyState&&o()}function o(){s("mark",["domContent",a()+O.offset],null,"api")}var a=t(22),s=t("handle"),c=t(28),f=t("ee"),u=t(26),d=t(23),l=t(17),p=t(19),h=l.getConfiguration("ssl")===!1?"http":"https",m=window,v=m.document,w="addEventListener",g="attachEvent",y=m.XMLHttpRequest,x=y&&y.prototype,b=!d(m.location);NREUM.o={ST:setTimeout,SI:m.setImmediate,CT:clearTimeout,XHR:y,REQ:m.Request,EV:m.Event,PR:m.Promise,MO:m.MutationObserver};var E=""+location,R={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1215.min.js"},S=y&&x&&x[w]&&!/CriOS/.test(navigator.userAgent),O=e.exports={offset:a.getLastTimestamp(),now:a,origin:E,features:{},xhrWrappable:S,userAgent:u,disabled:b};if(!b){t(16),t(24),v[w]?(v[w]("DOMContentLoaded",o,p(!1)),m[w]("load",r,p(!1))):(v[g]("onreadystatechange",i),m[g]("onload",r)),s("mark",["firstbyte",a.getLastTimestamp()],null,"api");var T=0}},{}],"wrap-function":[function(t,e,n){function r(t,e){function n(e,n,r,c,f){function nrWrapper(){var o,a,u,l;try{a=this,o=d(arguments),u="function"==typeof r?r(o,a):r||{}}catch(p){i([p,"",[o,a,c],u],t)}s(n+"start",[o,a,c],u,f);try{return l=e.apply(a,o)}catch(h){throw s(n+"err",[o,a,h],u,f),h}finally{s(n+"end",[o,a,l],u,f)}}return a(e)?e:(n||(n=""),nrWrapper[l]=e,o(e,nrWrapper,t),nrWrapper)}function r(t,e,r,i,o){r||(r="");var s,c,f,u="-"===r.charAt(0);for(f=0;f<e.length;f++)c=e[f],s=t[c],a(s)||(t[c]=n(s,u?c+r:r,i,c,o))}function s(n,r,o,a){if(!h||e){var s=h;h=!0;try{t.emit(n,r,o,e,a)}catch(c){i([c,n,r,o],t)}h=s}}return t||(t=u),n.inPlace=r,n.flag=l,n}function i(t,e){e||(e=u);try{e.emit("internal-error",t)}catch(n){}}function o(t,e,n){if(Object.defineProperty&&Object.keys)try{var r=Object.keys(t);return r.forEach(function(n){Object.defineProperty(e,n,{get:function(){return t[n]},set:function(e){return t[n]=e,e}})}),e}catch(o){i([o],n)}for(var a in t)p.call(t,a)&&(e[a]=t[a]);return e}function a(t){return!(t&&t instanceof Function&&t.apply&&!t[l])}function s(t,e){var n=e(t);return n[l]=t,o(t,n,u),n}function c(t,e,n){var r=t[e];t[e]=s(r,n)}function f(){for(var t=arguments.length,e=new Array(t),n=0;n<t;++n)e[n]=arguments[n];return e}var u=t("ee"),d=t(29),l="nr@original",p=Object.prototype.hasOwnProperty,h=!1;e.exports=r,e.exports.wrapFunction=s,e.exports.wrapInPlace=c,e.exports.argsToArray=f},{}]},{},["loader",2,13,4,3]);</script><script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam-cell.nr-data.net","errorBeacon":"bam-cell.nr-data.net","licenseKey":"8d5fb92f6e","applicationID":"2098939","transactionName":"ZwMAYEdSCktRWxZRXV5JJEFbUBBRX1ZNSEBfBA5RWEABTB5OC11FQ0gGUUFSDVQeSRddQUQPDVpqVwFMUVEOAmNFAxFAXFwKfFVMA1FeZg8HQxtUAUw=","queueTime":0,"applicationTime":51,"agent":""}</script>
    <title>Loading...</title>
    <meta property="og:title" content="" />

    
    <meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover' name='viewport' />
    
    <meta name="description" content="Level up your coding skills and quickly land a job. This is the best place to expand your knowledge and get prepared for your next interview." />
    
    <meta property="og:image" content="/static/images/LeetCode_Sharing.png" />
    <meta property="og:description" content="Level up your coding skills and quickly land a job. This is the best place to expand your knowledge and get prepared for your next interview." />

    

    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-57x57.png" />
    <link rel="apple-touch-icon" sizes="60x60" href="/apple-touch-icon-60x60.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-72x72.png" />
    <link rel="apple-touch-icon" sizes="76x76" href="/apple-touch-icon-76x76.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114x114.png" />
    <link rel="apple-touch-icon" sizes="120x120" href="/apple-touch-icon-120x120.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144x144.png" />
    <link rel="apple-touch-icon" sizes="152x152" href="/apple-touch-icon-152x152.png" />
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon-180x180.png" />
    <link rel="icon" type="image/png" href="/favicon-16x16.png" sizes="16x16" />
    <link rel="icon" type="image/png" href="/favicon-32x32.png" sizes="32x32" />
    <link rel="icon" type="image/png" href="/favicon-96x96.png" sizes="96x96" />
    <link rel="icon" type="image/png" href="/favicon-160x160.png" sizes="160x160" />
    <link rel="icon" type="image/png" href="/favicon-192x192.png" sizes="192x192" />
    <meta name="application-name" content="LeetCode"/>
    <meta name="msapplication-TileColor" content="#da532c" />
    <meta name="msapplication-TileImage" content="/mstile-144x144.png" />

    <script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s
  .createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m
  .parentNode.insertBefore(a,m)})(window,document,'script',
  '//www.google-analytics.com/analytics.js','ga');
  var currentDate=new Date();
  var thresholdDate=new Date(Date.UTC(2022, 0, 1, 0, 0, 0));
  ga('create', 'UA-159258186-1', 'leetcode.com', { userId: 3112098, sampleRate: currentDate <= thresholdDate ? 75 : 100 });
  ga('set', {'dimension1': 'false', 'dimension2': '3112098'});
  ga('require', 'displayfeatures');
  ga('send', 'pageview');
</script>

<script type="text/javascript" defer="defer" src="https://extend.vimeocdn.com/ga/124665836.js"></script>


    


<style>
  #app {
    height: 100%;
    width: 100%;
    overflow-y: auto;
  }
</style>

    
  </head>
  <body>
    
<style id="initial-loading-style">
  #initial-loading {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    background: white;
    transition: opacity .6s;
    z-index: 1;
  }

  #initial-loading[data-is-hide="true"] {
    opacity: 0;
    pointer-events: none;
  }

  #initial-loading .spinner {
    display: flex;
  }

  #initial-loading .bounce {
    width: 18px;
    height: 18px;
    margin: 0 3px;
    background-color: #999999;
    border-radius: 100%;
    display: inline-block;
    -webkit-animation: sk-bouncedelay 1.4s infinite ease-in-out both;
    animation: sk-bouncedelay 1.4s infinite ease-in-out both;
  }

  #initial-loading .bounce:nth-child(1) {
    -webkit-animation-delay: -0.32s;
    animation-delay: -0.32s;
  }

  #initial-loading .bounce:nth-child(2) {
    -webkit-animation-delay: -0.16s;
    animation-delay: -0.16s;
  }

  @-webkit-keyframes sk-bouncedelay {

    0%,
    80%,
    100% {
      -webkit-transform: scale(0);
      transform: scale(0);
    }

    40% {
      -webkit-transform: scale(1.0);
      transform: scale(1.0);
    }
  }

  @keyframes sk-bouncedelay {

    0%,
    80%,
    100% {
      -webkit-transform: scale(0);
      transform: scale(0);
    }

    40% {
      -webkit-transform: scale(1.0);
      transform: scale(1.0);
    }
  }
</style>

<div id="initial-loading">
  <div class="spinner">
    <div class="bounce"></div>
    <div class="bounce"></div>
    <div class="bounce"></div>
  </div>
</div>

<div id="app"></div>


<script>
  function recaptchaV2Callback() {
    window.grecaptchaV2 = Object.assign(Object.create(Object.getPrototypeOf(window.grecaptcha)), window.grecaptcha)
  }

  function recaptchaV3Callback() {
    window.grecaptchaV3 = Object.assign(Object.create(Object.getPrototypeOf(window.grecaptcha)), window.grecaptcha)
  }
</script>

<script type="text/javascript" src="https://www.recaptcha.net/recaptcha/api.js?onload=recaptchaV2Callback&render=explicit" async
  defer></script>


<script
  src="https://www.recaptcha.net/recaptcha/api.js?onload=recaptchaV3Callback&render=6LdBpsIUAAAAAKAYWjZfIpn4cJHVIk_tsmxpl7cz"></script>
<script>
  // Clean it after removing loading placeholder from this file.
  window.prerenderReady = false;
</script>

    <script type="text/javascript" src="https://assets.leetcode.com/static_assets/public/webpack_bundles/runtime.87724bff8.js" ></script>
    <script type="text/javascript" src="https://assets.leetcode.com/static_assets/public/webpack_bundles/common/global.727c8222f.js" ></script>
    <script type="text/javascript" src="https://assets.leetcode.com/static_assets/public/webpack_bundles/common/styles/index.4857ec0d1.js" ></script>
    <script type="text/javascript" src="https://assets.leetcode.com/static_assets/public/webpack_bundles/common/styles/new/index.f67a6c5db.js" ></script>
    <script type="text/javascript" src="https://assets.leetcode.com/static_assets/public/webpack_bundles/vendor-libs.9dd7acf68.js" ></script>
    <script type="text/javascript" src="https://assets.leetcode.com/static_assets/public/webpack_bundles/common-libs.bd38f57cb.js" ></script>
    <script type="text/javascript" src="https://assets.leetcode.com/static_assets/public/webpack_bundles/new-libs.bcba13131.js" ></script>

    

<script type="text/javascript" src="https://assets.leetcode.com/static_assets/public/webpack_bundles/new-apps/desktop.810a9192c.js" ></script>



    
      <script type="text/javascript">

  var eventURL = 'https://leetcode.com/jobs/';
  var CONTENT = "🔈 LeetCode is hiring! Apply NOW.🔈";

  function getHashCode(str) {
    var hash = 0,
      i,
      chr;
    if (str.length === 0) return hash;
    for (i = 0; i < str.length; i++) {
      chr = str.charCodeAt(i);
      hash = (hash << 5) - hash + chr;
      hash |= 0;
    }
    return hash;
  }

  var LOCAL_STORAGE_KEY = 'feedback-tab:' + getHashCode(eventURL + CONTENT);
  var CLOSE_BUTTON_CLICKED = false;

  var CLOSE_BUTTON_HTML =
    '\
        <?xml version="1.0" encoding="UTF-8"?>\
        <svg id="close-icon-svg" width="24px" height="24px" viewBox="0 0 24 24" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\
            <title>icon/close</title>\
            <defs></defs>\
            <g id="close-icon" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">\
                <polygon id="path-1" points="19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12"></polygon>\
            </g>\
        </svg>\
    ';

  function onClickClose(e) {
    e.preventDefault();
    document
      .querySelector('.feedback-anchor')
      .classList.add('feedback-anchor-closing');
    window.localStorage.setItem(LOCAL_STORAGE_KEY, Date.now());
    CLOSE_BUTTON_CLICKED = true;
  }

  function onTransitionEnd(event) {
    if (
      event.target &&
      CLOSE_BUTTON_CLICKED &&
      event.propertyName === 'opacity'
    ) {
      event.target.remove();
    }
  }

  function createFeedbackTab() {
    var closeButton = document.createElement('span');
    closeButton.classList.add('feedback-tab-close-button');
    closeButton.innerHTML = CLOSE_BUTTON_HTML;
    closeButton.addEventListener('click', onClickClose);

    var feedbackTabContent = document.createElement('span');
    feedbackTabContent.innerHTML = CONTENT;

    var feedbackTab = document.createElement('div');
    feedbackTab.classList.add('feedback-tab');

    feedbackTab.appendChild(feedbackTabContent);
    feedbackTab.appendChild(closeButton);

    var feedbackAnchor = document.createElement('a');
    feedbackAnchor.classList.add('feedback-anchor');
    feedbackAnchor.setAttribute('href', eventURL);
    feedbackAnchor.setAttribute('target', '_blank');
    feedbackAnchor.appendChild(feedbackTab);
    feedbackAnchor.addEventListener('transitionend', onTransitionEnd);
    return feedbackAnchor;
  }

  function createComingSoonBanner(text) {
    var banner = document.createElement('div');
    banner.classList.add('card-label');
    banner.style.background = 'rgb(95, 123, 230)';
    banner.style.color = 'white';
    banner.style['font-weight'] = 'bold';
    banner.innerHTML = text;
    return banner;
  }

  function insertFeedbackTab() {
    var feedbackTab = createFeedbackTab();
    var navbarRightContainer = document.getElementById(
      'navbar-right-container'
    );
    if (navbarRightContainer) {
      navbarRightContainer.insertBefore(
        feedbackTab,
        navbarRightContainer.firstChild
      );
    }
  }

  function insertComingSoonBanner(text, clsname) {
    var banner = createComingSoonBanner(text);
    var exploreCardContainer = document.getElementsByClassName(clsname);

    if (!exploreCardContainer.length) {
      return false;
    }

    var innerLayer = exploreCardContainer[0].getElementsByClassName(
      'top-inner-layer'
    );

    if (!innerLayer.length) {
      return false;
    }

    innerLayer[0].insertBefore(banner, innerLayer[0].firstChild);
    return true;
  }

  function loadLeetCodeChallenge() {
    if (!window.localStorage.getItem(LOCAL_STORAGE_KEY)) {
      setTimeout(insertFeedbackTab, 500);
    }

    if (window.location.pathname === '/explore/') {
      var comingSoonInterval = setInterval(function() {
        var res2 = insertComingSoonBanner(
          'Day 30',
          'september-leetcoding-challenge-2021'
        );
        if (/*res && */ res2 && comingSoonInterval) {
          clearInterval(comingSoonInterval);
        }
      }, 300);
    }

    var script = document.createElement('script');
    script.async = true;
    script.src = 'https://leetcode.com/static/cn.js';
    document.body.appendChild(script);
  }
</script>
<style>
  .feedback-tab {
    position: absolute;
    display: flex;
    align-items: center;
    top: 0px;
    right: 270px;
    background-color: #FFA400;
    color: white;
    opacity: 0.6;
    border-radius: 0 0 3px 3px;
    padding: 5px 10px;
    cursor: pointer;
    z-index: 2;
    transition: all 0.3s ease-in-out;
  }
  .feedback-tab:hover {
    opacity: 1;
  }
  .feedback-tab-close-button {
    margin-left: 5px;
    height: 1em;
    width: 1em;
    display: inline-flex;
    align-items: center;
    justify-content: center;
  }
  .feedback-anchor:focus {
    text-decoration: none;
  }
  .feedback-anchor-closing {
    opacity: 0;
    transition: opacity 0.3s ease-in-out;
  }
  aside#region_switcher {
    position: initial;
  }
  #close-icon-svg {
    opacity: 0.5;
    transition: all 0.3s ease-in-out;
  }
  #close-icon-svg:hover {
    opacity: 1;
  }
  #close-icon {
    fill: white;
  }
</style>


<!--@START: Nav Highlight Tag -->
<style>
  [id='interview-nav-item'] a.ant-dropdown-link::after {
    display: block;
    border-radius: 20px;
    padding: 0px 8px;
    color: white;
    font-size: 12px;
    position: absolute;
    top: -9px;
    font-weight: 500;
    transform: scale(0.6);
    right: -25px;
    content: 'New';
    background: rgb(236, 64, 122);
  }
  [class*='nav-item-container'] a[href='/contest/']::after {
    display: block;
    background: red;
    border-radius: 20px;
    padding: 0px 8px;
    color: white;
    font-size: 12px;
    position: absolute;
    top: -9px;
    right: -15px;
    font-weight: 500;
    transform: scale(0.6);
  }
</style>

<script type="text/javascript">
  var DISCOUNT_URL = '/subscribe/';
  var DISCOUNT_CONTENT =
    'In an effort to fight COVID-19, from now until a limited time only, users residing in India can enjoy discount on both&nbsp';
  var DISCOUNT_LINK = 'monthly and annual subscriptions';

  function createDiscountTab() {
    var discountTabContent = document.createElement('span');
    discountTabContent.innerHTML = DISCOUNT_CONTENT;
    var subscribeLink = document.createElement('a');
    subscribeLink.setAttribute('href', DISCOUNT_URL);
    subscribeLink.classList.add('subscribe-link');
    subscribeLink.innerHTML = DISCOUNT_LINK;
    var exclamation = document.createElement('span');
    exclamation.innerHTML = '!';

    var discountTab = document.createElement('div');
    discountTab.classList.add('col-md-12');
    discountTab.classList.add('alert');
    discountTab.classList.add('alert-warning');

    discountTab.appendChild(discountTabContent);
    discountTab.appendChild(subscribeLink);
    discountTab.appendChild(exclamation);

    var DiscountContainer = document.createElement('div');
    DiscountContainer.classList.add('container');
    DiscountContainer.classList.add('row');
    DiscountContainer.classList.add('no-margin');
    DiscountContainer.classList.add('container-center');
    DiscountContainer.appendChild(discountTab);
    return DiscountContainer;
  }

  function insertDiscountTab() {
    var discountTab = createDiscountTab();
    var container = document.getElementById('base_content');
    if (container) {
      container.insertBefore(discountTab, container.firstChild);
    }
  }

  window.onload = function() {
    if (window.LeetCodeData) {
      const {
        features: { enableIndiaPricing },
        userStatus: { countryCode },
      } = window.LeetCodeData;
      if (
        (window.location.pathname === '/' ||
          window.location.pathname.startsWith('/problemset')) &&
        enableIndiaPricing &&
        countryCode === 'IN'
      ) {
        setTimeout(insertDiscountTab, 500);
      }

      var script = document.createElement('script');
      script.async = true;
      document.body.appendChild(script);
    }
    loadLeetCodeChallenge();
    setTimeout(function() {
        document.getElementsByClassName("sidebar-challenge-ad")[0].style.display = "none";
    }, 1000);
  };
</script>
<style>
  .container-center {
    margin: auto;
    display: flex;
    justify-content: center;
    padding: 0;
    text-align: center;
    margin-top: -10px;
  }
  .subscribe-link {
    cursor: pointer;
  }
</style>
    
  </body>
</html>
