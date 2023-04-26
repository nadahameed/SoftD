//heading

var c = document.getElementById("playground");
//get dot button
var dotButton = document.getElementById("buttonCircle");
//stop button
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = '#ff0000';

//global var for use with animation frames
var requestID;

var clear = (e) => {
    ctx.clearRect(0,0,500,500);
};

var radius = 0;
var growing = true;

var drawDot = () => {

    window.cancelAnimationFrame(requestID);
    
    //ctx.clearRect(0,0,c.clientWidth,c.clientHeight)
    //or clear method
    clear();

    //repaint the circle
    ctx.beginPath();
    ctx.arc(250, 250, radius, 0, 2 * Math.PI);
    ctx.fill();

    if(growing) {
        if (radius < 100) {
            //grow
            radius = radius + 2;
        }
        else {
            growing = false;
        }
    }
    else {
        if (radius > 0) {
            //shrink
            radius = radius - 2;
        }
        else {
            growing = true;
        }
    }

    requestID = window.requestAnimationFrame(drawDot);
}

//var stopIt = function
var stopIt = () => {
    window.cancelAnimationFrame(requestID);
}

dotButton.addEventListener( "click", drawDot);
stopButton.addEventListener( "click", stopIt);