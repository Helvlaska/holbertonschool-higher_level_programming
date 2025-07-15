document.addEventListener('DOMContentLoaded',
    function () {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            document.getElementById('hello').textContent = data.hello;
        });
    });
