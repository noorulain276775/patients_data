const spinnerbox = document.getElementById('spinner-box')
const alert_box = document.getElementById('alertbox')
const modal_close = document.getElementById('my_modal')

console.log(alert_box)
console.log(spinnerbox)

function spinner() {
    spinnerbox.classList.remove('not-visible')
}

function buttonclose(){ 
    alert_box.classList.add('not-visible'); 

};

function modalshow(){
    $('.ui.modal').modal('show');
}

function modalclose(){
    modal_close.classList.add('not-visible')
}