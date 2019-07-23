// console.log("Hello World");
//
// var h1tag = document.getElementsByTagName("h1")[0];

var adjectives = ["us", "artistic", "hair"];
var pos = 0;

var loc = document.getElementById("adjective")

function changeAdj(){
  loc.innerHTML = adjectives[pos];
  pos ++;
  if (pos >= adjectives.length){
    pos = 0;
  }
}


Math.random()

var x = document.getElementsByTagName("body")[0]

function colorfulBackground(){
  x.setAttribute("style", `background-color:rgb(${Math.floor(Math.random() * 256)},${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}`)
}
