// hello world in node js
console.log("hello world");
console.log(this);

//values and datatypes

// - primitive data types

// - number: 2,3,4,4.5,24
// - string: "pw skills" or 'pw skills'
// - Boolean: true, false
// - null
//- undefined

//let a; // it is undefined

// - Non primitive data types
// - Array

let name1 = "mohit";
let name2 = "rohit";
let name3 = "sohit";
let name4 = "hohit";
let name5 = "kohit";

let names = ["mohit", "rohit", "sohit", "hohit", "kohit", 2, 3, false];
console.log(names);

// - object: {}

let myName = "hitesh";

myName = "mohit kumar"; // the value we decleare by let can be changed but the value decleared by const cannot be changed.

// - Assignment operators
let highScore = 300;
console.log(highScore);

let pwSkillsCoursePrice = 3500;
console.log(pwSkillsCoursePrice);

let userBankBAlance = 500;
console.log(userBankBAlance);

pwSkillsCoursePrice = 2000;
console.log(pwSkillsCoursePrice);

let pwCoursePrice = 200;
let gstOnCourse = 36;
let finalPurchaseAmount = pwCoursePrice + gstOnCourse;
console.log("final amount to be paid", finalPurchaseAmount);

let pwDsaCourse = 500;
console.log("final price pf DSA course:", pwDsaCourse + gstOnCourse);

console.log("answer is:", 5 % 2);
console.log("answer is:", 5 / 2);
console.log("answer is:", 3 ** 2); // ** it is used for power

let hiteshHighScore = 200;
let rajuScore = 300;
//let rajuScore = "300"
//console.log(hiteshHighScore == rajuScore); // - == it isused as assignment operator
//console.log(hiteshHighScore === rajuScore); // - === is used to check the type then compare
// console.log(hiteshHighScore >= rajuScore);
// console.log(hiteshHighScore <= rajuScore);
// console.log(hiteshHighScore != rajuScore);

let value1 = true;
let value2 = false;
let value3 = true;
let value4 = false;

console.log(value1 && value3); // - In And operator both value should be true then only it returns true value

let isLoggedIn = true;
let carDetails = true;

let gmailAccount = true;
let emailAccount = false;
console.log(gmailAccount || emailAccount); // - In or operatoronly any of the one statement should be true

