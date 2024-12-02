function fetchData(){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const data = "fetched data";
            if (data) {
            resolve(data);
            } else {
            reject("Data Tidak Ada");
            }
        }, 1000);
    })
}
// memanggil promises 
fetchData()
    .then((data) => {
        console.log(data);
    })
    .catch((error) => {
        counsule.error(`Error: Unable to fetch data: ${error}`);
    })