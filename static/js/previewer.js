function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


function pre(){
        $.ajax({
            type: "POST",
            data: { 'content': $('#content').val()},
            url: "/api/markdown_preview/",
            cache: false,
            dataType: "html",
            success: function(result, textStatus) {
                $(".previewer").html($.parseJSON(result).data)
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
            }
        });
}

$(document).ready(function(){
    $(document).keypress(function(e){
        if(e.ctrlKey && e.which==13 || e.which==10)
        {
            $('#submit').click()
        }
    });
    $('#pre-btn').click(
        function(){
           pre();
        });
});
