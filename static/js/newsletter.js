var formEmail = document.getElementById('email_address');

function sendMail() {
    emailjs.init('user_TRwsZUpJla2MRcQgJKZEc');
    emailjs.send("service_vgdcg0c","ms4_email", {
        "to_email": formEmail.value
    }).then(
        function (response) {
            console.log("SUCCESS");
            $("#newsletter-message").replaceWith( "Thanks for subscribing to our mailing list" );
        },
        function (error) {
            console.log("FAILED", error);
        }
    );
    return false;  // To block from loading a new page
}