// Bootstrap carousel - rotate images


var myCarousel = document.querySelector('#mainCarousel');
var carousel = new bootstrap.Carousel(myCarousel, {
    interval: 3000,
    wrap: true
});