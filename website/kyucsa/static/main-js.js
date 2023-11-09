$('#registrationForm').submit(function (e) {
    e.preventDefault();

    // Serialize form data
    const formData = $(this).serialize();

    // Submit form data using AJAX
    $.ajax({
        url: '/membership/',  // URL mapped to the Django view
        type: 'POST',
        data: formData,
        success: function(response) {
            if (response.error_messages) {
                // Display error messages in a Bootstrap modal
                $('#errorModal .modal-body').html(response.error_messages);
                $('#errorModal').modal('show');
                setTimeout(function(){
                    $('#errorModal').modal('hide');
                }, 5000); // Close modal after 5 seconds
            } else {
                // Display success message in a Bootstrap modal
                $('#myModal .modal-body').html(response.message);
                $('#myModal').modal('show');
                setTimeout(function(){
                    $('#errorModal').modal('hide');
                }, 5000); // Close modal after 5 seconds
            }
        },
        error: function(error) {
            console.log('Error:', error);
        }
    });
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