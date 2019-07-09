//webkitURL is deprecated but nevertheless
URL = window.URL || window.webkitURL;
var AUDIO_EMOTION_JSON;
var AUDIO_EMOTION_float;
var AUDIO_EMOTION_float_moving_LIST;
var AUDIO_EMOTION_float_moving_AVG;
var gumStream; //stream from getUserMedia()
var rec; //Recorder.js object
var input; //MediaStreamAudioSourceNode we'll be recording
var AudioContext = window.AudioContext || window.webkitAudioContext;
var audioContext; //audio context to help us record
var recordButton = document.getElementById("recordButton");
var stopButton = document.getElementById("stopButton");
var EMOTION = document.querySelector("#Emotion-Result");
recordButton.addEventListener("click", startRecording);
stopButton.addEventListener("click", stopRecording);
async function startRecording() {
  console.log("recordButton clicked");
  var constraints = { audio: true, video: false };
  recordButton.disabled = true;
  stopButton.disabled = false;
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

      rec = new Recorder(input, { numChannels: 1 });

      //start the recording process
      await rec.record();
      
      await console.log("Recording started");
      //await console.log(rec);
      
    })
    .catch(function(err) {
      //enable the record button if getUserMedia() fails
      recordButton.disabled = false;
      stopButton.disabled = true;
      
    });
}






async function stopRecording() {
  console.log("stopButton clicked");

  //disable the stop button, enable the record too allow for new recordings
  stopButton.disabled = true;
  recordButton.disabled = false;
  await rec.stop();
  //await console.log(rec.exportWAV);
  //stop microphone access
  await gumStream.getAudioTracks()[0].stop();
  await rec.exportWAV(sendData);
 
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
//recordButton.click();

//window.onload = async function(){
//  await wait(5000);
  //await wait(5000);
  
//  await stopButton.click();
  //await console.log(rec);
  
//}



Clip_Time = 5000;   // 3000 ms = 3 seconds

//getSpeechEmotion();

//getSpeechEmotion();
//recordButton.click();
//wait(100); //
//setTimeout(async function dummy(){ 
  
  //await wait(1000);
  
 // await stopButton.click(); 
 // await wait(1000); // allow  a 1 second delay for emotion analysis
 // await recordButton.click();
 // setTimeout(dummy, Clip_Time);
//}, Clip_Time)

setTimeout(async function dummy(){ 
  
  
  dummy1();
}, 0)



async function dummy1(){ 
  await recordButton.click();
  //await wait(1000);
  
  
  setTimeout(dummy2, Clip_Time);
}

async function dummy2(){ 
  
  //await wait(1000);
  
  await stopButton.click(); 
  
  setTimeout(dummy1, 1000);
}