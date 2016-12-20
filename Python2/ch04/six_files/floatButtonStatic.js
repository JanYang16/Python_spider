(function(){
    var isIE6 = (function(a){
        if (a.indexOf("MSIE") > 0) {
            var reg = /msie([^;]+);/i;
            var match = a.match(reg);
            if (parseFloat(match[1]) <= 7) {
                return true;
            }
        }
        return false;
    })(navigator.userAgent);
    var isMobile = (function(a){
		if(a) a=a.toLowerCase();
		var deviceKeys=["iPhone","iPad","iPod","Android","Mobile","Linux","SymbianOS","BlackBerry","Phone"];
		for ( var i = 0; i < deviceKeys.length; i++) {
			var index =a.indexOf(deviceKeys[i].toLowerCase());
			if(index!=-1){
				return true;
			}		
		}
		return false;
	})(navigator.userAgent);
	var isSougou = (function(a){
		if(a) a=a.toLowerCase();
		var index = a.indexOf("se 2.x");
		if(index!=-1){
			return true;
		}else return false;
	})(navigator.userAgent);
	var isyl = (typeof releaseVersion !="undefined")&&releaseVersion=="yl";
	var isOpenNewTab = isMobile||isSougou||isyl;

    var protocol = ((document.location.protocol == "https:") ? "https://" : "http://");
    function $class(className){
        var childs = document.getElementsByTagName("*"), length = childs.length;
        var items = [];
        for (var i = 0; i < length; i++) {
            if (childs[i].className.match(new RegExp("(^|\\s)" + className + "(\\s|$)"))) {
                items.push(childs[i]);
            }
        }
        return items;
    };
    function urlToParams(s){
        if (typeof s == "undefined") {
            return;
        }
        var urlMap = s.split("&"), map = [];
        if (null != urlMap) {
            var temp = [];
            for (var i = 0; i < urlMap.length; i++) {
                if (typeof urlMap[i] == "string") 
                    temp = urlMap[i].split("=");
                map[temp[0]] = temp[1];
            }
            return map;
        }
        return [];
    };
    function setCookie(name, value){
        var Days = 30;
        var exp = new Date();
        exp.setTime(exp.getTime() + Days * 24 * 60 * 60 * 1000);
        document.cookie = name + "=" + escape(value) + ";path=/";
    };
    function setSessionCookie(name,value){
	  document.cookie = name + "="+ escape (value) + ";path=/";
    };
    function getCookie(name){
        var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
        if (arr = document.cookie.match(reg)) 
            return unescape(arr[2]);
        else 
            return null;
    };
    function isCookie(){
     document.cookie = "testcookie=testvalue";
		var cookiestr = new String(document.cookie);
		var cookiename = "testcookie=testvalue";
		var beginpos = cookiestr.indexOf(cookiename);
		if (beginpos != -1) {
			delCookie("testcookie");
			return true;
		} else {
			return false;
		}
    
    };
    function delCookie(name){
   	 var exp = new Date();
          exp.setTime(exp.getTime() - 1);
     	 var cval=getCookie(name);
          if(cval!=null){document.cookie= name + "="+cval+";expires="+exp.toGMTString();}
   };
    function getIconParams(live800_configContent,live800_companyID){
        var params = [], queryParam = [];
        if (typeof live800_configContent == "undefined" || typeof live800_companyID == "undefined") {
            return false;
        }
        params = urlToParams(live800_configContent);
        params['company'] = live800_companyID;
        var rs = {
            "company": params["company"],
            "float": typeof params["live800_floatToRight"] != "undefined" ? params["live800_floatToRight"] : 1,
            "side": typeof params["live800_floatSide"] != "undefined" ? params["live800_floatSide"] : 5,
            "top": typeof params["live800_floatTop"] != "undefined" ? params["live800_floatTop"] : 150,
            "close": typeof params["live800_closeIcon"] != "undefined" ? params["live800_closeIcon"] : 0,
            "online": typeof params["live800_online"] != "undefined" ? params["live800_online"] : "",
            "offline": typeof params["live800_offline"] != "undefined" ? params["live800_offline"] : ""
        };
        if (typeof params["live800_operator"] != "undefined") {
            rs["operator"] = params["live800_operator"];
        }
        if (typeof params["live800_skill"] != "undefined") {
            rs["skill"] = params["live800_skill"];
        }
        return rs;
    };
    function iconGenerator(live800_configContent,live800_companyID,live800_configID){
        var icons = document.getElementById(live800_companyID+"live800"+live800_configID);
        if (!icons) {
            var pms = getIconParams(live800_configContent,live800_companyID);
            if (!pms) {
                return false;
            }
            var divhtmls = "<div class='lim_float_icon' id='"+live800_companyID+"live800"+live800_configID+"' lim_company='" + pms["company"] + "' lim_float='" + pms["float"] + "' lim_close='" + pms['close'] + "' lim_side='" + pms["side"] + "' lim_top='" + pms["top"] + "' lim_online='" + pms["online"] + "' lim_offline='" + pms["offline"] + "'";
            if (typeof pms["operator"] != "undefined") {
                divhtmls += " lim_operator='" + pms["operator"] + "'";
            }
            if (typeof pms["skill"] != "undefined") {
                divhtmls += " lim_skill='" + pms["skill"] + "'";
            }
            divhtmls += "></div>";
            var floatdiv = document.createElement("div");
            floatdiv.innerHTML = divhtmls;
            document.body.appendChild(floatdiv);
           icons = document.getElementById(live800_companyID+"live800"+live800_configID);
        }
         var items = [];
         items.push(icons);
        return items;
    };
    function lockIcon(el){
        this.topSide = parseInt(el.getAttribute("lim_top"));
        this.floatRight = parseInt(el.getAttribute("lim_float"));
        this.side = parseInt(el.getAttribute("lim_side"));
        this.element = el;
        this.init();
    };
    lockIcon.prototype = {
        init: function(){
            var lockObj = this.element, objStyle = lockObj.style, ua = navigator.userAgent;
            objStyle.position = "absolute";
            objStyle.zIndex = "2147483647";
            objStyle.top = this.topSide + "px";
            if (ua.toLowerCase().indexOf('360se') > -1) {
                this.isBlock = true;
            }
            else 
                if (ua.toLowerCase().indexOf("theworld") > 0) {
                    this.isBlock = true;
                }
            this.floatRight == 1 ? objStyle.right = this.side + "px" : objStyle.left = this.side + "px";
            var locker = this;
            setInterval(function(){
                locker.lock.call(locker)
            }, 20);
        },
        lockTop: function(el, position, page, scroll, icon){
            var y = scroll.top + icon.topSide, offsetTop = (y - parseInt(el.style.top)) / 20;
            if (this.isBlock) {
                offsetTop = (y - parseInt(el.style.top));
            }
            var topSide = parseInt(el.style.top) + offsetTop;
            if ((topSide + position.height) < page.height) {
                el.style.top = topSide + "px";
            }
        },
        lockLeft: function(el, scroll, icon){
            var x = scroll.left + icon.side, offsetLeft = (x - parseInt(el.style.left)) / 20;
            el.style.left = (parseInt(el.style.left) + offsetLeft) + "px";
        },
        lockRight: function(el, scroll, icon){
            var d = document;
            if (scroll.left == 0) {
                var x = icon.side, offsetRight = (Math.abs(x) - Math.abs(parseInt(el.style.right))) / 20;
                el.style.right = (Math.abs(parseInt(el.style.right)) + offsetRight) + "px";
            }
            else {
                if (isIE6) {
                    ;
                }
                else {
                    var x = scroll.left - icon.side, offsetRight = (Math.abs(x) - Math.abs(parseInt(el.style.right))) / 20;
                    el.style.right = -(Math.abs(parseInt(el.style.right)) + offsetRight) + "px";
                }
            }
        },
        lock: function(){
            var el = this.element, position = this.currentPosition(el), win = this.windowDimension(), scroll = this.scrollPosition(), page = this.pageDimension(), icon = this;
            this.lockTop(el, position, page, scroll, icon);
            if (this.floatRight == 1) {
                this.lockRight(el, scroll, icon);
            }
            else {
                this.lockLeft(el, scroll, icon);
            }
            if (this.isBlock) {
                if (this.lastTop != el.style.top) {
                    el.style.visibility = "hidden";
                    this.lastTop = el.style.top;
                }
                else {
                    el.style.visibility = "visible";
                }
            }
        },
        currentPosition: function(el){
            return {
                top: el.offsetTop,
                left: el.offsetLeft,
                width: el.offsetWidth,
                height: el.offsetHeight
            };
        },
        windowDimension: function(){
            if ((typeof innerWidth != "undefined" && innerWidth != 0) && (typeof innerHeight != "undefined" && innerHeight != 0)) {
                return {
                    width: innerWidth,
                    height: innerHeight
                };
            }
            var d = document;
            return {
                width: Math.min(d.body.clientWidth, d.documentElement.clientWidth),
                height: Math.min(d.body.clientHeight, d.documentElement.clientHeight)
            };
        },
        scrollPosition: function(){
            var d = document;
            return {
                top: Math.max(d.body.scrollTop, d.documentElement.scrollTop),
                left: Math.max(d.body.scrollLeft, d.documentElement.scrollLeft)
            };
        },
        pageDimension: function(){
            var d = document;
            return {
                width: Math.max(d.body.scrollWidth, d.documentElement.scrollWidth),
                height: Math.max(d.body.scrollHeight, d.documentElement.scrollHeight)
            }
        }
    };
    window.limIconClose = function(el){
        var pNode = el.parentNode;
        if (pNode.className.indexOf('lim_float_icon') == -1) {
            pNode = pNode.parentNode;
        }
        pNode.style.visibility = "hidden";
    };
    var _encoder = function(Str){
        if (Str == null || Str == "") {
            return "";
        }
        var newStr = "";
        function toCase(sStr){
            return sStr.toString(16).toUpperCase();
        }
        for (var i = 0, icode, len = Str.length; i < len; i++) {
            icode = Str.charCodeAt(i);
            if (icode < 0x10) {
                newStr += "%0" + icode.toString(16).toUpperCase();
            }
            else 
                if (icode < 0x80) {
                    if (icode == 0x20) {
                        newStr += "+";
                    }
                    else 
                        if ((icode >= 0x30 && icode <= 0x39) || (icode >= 0x41 && icode <= 0x5A) || (icode >= 0x61 && icode <= 0x7A)) {
                            newStr += Str.charAt(i);
                        }
                        else {
                            newStr += "%" + toCase(icode);
                        }
                }
                else 
                    if (icode < 0x800) {
                        newStr += "%" + toCase(0xC0 + (icode >> 6));
                        newStr += "%" + toCase(0x80 + icode % 0x40);
                    }
                    else {
                        newStr += "%" + toCase(0xE0 + (icode >> 12));
                        newStr += "%" + toCase(0x80 + (icode >> 6) % 0x40);
                        newStr += "%" + toCase(0x80 + icode % 0x40);
                    }
        }
        return newStr;
    };
    window.openChat = function(el){
        try {
            parent.closeMini();
        } 
        catch (e) {
            ;
        }
        var pagetitle;
		if (document.title.length > 80) {
			pagetitle = _encoder(document.title.substring(0, 80));
		} else {
			pagetitle = _encoder(document.title);
		}
        var openUrl = protocol + live800_baseUrl + live800_baseWebApp + live800_baseChatHtmlDir + "/chatbox.jsp"+jsessionId+"?";
        openUrl += "companyID=" + el.getAttribute("lim_company");
        if (typeof jid != "undefined") {
            openUrl += "&jid=" + jid;
        }
        if (el.getAttribute("lim_operator")) {
            openUrl += "&operatorId=" + el.getAttribute("lim_operator");
        }
        if (el.getAttribute("lim_skill")) {
            openUrl += "&skillId=" + el.getAttribute("lim_skill");
        }
       
        openUrl += "&enterurl=" + _encoder(document.URL);
        openUrl += "&pagetitle=" + pagetitle;
        if (typeof trustfulInfo != "undefined") {
            openUrl += "&info=" + trustfulInfo;
        }
        var pagereferrinsession=getCookie("pageReferrInSession");
		if(pagereferrinsession==null || pagereferrinsession==" ")pagereferrinsession="";
		openUrl += "&pagereferrer="+_encoder(pagereferrinsession);
		
		var firstenterurlinsession=getCookie("firstEnterUrlInSession");
		if(firstenterurlinsession==null || firstenterurlinsession==" ")firstenterurlinsession="";
		openUrl += "&firstEnterUrl="+_encoder(firstenterurlinsession);
		
		if(typeof live800_Language!="undefined"){
			openUrl += "&lan=" + live800_Language;
		}

		openUrl += "&tm=" + (new Date()).getTime();
        if(isOpenNewTab){
			el.setAttribute('href',openUrl);
			return true;
		}
        var winAttr = globalWindowAttribute;
        var winnName = "chatbox"+el.getAttribute("lim_company");
        winnName += (new Date()).getTime();
        var wnd = window.open(openUrl,winnName, winAttr);
        if(typeof wnd !="undefined"){
			wnd.focus();
		}
		return false;
    };
    function flashIcon(item, imageUrl, pm, maskUrl){
        var html = '<object id="inviteFlash" classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=9,0,0,0" width="' + item.getAttribute("lim_width") + '" height="' + item.getAttribute("lim_height") + '" >';
        html += '<param name="movie" value="' + imageUrl + '" /><param name="quality" value="high" /><param name="wmode" value="opaque">';
        html += '<embed src="' + imageUrl + '" quality="high" width="' + item.getAttribute("lim_width") + '" height="' + item.getAttribute("lim_height") + '" wmode="opaque" name="movie"';
        html += ' type="application/x-shockwave-flash" pluginspage="http://www.adobe.com/go/getflashplayer"/></object>';
        html += '<div ' + pm + ' onclick="openChat(this);" style="cursor:pointer;z-index:1001;top:0;left:0;position:absolute;"><img height="' + item.getAttribute("lim_height") + '" width="' + item.getAttribute("lim_width") + '" src="' + maskUrl + '" border="0"/></div>';
        return html;
    };
    function setSessionPageReferrer(){
    	//get session ref,if ref == null ,try get from document. 		
		var dfer = getCookie("pageReferrInSession");
		if(dfer === null || dfer === ""){
			dfer = document.referrer;
			if(dfer !== null && dfer !== ""){
				var maxRefLen = 700;
				if(dfer.length >maxRefLen){
					var tempRef = dfer.substring(0,maxRefLen);
					var isbd = isBaidu(dfer);
					if(isbd){
						//if baidu,pagereffer  length maybe > maxRefLen,
						var wdArray = getBaiduWd(dfer);
						if(wdArray !== null){							
							var tempWd = getBaiduWd(tempRef);					
							if(tempWd === null){
								tempRef = tempRef + wdArray[0] + wdArray[1];
							}else{
								if(wdArray[1] !== tempWd[1]){
									tempRef = tempRef.replace(wdArray[0], wdArray[0]+wdArray[1]+"&");
								}
							}
						}
						
						var eqidArray = getBDEqid(dfer);
						if(eqidArray !== null){							
							var tempEqid = getBDEqid(tempRef);					
							if(tempEqid === null){
								tempRef = tempRef + eqidArray[0] + eqidArray[1];
							}else{
								if(eqidArray[1] !== tempEqid[1]){
									tempRef = tempRef.replace(eqidArray[0], eqidArray[0]+eqidArray[1]+"&");
								}
							}
						}
					}
					dfer = tempRef;
				}
				setSessionCookie("pageReferrInSession",dfer);
			}
		}
	};
	function isBaidu(refurl){
		var regStr = /[a-zA-Z0-9\u4E00-\u9FA5][\-a-zA-Z0-9\u4E00-\u9FA5]{0,62}(\.[a-zA-Z0-9\u4E00-\u9FA5][\-a-zA-Z0-9\u4E00-\u9FA5]{0,62})+/gi;
		var darr = refurl.match(regStr);
		if (darr && darr[0].indexOf(".baidu.")>0) {
			return true;;
		}else{
			return false;
		}
	};
	function getBDParam(refurl,keys){
		var wd = null;
		for (var i = 0, length = keys.length; i < length; i++) {
			var start = refurl.indexOf(keys[i]);
			if(start>0){
				var end = refurl.indexOf("&",start+1);
				if(end<0){
					end = refurl.length;
				}
				wd = [keys[i],refurl.substring(start+keys[i].length,end)];
				break;
			}
		}
		return wd;
	};
	function getBaiduWd(refurl){
		var keys = ["&wd=","&word=","&rqwd=","?wd=","?word=","?rqwd="];
		return getBDParam(refurl,keys);
	};
	function getBDEqid(refurl){
		var keys = ["&eqid=","?eqid="];
		return getBDParam(refurl,keys);
	};
	function setSessionFirstEnterUrl(){
	   var firstEnterUrl = getCookie("firstEnterUrlInSession");
	   if(firstEnterUrl==null){
		   firstEnterUrl = window.location;
		   if(firstEnterUrl == null){
			   firstEnterUrl = " ";
		   }
		   setSessionCookie("firstEnterUrlInSession",firstEnterUrl);
	   }
	};
    function iconProcess(live800_configContent,live800_companyID,live800_configID){
        setSessionPageReferrer();
        setSessionFirstEnterUrl();
        var icons = iconGenerator(live800_configContent,live800_companyID,live800_configID), pm, iconClose;
        if((!icons || icons.length == 0) && loadicontimes < 10){
          loadicontimes++;
          iconProcess(live800_configContent,live800_companyID,live800_configID);
          return;
        }
        if (!icons) {
            return;
        }
        
        
        var item, urlPrefix = protocol + live800_baseUrl + live800_baseWebApp + "/SurferServer?cmd=111", imageUrl, imageHtml;
        
        for (var i = 0; i < icons.length; i++) {
         
            item = icons[i];
            pm = "", imageUrl = "", imageHtml = "";
            imageUrl = urlPrefix;
            if (item.getAttribute("lim_company")) {
                imageUrl += "&amp;companyID=" + item.getAttribute("lim_company");
                pm += "lim_company='" + item.getAttribute("lim_company") + "' ";
            }
            
            var ptl = protocol.replace("://", "");
            var limOnline = item.getAttribute("lim_online");
            if (limOnline) {
            	if(ptl=="https" && !(limOnline.indexOf("https") === 0)){
            		limOnline = limOnline.replace("http", "https");
            	}
            	
                imageUrl += "&amp;online=" + limOnline;
            }
            var limOffline = item.getAttribute("lim_offline");
            if (limOffline) {
            	if(ptl=="https" && !(limOffline.indexOf("https") === 0)){
            		limOffline = limOffline.replace("http", "https");
            	}
            	
                imageUrl += "&amp;offline=" + limOffline;
            }
            
            if (item.getAttribute("lim_operator")) {
                imageUrl += "&amp;operatorId=" + item.getAttribute("lim_operator");
                pm += "lim_operator='" + item.getAttribute("lim_operator") + "' ";
                setCookie("operatorId", item.getAttribute("lim_operator"));
            }
            
            if (item.getAttribute("lim_skill")) {
                imageUrl += "&amp;skillId=" + item.getAttribute("lim_skill");
                pm += "lim_skill='" + item.getAttribute("lim_skill") + "' ";
                if (live800_companyID == "65654" || live800_companyID == "66181") {
                    if (typeof(window["lim_skills"]) != "undefined") {
                        window["lim_skills"].push(item.getAttribute("lim_skill"));
                    }
                    else {
                        window["lim_skills"] = [item.getAttribute("lim_skill")];
                    }
                }
                else {
                    setCookie("skillId", item.getAttribute("lim_skill"));
                }
            }
            imageUrl += "&amp;tm=" + (new Date()).getTime();
            iconClose = item.getAttribute("lim_close");
            imageHtml = "";
            if (iconClose && iconClose == "1") {
                imageHtml = "<div style='background:transparent;overflow:visible;position:relative;z-index:2147483647;clear:both;' onclick='limIconClose(this);'><img src='" + protocol + live800_baseUrl + live800_baseWebApp + "/images/close.gif" + "' onmouseover='this.src=\"" + protocol + live800_baseUrl + live800_baseWebApp + "/images/close_hover.gif" + "\"' onmouseout='this.src=\"" + protocol + live800_baseUrl + live800_baseWebApp + "/images/close.gif" + "\"' style='cursor:pointer;position:absolute;top:-6px;" + (item.getAttribute('lim_float') == 1 ? "left" : "right") + ":-6px;'/></div>";
            }
            imageHtml += "<div style='position:relative;z-index:2147483647;'><a id='live800iconlink' target='_blank' href='javascript:void(0)' onclick='return openChat(this) ' " + pm + "><img src='" + imageUrl + "' border='0' style='cursor:pointer;'  /></a></div>";
            if (item.getAttribute("lim_flash") && item.getAttribute("lim_flash") == "1") {
                imageHtml = flashIcon(item, imageUrl, pm, protocol + live800_baseUrl + live800_baseWebApp + "/chatClient/images/mask.gif");
            }
            item.innerHTML = imageHtml;
            new lockIcon(item);
        }
    };
    try {
        if (parent && parent.document.body.getAttribute("lim_initchat") == "1") {
            return;
        }
    } 
    catch (e) {
    }
    //解决chrome浏览器偶尔执行不了innerhtml的问题
    var loadicontimes = 0;
    if(isIE6){
    //解决IE6不能正常加载的问题
     checkdocumentready(live800_configContent,live800_companyID,live800_configID);
    }else{
   iconProcess(live800_configContent,live800_companyID,live800_configID);
    }
    function checkdocumentready(live800_configContent,live800_companyID,live800_configID){
       if(document.readyState == 'complete'){
       iconProcess(live800_configContent,live800_companyID,live800_configID);
       }else{
        document.onreadystatechange = function(){
        if(document.readyState == 'complete'){
           iconProcess(live800_configContent,live800_companyID,live800_configID);
          }
        }
       
       }
    };
    function startFlowCapacity(){
    if(isCookie() && document.body.getAttribute("lim:VisitorCapacity") != "1"){
       document.body.setAttribute("lim:VisitorCapacity","1");
	   var capacityCookie = getCookie("VisitorCapacity");
	   if(capacityCookie == null || capacityCookie == ''){
	   var execurl = protocol + live800_baseUrl + live800_baseWebApp + "/SurferServer?cmd=115&companyID="+live800_companyID;
	   var capacityImg =  new Image();
	   capacityImg.onload=function(){setSessionCookie("VisitorCapacity","1"); };
	   capacityImg.src=execurl;
		     
	   }
	 }
    
    };
    setTimeout(function(){startFlowCapacity();},5000);
})();
