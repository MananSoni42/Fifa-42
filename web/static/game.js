const socket = io(location.protocol + '//' + document.domain + ':' + location.port);

canvas = document.getElementById("canvas");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

var W = canvas.width;
var H = canvas.height
FPS = 40

var ctx = canvas.getContext("2d");

ctx.lineWidth=2;

var BALL_RADIUS=3;
var PLAYER_RADIUS=15;

function draw_field(name1, name2) {
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

    // name of player
    ctx.font = "bold 24px verdana, sans-serif ";
    ctx.textAlign = "start";
    ctx.textBaseline = "bottom";
    ctx.fillStyle = "red";
    ctx.fillText(name1, 150, 50);

    ctx.fillStyle = "blue";
    ctx.fillText(name2, W - 150, 50);
}

function draw_ball(x,y,w,h) {
    ctx.beginPath();
    ctx.arc(Math.round(x*W/w), Math.round(y*H/h), BALL_RADIUS, 0, 2 * Math.PI, true);
    ctx.stroke();
    ctx.closePath();
    ctx.fillStyle = "black";
    ctx.fill();
}

function draw_player(x,y,w,h,color) {
    ctx.beginPath();
    ctx.rect(Math.round((x-PLAYER_RADIUS)*W/w),Math.round((y-PLAYER_RADIUS)*H/h),2*PLAYER_RADIUS*W/w,2*PLAYER_RADIUS*H/h);
    ctx.fillStyle=color;
    ctx.fill();
    ctx.closePath();
}

function get_next() {
    console.log('game next sent');
    socket.emit('get_next', {'name': NAME});
}

socket.on('next', data => {
    console.log('game next received')
    state=data['state'];
    console.log(state)
    draw_field(state['name1'], state['name2'])
    for(i=0;i<11;i++) {
        draw_player(state["team1"]["pos"][i][0], state["team1"]["pos"][i][1], state['W'], state['H'], "red");
        draw_player(state["team2"]["pos"][i][0], state["team2"]["pos"][i][1], state['W'], state['H'], "blue");
    }
    draw_ball(state["ball"][0], state["ball"][1], state['W'], state['H']);
});

$(document).ready(() => {
    if (NEXT) {
        console.log('hello next')
        setInterval(get_next, Math.round(1000/FPS));
    }

    document.addEventListener('keydown', function(key) {
      if(event.code == "KeyW") {
          socket.emit('move', {'name': NAME, 'key': 'w'})
      }
      if(event.code == "KeyQ") {
          socket.emit('move', {'name': NAME, 'key': 'q'})
      }
      if(event.code == "KeyE") {
          socket.emit('move', {'name': NAME, 'key': 'e'})
      }
      if(event.code == "KeyA") {
          socket.emit('move', {'name': NAME, 'key': 'a'})
      }
      if(event.code == "KeyD") {
          socket.emit('move', {'name': NAME, 'key': 'd'})
      }
      if(event.code == "KeyZ") {
          socket.emit('move', {'name': NAME, 'key': 'z'})
      }
      if(event.code == "KeyX") {
          socket.emit('move', {'name': NAME, 'key': 'x'})
      }
      if(event.code == "KeyC") {
          socket.emit('move', {'name': NAME, 'key': 'c'})
      }
      if(event.code == "ArrowUp") {
          socket.emit('move', {'name': NAME, 'key': 'up'})
      }
      if(event.code == "ArrowRight") {
          socket.emit('move', {'name': NAME, 'key': 'right'})
      }
      if(event.code == "ArrowDown") {
          socket.emit('move', {'name': NAME, 'key': 'down'})
      }
      if(event.code == "ArrowLeft") {
          socket.emit('move', {'name': NAME, 'key': 'left'})
      }
      if(event.code == "Space") {
          socket.emit('move', {'name': NAME, 'key': 'space'})
      }
    });

});
