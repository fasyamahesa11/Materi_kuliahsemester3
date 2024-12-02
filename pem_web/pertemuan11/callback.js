function fetchData(callback){
    setTimeout(function(){
        const data = 'fetched data';
        callback(data);
    },5000)
}
fetchData (function(data){
    consule.log(data);
});
// membuat proses 2
console.log("ini proses 2");
