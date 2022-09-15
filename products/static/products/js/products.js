// Back to top icon functionality for products html
$('.btt-link').click(function(e) {
    window.scrollTo(0,0)
})

// Javascript from product.html to sort products
$('#sort-selector').change(function() {
    var selector = $(this);
    var currentUrl = new URL(window.location);

    var selectedVal = selector.val();
    if(selectedVal != "reset"){
        var sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
})

// Javascript from edit and add product html to display image name
$('#new-image').change(function() {
    var file = $('#new-image')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
});