# ML_Exploit_Image_App
Flask app to demonstrate methods of exploiting h5 convolutional image detection model (using scenery deep learning model as an example)

Video demonstration: https://youtu.be/tcCorJ6UWIc

- includes server side template injection vulnerability to perform remote code execution and gain reverse shell to exploit and replace convolutional neural network model
- deep learning model includes mitigations against bias manipulation and backdooring, using sanitisation and hash verification. 


## cnn model 

![image](https://user-images.githubusercontent.com/85758021/184241197-8f110336-65f2-40d5-a1f3-492fc9904e07.png)
<br>
![image](https://user-images.githubusercontent.com/85758021/184241224-af022fdb-bf40-48de-b046-f6fd7759f3b4.png)
<br>
![image](https://user-images.githubusercontent.com/85758021/184241247-ee8fde51-b9fc-4646-bd7b-7b2a875e0cad.png)
<br>
![image](https://user-images.githubusercontent.com/85758021/184241267-5b59ac28-e08f-4b8b-9fbf-d8452ae32584.png)


## flask application

![image](https://user-images.githubusercontent.com/85758021/184241298-aebae7f0-fb59-4558-beed-0f9012bc4a43.png)
