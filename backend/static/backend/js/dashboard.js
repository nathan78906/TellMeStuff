(function(){
    "use strict";

    window.addEventListener('load', function(){
        function submitLocation(){
            if (document.querySelector('#locationform').checkValidity()){
                var location = document.querySelector("#userlocation").value;
                console.log(api);
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


        document.querySelector('#setlocation').addEventListener('click', function(e){
            submitLocation();
        });
        
        document.querySelector('#locationform').addEventListener('submit', function(e){
            e.preventDefault();
        });
    });




}())