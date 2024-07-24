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


Step 5: 