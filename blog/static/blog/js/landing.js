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



search_button.addEventListener("click", ()=>{
   leftmenu.classList.toggle('search-box-display-on-click')
    document.getElementById('searchbox').focus()
})



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


// Ajax

// $(document).ready(function() {
//     let loginForm = $('#login-form');
//     loginForm.submit(function(event){
//         event.preventDefault();
//         console.log('default prevented')
//     })
//
//
// });