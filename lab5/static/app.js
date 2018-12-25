function getRq(url, callback, error) {
    console.log("Requesting url " + url);
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState === 4) {
            if (xmlHttp.status === 200) {
                callback(xmlHttp.responseText);
            } else {
                error(xmlHttp.status, xmlHttp.responseText)
            }
        }
    };
    xmlHttp.open("GET", url, true); // true for asynchronous
    xmlHttp.send(null);
}

function getGuessResult(objectIdForId, objectIdForName, objectIdForResult) {
    document.getElementById(objectIdForResult).innerHTML = "loading";
    var id = document.getElementById(objectIdForId).innerHTML;
    var name = document.getElementById(objectIdForName).value;
    getRq("/guess/" + id + "/" + name,
        function (s) {
            document.getElementById(objectIdForResult).innerHTML = s;
        },
        function (err, s) {
            document.getElementById(objectIdForResult).innerHTML = "Error " + err;
        });
}

function myFunction() {
  // Get the snackbar DIV
  var x = document.getElementById("snackbar");

  // Add the "show" class to DIV
  x.className = "show";

  // After 3 seconds, remove the show class from DIV
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}