(function(){
    "use strict";

    function submitLocation(){
        if (document.querySelector('#locationform').checkValidity()){
            var location = document.querySelector("#userlocation").value;
            api.setLocation(location, function(err, res){
                if (err) {
                    document.querySelector('.location_success').style.display = 'none';                    
                    document.querySelector('.location_error').style.display = 'block';
                    document.querySelector('.location_error').innerHTML = err;
                }
                else {
                    document.querySelector('.location_error').style.display = 'none';                    
                    document.querySelector('.location_success').style.display = 'block';
                    document.querySelector('.location_success').innerHTML = "Successfully submitted your location!";
                }
            });
        }
    }

    function submitSubreddit(){
        if (document.querySelector('#subredditform').checkValidity()){
            var subreddit = document.querySelector("#usersubreddit").value;
            api.setSubreddit(subreddit, function(err, res){
                if (err) {
                    document.querySelector('.subreddit_success').style.display = 'none';                                        
                    document.querySelector('.subreddit_error').style.display = 'block';
                    document.querySelector('.subreddit_error').innerHTML = err;
                }
                else {
                    document.querySelector('.subreddit_error').style.display = 'none';                                        
                    document.querySelector('.subreddit_success').style.display = 'block';
                    document.querySelector('.subreddit_success').innerHTML = "Successfully submitted your subreddit!";
                }
            });
        }
    }

    function checkWeather(){
        api.getWeather (function(err, res){
            if (err) console.log(err);
            if (res.location != ""){
                if (res.active == true){
                    document.querySelector('#off_weather').setAttribute("class", "btn btn-warning");
                    document.querySelector('#on_weather').setAttribute("class","btn btn-warning active");
                    document.querySelector('#userlocation').placeholder = res.location;
                }
                else if (res.active == false){
                    document.querySelector('#on_weather').setAttribute("class", "btn btn-warning");
                    document.querySelector('#off_weather').setAttribute("class","btn btn-warning active");
                    document.querySelector('#userlocation').placeholder = res.location;               
                }
            }
            else{
                document.querySelector('#off_weather').setAttribute("class","btn btn-warning active");
                document.querySelector('#userlocation').placeholder = "Enter your city:";               
                              
            }
            
        });
    }

    function checkMotivation(){
        api.getMotivation (function(err, res){
            if (err) console.log(err);
            if (res.active != ""){
                if (res.active == true){
                    document.querySelector('#off_motivation').setAttribute("class", "btn btn-warning")
                    document.querySelector('#on_motivation').setAttribute("class","btn btn-warning active");
                }
                else if (res.active == false){
                    document.querySelector('#on_motivation').setAttribute("class", "btn btn-warning")
                    document.querySelector('#off_motivation').setAttribute("class","btn btn-warning active");             
                }
            }
            else{
                document.querySelector('#off_motivation').setAttribute("class","btn btn-warning active");         
                              
            }
            
        });
    }

    function checkSubreddit(){
        api.getSubreddit (function(err, res){
            if (err) console.log(err);
            if (res.subreddit != ""){
                if (res.active == true){
                    document.querySelector('#off_subreddit').setAttribute("class", "btn btn-warning");
                    document.querySelector('#on_subreddit').setAttribute("class","btn btn-warning active");
                    document.querySelector('#usersubreddit').placeholder = res.subreddit;
                }
                else if (res.active == false){
                    document.querySelector('#on_subreddit').setAttribute("class", "btn btn-warning");
                    document.querySelector('#off_subreddit').setAttribute("class","btn btn-warning active");
                    document.querySelector('#usersubreddit').placeholder = res.subreddit;               
                }
            }
            else{
                document.querySelector('#off_subreddit').setAttribute("class","btn btn-warning active");
                document.querySelector('#usersubreddit').placeholder = "Enter a subreddit:";               
                              
            }
            
        });
    }

    function insertQuote(motivation){
        var element = document.querySelector('#motivation_example');
        element.innerHTML = motivation;
    }

    window.addEventListener('load', function(){

        checkWeather();
        checkMotivation();
        checkSubreddit();

        document.querySelector('#mot_example').addEventListener('click', function(e){
            api.getQuote(function(err, res){
                console.log(res.content);
                if (err) console.log(err);
                insertQuote(res.content);
            });
            
        });
        
        document.querySelector('#locationform').addEventListener('submit', function(e){
            e.preventDefault();
            submitLocation();
        });

        document.getElementById('off_weather').addEventListener('click', function(){
            api.toggle("weather", "False", function(err, res){
                if (err) console.log(err);
            });
        });

        document.getElementById('on_weather').addEventListener('click', function(){
            api.toggle("weather", "True", function(err, res){
                if (err) console.log(err);
            });
        });

        document.getElementById('off_motivation').addEventListener('click', function(){
            api.toggle("motivation", "False", function(err, res){
                if (err) console.log(err);
            });
        });

        document.querySelector('#subredditform').addEventListener('submit', function(e){
            e.preventDefault();
            submitSubreddit();
        });

        document.getElementById('off_subreddit').addEventListener('click', function(){
            api.toggle("subreddit", "False", function(err, res){
                if (err) console.log(err);
            });
        });

        document.getElementById('on_motivation').addEventListener('click', function(){
            api.toggle("motivation", "True", function(err, res){
                if (err) console.log(err);
            });
        });
      
        document.getElementById('on_subreddit').addEventListener('click', function(){
            api.toggle("subreddit", "True", function(err, res){
                if (err) console.log(err);
            });
        });
    });




}())