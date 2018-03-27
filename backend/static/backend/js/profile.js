(function(){
    "use strict";


    function getFacebookUrl(){
        api.getUser(function(err, res){
            if (err) console.log(err);
            var url = "https://m.me/tellmestuff1?ref=" + res.user_id;
            document.querySelector('#fblogin').setAttribute("href", url);      
        });
    }

    function checkPhoneNumber(){
        api.getPhoneNumber(function(err, res){
            if (err) console.log(err);
            if (res.phone_number != null){
                document.querySelector('#phonenum').placeholder = res.phone_number;  
            }
            else{
                document.querySelector('#phonenum').placeholder = "Phone number:";                   
            }
            
        });
    }

    function submitPhoneNumber(){
        if (document.querySelector('#phonenumberform').checkValidity()){
            var phone_number = document.querySelector("#phonenum").value;
            api.setPhoneNumber(phone_number, function(err, res){
                if (err) {
                    document.querySelector('.phonenum_success').style.display = 'none';
                    document.querySelector('.phonenum_error').style.display = 'block';
                    document.querySelector('.phonenum_error').innerHTML = err;
                }
                else {
                    document.querySelector('.phonenum_error').style.display = 'none';
                    document.querySelector('.phonenum_success').style.display = 'block';
                    document.querySelector('.phonenum_success').innerHTML = "Successfully added your phone number!";
                }
            });
        }
    }

    window.addEventListener('load', function(){
        getFacebookUrl();
        checkPhoneNumber();

        document.querySelector('#phonenumberform').addEventListener('submit', function(e){
            e.preventDefault();
            submitPhoneNumber();
        });
    });
}())
