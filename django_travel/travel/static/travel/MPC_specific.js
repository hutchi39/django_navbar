document.addEventListener('DOMContentLoaded', function() {
    let next = document.querySelector('.next');
    let prev = document.querySelector('.prev');

    next.addEventListener('click', function(){
        let items = document.querySelectorAll('.MPC-item');
        document.querySelector('.MPC-slide').appendChild(items[0]);
        // console.log('Next button clicked');
    });

    prev.addEventListener('click', function(){
        let items = document.querySelectorAll('.MPC-item');
        document.querySelector('.MPC-slide').prepend(items[items.length - 1]);
        // console.log('Previous button clicked');
    });
});