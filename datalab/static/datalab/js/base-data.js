$(document).ready(function () {

    $('#li-flex-first-child').addClass('li-flex-hover')

    $('.li-flex').each(function () {
        $(this).click(function () {
            $(this).prevAll('.li-flex').removeClass('li-flex-hover')
            $(this).addClass('li-flex-hover')
            $(this).nextAll('.li-flex').removeClass('li-flex-hover')

        })


    })


    $('#add-post-wrap-id').click(function () {
        $('#body-wrap-id').css('opacity', '0.09')
        $('#left-sticky-id').css('opacity', '0.09')
        $('body').css('overflow-y','hidden')
        $('#add-post-form-wrap-id').show()
        $('#content-area').focus()
        if ($(this).val().length === 0) {
            $('#post-post-btn').attr('disabled', true)
        }

    })


    $(document).on('click', '.view-code-snip', function (e) {
        $(this).addClass('no-view')
            $(this).next('.hide-code-snip').removeClass('no-view')

            let post_body = $(this).parent().prevAll('.post-body-text').children('.content-code-wrap').children('.post-code-text').show()


    })



    $(document).on('click', '.hide-code-snip', function (e) {
            $(this).addClass('no-view')

            $(this).prev('.view-code-snip').removeClass('no-view')

            let post_body = $(this).parent().prevAll('.post-body-text').children('.content-code-wrap').children('.post-code-text').hide()

    })




    $('#cross-btn').click(function () {
        $('#add-post-form-wrap-id').hide()
        $('#body-wrap-id').css('opacity', '1')
        $('#left-sticky-id').css('opacity', '1')
        $('#code-area').addClass('no-view')
        $('body').css('overflow','scroll')




    })


    $('#code-snip-btn-id').click(function () {
        $('#code-area').removeClass('no-view').focus()


    })


    $('#content-area').keyup(function () {
        if ($(this).val().length > 0) {
            $('#post-post-btn').attr('disabled', false)
        }

        if ($(this).val().length === 0) {
            $('#post-post-btn').attr('disabled', true)
        }


    })

    $('#post-post-btn').click(function (event) {

        postForm = $('#post-submit-form')
        event.preventDefault()

        let endPoint = postForm.attr('action')
        let httpMethod = postForm.attr('method')
        let formData = postForm.serialize();


        $.ajax({
            headers: { "X-CSRFToken": $.cookie("csrftoken") },
            url: endPoint,
            method: httpMethod,
            data: formData,
            mode: 'same-origin',

            beforeSend: function () {
                $('#post-post-btn').text('posting.....')




            },

            success: function (data) {
                console.log(data.messages)
                $('#content-area').val('')
                $('#code-area').val('').addClass('no-view')
                $('#post-post-btn').text('Post')
                $('#body-wrap-id').css('opacity', '1')
                $('#left-sticky-id').css('opacity', '1')
                $('body').css('overflow-y','scroll')


                $('#add-post-form-wrap-id').hide()


                $('#body-wrap-id').load(location.href + " #body-wrap-id > * ", "");
            },
            //
            // error: function(errorData){
            //     console.log("errorloss")
            //
            //     console.log(errorData.form_error_message)
            // }



        })




    })


    $(document).on('click', '.post-comment-btn', function () {
        let comment_input_wrapper = $(this).parent().parent().parent().next()
        comment_input_wrapper.toggleClass('no-view')
        comment_input_wrapper.children().children('.comment-form').children('.input-des').focus()

        comment_display_wrapper = comment_input_wrapper.next()
        comment_display_wrapper.toggleClass('no-view')




        let postId = $(this).attr('value')
        let endPoint = 'post/get-comments/'
        let httpMethod = 'get'
        if($(this).parent().parent().parent().next().hasClass('no-view')){
            comment_display_wrapper.children().remove()


        }
        else{

            $.ajax({
                    url: endPoint,
                    method: httpMethod,
                    data: {
                        'postId': postId

                    },
                    mode: 'same-origin',


                    beforeSend: function () {
                        eachComment = $('#user-disp-wrap-id').clone()
                        eachComment.removeClass('no-view')
                        eachComment.find('.comment-each').children('p').empty().append('Loading......')




                    },


                    success: function (data) {

                        $.each(data.comments, function(index, element) {
                            eachComment = $('#user-disp-wrap-id').clone()
                            eachComment.removeClass('no-view')
                            eachComment.find('.comment-each').children('p').empty().append(element.comment)
                            comment_display_wrapper.append(eachComment)

                        });








                    }




                })


        }







    })


    $(document).on('keypress', '.input-des', function (e) {

        if(e.keyCode === 13){
            let commentForm = $(this).parent()

            let endPoint = commentForm.attr('action')
            let httpMethod = commentForm.attr('method')
            let postId = commentForm.attr('data-post-type')

            let formData = commentForm.serialize() + '&postid=' + postId;

            if($(this).val().trim().length > 0){

                $.ajax({
                    headers: { "X-CSRFToken": $.cookie("csrftoken") },
                    url: endPoint,
                    method: httpMethod,
                    data: formData,
                    mode: 'same-origin',

                    beforeSend: function () {






                    },

                    success: function (data,) {
                        commentForm.children('.input-des').val('').focus()





                    },
                    //
                    // error: function(errorData){
                    //     console.log("errorloss")
                    //
                    //     console.log(errorData.form_error_message)
                    // }



        })



            }





        }


    })

})




