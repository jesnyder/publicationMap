urlGit = 'https://raw.githubusercontent.com/jesnyder/publicationMap/main/dfMonthly/month72.csv'
//url = 'https://drive.google.com/file/d/1Xjsm_mhlm1qsnNwL9QJE3EE1_Wne86tR/view?usp=sharing'
//url = 'https://data.cdc.gov/resource/w9j2-ggv5.csv'



function fetchCSV(){
    var corsProxy = "https://cors-anywhere.herokuapp.com/"; //having CORS issues so using a cors proxy currently
    var url = urlGit;
    return fetch(corsProxy + url)
       .then((responseObj)=>{
          return responseObj.text();
       });
    return true;  // Will respond asynchronously.
}

console.log(fetchCSV()); //returns a promise object with resolve value that contains entire github webpage html
