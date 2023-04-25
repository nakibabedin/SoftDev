/*
DAN: David Chen and Nakib Abedin
SoftDev pd8
k30 -- JS Paint
2023-04-24
Time Spent: 1.0 hr
*/

//retrieve node in DOM via ID
var c = getElementById("slate");

//instantiate a CanvasRenderingCOntext2D object
var ctx = c.getContext("2d");

//init global state var
var mode = "rect";

//var toggleMode = function(e) {
var toggleMode = (e) => {
    console.log("toggling...");
    if(mode == "rect"){
        mode = "circle";
    }else{
        mode = "rect";
    }
}

var drawRect = function(e){
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillRect(mouseX, mouseY, 80, 100);
}

//var drawCircle = function(e) {
var drawCircle = (e) => {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 75, 0, 2 * 3.1415, true);
    ctx.stroke();
    ctx.fill();
}

//var draw = function(e){
var draw = (e) => {
    if(mode == "rect") drawRect();
    else drawCircle();
}

// //var wipeCanvas = function() {
// var wipeCanvas = () => {

// }

// c.addEventListener("click", draw);
// var bToggler = document. ;
// bToggler. ;
// var clearB = ;
// clearB. ;

// // HINT: TRY TO PRINT OBJECTs LIKE E

