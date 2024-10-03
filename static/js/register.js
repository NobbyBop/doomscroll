function isValidPassword(password){
    return /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,24}$/.test(password)
}

function isValidEmail(email){
    return /^[^@]+@[^@]+\.[^@]+$/.test(email)
}

$("#email").on("keyup paste change",() => {
    let email = $("#email").val().trim()
    if(!isValidEmail(email)){
        $("#emailFeedback").text("Invalid email.")
        // $("#validEmail").val("")
    } else {
        $("#emailFeedback").text("")
        // $("#validEmail").val("true")
    }

})
$("#password").on("keyup paste change",() => {
    let text = $("#password").val().trim()
    if (!isValidPassword(text)) {
        $("#passwordFeedback").text("Invalid password.")
        // $("#validPassword").val("")
    } else {
        $("#passwordFeedback").text("")
        // $("#validPassword").val("true")
    }
})
$("#submit").click((event) =>{
    let email = $("#email").val().trim()
    let password = $("#password").val().trim()
    if(!isValidEmail(email) || !isValidPassword(password)){
        event.preventDefault()
        $("#goodToGo").text("Fields are invalid.")
    }
})


