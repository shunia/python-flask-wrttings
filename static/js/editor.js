define(['jquery'], function ($) {

    var elm = $(".editor-user-input");
    if (elm) {
        $(window).resize(function () {
            $(elm).height(1000);
        });
    }

})
