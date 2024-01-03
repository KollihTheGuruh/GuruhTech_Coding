const countdown = document.getElementById('countdown');
const daysSpan = document.getElementById('days');
const hoursSpan = document.getElementById('hours');
const minutesSpan = document.getElementById('minutes');
const secondsSpan = document.getElementById('seconds');
const fireworksCanvas = document.getElementById('fireworks');
const ctx = fireworksCanvas.getContext('2d');

let countdownDate = new Date('January 1, 2024 00:00:00').getTime();

function updateCountdown() {
    const now = new Date().getTime();
    const distance = countdownDate - now;

    if (distance > 0) {
        // Calculate the time left if the countdown is still going
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        daysSpan.innerHTML = days + 'd ';
        hoursSpan.innerHTML = hours + 'h ';
        minutesSpan.innerHTML = minutes + 'm ';
        secondsSpan.innerHTML = seconds + 's';
    } else {
        // If the countdown has finished, clear the interval, hide the countdown, show the message, and start fireworks
        clearInterval(interval);
        countdown.style.display = 'none'; // Hide the countdown numbers
        displayNewYearMessage();
        showFireworks();
    }
}

let interval = setInterval(updateCountdown, 1000);

class Firework {
    constructor(x, y, color) {
        this.x = x;
        this.y = y;
        this.color = color;
        this.radius = 0;
        this.alpha = 1;
    }

    draw() {
        ctx.save();
        ctx.globalAlpha = this.alpha;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.restore();
    }

    update() {
        this.radius += 2;
        this.alpha -= 0.03;
    }
}

let fireworks = [];

function showFireworks() {
    fireworksCanvas.style.display = 'block';
    animate();
}

function animate() {
    if (fireworks.length < 50) {
        const x = Math.random() * fireworksCanvas.width;
        const y = Math.random() * fireworksCanvas.height;
        const color = 'rgb(' + [Math.floor(Math.random() * 256), Math.floor(Math.random() * 256), Math.floor(Math.random() * 256)].join(',') + ')';
        fireworks.push(new Firework(x, y, color));
    }

    ctx.clearRect(0, 0, fireworksCanvas.width, fireworksCanvas.height);
    fireworks.forEach((firework, index) => {
        firework.update();
        firework.draw();
        if (firework.alpha <= 0) {
            fireworks.splice(index, 1);
        }
    });

    requestAnimationFrame(animate);
}

function displayNewYearMessage() {
    const newYearMessage = document.getElementById('newYearMessage');
    newYearMessage.style.display = 'block'; // Make sure the message is visible
    newYearMessage.innerHTML = 'Happy New Year! From GuruhTech Coding <br>' + new Date().toLocaleString();
}

// Set canvas size
fireworksCanvas.width = window.innerWidth;
fireworksCanvas.height = window.innerHeight;
