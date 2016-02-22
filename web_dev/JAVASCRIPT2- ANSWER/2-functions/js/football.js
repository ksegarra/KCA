var team1 = 'Bengals';
var team2 = 'Steelers';

var touchdown = 6;
var extraPoint = 1;
var twoPointConversion =  2;
var fieldGoal = 3;

//Display team 1 Name
var elTeam1 = document.getElementById('team1Name');
elTeam1.innerHTML = team1;

//Display team 2 Name
var elTeam2 = document.getElementById('team2Name');
elTeam2.innerHTML = team2;

var team1Score = 0;
var team2Score = 0;

//Display team 1 score
var elTeam1Score = document.getElementById('team1Score');
elTeam1Score.innerHTML = team1Score;

//Display team 2 score
var elTeam2Score = document.getElementById('team2Score');
elTeam2Score.innerHTML = team2Score;

var team1Td = function(score){
    if(score == 'td'){
        team1Score = team1Score + touchdown;
    }
    else if(score == 'fg'){
        team1Score = team1Score + fieldGoal;
    }

    elTeam1Score.innerHTML = team1Score;
};

var team2Td = function(){
    team2Score = team2Score + touchdown;
    elTeam2Score.innerHTML = team2Score;
};

