function load_content() {
    const content = document.getElementById('content');
    content.style.display = '';
    const contact = document.getElementById('contact');
    contact.setAttribute('class', 'contact active');
    const slide_content = document.getElementById('slide-content');
    slide_content.style.display = 'none';
}

function spinner() {
    const spin = document.getElementById('spin');
    const spin1 = document.getElementById('spin1');
    const frame = document.getElementById('frame');
    setTimeout(function () {
        spin.style.display = 'none';
        spin1.style.display = 'block';
        frame.style.display = '';
    }, 2500);
    setTimeout(function () {
        spin1.style.display = 'none';
    }, 5000);
}

try {
    Typekit.load({async: true});
} catch (e) {
}

$(document).on('submit', '#post-form', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/send',
        data: {
            username: $('#username').val(),
            comp_name: $('#comp_name').val(),
            message: $('#message').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            //alert(data)
        }
    });
    document.getElementById('message').value = ''
});


// Javascript inbuilt templates

$(".messages").animate({scrollTop: $(document).height()}, "fast");
//
$("#profile-img").click(function () {
    $("#status-options").toggleClass("active");
});
//
$(".expand-button").click(function () {
    $("#profile").toggleClass("expanded");
    $("#contacts").toggleClass("expanded");
});
//
$("#status-options ul li").click(function () {
    $("#profile-img").removeClass();
    $("#status-online").removeClass("active");
    $("#status-away").removeClass("active");
    $("#status-busy").removeClass("active");
    $("#status-offline").removeClass("active");
    $(this).addClass("active");

    if ($("#status-online").hasClass("active")) {
        $("#profile-img").addClass("online");
    } else if ($("#status-away").hasClass("active")) {
        $("#profile-img").addClass("away");
    } else if ($("#status-busy").hasClass("active")) {
        $("#profile-img").addClass("busy");
    } else if ($("#status-offline").hasClass("active")) {
        $("#profile-img").addClass("offline");
    } else {
        $("#profile-img").removeClass();
    }
    ;

    $("#status-options").removeClass("active");
});

//                 var docHeight = $(document).height();
//
//                 function newMessage() {
//                     message = $(".message-input input").val();
//                     if ($.trim(message) == '') {
//                         return false;
//                     }
//                     $('<li class="sent">' +
//                         '{% if user.extendedusers.p_pic == '' %}'+
//                             '<img src = "static/profile.png" alt = "" / >'+
//                             '{% else %}'+
//                             '<img src="static/{{ user.extendedusers.p_pic }}" alt="my image" />'+
//                             '{% endif %}' +
//                         '<p class="text-break"> ' +
//                         message +
//                         '</p>' +
//                         '</li>').appendTo($('.messages ul'));
// $('<li class="sent">{% include "profile_image.html" %}<p>' + message + '</p></li>').appendTo($('.messages ul'));
//                     $('.message-input input').val(null);
//                     $('.contact.active .preview').html('<span>You: </span>' + message);
//                     $(".messages").animate({scrollTop: docHeight + 93}, "fast");
//                     docHeight += 93;
//                 };
//
//                 $('.submit').click(function () {
//                     newMessage();
//                 });
//
$(window).on('keydown', function (e) {
    if (e.which == 13) {
        newMessage();
        return false;
    }
});
// #sourceURL=pen.js
