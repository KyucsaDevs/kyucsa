$(document).ready(function () {
    let currentStep = 1;
    const stepCount = $('.step').length;

    $('.next-step').click(function (e) {
        e.preventDefault();

        // Validate the current step before proceeding
        if (currentStep === 1) {
            const name = $('#name').val();
            if (name === '') {
                alert('Please enter your name.');
                return;
            }
        } else if (currentStep === 2) {
            const email = $('#email').val();
            if (email === '') {
                alert('Please enter your email.');
                return;
            }
        }

        // Proceed to the next step
        if (currentStep < stepCount) {
            $(`.step[data-step="${currentStep}"]`).removeClass('active');
            currentStep++;
            $(`.step[data-step="${currentStep}"]`).addClass('active');
            updateProgressBar();
        }
    });

    $('.prev-step').click(function (e) {
        e.preventDefault();
        if (currentStep > 1) {
            $(`.step[data-step="${currentStep}"]`).removeClass('active');
            currentStep--;
            $(`.step[data-step="${currentStep}"]`).addClass('active');
            updateProgressBar();
        }
    });

    $('#registrationForm').submit(function (e) {
        e.preventDefault();
        // Form submission logic here
        alert('Form submitted successfully!');
    });

    function updateProgressBar() {
        const progressValue = Math.round((currentStep / stepCount) * 100);
        $('.progress-bar').css('width', progressValue + '%').attr('aria-valuenow', progressValue).text(progressValue + '%');
    }
});

//Owl-Carousal Script
$(document).ready(function () {
    $('.partners-carousel').owlCarousel({
        autoplay: true,
        loop: true,
        margin: 15,
        dots: false,
        slideTransition: 'linear',
        autoplayTimeout: 4500,
        autoplayHoverPause: true,
        autoplaySpeed: 4500,
        responsive: {
            0: {
                items: 2
            },
            500: {
                items: 3
            },
            600: {
                items: 4
            },
            800: {
                items: 4
            },
            1200: {
                items: 4
            }

        }
    });
});