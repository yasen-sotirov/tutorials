// restart game button
let restart = document.querySelector('#b');

//grads all the squares
let squares = document.querySelectorAll('td');

// clear all the squares
function clearBoard() {
    for (let i=0; i < squares.length; i++) {
        squares[i].textContent = '';
    }
}

restart.addEventListener('click', clearBoard);


// check square markers





// forloop to add event listener0