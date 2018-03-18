var api = (function(){
    "use strict";
    
    function send(method, url, data, callback){
        var xhr = new XMLHttpRequest();
        xhr.onload = function() {
            if (xhr.status !== 200) callback("[" + xhr.status + "] " + xhr.responseText, null);
            else callback(null, JSON.parse(xhr.responseText));
        };
        xhr.open(method, url, true);
        if (!data) xhr.send();
        else{
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.send(JSON.stringify(data));
        }
    }
    
    var module = {};
    
    module.getCurrentUser = function(){
        var l = document.cookie.split("username=");
        if (l.length > 1) return l[1];
        return null;
    }
    
    module.signin = function (username, password, callback){
        send("POST", "/api/signin/", {username: username, password: password}, callback);
    }
    
    module.signup = function (username, password, password_confirm, callback){
        send("POST", "/api/signup/", {username: username, password: password, password_confirm: password_confirm}, callback);
    }
    
    return module;
})();
