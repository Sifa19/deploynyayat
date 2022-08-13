/*----------------HOME------------------*/
function openNav(){
    document.getElementById("myHome").style.width="300px";
}

function closeNav(){
    document.getElementById("myHome").style.width="0px";
}


/*--------------------------------------ACCOUNT---------------------------------------*/
function register(){
    document.getElementById("RegForm").style.transform = "translateX(0px)";
    document.getElementById("LoginForm").style.transform = "translateX(0px)";
    document.getElementById("Indicator").style.transform = "translateX(55px)";
  }
  
  function login(){
    document.getElementById("RegForm").style.transform = "translateX(400px)";
    document.getElementById("LoginForm").style.transform = "translateX(400px)";
    document.getElementById("Indicator").style.transform = "translateX(-55px)";
    
  }