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

// var drawRect = function(e){
//     var mouseX = e.offsetX;
//     var mouseY = e.offsetY;
//     console.log("mouseclick registered at ", mouseX, mouseY);

// }

// //var drawCircle = function(e) {
// var drawCircle = (e) => {

//     console.log("mouseclick registered at ", mouseX, mouseY);

// }

// //var draw = function(e){
// var draw = (e) => {

// }

// //var wipeCanvas = function() {
// var wipeCanvas = () => {

// }

// c.addEventListener("click", draw);
// var bToggler = document. ;
// bToggler. ;
// var clearB = ;
// clearB. ;

// // HINT: TRY TO PRINT OBJECTs LIKE E

