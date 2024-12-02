function proses1() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Hello");
        }, 1000);
    });
}
function proses2(greetings) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(`${greetings} world`);
        }, 1000);
    });
}
function proses3(pesan) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(`${pesan} Have a great day !`);
        }, 1000);
    });
}
// memanggil chainin promises
proses1()
    .than((greetings) => {
    return proses2(greetings);
})
    .than((pesan) => {
    return proses3(pesan);
})
    .than((result) => {
    console.log(result);
})
    .catch((error) => {
    consule.error(`Error: ${error}`);
})