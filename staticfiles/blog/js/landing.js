$(document).ready(function(){
    // $( "#display-banner-id" ).animate({
    //     // opacity: 0.25,
    //     left: "+=50",
    //     width: '40%',
    //     height: "easyIn"
    //   }, 5000, function() {
    //     // Animation complete.
    //  });

    $('#search-icon').click(function (e) {
        $('#search-box-drop-id').removeClass('no-view')
            $("main").addClass('no-view'); // show/hide the overlay
             $('#search-box-id').focus()

            $('#login-btn-id').addClass('no-view')
            $('#account-logged').addClass('no-view')
            $('#cross-search-id').removeClass('no-view')





    })

    $('#cross-search-id').click(function () {
        $('#search-box-drop-id').addClass('no-view')
         $("main").removeClass('no-view');

         $('#login-btn-id').removeClass('no-view')
                    $('#account-logged').removeClass('no-view')

        $('#cross-search-id').addClass('no-view')
    })


    //Search Ajax Request
    $('#search-box-id').keyup(function (e) {

        let query = $(this).val()

        $.ajax({
                  headers: { "X-CSRFToken": $.cookie("csrftoken") },
                  url: '/ajax/search/',
                  method: 'POST',
                  mode: 'same-origin',
                  data: {
                    'query': query,
                  },

                  beforeSend: function(){
                      $('<h3>').addClass('each-result-para').text('Searching......').appendTo($('#each-result-id'))



                  },

                  success: function (data) {
                        eachSearchResult = $('#each-result-id')
                        eachSearchResult.empty()

                        $.each(data.data, function (index,value) {
                            let searchPara = $("<p>").addClass('each-result-para')
                            $("<a>").text(value[0]).attr('href','http://127.0.0.1:8000/posts/'+value[1]+'/').appendTo(searchPara)
                            searchPara.appendTo($('#each-result-id'))
                        })

                       if((e.keyCode === 8) && (query.length < 1) ){
                                 eachSearchResult.empty()

                       }

                       if(data.data.length === 0){
                           let searchPara = $("<h1>").addClass('each-result-para')
                            searchPara.text('Sorry, no data Found!').appendTo(eachSearchResult)

                       }
                },
        })


    })
//    Search ajax Ends



})



let hamburger = document.querySelector('.hamburger');
let hamburgermobile = document.querySelector('.hamburger-mobile')
let content = document.querySelector('.main');
let search_button = document.querySelector('.search');
let leftmenu = document.querySelector('.leftmenu');
let searchbox = document.querySelector('.search-box');
let profile_modal = document.querySelector('.profile-modal')
let userprofilemobile = document.querySelector('.user-profile-mobile')

hamburger.addEventListener("click", ()=>{
    content.classList.toggle('click_collapse')
});
if (userprofilemobile) {
    userprofilemobile.addEventListener('click', () => {
        profile_modal.classList.toggle('active_display')
    });
}



hamburgermobile.addEventListener("click", ()=>{
    content.classList.toggle('click_collapse')
});





// Login Modal

var modal = document.querySelector('.login-modal')
var modal_signup = document.querySelector('.login-wrapper-signup')
var loginBtn = document.querySelector('.user-login')
var loginBtnMobile = document.querySelector('.user-login-mobile')
var bodyContentWrapper = document.getElementById('contentWrapper')
var closemodal = document.getElementById('closeButton')



var register_el = document.querySelector('.register-link');
var login_el = document.querySelector('.login-link')
var login_wrapper = document.querySelector('.login-wrapper')
var crossBtn = document.querySelector('.close-circle')
var crossBtnRegister = document.querySelector('.close-circle-signup')
var closeNav = document.querySelector('.close-nav')
var signupform = document.querySelector('.login-wrapper-signup')

if (loginBtn){
loginBtn.addEventListener('click', ()=> {
    modal.classList.toggle('login-modal-none');
    login_wrapper.classList.remove('active_display')
    modal_signup.classList.add('active_display')

});
}

if (crossBtn){
crossBtn.addEventListener('click', ()=> {
    modal.classList.add('login-modal-none')
})
}

if (crossBtnRegister) {
    crossBtnRegister.addEventListener('click', () => {
        modal.classList.add('login-modal-none')

    })
}

closeNav.addEventListener('click', ()=> {
    content.classList.remove('click_collapse')

})





loginBtnMobile.addEventListener('click', ()=> {

    modal.classList.toggle('login-modal-none');
    login_wrapper.classList.remove('active_display')
    modal_signup.classList.add('active_display')

});
if (register_el){
    register_el.addEventListener('click', ()=>{
        login_wrapper.classList.toggle('active_display')
        modal_signup.classList.toggle('active_display')

});
}
if (login_el){
login_el.addEventListener('click', ()=>{
    login_wrapper.classList.toggle('active_display')
    modal_signup.classList.toggle('active_display')

});
}



