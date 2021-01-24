var state = {'ball': (683, 384),
 'team1': {'goal_x': 0,
           'players': [{ "id": 0, "pos": (33, 384), "img": "L0" },
                       { "id": 1, "pos": (341, 308), "img": "L0" },
                       { "id": 2, "pos": (341, 460), "img": "L0" },
                       { "id": 3, "pos": (426, 109), "img": "L0" },
                       { "id": 4, "pos": (426, 658), "img": "L0" },
                       { "id": 5, "pos": (683, 308), "img": "L0" },
                       { "id": 6, "pos": (683, 460), "img": "L0" },
                       { "id": 7, "pos": (768, 109), "img": "L0" },
                       { "id": 8, "pos": (768, 658), "img": "L0" },
                       { "id": 9, "pos": (1109, 231), "img": "L0" },
                       { "id": 10, "pos": (1109, 537), "img": "L0" }]},
 'team2': {'goal_x': 1366,
           'players': [{ "id": 0, "pos": (1333, 384), "img": "L0" },
                       { "id": 1, "pos": (1025, 460), "img": "L0" },
                       { "id": 2, "pos": (1025, 308), "img": "L0" },
                       { "id": 3, "pos": (940, 659), "img": "L0" },
                       { "id": 4, "pos": (940, 110), "img": "L0" },
                       { "id": 5, "pos": (656, 576), "img": "L0" },
                       { "id": 6, "pos": (656, 192), "img": "L0" },
                       { "id": 7, "pos": (792, 384), "img": "L0" },
                       { "id": 8, "pos": (520, 384), "img": "L0" },
                       { "id": 9, "pos": (257, 537), "img": "L0" },
                       { "id": 10, "pos": (257, 231), "img": "L0" }]}}


canvas = document.getElementById("canvas");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
var W = canvas.width;
var H = canvas.height;

var ctx = canvas.getContext("2d");

ctx.lineWidth=2;

var BALL_RADIUS=3;

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

function draw_ball(state) {
    "use strict";
    var img = document.getElementById("ball");
    ctx.drawImage(img,50,50);
} 

//function draw_player()

$(document).ready(() => {
    field_draw();
    draw_ball(state);
})
