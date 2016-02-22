// Create a variable to hold a random number between 1 and 10
//var randomNum = Math.floor((Math.random() * 10) + 1); //

// Create a variable called el to hold the element whose id attribute has a value of info
var el = document.getElementById('info');

//function for random number within a range
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

var randomNum = getRandomInt(50,100);

// Write the number into that element
el.innerHTML = '<h2>random number</h2><p>' + randomNum + '</p>';