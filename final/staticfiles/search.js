document.addEventListener('DOMContentLoaded', function(){
    const Rows = document.querySelectorAll('.song-row');

    Rows.forEach((row) => {
        row.addEventListener('mouseenter', () => {
            row.style.overflowX = 'auto';
        });

        row.addEventListener('mouseleave', () => {
            row.style.overflowX = 'hidden';
        });
    });
} )


document.getElementById('searchInput').addEventListener('keyup', function (event) {

    const search = event.target.value;
    tunes(search);

});

function tunes(term) {
const url = `https://itunes.apple.com/search?term=${term}&media=music&entity=song&limit=100`;

fetch(url)
    .then(response => response.json())
    .then(data => {
        const results = document.getElementById('results');
        results.innerHTML = '';
        data.results.forEach(song => {
            const songname = song.trackName;
            const songele = document.createElement('div');
            songele.innerHTML = `<p >${songname} </p>`;
            results.appendChild(songele);



        });
    })
    .catch(error => console.error('Error ', error));
}
