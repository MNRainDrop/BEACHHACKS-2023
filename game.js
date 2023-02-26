function draw() {
    const canvas = document.getElementById("canvas");
    if (canvas.getContext) {
        const ctx = canvas.getContext("2d");

        ctx.fillStyle = "green";
        ctx.fillRect(0, 0, screen.width, screen.height);
    }
}


