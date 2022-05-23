/* Code written with the help of the official 
EmailJS tuttorial https://www.emailjs.com/docs/tutorial/creating-contact-form/ */

function sendMail(contactForm) {
    emailjs.init('user_TRwsZUpJla2MRcQgJKZEc');
    emailjs.send("service_vgdcg0c","ms4_email", {
        "to_email": contactForm.email_address.value
    }).then(
        function (response) {
            console.log("SUCCESS");
            $("#mailing-list").replaceWith( "Thanks for subscribing to our mailing list!" );
        },
        function (error) {
            console.log("FAILED", error);
        }
    );
    return false;  // To block from loading a new page
}