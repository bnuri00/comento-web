const html = document.documentElement;
const canvas = document.getElementById("duck");
const context = canvas.getContext("2d");

const divAnime = document.getElementById('scroll-content');
const absoluteTop = window.pageYOffset + divAnime.getBoundingClientRect().top;



// duck interactive scroll animation
// https://css-tricks.com/lets-make-one-of-those-fancy-scrolling-animations-used-on-apple-product-pages/

const frameCount = 66;
const currentFrame = index => (
  `static/images/duck${index.toString().padStart(4, '0')}.png`
)

const preloadImages = () => {
  for (let i = 1; i < frameCount; i++) {
    const img = new Image();
    img.src = currentFrame(i);
  }
};

const img = new Image()
img.src = currentFrame(1);
canvas.width=960;
canvas.height=540;
img.onload=function(){
  context.drawImage(img, 0, 0);
}

const updateImage = index => {
  img.src = currentFrame(index);
  context.drawImage(img, 0, 0);
}

window.addEventListener('scroll', () => {
    const scrollTop =  html.scrollTop - absoluteTop;
    const maxScrollTop = divAnime.scrollHeight - window.innerHeight;

    const scrollFraction = scrollTop / maxScrollTop;
    const frameIndex = Math.min(
    frameCount - 1,
    Math.ceil(scrollFraction * frameCount)
  );

    if(scrollTop>0)
        requestAnimationFrame(() => updateImage(frameIndex + 1))
});

preloadImages()


//Change Background Color

