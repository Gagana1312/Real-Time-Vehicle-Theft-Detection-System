# Real-Time-Vehicle-Theft-Detection-System
Final Year Project
This project is an IoT-based security system designed to monitor and alert for unauthorized access or hazardous conditions using a Raspberry Pi. It utilizes various sensors, a camera, and a GSM module to send alerts and captures images when specific triggers are detected.

## Features

- **Motion Detection:** Uses an IR sensor to detect motion and trigger alerts.
- **Gas Detection:** Monitors for gas leaks and triggers an alarm.
- **Camera Surveillance:** Captures images when unauthorized access is detected.
- **SMS Alerts:** Sends SMS alerts via GSM module for any security breaches or hazardous conditions.
- **Email Notifications:** Emails captured images along with a predefined message in case of security breaches.

## Hardware Requirements

- Raspberry Pi (any model that supports Pi Camera and GPIO pins)
- Pi Camera
- GSM Module (e.g., SIM900)
- IR Sensor for motion detection
- Gas Sensor (e.g., MQ-2 for smoke and gas)
- Buzzer for audible alerts
- GPIO Cables and Breadboard for connections
- Power Supply for Raspberry Pi and Sensors

## Software Requirements

- Raspbian OS (or any compatible Raspberry Pi OS)
- Python 3.x
- OpenCV library for Python (`cv2`)
- PiCamera Python library
- Serial Python library
- GPIO library for Raspberry Pi

## Setup Instructions

### Hardware Setup

1. Connect the Pi Camera to the Raspberry Pi.
2. Connect the IR sensor, gas sensor, and buzzer to the GPIO pins according to the pin configuration in the script.
3. Setup the GSM module with the Raspberry Pi via serial connection.

### Software Setup

1. Install the Raspbian OS on your Raspberry Pi.
2. Install Python 3 and PIP.
3. Use PIP to install required Python libraries: `pip install opencv-python picamera RPi.GPIO pyserial`.
4. Place the project script in a directory on your Raspberry Pi.

### Configuration

- Update the GSM module's phone number in the script to receive alerts.
- Configure the email settings in the script to send email notifications.

## Running the Project

To run the project, navigate to the project directory in a Raspbian terminal and execute the following command:

```bash
python iot_security_system.py
