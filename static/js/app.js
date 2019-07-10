//webkitURL is deprecated but nevertheless
URL = window.URL || window.webkitURL;
var AUDIO_EMOTION_JSON;
var AUDIO_EMOTION_float;
var AUDIO_EMOTION_float_moving_LIST;
var AUDIO_EMOTION_float_moving_AVG;
var gumStream; //stream from getUserMedia()
var rec_audio; //Recorder.js object
var input; //MediaStreamAudioSourceNode we'll be recording
var AudioContext = window.AudioContext || window.webkitAudioContext;
var audioContext; //audio context to help us record
var recordButton = document.getElementById("recordButton");
var stopButton = document.getElementById("stopButton");
var EMOTION = document.querySelector("#Emotion-Result");
async function startAudioRecording() {
  var constraints = { audio: true, video: false };
  await navigator.mediaDevices
    .getUserMedia(constraints)
    .then(async function(stream) {
      console.log(
        "getUserMedia() success, stream created, initializing Recorder.js ..."
      );
      audioContext = new AudioContext();
      
      document.getElementById("formats").innerHTML =
        "Format: 1 channel pcm @ " + audioContext.sampleRate / 1000 + "kHz";

      /*  assign to gumStream for later use  */
      gumStream = stream;

      /* use the stream */
      input = audioContext.createMediaStreamSource(stream);

      rec_audio = new Recorder(input, { numChannels: 1 });

      //start the recording process
      await rec_audio.record();
      
      await console.log("Recording started");
      //await console.log(rec);
      
    })
    .catch(function(err) {
      //enable the record button if getUserMedia() fails
      recordButton.disabled = false;
      stopButton.disabled = true;
      
    });
}






async function stopAudioRecording() {
  

  //disable the stop button, enable the record too allow for new recordings
  
  await rec_audio.stop();
  
  //stop microphone access
  await gumStream.getAudioTracks()[0].stop();
  await rec_audio.exportWAV(sendData);
 
 await fetch('/messages')
    .then(res => res.json())
    .then((out) => {
		AUDIO_EMOTION_JSON = out;
    AUDIO_EMOTION_float = parseFloat(AUDIO_EMOTION_JSON);
  }).catch(err => console.error(err));
  EMOTION.textContent = AUDIO_EMOTION_float
 //await console.log(AUDIO_EMOTION_JSON);
}
function sendData(blob) {
  // sends data to flask url /messages as a post with data blob - in format for wav file, hopefully. it is a promise
  
   fetch("/messages", {
    method: "post",
    body: blob
  });

}

function wait(ms){
  var start = new Date().getTime();
  var end = start;
  while(end < start + ms) {
    end = new Date().getTime();
 }
}




Clip_Time = 5000;   // 3000 ms = 3 seconds



setTimeout(async function dummy(){ 
  
  
  dummy1();
}, 0)



async function dummy1(){ 
  await startAudioRecording();//recordButton.click();
  //await wait(1000);
  
  
  setTimeout(dummy2, Clip_Time);
}

async function dummy2(){ 
  
  //await wait(1000);
  
  await stopAudioRecording();//stopButton.click(); 
  
  setTimeout(dummy1, 1000);
}