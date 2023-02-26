var canvasWidth = 600;
var canvasHeight = 400;

function startGame() {
    gameCanvas.start();
    let card = new Card('S', 'A');
    card.writeToConsole();
}

var gameCanvas = {
    canvas : document.createElement("canvas"),
    start : function() {
        this.canvas.width = canvasWidth;
        this.canvas.height = canvasHeight;
        this.context = this.canvas.getContext("2d");
        document.body.insertBefore(this.canvas, document.body.childNodes[0]);
    }
}

function update() {
    const canvas = document.getElementById("canvas");
    if (canvas.getContext) {
        const ctx = canvas.getContext("2d");

        ctx.fillStyle = "green";
        ctx.fillRect(0, 0, window.innerWidth, window.innerHeight);
    }
}