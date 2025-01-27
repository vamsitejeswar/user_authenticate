// login in login page
function validate(){
    var emails=document.getElementById('emails').value;
    var pass=document.getElementById('pass').value;
  
    //for email
    if (emails==""){
        document.getElementById('emailids').innerHTML="**please fill the mail id field";
        return false;
    }
    if(emails.indexOf('@')<=0){
        document.getElementById('emailids').innerHTML="**must include '@'";
        return false;
    }
    if ((emails.charAt(emails.length-4)!='.')&&(emails.charAt(emails.length-3)!='.')){
        document.getElementById('emailids').innerHTML="** .Invalid position";
        return false;
    }
    //password
    if (pass == ""){
        document.getElementById("password").innerHTML="**please fill the password field";
        return false;
    }
    if ((pass.length <=5 ) || (pass.length > 20)){
        document.getElementById("password").innerHTML="**password length must be b/w 5 and 20";
        return false;
    }
  }
