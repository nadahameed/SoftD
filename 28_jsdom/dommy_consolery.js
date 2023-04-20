/*
- open index.html on FireFox (click on the file and it'll open in the web browser)
- open console 
--> to open console on mac, use option command c


*/

// Team iHeartAI :: Nada Hameed, Erica Li 
// SoftDev pd2
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-05w
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
//to test: console.log(f(x)) with x being any number 
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
//to test name: console.log(o.name)
//to test age: console.log(o.age)
//to test items: console.log(o.items) --> 
//to test morestuff: console.log(o.morestuff)
//to test func: console.log(o.func(x)) with x being any number
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FIB
function fib (n) { 
  if (n <= 1)
      return n; 

  else
      return fib(n-1) + (fib(n-2));
} //into console: console.log(fib(10)); -> 55
// FAC
function fac (n) {
  if (n < 2)
      return 1; 
  else
      return n * (fac (n -1));
} //into console: console.log(fac(10)); -> 3628800
// GCD (from piazza)
function gcd (a, b) {
  if (a % b === 0){
    return b;
  }
  return gcd(b, a%b);
} //into console: console.log(gcd(10,30)); -> 10


// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};


