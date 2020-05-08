let hamburger = document.querySelector('.hamburger');
let content = document.querySelector('.main');
let search_button = document.querySelector('.search');
let leftmenu = document.querySelector('.leftmenu');
let searchbox = document.querySelector('.search-box');
// let product = document.querySelector('.img-class-product')
// let shop_btn = document.querySelector('.product-shop-btn')


hamburger.addEventListener("click", ()=>{
    content.classList.toggle('click_collapse')
});


search_button.addEventListener("click", ()=>{
   leftmenu.classList.toggle('search-box-display-on-click')
    document.getElementById('searchbox').focus()
})



