# Darkflow using android camera
Real-time object detection and classification using Android Camera

See demo below or see on [this imgur](http://i.imgur.com/EyZZKAA.gif)

<p align="center"> <img src="demo.gif"/> </p>


## Dependencies

Python3, tensorflow 1.0, numpy, opencv 3 and IP Webcam APP 

### Getting started

1. Follow Darkflow's instructions [here](https://github.com/thtrieu/darkflow/blob/master/README.md)

2. Install IP Webcam APP [here](https://play.google.com/store/apps/details?id=com.pas.webcam)

3. Move `run.py` file into the `darkflow/` folder

4. After install IP Webcam App, get your IP and port then change the line below into `darkflow/run.py` file:

```
capture = cv2.VideoCapture("rtsp://ip:port/h264_pcm.sdp", cv2.CAP_FFMPEG) 
```

### Run

Inside darkflow folder run:
```
python run.py
```

