var clickbutton = document.createElement('button');
clickbutton.id = 'myButton';
clickbutton.className = 'myButton';
var i = 0;
clickbutton.innerHTML = i;
clickbutton.style.background = '#4fff8f';
document.body.appendChild(clickbutton);
clickbutton.onclick = function() {
    i = ++i;
    clickbutton.innerHTML = i;
};