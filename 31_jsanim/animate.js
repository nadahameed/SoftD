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

};

var radius = 100;
var growing = true;

var drawDot = () => {
    //clear
    ctx.clearRect(0,0,c.clientWidth,c.clientHeight)

    //repaint the circle
    ctx.beginPath();
    ctx.arc(300, 300, radius, 0, 2 * Math.PI);
    ctx.fill();
    ctx.stroke();

    requestID = window.requestAnimationFrame(requestID);

    while
}

//var stopIt = function
var stopIt = () => {

    window.cancelAnimationFrame(requestID);
}

dotButton.addEventListener( "click", drawDot);
stopButton.addEventListener( "click", stopIt);