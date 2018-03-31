var api = (function(){
    "use strict";

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    function send(method, url, data, callback){
        var xhr = new XMLHttpRequest();
        var csrftoken = getCookie('csrftoken');
        xhr.onload = function() {
            if (xhr.status !== 200) callback("[" + xhr.status + "] " + xhr.responseText, null);
            else callback(null, JSON.parse(xhr.responseText));
        };
        xhr.open(method, url, true);
        if (!data) xhr.send();
        else{
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
            xhr.send(JSON.stringify(data));
        }
    }
    
    var module = {};
    
    
    module.signin = function (username, password, callback){
        send("POST", "/api/signin/", {username: username, password: password}, callback);
    }
    
    module.signup = function (username, password, password_confirm, callback){
        send("POST", "/api/signup/", {username: username, password: password, password_confirm: password_confirm}, callback);
    }

    module.setLocation = function (location, callback){
        send("POST", "/api/location/", {location: location}, callback);
    }

    module.setSubreddit = function(subreddit, callback){
        console.log(subreddit)
        send("POST", "/api/subreddit/", {subreddit: subreddit}, callback);
    }

    module.getSubreddit = function(callback){
        send("GET", "/api/subreddit/", null, callback);
    }

    module.toggle = function (type, action, callback){
        send("PATCH", "/api/toggle/", {type: type, action: action}, callback);
    }

    module.getQuote = function (callback){
        send("GET", "/api/getQuote/", null, callback)
    }

    module.getMotivation = function (callback){
        send("GET", "/api/getMotivation/", null, callback)
    }

    module.getUWordOfTheDay = function (callback){
        send("GET", "/api/getUWordOfTheDay/", null, callback)
    }

    module.getUrbanDictionary = function (callback){
        send("GET", "/api/getUrbanDictionary/", null, callback)
    }

    module.getWeather = function(callback){
        send("GET", "/api/getWeather/", null, callback);
    }

    module.getUser = function(callback){
        send("GET", "/api/user/", null, callback);
    }

    module.setPhoneNumber = function (phone_number, callback){
        send("POST", "/api/phonenumber/", {phone_number: phone_number}, callback);
    }

    module.getPhoneNumber = function (callback){
        send("GET", "/api/phonenumber/", null, callback);
    }

    module.getNews = function (callback){
        send("GET", "/api/news/", null, callback);
    }

    module.getNewsExample = function (callback){
        send("GET", "/api/newsExample/", null, callback);
    }

    module.getRedditExample = function (callback){
        send("GET", "/api/redditExample/", null, callback);
    }

    module.getPhoto = function (callback){
        send("GET", "/api/photo/", null, callback);
    }

    module.getPhotoExample = function (callback){
        send("GET", "/api/photoExample/", null, callback);
    }
    return module;
})();
