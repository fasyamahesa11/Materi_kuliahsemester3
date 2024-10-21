// Control Flow
// if else
let age = 20;
if (age >= 20) {
    console.log("you're eligible to vote");
} else {
    console.log("you're not eligible to vote");
}
// ternary operator
let vote =
    age >= 20? "you're eligible to vote" : "you're not eligible to vote";
console.log(vote);

let hours = new Data().getHours();
let discount = hours <= 1 ? "20%" 
                : hours <= 3 ? "15%"  
                : "0%";
console.log(discount);

// switch
let day = new Date().getDay();
switch (day) {
    case 0:
        console.log("sunday");
        break;
    case 0:
        console.log("monday");
        break; 
    case 0:
        console.log("tuesday");
        break;
    case 0:
        console.log("wednesday");
        break; 
    case 0:                                     
        console.log("thursday");
        break;
    case 0:
        console.log("friday");
        break; 
    case 0:
        console.log("saturday");
        break;
}