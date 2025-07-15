const list = document.querySelector('.my_list');
const add_item = document.getElementById('add_item');

add_item.addEventListener('click',
    function () {
        const item = document.createElement('li');
        item.textContent = 'Item';
        list.appendChild(item);
    }
);
