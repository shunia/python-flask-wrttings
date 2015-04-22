define(['jquery', 'bootstrap'], function ($) {

    var registerd_validators = {
        "email": email_validator, 
        "password": password_validator, 
        "text": text_validator
    };
    var emailRegex;

    $("#login_form").submit(function (e) {
        // iter every submit field for validation
        $(".form-validate-field").each(function (i, vfield) {
            if (!login_form_validation(vfield)) {
                // if validation fails, stop submitting
                e.preventDefault();
                return false;
            }
        });
    });

    function login_form_validation(vfield) {
        var type = $(vfield).attr('type'), 
            validator = registerd_validators[type];

        return validator && validator(vfield);
    };

    function email_validator(vfield) {
        var size = $(vfield).attr('size'), 
            fvalue = $(vfield).val(), 
            valid = false, 
            errtype = 0;
        
        if (size && fvalue && fvalue.length <= size) {
            if (!emailRegex) 
                emailRegex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
            valid = emailRegex.test(fvalue);
        } else {
            errtype = 1;
        }

        if (!valid) 
            make_tooltip(vfield, "right", "Email error!")
        return valid;
    }

    function password_validator(vfield) {

    }

    function text_validator(vfield) {

    }

    function make_tooltip(target, placement, title) {
        $(target).tooltip({
            "placement": placement, 
            "title": title
        });
        $(target).tooltip('show');
        $(target).focus(function () {
            $(this).tooltip('destroy');
        });
    }

})