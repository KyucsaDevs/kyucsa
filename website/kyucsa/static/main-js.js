$(document).ready(function () {
    let currentStep = 1;
    const stepCount = $('.step').length;

    $('.next-step').click(function (e) {
        e.preventDefault();
        // Validate the current step before proceeding
        if (currentStep === 1) {
            const firstName = $('#firstName').val().trim();
            const lastName = $('#lastName').val().trim();
            const program = $('#sel1').val();
            const gender = $('#sel2').val();

            if (firstName === '' || lastName === '' || program === 'Choose...' || gender === 'Choose...') {
                alert('Please fill out all the fields.');
                return;
            }
        } else if (currentStep === 2) {
            const academicStatus = $('#sel3').val();
            const studentNumber = $('#stdno').val().trim();
            const enrollmentYear = $('#sel4').val();
            const email = $('#email').val().trim();
            const emailRegex = /^[\w-]+(\.[\w-]+)*@gmail\.com$|^[\w-]+(\.[\w-]+)*@std\.kyu\.ac\.ug$/i;

            if (academicStatus === 'Choose...' || studentNumber === '' || enrollmentYear === 'Choose...' || !email.match(emailRegex)) {
                alert('Please fill out all the fields correctly.');
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