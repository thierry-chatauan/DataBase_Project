var username = "admin";
var password = "machinery";

function validate() {
    console.log("validate function called");
    var user = document.getElementById("username").value;
    var pass = document.getElementById("password").value;

    if (user === username && pass === password) {
        alert("Login Successful");
        // Redirect to home.html
       window.location.href = "/home"; 
        return false;
    } else {
        alert("Login Failed");
        return false;
    }
}