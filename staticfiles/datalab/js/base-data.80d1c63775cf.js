$(document).ready(function () {

    $('#li-flex-first-child').addClass('li-flex-hover')

    $('.li-flex').each(function () {
        $(this).click(function () {
            $(this).prevAll('.li-flex').removeClass('li-flex-hover')
            $(this).addClass('li-flex-hover')
            $(this).nextAll('.li-flex').removeClass('li-flex-hover')

        })


    })



})

