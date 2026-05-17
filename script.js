// Glow Effect on Buttons
document.querySelectorAll('.link-button').forEach(button => {
    button.addEventListener('mouseenter', () => {
        button.style.textShadow = '0 0 10px rgba(255, 255, 255, 0.9)';
    });
    button.addEventListener('mouseleave', () => {
        button.style.textShadow = '0 0 5px rgba(0, 0, 0, 0.5)';
    });
});

// Easter Egg: Click Logo 3 Times
let clickCount = 0;
document.getElementById('logo').addEventListener('click', () => {
    clickCount++;
    if (clickCount === 3) {
        document.body.style.animation = 'shake 0.5s';
        setTimeout(() => {
            document.body.style.animation = '';
        }, 500);
        clickCount = 0;
    }
});

// Konami Code Easter Egg
const konamiCode = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];
let konamiIndex = 0;

document.addEventListener('keydown', (e) => {
    if (e.key === konamiCode[konamiIndex]) {
        konamiIndex++;
        if (konamiIndex === konamiCode.length) {
            document.body.style.background = 'linear-gradient(135deg, #ff0000, #ffff00, #00ff00, #00ffff, #0000ff, #ff00ff)';
            setTimeout(() => {
                document.body.style.background = 'linear-gradient(135deg, var(--dark-purple) 0%, var(--neon-purple) 50%, var(--light-purple) 100%)';
            }, 3000);
            konamiIndex = 0;
        }
    } else {
        konamiIndex = 0;
    }
});

// Retro Music Player (Hidden)
const music = new Audio('https://assets.mixkit.co/sfx/preview/mixkit-retro-game-notification-212.mp3');
document.addEventListener('keydown', (e) => {
    if (e.key === 'm') {
        music.loop = true;
        music.play();
    }
});