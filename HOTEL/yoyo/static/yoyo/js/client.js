var stripe = Stripe(
    "pk_test_51HEuZ4DfnXAAr03AVbCjf29QVPSGwytLtFSqRVkySa7Q5mbUfdwoUsSjFBD6El4aWA2fhJUNSWOZzqRZsWPbvuaZ00EimrQOhb"
);
var elements = stripe.elements();

var clientSecret = document
    .getElementById("card-button")
    .getAttribute("data-secret");

// Custom styling can be passed to options when creating an Element.
var style = {
    base: {
        // Add your base input styles here. For example:
        fontSize: "16px",
        color: "#32325d",
    },
};

var card = elements.create("card", { style: style });
card.mount("#card-element");

card.on("change", ({ error }) => {
    const displayError = document.getElementById("card-errors");
    if (error) {
        displayError.textContent = error.message;
    } else {
        displayError.textContent = "";
    }
});
console.log();

var form = document.getElementById("payment-form");

form.addEventListener("submit", function (ev) {
    var x = document.getElementById("card-name").textContent;
    console.log(x);
    ev.preventDefault();
    stripe
        .confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: "ab2c",
                },
            },
        })
        .then(function (result) {
            if (result.error) {
                // Show error to your customer (e.g., insufficient funds)
                console.log(result.error.message);
            } else {
                // The payment has been processed!
                console.log("success");
                if (result.paymentIntent.status === "succeeded") {
                    console.log("success2");
                    // Show a success message to your customer
                    // There's a risk of the customer closing the window before callback
                    // execution. Set up a webhook or plugin to listen for the
                    // payment_intent.succeeded event that handles any business critical
                    // post-payment actions.
                }
            }
        });
});