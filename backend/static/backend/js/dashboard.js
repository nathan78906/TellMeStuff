(function(){
    "use strict";

    function submitLocation(){
        if (document.querySelector('#locationform').checkValidity()){
            var location = document.querySelector("#userlocation").value;
            api.setLocation(location, function(err, res){
                if (err) {
                    document.querySelector('.location_error').style.display = 'block';
                    document.querySelector('.location_error').innerHTML = err;
                }
                else {
                    document.querySelector('.location_success').style.display = 'block';
                    document.querySelector('.location_success').innerHTML = "Successfully submited your location!";
                }
            });
        }
    }

    function checkWeather(){
        api.getWeather (function(err, res){
            if (err) console.log(err);
            if (res.active == true){
                document.querySelector('#off_weather').setAttribute("class", "btn btn-warning")
                document.querySelector('#on_weather').setAttribute("class","btn btn-warning active");
                document.querySelector('#userlocation').placeholder = res.location;
            }
            else if (res.active == false){
                document.querySelector('#on_weather').setAttribute("class", "btn btn-warning")
                document.querySelector('#off_weather').setAttribute("class","btn btn-warning active");
                document.querySelector('#userlocation').placeholder = res.location;               
            }
        });
    }

    window.addEventListener('load', function(){

        checkWeather();
              
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
    });




}())