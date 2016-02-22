var msg;        // Message
var level = 'hi';  // Level

// Determine message based on level
switch (level) {
case 'hi':
    msg = 'Good luck on the first test';
    break;

case 'hello':
    msg = 'Second of three - keep going!';
    break;

case 'goodbye':
    msg = 'Final round, almost there!';
    break;

default:
    msg = 'Good luck!';
    break;
}

var el = document.getElementById('answer');
el.textContent = msg;