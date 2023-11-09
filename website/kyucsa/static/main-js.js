$(document).ready(function () {
    let currentStep = 1;
    const stepCount = $('.step').length;

    $('.next-step').click(function (e) {
        e.preventDefault();
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
        // Submit the form data using AJAX to Django views
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: $(this).serialize(),
            success: function (response) {
                // Check the response from Django views
                if (response.success) {
                     // If successful, update modal body with the message from views
                     $('#myModal .modal-body').text(response.message);
                     $('#myModal').modal('show');
                     setTimeout(function(){
                         $('#myModal').modal('hide');
                     }, 5000); // Close modal after 5 seconds
                } else {
                    // If there are errors, handle them in Django views and return appropriate response
                    console.log(response.errors); // Log errors for debugging
                    // Optionally, display error messages to the user if needed
                }
            },
            error: function (xhr, errmsg, err) {
                // Handle AJAX errors if any
                console.log(xhr.status + ": " + xhr.responseText); // Log errors for debugging
                // Optionally, display error messages to the user if needed
            }
        });
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