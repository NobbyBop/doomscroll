$(document).ready(() =>{
    $("#submit").prop("disabled", true)
    $("#validEmail").val("")
    $("#validPassword").val("")
})
$(document).keyup(() =>{
    if($("#validEmail").val() == "true" &&
        $("#validPassword").val() == "true" 
    ){
        $("#goodToGo").text("Both fields are good")
        $("#submit").prop("disabled", false)
    } else{
        $("#goodToGo").text("Both fields are not.")
        $("#submit").prop("disabled", true)
    }
})

$("#email").keyup(() => {
    let text = $("#email").val().trim()
    if(!(/^[^@]+@[^@]+\.[^@]+$/.test(text))){
        $("#emailFeedback").text("Invalid email.")
        $("#validEmail").val("")
    } else {
        $("#emailFeedback").text("")
        $("#validEmail").val("true")
    }

})

$("#password").keyup(() => {
    let text = $("#password").val().trim()
    console.log(text)
    if (!(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,24}$/.test(text))) {
        $("#passwordFeedback").text("Invalid password.")
        $("#validPassword").val("")
    } else {
        $("#passwordFeedback").text("")
        $("#validPassword").val("true")
    }
})


