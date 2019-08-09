'use strict';

$(document).ready(function () {


    $("input:checkbox").on('click', function() {
        let $box = $(this);
        if ($box.is(":checked")) {
            let group = "input:checkbox[name='" + $box.attr("name") + "']";
            $(group).prop("checked", false);
            $box.prop("checked", true);
        } else {
            $box.prop("checked", false);
        }
    });


    const response = $('#response');
    response.hide();

    function beforeSend(data){
        response.show();
        response.text('Loading data...');
        console.log(data)
    }


    function funcError() {
        alert('Oops! Something wrong!');
        return false
    }

    function funcSuccess(data) {
        response.show();
        response.empty();

        if (data.length) {
            response.append('<p>Data loaded</p>');
            response.append(`<p>${JSON.stringify(data)}</p>`);
        }else {
            response.append('<p>No questions!</p>');
        }
    }

    function objectifyForm(formArray) {
        let returnArray = {};
        for (let i = 0; i < formArray.length; i++){
            returnArray[formArray[i]['name']] = formArray[i]['value'];
        }
        return returnArray;
    }

    function submit(){

        let data = objectifyForm($('#myForm').serializeArray());

        const response = $('#response');
        response.hide();

        let cookie = document.cookie;
        let token = cookie.slice(cookie.indexOf('=')+1) ;

        $.ajax({
            url: "/",
            headers: { "X-CSRFToken": token },
            dataType: "json",
            type: "POST",
            data: data,
            beforeSubmit: beforeSend,
            success: funcSuccess,
            error: funcError
        });
    }

    $('#myForm').on('submit', function (event) {
        event.preventDefault();
        submit()
    })
});

