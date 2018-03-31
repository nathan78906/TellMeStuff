(function(){
    "use strict";

    // Sets the given location of the user
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
                    checkWeather();
                }
            });
        }
    }

    // Sets the given subreddit of the user
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
                    checkSubreddit();
                }
            });
        }
    }

    // Upon dashboard load, checks the weather active status
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

    // Upon dashboard load, checks the quote active status    
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

    // Upon dashboard load, checks the word of the day active status    
    function checkUrbanDictionary(){
        api.getUrbanDictionary (function(err, res){
            if (err) console.log(err);
            if (res.active != ""){
                if (res.active == true){
                    document.querySelector('#off_urban').setAttribute("class", "btn btn-warning")
                    document.querySelector('#on_urban').setAttribute("class","btn btn-warning active");
                }
                else if (res.active == false){
                    document.querySelector('#on_urban').setAttribute("class", "btn btn-warning")
                    document.querySelector('#off_urban').setAttribute("class","btn btn-warning active");             
                }
            }
            else{
                document.querySelector('#off_urban').setAttribute("class","btn btn-warning active");         
                              
            }
            
        });
    }

    // Upon dashboard load, checks the news active status    
    function checkNews(){
        api.getNews (function(err, res){
            if (err) console.log(err);
            if (res.active != ""){
                if (res.active == true){
                    document.querySelector('#off_news').setAttribute("class", "btn btn-warning")
                    document.querySelector('#on_news').setAttribute("class","btn btn-warning active");
                }
                else if (res.active == false){
                    document.querySelector('#on_news').setAttribute("class", "btn btn-warning")
                    document.querySelector('#off_news').setAttribute("class","btn btn-warning active");             
                }
            }
            else{
                document.querySelector('#off_news').setAttribute("class","btn btn-warning active");         
                              
            }
            
        });
    }

    // Upon dashboard load, checks the photo active status    
    function checkPhoto(){
        api.getPhoto (function(err, res){
            if (err) console.log(err);
            if (res.active != ""){
                if (res.active == true){
                    document.querySelector('#off_photo').setAttribute("class", "btn btn-warning")
                    document.querySelector('#on_photo').setAttribute("class","btn btn-warning active");
                }
                else if (res.active == false){
                    document.querySelector('#on_photo').setAttribute("class", "btn btn-warning")
                    document.querySelector('#off_photo').setAttribute("class","btn btn-warning active");             
                }
            }
            else{
                document.querySelector('#off_photo').setAttribute("class","btn btn-warning active");         
                              
            }
            
        });
    }

    // Upon dashboard load, checks the subreddit active status    
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

    // Checking if the user has any notification platforms set up already
    function checkPlatforms(){
        var profile;
        
        api.getUser(function(err, res){
            if (err) console.log(err);
            profile = res.profile;
            if (!profile){
                document.querySelector('#settings_reminder').style.display = 'block';
            } 
        });
    }

    // Inserts the quote into the example modal
    function insertQuote(motivation){
        var element = document.querySelector('#motivation_example');
        element.innerHTML = motivation;
    }

    // Inserts the word of the day into the example modal    
    function insertUWordOfTheDay(urban){
        var element = document.querySelector('#urbanDictionary_example');
        element.innerHTML = urban;
    }

    // Inserts the subreddit information into the example modal    
    function insertReddit(reddit){
        var element = document.querySelector('#reddit_examplebody');
        element.innerHTML = reddit.replace(/\n/g, "<br>");
    }

    // Inserts the current news into the example modal    
    function insertNews(news){
        var element = document.querySelector('#news_examplebody');
        element.innerHTML = news.replace(/\n/g, "<br>");
    }

    // Inserts a random photo into the example modal    
    function insertPhoto(photo){
        var element = document.querySelector('#photo_examplebody');
        element.innerHTML = `
        <div class="card" style="width: 18rem;">
            <img class="card-img-top" src="${photo.url}" alt="${photo.author}">
            <div class="card-body">
                <p class="card-text">${photo.author}</p>
                <a href="${photo.source}">Photo Source</a>
            </div>
        </div>`;
    }

    window.addEventListener('load', function(){
        
        // Checking active subscriptions status on load
        checkWeather();
        checkMotivation();
        checkSubreddit();
        checkUrbanDictionary();
        checkNews();
        checkPhoto();
        checkPlatforms();

        // Toggle, example and form listeners to call their respective API functions
        document.querySelector('#mot_example').addEventListener('click', function(e){
            api.getQuote(function(err, res){
                if (err) console.log(err);
                insertQuote(res.content);
            });
        });
        
        document.querySelector('#urban_example').addEventListener('click', function(e){
            api.getUWordOfTheDay(function(err, res){
                if (err) console.log(err);
                insertUWordOfTheDay(res.content);
            });
        });

        document.querySelector('#reddit_example').addEventListener('click', function(e){
            api.getRedditExample(function(err, res){
                if (err) console.log(err);
                insertReddit(res.content);
            });
        });

        document.querySelector('#news_example').addEventListener('click', function(e){
            api.getNewsExample(function(err, res){
                if (err) console.log(err);
                insertNews(res.content);
            });
            
        });

        document.querySelector('#photo_example').addEventListener('click', function(e){
            api.getPhotoExample(function(err, res){
                if (err) console.log(err);
                insertPhoto(res);
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
                if (err) {
                    document.querySelector('#on_weather').setAttribute("class", "btn btn-warning");
                    document.querySelector('#off_weather').setAttribute("class","btn btn-warning active");
                    document.querySelector('.location_success').style.display = 'none';                    
                    document.querySelector('.location_error').style.display = 'block';
                    document.querySelector('.location_error').innerHTML = err;
                    
                    
                }
            });
        });

        document.getElementById('off_motivation').addEventListener('click', function(){
            api.toggle("motivation", "False", function(err, res){
                if (err) console.log(err);
            });
        });

        document.getElementById('off_urban').addEventListener('click', function(){
            api.toggle("urban", "False", function(err, res){
                if (err) console.log(err);
            });
        });

        document.getElementById('on_urban').addEventListener('click', function(){
            api.toggle("urban", "True", function(err, res){
                if (err) console.log(err);
            });
        });

        document.getElementById('off_news').addEventListener('click', function(){
            api.toggle("news", "False", function(err, res){
                if (err) console.log(err);
            });
        });

        document.getElementById('on_news').addEventListener('click', function(){
            api.toggle("news", "True", function(err, res){
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
                if (err) {
                    document.querySelector('#on_subreddit').setAttribute("class", "btn btn-warning");
                    document.querySelector('#off_subreddit').setAttribute("class","btn btn-warning active");
                    document.querySelector('.subreddit_success').style.display = 'none';                    
                    document.querySelector('.subreddit_error').style.display = 'block';
                    document.querySelector('.subreddit_error').innerHTML = err;
                }
            });
        });

        document.getElementById('off_photo').addEventListener('click', function(){
            api.toggle("photo", "False", function(err, res){
                if (err) console.log(err);
            });
        });

        document.getElementById('on_photo').addEventListener('click', function(){
            api.toggle("photo", "True", function(err, res){
                if (err) console.log(err);
            });
        });
    });




}())