# Super Focus
Super Focus is my first Python project, created to learn how to use OpenCV, Twilio, and Tkinter.


## Description
The Super Focus project focuses on detecting eyes in real-time using the computer's camera. It utilizes the OpenCV library and the Haar cascade classifiers for eye and face detection. The project provides functionality to monitor if the user's eyes are detected, indicating that they are paying attention. If the user's eyes are not detected, the project sends a text message notification to remind them to pay attention.



### Dependencies

- OpenCV: Install OpenCV library using the package manager of your choice (pip, conda, etc.).
- Twilio: Install Twilio library using the package manager of your choice (pip, conda, etc.).

### Installing

1. Install the required dependencies:
   - OpenCV: Install OpenCV library using the package manager of your choice (pip, conda, etc.).
   - Twilio: Install Twilio library using the package manager of your choice (pip, conda, etc.).

2. Clone the project repository:
   ```shell
   git clone https://github.com/your-username/eye-detector.git
3. Navigate to the project directory:
    cd Super-Focus
4. Update the Twilio credentials:
    Open the text.py file and replace the account_sid, auth_token, and twilioNumber with your own Twilio credentials.
    Save the file.
4. Run the Gui:
    python gui.py


### Usage

Upon running the Eye Detector project, it will access the computer's camera and start detecting the user's eyes. If the user's eyes are not detected for a certain period, a text message notification will be sent to remind them to pay attention.

The project includes a graphical user interface (GUI) built using the customtkinter library. The GUI allows the user to input their phone number and start the eye detection process.

Enter your phone number in the provided text field.
Click the "Submit" button to proceed.
The application will display the currently texting number.
Click the "Start Focus" button to start the eye detection process.
If the user's eyes are not detected, a text message will be sent to the provided phone number.
To stop the eye detection process, click the "Stop" button.

