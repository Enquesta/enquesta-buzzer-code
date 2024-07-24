# Enquesta Buzzer

## Buzzer

Each buzzer is made of the following parts:

* ESP8266 Node MCU Module (with WiFi)
* Red LED
* Push Button
* 18650 Li-Ion Battery
* 1U 18650 Battery Holder
* Jumper Wires
* CCTV Box (to hold all the parts together)

The Schematic is as follows:
![Schematic Diagram](esp_circuit.png)

After all the connection are made, the buzzer will look like this:
![Schematic Diagram](final_photo.jpeg)

A small hole was made for the micro-usb port of the Node MCU.

## Software

Step 1: First set up a mobile hotspot where you can connect your laptop, and the six buzzers.

Step 2: Download or clone the repository.

Step 3: Install virtualenv
```
pip install virtualenv
```
Step 4: Make a virtual environment
```
python -m virtualenv buzzer
```

## Buzzer

Each buzzer is made of the following parts:

* ESP8266 Node MCU Module (with WiFi)
* Red LED
* Push Button
* 18650 Li-Ion Battery
* 1U 18650 Battery Holder
* Jumper Wires
* CCTV Box (to hold all the parts together)

The Schematic is as follows:
![Schematic Diagram](esp_circuit.png)

After all the connection are made, the buzzer will look like this:
![Schematic Diagram](final_photo.jpeg)

A small hole was made for the micro-usb port of the Node MCU.

## Software

Step 1: First set up a mobile hotspot where you can connect your laptop, and the six buzzers.

Step 2: Download or clone the repository.

Step 3: Move to the code directory
```
cd code
```

Step 4: Install virtualenv

For Linux:
```
pip install virtualenv
```

For Windows:
```
pip install virtualenv
```

Step 5: Make a virtual environment
```
python -m virtualenv buzz
```

Step 6: Activate Virtual Environment

For Linux:
```
source buzz/bin/activate
```

For Windows:
```
.\buzz\Scripts\activate
```

Step 7: Install all dependencies
```
pip install -r requirements.txt
```

Step 8: Run manage.py
```
python manage.py
```

Step 9: Note down the IP address in the hotspot network. (eg: http://192.168.x.x/5000)

Step 10: Download the Arduino IDE

Step 11: Go to File > Preferences and add 'http://arduino.esp8266.com/stable/package_esp8266com_index.json' to the Additional Board Manager URLs

Step 12: 
