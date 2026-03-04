function fetchLatestData() {
            fetch('/get_latest')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('last-description').innerText = data.description;
                    document.getElementById('last-date').innerText = data.date;

                    if (data.filename) {
                        const imgElement = document.getElementById('last-image');
                        imgElement.src = '/static/uploads/' + data.filename;
                    }
                })
                .catch(error => console.error('Blad polaczenia: ', error));
                }

setInterval(fetchLatestData, 1000);
fetchLatestData();