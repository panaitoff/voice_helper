var a = ''


async function display(task) {
        var val = await eel.command(task)();

        document.getElementById("push").innerHTML += '<div class="container darker"><img src="https://img.icons8.com/ios-filled/50/000000/voice-presentation--v2.png" class="right"><p>' + task + '</p><div>';
        document.getElementById("action").value = '';

        document.getElementById("push").innerHTML += '<div class="container white"><img src="https://img.icons8.com/ios-glyphs/30/000000/voice-id.png"<p>' + await eel.speak(val)() + '</p><div>';
}


async function startRecognize() {

  	    var rec = new webkitSpeechRecognition();
  	    rec.lang = 'ru';

  	    rec.onresult = async function (e){
  	        var a = '';
            var rez = e.results[e.resultIndex];
            var str = rez[0].transcript;
            a = str
            var val = await eel.command(a)();
            document.getElementById("push").innerHTML += '<div class="container darker"><img src="https://img.icons8.com/ios-filled/50/000000/voice-presentation--v2.png" class="right"><p>' + a + '</p><div>';
            a = ''
            document.getElementById("push").innerHTML += '<div class="container white"><img src="https://img.icons8.com/ios-glyphs/30/000000/voice-id.png"<p>' + val + '</p><div>';
            console.log(a);
        }
        rec.onend = function() {
             startRecognize()
        }

  	    rec.start();
}


function main_fun() {
    var task = document.getElementById("action").value;
    if (task == '') {
       startRecognize()
    } else {
        display(task)
    }
}
