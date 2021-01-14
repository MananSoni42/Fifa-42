canvas = document.getElementById("canvas");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
var W = canvas.width;
var H = canvas.height;

var ctx = canvas.getContext("2d");

ctx.lineWidth=2;

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

field_draw();