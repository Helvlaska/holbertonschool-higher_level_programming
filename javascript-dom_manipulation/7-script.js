const list_movies = document.getElementById('list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
        data.results.forEach(function (films) {
            const movie = document.createElement('li');
            movie.textContent = films.title;
            list_movies.appendChild(movie);
        });
    });

