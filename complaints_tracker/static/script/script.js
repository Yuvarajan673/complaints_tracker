var icon = document.getElementById('pass-icon')
var icon1 = document.getElementById('pass1-icon')
var icon2 = document.getElementById('pass2-icon')
var pass = document.getElementById('password')
var pass1 = document.getElementById('password1')
var pass2 = document.getElementById('password2')

icon.onclick = function(){
    icon.classList.toggle('fa-eye')
    if(pass.getAttribute('type')=='password'){
        pass.setAttribute('type','text')
    }else{
        pass.setAttribute('type','password')
    }
}


icon1.onclick = function(){
    icon1.classList.toggle('fa-eye')
    if(pass1.getAttribute('type')=='password'){
        pass1.setAttribute('type','text')
    }else{
        pass1.setAttribute('type','password')
    }
}
icon2.onclick = function(){
    icon2.classList.toggle('fa-eye')
    if(pass2.getAttribute('type')=='password'){
        pass2.setAttribute('type','text')
    }else{
        pass2.setAttribute('type','password')
    }
}

