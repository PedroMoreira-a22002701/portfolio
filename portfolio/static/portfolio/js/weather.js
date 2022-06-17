
function tempo() {
fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/hp-daily-forecast-day0https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/' +
'1110600').then(response => console.log(response.data[0].tMin))
}
tempo()