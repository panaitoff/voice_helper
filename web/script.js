

async function display() {





        var task = document.getElementById("action").value;
        var val = await eel.command(task)();

        if (task == '') {
            alert( 'Если вы вводите команду через текстовое поле то не оставляйте его пустым' );
        }
        else{
            document.getElementById("push").innerHTML += '<div class="container darker"><img src="https://img.icons8.com/ios-filled/50/000000/voice-presentation--v2.png" class="right"><p>' +
                                                        task +
                                                        '</p><div>';

            document.getElementById("action").value = '';


        }



        document.getElementById("push").innerHTML += '<div class="container white"><img src="https://img.icons8.com/ios-glyphs/30/000000/voice-id.png"<p>' +
                                                                       await eel.speak(val)() +
                                                                       '</p><div>';
}

async function inp() {
    var change = document.getElementById("btn");
    var element = document.getElementById("action");

    if (element.clicked == true)
    {
        change.innerHTML = "push";
    }
    else {
        change.innerHTML = "speak";
    }

}
