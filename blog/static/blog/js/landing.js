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
var loginBtn = document.querySelector('.user-login')
var bodyContentWrapper = document.getElementById('contentWrapper')
var closemodal = document.getElementById('closeButton')

loginBtn.addEventListener('click', ()=> {
    console.log(' neoal')
    modal.classList.toggle('login-modal-none');

});

