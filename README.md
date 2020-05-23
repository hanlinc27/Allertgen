# 🥑 Allertgen | DeltaHacks 2020
Allertgen is a web application which detects if an unfamiliar food item has a possibility of containing allergens that a user enters. It determines this through three different methods --> translating and parsing an unfamiliar menu or through a picture of the food item (identified through a image classification model). 

### Tech Stack and How We Built Allertgen
After having planned out the design flow, we sketched out our designs using Figma to build the UI using HTML/CSS. The majority of the back-end of our program was built using __Python__, which facilitated the use of Google Cloud for image classification (including building and training a machine learning model using __Google Cloud's AutoML__), and text detection/translation with Google Cloud's __Vision API__ and Google Cloud's __Translation API__. We also used Google Cloud's App Engine with Flask in order to integrate the Python back-end with the HTML/CSS front-end.
![Figma Landing Page](https://user-images.githubusercontent.com/19617248/73986907-d4644e00-490c-11ea-89e5-512b8ba7a603.png)
![P1](https://user-images.githubusercontent.com/19617248/74207588-3ba43a00-4c4e-11ea-9821-67a674078525.png)
![P2](https://user-images.githubusercontent.com/19617248/74207590-3cd56700-4c4e-11ea-951d-a7e6dc5a92a8.png)
![P3](https://user-images.githubusercontent.com/19617248/74207594-3d6dfd80-4c4e-11ea-8891-3f58a588889a.png)
![P4](https://user-images.githubusercontent.com/19617248/74207595-3e069400-4c4e-11ea-941b-52535ca7c641.png)
![P5](https://user-images.githubusercontent.com/19617248/74207596-3e069400-4c4e-11ea-9dc4-b80d46115e5e.png)
![P6](https://user-images.githubusercontent.com/19617248/74207597-3e9f2a80-4c4e-11ea-9141-54641909d4de.png)
![P7](https://user-images.githubusercontent.com/19617248/74207599-3e9f2a80-4c4e-11ea-925c-fa649e6163da.png)

