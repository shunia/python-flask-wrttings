define(['jquery', 'bootstrap'], function ($) {

    $(document).ready(function() {
        var isViewing = false;

        function update() {
            if (isViewing) {

            } else {

            }
        }

        $(".form-control").each(update);
    });

})