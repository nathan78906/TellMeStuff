(function(){
    "use strict";
    
    window.addEventListener('load', function(){
        
        function submit(){
            if (document.querySelector("form").checkValidity()){
                var username = document.querySelector("form [name=username]").value;
                var password = document.querySelector("form [name=password]").value;
                var password_confirm = document.querySelector("form [name=password_confirm]").value;
                var action = document.querySelector("form [name=action]").value;
                
                api[action](username, password, password_confirm, function(err, res){
                    if (err) {
                      document.querySelector('.auth_error').style.display = 'block';
                      document.querySelector('.auth_error').innerHTML = err;
                    }
                    else window.location = '/dashboard/';
                });
            }
        }
        
        document.querySelector('#signup').addEventListener('click', function(e){
            document.querySelector("form [name=action]").value = 'signup';
            submit();
        });
        
        document.querySelector('form').addEventListener('submit', function(e){
            e.preventDefault();
        });
    });
}())


