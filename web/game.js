canvas = document.getElementById("canvas");
canvas.width = screen.width;
canvas.height = screen.height;
var W = canvas.width;
var H = canvas.height;

var ctx = canvas.getContext("2d");

function field_draw() {
    ctx.fillStyle = "green";
    ctx.fillRect(0, 0, W, H);

    ctx.strokeStyle = "white";
    ctx.beginPath();
    ctx.arc(W/2, H/2, H/10, 0, 2 * Math.PI, false);
    ctx.stroke();
    cts.closePath();
}

field_draw();
