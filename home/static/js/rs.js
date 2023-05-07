function regValidate(){
    var name = document.getElementById('name').value;
    var isNumber = hasNumber(name);
    if((name.length<4) || isNumber){
        document.getElementById("alert1").style.display = "block";
        return false;
    }
    var mobile = document.getElementById('mobile').value;
    if((mobile.length!=11) || isNaN(mobile)){
        document.getElementById("alertmobile").style.display = "block";
        return false;
     }
     var email = document.getElementById('email').value;
     var isE = validateEmail(email);
    if(!isE){
        document.getElementById("alertemail").style.display = "block";
        return false;
     }

    var designation = document.getElementById('designation').value;
    isNumber = hasNumber(designation);
    if((designation.length<4) || isNumber){
        document.getElementById("alertdesignation").style.display = "block";
        return false;
    }
    var organization = document.getElementById('organization').value;
    isNumber = hasNumber(organization);
    if((organization.length<4) || isNumber){
        document.getElementById("alertorganization").style.display = "block";
        return false;
    }
    var password = document.getElementById('password').value;
    if((password.length<6)){
        document.getElementById("alertpassword").style.display = "block";
        return false;
    }
    return true;
}

function regValidateupdate(){
    var name = document.getElementById('name').value;
    var isNumber = hasNumber(name);
    if((name.length<4) || isNumber){
        document.getElementById("alert1").style.display = "block";
        return false;
    }
    var mobile = document.getElementById('mobile').value;
    if((mobile.length!=11) || isNaN(mobile)){
        document.getElementById("alertmobile").style.display = "block";
        return false;
     }
     var email = document.getElementById('email').value;
     var isE = validateEmail(email);
    if(!isE){
        document.getElementById("alertemail").style.display = "block";
        return false;
     }

    var designation = document.getElementById('designation').value;
    isNumber = hasNumber(designation);
    if((designation.length<4) || isNumber){
        document.getElementById("alertdesignation").style.display = "block";
        return false;
    }
    var organization = document.getElementById('organization').value;
    isNumber = hasNumber(organization);
    if((organization.length<4) || isNumber){
        document.getElementById("alertorganization").style.display = "block";
        return false;
    }
    var password = document.getElementById('password').value;
    if((password.length<6) && (password.length>0)){
        document.getElementById("alertpassword").style.display = "block";
        return false;
    }
    return true;
}

function hasNumber(myString) {
    return /\d/.test(myString);
  }


function validateEmail(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}

function productValidate(){
    var name = document.getElementById('product_name').value;
    if(name.length<4){
        document.getElementById("alert1").style.display = "block";
        return false;
    }
    

    var organization = document.getElementById('organization').value;
    if(organization.length<4){
        document.getElementById("alertorganization").style.display = "block";
        return false;
    }
    var vendor = document.getElementById('vendor').value;
    if(vendor.length<4){
        document.getElementById("alertvendor").style.display = "block";
        return false;
    }
    var issue_date = document.getElementById('issue_date').value;
    if(!isValidDate(issue_date)){
        document.getElementById("alertdate").style.display = "block";
        return false;
    }
    return true;
}

function isValidDate(d){
    return !isNaN((new Date(d)).getTime());
}
  