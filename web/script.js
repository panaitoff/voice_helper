async function display(task) {
        var val = await eel.command(task)();

        document.getElementById("push").innerHTML += '<div class="container darker"><img src="https://img.icons8.com/ios-filled/50/000000/voice-presentation--v2.png" class="right"><p>' + task + '</p><div>';
        document.getElementById("action").value = '';

        document.getElementById("push").innerHTML += '<div class="container white"><img src="https://img.icons8.com/ios-glyphs/30/000000/voice-id.png"<p>' + await eel.speak(val)() + '</p><div>';
}


function startRecognize() {

  	    var rec = new webkitSpeechRecognition();
  	    rec.lang = 'ru';

  	    rec.onresult = async function (e){
            var rez = e.results[e.resultIndex];
            var str = rez[0].transcript;
            var val = await eel.command(str)();
            document.getElementById("push").innerHTML += '<div class="container darker"><img src="https://img.icons8.com/ios-filled/50/000000/voice-presentation--v2.png" class="right"><p>' + str + '</p><div>';
            document.getElementById("push").innerHTML += '<div class="container white"><img src="https://img.icons8.com/ios-glyphs/30/000000/voice-id.png"<p>' + val + '</p><div>';
            console.log(str);
        }
        rec.onend = function() {
             startRecognize()
        }

  	    rec.start();
}


function main_fun() {
    var task = document.getElementById("action").value;
    if (task == '') {
       startRecognize();
       console.log('Начало работы с голосвыми командами: ');
    } else {
        display(task);
        console.log('Начало работы с командами: ');
    }
}