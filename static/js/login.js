define(['jquery', 'bootstrap'], function ($) {

    var registerd_validators = {
        "email": {
            "validator": email_validator, 
            "helper": {
                "errmsg": [
                    "Empty content not allowed!", 
                    "Invalid email address!"
                ]
            }
        }, 
        "password": {
            "validator": password_validator, 
            "helper": {}
        }, 
        "text": {
            "validator": text_validator, 
            "helper": {}
        }
    };
    var emailRegex;

    $("#login_form").submit(function (e) {
        return true;
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
            v = registerd_validators[type];

        return v.validator && v.validator(vfield, v.helper);
    };

    function email_validator(vfield, helper) {
        var size = $(vfield).attr('size'), 
            fvalue = $(vfield).val(), 
            valid = false, 
            errtype = -1;
        
        if (size && fvalue && fvalue.length <= size) {
            if (!emailRegex) 
                emailRegex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
            valid = emailRegex.test(fvalue);
        } else {
            errtype = 0;
        }
        
        if (!valid) {
            errtype = 1;
            make_tooltip(vfield, "right", helper.errmsg[errtype]);
        }
        return valid;
    }

    function password_validator(vfield, helper) {

    }

    function text_validator(vfield, helper) {

    }

    function make_tooltip(target, placement, title) {
        $(target).addClass('has-warning');
        $(target).tooltip({
            "container": "body", 
            "placement": placement, 
            "title": title
        });
        $(target).tooltip('show');
        $(target).focus(function () {
            $(this).tooltip('destroy');
        });
    }

})