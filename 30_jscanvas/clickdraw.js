//Team iHeartAI - Erica and Nada
//SoftDev pd2
//K30 -- canvas based JS drawing
//2023-04-24m

//retrieve node in DOM via ID
var c = document.getElementById("slate")

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init global state var
var mode = "rect";

//var toggleMode = function(e) {
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode == "rect") {
        mode = "circ"
    }
    else {
        mode = "rect"
    }
}

var drawRect = function(e) {
    var mouseX = event.offsetX;
    var mouseY = event.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
}

//var draw = function(e) {
var draw = (e) => {
    console.log("draw")
    if (mode == "rect") {
        drawRect();
    }
    else {
        drawCircle();
    }
}
