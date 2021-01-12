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
    ctx.arc(W/2, H/2, H/10, 0, 2 * Math.PI, false);
    ctx.stroke();
    ctx.closePath();
    ctx.strokeRect(0, 0, W-ctx.lineWidth, H-ctx.lineWidth);
    ctx.strokeRect(0, 0, W-ctx.lineWidth, H-ctx.lineWidth);
}

field_draw();