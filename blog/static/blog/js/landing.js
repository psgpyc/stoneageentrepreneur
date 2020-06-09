let hamburger = document.querySelector('.hamburger');
let hamburgermobile = document.querySelector('.hamburger-mobile')
let content = document.querySelector('.main');
let search_button = document.querySelector('.search');
let leftmenu = document.querySelector('.leftmenu');
let searchbox = document.querySelector('.search-box');


hamburger.addEventListener("click", ()=>{
    content.classList.toggle('click_collapse')
});


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
var bodyContentWrapper = document.getElementById('contentWrapper')
var closemodal = document.getElementById('closeButton')



var register_el = document.querySelector('.register-link');
var login_el = document.querySelector('.login-link')
var login_wrapper = document.querySelector('.login-wrapper')


loginBtn.addEventListener('click', ()=> {
    modal.classList.toggle('login-modal-none');
    login_wrapper.classList.remove('active_display')
    modal_signup.classList.add('active_display')

});

register_el.addEventListener('click', ()=>{
    login_wrapper.classList.toggle('active_display')
    modal_signup.classList.toggle('active_display')
    console.log('help me');

})

login_el.addEventListener('click', ()=>{
    login_wrapper.classList.toggle('active_display')
    modal_signup.classList.toggle('active_display')
    console.log('help me');

})