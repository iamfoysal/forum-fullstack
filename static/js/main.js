// message section
const message = document.querySelector('.message');


if (message) {
   setTimeout(() => {
     message.classList.add("message-hide");
   }, 5000);
}

// login and register with js 
function login(){
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    var csrf = document.getElementById('csrf').value
    if(username == '' && password == ''){
        alert('You must enter both')
    }
    var data = {
        'username' : username,
        'password' : password
    }
    fetch('/api/login/' , {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrf,
        },
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        
        if(response.status == 200){
           
            window.location.href = '/'
            
        }
        else{
            alert(response.message)
            
        }
    })
}
function register(){
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    // var userfirstname = document.getElementById('UserFname').value
    // var userlastname = document.getElementById('UserLname').value
    var csrf = document.getElementById('csrf').value

    if( username == '' && password == ''){
        alert('You must enter both')
    }
    var data = {

        // 'first_name': userfirstname,
        // 'last_name': userlastname,
        'username' : username,
        'password' : password
    }

    fetch('/api/register/' , {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrf,
        },

        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        console.log(response)
        if(response.status == 200){
            window.location.href = '/'
        }
        else{
            alert(response.message)
        }

    })

}
