$(document).ready(() => {
    let counter = 0;
    
    setInterval(() => {
        counter++;
        $("#counter").text(String(counter));
    }, 1000);
});