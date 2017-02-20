# social-facemash

**A Python script that scrapes tagged images from Facebook and LinkedIn, and then identifies & overlays the faces using OpenCV.**

There are a few different Python scripts you can run. One lets you download all the Facebook images you (or your friend) are tagged in. Another lets you download all the LinkedIn profile pictures from your connections.

Once you have a folder of images, you can run "facemash.py", which will identify the face in each picture and then overlay the face on top of each other.

Thanks to these instructions from Leon Eckart: https://github.com/leoneckert/facemash-workshop

##Instructions

**Dependencies**

* Set up a virtual environment.
* Install requisite Python packages. Follow these steps: https://github.com/leoneckert/facemash-workshop#installation-guide-for-basic-requirements
* Download the file you find here and pull into your project folder: https://github.com/biometrics/openbr-models/blob/master/dlib/shape_predictor_68_face_landmarks.dat

**Steps**

* Activate virtual environment. Make sure dependencies are properly installed using pip.
* For the Facebook scraper, run "python facebook.py". For LinkedIn scraper, run "python linkedin.py". Images will download automatically to your project folder.
* Put all the images into a folder called "images".
* For the Facebook tagged photos, you will need to manually go through your images and crop it to just your face (the script unfortunately can't yet pick out your face from a friend's).
* Run the script "python facemash.py images" and a window will pop up with the overlaid face image.
