// - variable and values (Number, String, Boolean)
// - Operators

// - Condition and Loops

// let age = 19

// if(age >= 18){
//     console.log("you are allowed")
// }
// else{
//     console.log("you are not allowed")
// }

let signal = "red";

if (signal == "red") {
  console.log("red => STOP");
} // condition 1
else if (signal == "yellow") {
  console.log("yellow => Go slow");
} // condition 2
else {
  console.log("green => Go fast");
} //last condition

// Switch case
let user = "student";

switch (user) {
  case "admin":
    console.log("He is Admin");
    break;

  case "student":
    console.log("He is Student");
    break;

  case "mentor":
    console.log("he is mentor");
    break;

  default:
    console.log("I am default");
}

// Loops
// do-while, while, for

// For loops
// for takes three things initalizor,condition and increment
for(let i=0; i<5; i++){
    console.log(i);
}

// While Loop
//let i = 4;
// while (i>5){
//     console.log(i);
//     i++;
// }

// Do-while
let i=0;
do{
    console.log("hello world");
    i++;
}
while (i<5);

// Teernary operator/ Ternary Condition
// condition ? TRUE:False
// it is also loosely typed means it does not need any data types to run
isloggedin = true;
isloggedin ? console.log("HOME PAGE") : console.log("loginpage")