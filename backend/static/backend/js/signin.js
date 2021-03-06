(function(){
    "use strict";
    
    window.addEventListener('load', function(){
        
        function submit(){
            if (document.querySelector("form").checkValidity()){
                var username = document.querySelector("form [name=username]").value;
                var password = document.querySelector("form [name=password]").value;
                var action =document.querySelector("form [name=action]").value;
                
                api[action](username, password, function(err, res){
                    if (err) {
                      document.querySelector('.auth_error').style.display = 'block';
                      document.querySelector('.auth_error').innerHTML = err;
                    }
                    else window.location = "/dashboard/";
                });
            }
        }
        
        document.querySelector('#signin').addEventListener('click', function(e){
            document.querySelector("form [name=action]").value = 'signin';
            submit();
        });
        
        document.querySelector('form').addEventListener('submit', function(e){
            e.preventDefault();
        });
    });
}())


