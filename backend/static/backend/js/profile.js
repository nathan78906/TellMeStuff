(function(){
    "use strict";


    function getFacebookUrl(){
        api.getUser(function(err, res){
            if (err) console.log(err);
            var url = "https://m.me/tellmestuff1?ref=" + res.user_id;
            document.querySelector('#fblogin').setAttribute("href", url);      
        });
    }

    window.addEventListener('load', function(){
        getFacebookUrl();
    });
}())
