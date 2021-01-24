/*var state = {
  'W': 1920,
  'H': 1080,
  'ball': [683, 384],
  'team1': {'goal_x': 0,
           'players': [{ "id": 0, "pos": [33, 384], "img": "L0" },
                       { "id": 1, "pos": [341, 308], "img": "L0" },
                       { "id": 2, "pos": [341, 460], "img": "L0" },
                       { "id": 3, "pos": [426, 109], "img": "L0" },
                       { "id": 4, "pos": [426, 658], "img": "L0" },
                       { "id": 5, "pos": [683, 308], "img": "L0" },
                       { "id": 6, "pos": [683, 460], "img": "L0" },
                       { "id": 7, "pos": [768, 109], "img": "L0" },
                       { "id": 8, "pos": [768, 658], "img": "L0" },
                       { "id": 9, "pos": [1109, 231], "img": "L0" },
                       { "id": 10, "pos": [1109, 537], "img": "L0" }]},
 'team2': {'goal_x': 1366,
           'players': [{ "id": 0, "pos": [1333, 384], "img": "L0" },
                       { "id": 1, "pos": [1025, 460], "img": "L0" },
                       { "id": 2, "pos": [1025, 308], "img": "L0" },
                       { "id": 3, "pos": [940, 659], "img": "L0" },
                       { "id": 4, "pos": [940, 110], "img": "L0" },
                       { "id": 5, "pos": [656, 576], "img": "L0" },
                       { "id": 6, "pos": [656, 192], "img": "L0" },
                       { "id": 7, "pos": [792, 384], "img": "L0" },
                       { "id": 8, "pos": [520, 384], "img": "L0" },
                       { "id": 9, "pos": [257, 537], "img": "L0" },
                       { "id": 10, "pos": [257, 231], "img": "L0" }]}};*/

var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

document.addEventListener("keypress", function(event) {
  if(event.keyCode == 87) {
      socket.emit('move', {'name': NAME, 'key': 'w'})
  }
  if(event.keyCode == 81) {
      socket.emit('move', {'name': NAME, 'key': 'q'})
  }
  if(event.keyCode == 69) {
      socket.emit('move', {'name': NAME, 'key': 'e'})
  }
  if(event.keyCode == 65) {
      socket.emit('move', {'name': NAME, 'key': 'a'})
  }
  if(event.keyCode == 68) {
      socket.emit('move', {'name': NAME, 'key': 'd'})
  }
  if(event.keyCode == 90) {
      socket.emit('move', {'name': NAME, 'key': 'z'})
  }
  if(event.keyCode == 88) {
      socket.emit('move', {'name': NAME, 'key': 'x'})
  }
  if(event.keyCode == 67) {
      socket.emit('move', {'name': NAME, 'key': 'c'})
  }
  if(event.keyCode == 38) {
      socket.emit('move', {'name': NAME, 'key': 'up'})
  }
  if(event.keyCode == 39) {
      socket.emit('move', {'name': NAME, 'key': 'right'})
  }
  if(event.keyCode == 40) {
      socket.emit('move', {'name': NAME, 'key': 'down'})
  }
  if(event.keyCode == 37) {
      socket.emit('move', {'name': NAME, 'key': 'left'})
  }
  if(event.keyCode == 32) {
      socket.emit('move', {'name': NAME, 'key': 'space'})
  }
});

socket.on('next', data => {
  state=data['state'];
  draw_ball(state["ball"][0], state["ball"][1], state['W'], state['H']);
  for(i=0;i<11;i++) {
    draw_player(state["team1"]["players"][i]["pos"][0], state["team1"]["players"][i]["pos"][1], state['W'], state['H'], "red");
    draw_player(state["team2"]["players"][i]["pos"][0], state["team2"]["players"][i]["pos"][1], state['H'], state['H'], "blue");
  }
});

// socket.emit('move', {'name': NAME, 'key': k})

canvas = document.getElementById("canvas");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

var W = canvas.width;
var H = canvas.height;

var ctx = canvas.getContext("2d");

ctx.lineWidth=2;

var BALL_RADIUS=3;
var PLAYER_RADIUS=15;

function field_draw() {
    ctx.fillStyle = "green";
    ctx.fillRect(0, 0, W, H);
    ctx.strokeStyle = "white";

    ctx.beginPath();
    ctx.arc(W/2, H/2, H/7, 0, 2 * Math.PI, false); // center circle
    ctx.stroke();
    ctx.closePath();

    ctx.strokeRect(0, 0, W-ctx.lineWidth, H-ctx.lineWidth); // border
    ctx.strokeRect(W/2 - ctx.lineWidth/2, 0, ctx.lineWidth, H) // center line
    ctx.strokeRect(0.9*W - ctx.lineWidth/2, 0.2*H, 0.1*W, 0.6*H) // right penalty area
    ctx.strokeRect(ctx.lineWidth/2,0.2*H, 0.1*W, 0.6*H) // left penalty area
}

function draw_ball(x,y,w,h) {
    // "use strict";
    // var img = document.getElementById("ball");
    // ctx.drawImage(img,5,5);
    console.log("drawing at" + x + " " + y);
    ctx.beginPath();
    ctx.arc(Math.round(x*W/w), Math.round(y*H/h), BALL_RADIUS, 0, 2 * Math.PI, true);
    ctx.stroke();
    ctx.closePath();
    ctx.fillStyle = "black";
    ctx.fill();
}

function draw_player(x,y,w,h,color) {
    ctx.beginPath();
    ctx.rect(Math.round((x-PLAYER_RADIUS)*W/w),Math.round((y-PLAYER_RADIUS)*H/h),2*PLAYER_RADIUS,2*PLAYER_RADIUS);
    ctx.fillStyle=color;
    ctx.fill();
    ctx.closePath();
}

$(document).ready(() => {
    field_draw();
    console.log(state["ball"]);
    draw_ball(state["ball"][0], state["ball"][1], state['W'], state['H']);
    for(i=0;i<11;i++) {
      draw_player(state["team1"]["players"][i]["pos"][0], state["team1"]["players"][i]["pos"][1], state['W'], state['H'], "red");
      draw_player(state["team2"]["players"][i]["pos"][0], state["team2"]["players"][i]["pos"][1], state['H'], state['H'], "blue");
    }
});
