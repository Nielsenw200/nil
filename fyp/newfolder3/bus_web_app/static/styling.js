
const menu = document.querySelector ('#mobile-menu')
const menuLinks = document.querySelector('.navbar__menu' )
const alertList = document.querySelectorAll('.alert')
const alerts = [...alertList].map(element => new bootstrap.Alert(element))


//Display for the mobile menu


const mobileMenu = () => {
   
   menu.classList.toggle('is-active')
   menuLinks.classList.toggle('active')

}
menu.addEventListener('click', mobileMenu);





var button = document.querySelector('#submit-button');

braintree.dropin.create({
  authorization: 'sandbox_g42y39zw_348pk9cgf3bgyw2b',
  selector: '#dropin-container'
}, function (err, instance) {
  button.addEventListener('click', function () {
    instance.requestPaymentMethod(function (err, payload) {
      // Submit payload.nonce to your server
    });
  })
});