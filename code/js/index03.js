fetch('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-03-2020.csv').then(response => response.text()).then(data => console.log(data));
