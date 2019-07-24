console.log("Hello World!")


// LOOPS
// var i = 0;
// for (i = 0; i <= 20; i+= 2) {
//   console.log(i);
// }
//
// i = 0
// while (i <= 20){
//   console.log(i);
//   i += 2
// }
//
// i = 0
// while (i <= 20) {
//   if (i % 2 == 0){
//     console.log(i);
//   }
//   i += 1;
// }

// var fontz= ["'Bonbon', cursive;" "'Butcherman', cursive;" "'Bungee Outline', cursive;" "'Butterfly Kids', cursive;"];
//
// var foz= document.getElementById("fontz")
// var poz= 0;
//
// function fontChange(){
//   foz.setAttribute("style", `font-family;${fontz[poz]}`);
//   poz ++;
//   if (poz >= fonts.length){
//     poz = 0;
//   }
// }


// Math.random()
//
// var x = document.getElementsByTagName("body")[0]
//
// function changeFontz(){
//   x.setAttribute("style", `font-family:rgb(${Math.floor(Math.random() * 256)},${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}`)
// }


//
// function getTemp(){
//   return 22.5;
// }
//
// var temperature = getTemp();
// console.log(temperature);
//
// function getTemp2(type){
//   if (type == "c"){
//     alert("It is hot today")
//     return 22.5;
//   }
//   if (type == "f"){
//     alert("It is rainy today")
//     return 100;
//   }
// }
//
// console.log(getTemp2("f"))
// console.log(getTemp2("c"))


document.getElementById("specialfont").addEventListener("click",
  function (){
    document.getElementById("specialfont").style.color = "red";
  }
)

document.getElementById
