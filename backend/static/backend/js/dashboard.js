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
            if (res.active != ""){
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

    function insertQuote(motivation){
        var element = document.createElement('div');
        element.innerHTML = `
        <div class="modal fade" id="exampleMotivation" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLongTitle">Motivation Example</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
            ${motivation}
            </div>
          </div>
        </div>
    </div>
        `;
        document.querySelector('#motivation_example').prepend(element);
    }

    window.addEventListener('load', function(){

        checkWeather();
        checkMotivation();

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

        document.getElementById('on_motivation').addEventListener('click', function(){
            api.toggle("motivation", "True", function(err, res){
                if (err) console.log(err);
            });
        });
    });




}())