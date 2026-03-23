// Fade-in on scroll
const faders = document.querySelectorAll('.fade-in');

const appearOptions = {
    threshold: 0.3
};

const appearOnScroll = new IntersectionObserver(function(entries, observer) {
    entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
    });
}, appearOptions);

faders.forEach(fader => {
    appearOnScroll.observe(fader);
});


// Image slider
const slider = document.querySelector('.slider');
const images = document.querySelectorAll('.slider img');
let index = 0;

function showSlide(i) {
    index = (i + images.length) % images.length;
    slider.style.transform = `translateX(${-index * 100}%)`;
}

document.querySelector('.next').onclick = () => showSlide(index + 1);
document.querySelector('.prev').onclick = () => showSlide(index - 1);

// Swipe support
let startX = 0;

slider.addEventListener('touchstart', e => {
    startX = e.touches[0].clientX;
});

slider.addEventListener('touchend', e => {
    let endX = e.changedTouches[0].clientX;
    if (startX - endX > 50) showSlide(index + 1);
    if (endX - startX > 50) showSlide(index - 1);
});
