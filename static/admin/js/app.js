const spinnerbox = document.getElementById('spinner-box')
const alert_box = document.getElementById('alertbox')
console.log(alert_box)
console.log(spinnerbox)

function spinner() {
    spinnerbox.classList.remove('not-visible')
}

function buttonclose(){ 
    alert_box.classList.add('not-visible'); 
 };
