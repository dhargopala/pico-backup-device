# pico-backup-device
This is a DIY Project to build a compact QR code backup device, on the Raspberry Pi Pico, that can be used to store Authenticator QR codes and seed phrases of wallets
## Requirements

* Hardware:
  * [Rasberry Pi Pico Micro-controller](https://www.raspberrypi.org/products/raspberry-pi-pico/) 
  * [1.3 inch 65K Color LCD](https://www.waveshare.com/pico-lcd-1.3.htm)
  * Micro-USB connector cable
 
* Software:
  * [Thonny Editor](https://thonny.org/)
  * [UF2 File](https://github.com/waveshare/Pico_code/blob/main/Python/pico_micropython_20210121.uf2)
  * [Python 3.5](https://www.python.org/downloads/release/python-350/)
  * [OpenCV](https://www.geeksforgeeks.org/how-to-install-opencv-for-python-in-windows/)
 
## Setup
* Push and hold the BOOTSEL button and plug your Pico into the USB port of your computer.
* Release the BOOTSEL button after your Pico is connected, It will mount as a Mass Storage Device called RPI-RP2.
* Drag and drop the MicroPython UF2 file onto the RPI-RP2 volume. Your Pico will reboot. You are now running MicroPython.
* Incase of any doubts, refer the [official documentation page](https://www.raspberrypi.org/documentation/rp2040/getting-started/#getting-started-with-micropython).
* In order to get familiar with Thonny editor for Pico, please watch this [YouTube](https://www.youtube.com/watch?v=_ouzuI_ZPLs) tutorial.

## Getting Started
* If we have a QR Code that we want to take backup of, we need to first transfer its contents from our mobile device to a PC, we can use [QR Scanner](https://webqr.com/) for this purpose and copy the textual data
* After copying the textual data of the QR code, go to a [QR Generation Website](https://www.qrcode-monkey.com/#text).
* Paste the text here, and set the Background Color to #000000 (Black) and the Foreground Color to #00FF00 (Green), Note that we may use any combination, but this gives a good contrast and makes the QR easily scanable.
* NOTE: If we decide to change the background color, We are requied to change [this vairiable](./Pico%20Micropython/lcd_lib.py#L165) in this code base to the corresponding HEX value, if we're using the default values, then this step can be skipped.
* On the scroll bar on right side, select Lowest Quality (200 x 200 Px) and Generate the QR.
* Try scanning the QR with your mobile device, if it works, then we can go ahead and download the PNG image.
* After Cloning the repo in a directory, paste the PNG files in the same directory on your local machine.
* The files present in [Pico Micropython](./Pico%20Micropython) folder should be copied to the Pico device using Thonny, we can do this by opening the files in Thonny and then saving them to Pico.
* On your local machine, edit the [image_encoder.py](./image_encoder.py) file and change the [file_name](./image_encoder.py#L22) as per the name of your PNG file, and then run the python file, you may repeat this step if you have multiple QR codes to backup.
* Each time we run this python file, a new file will be created in the same directory, we can open these generated files using notepad or any other text editor.
* After opening this file, we can select and then copy all of its content.
* The copied content can be pasted in either of the three existing files, namely: QR1, QR2 or QR3 inside Pico using the Thonny editor, Note that we may change the file names, but then the [code](./Pico%20Micropython/main.py) would also need to be refactored.
* If we want to edit what will be shown on screen, we may change [these variables](./Pico%20Micropython/main.py#L23), inside Pico using Thonny.
* We can save the file, and then run [main.py](./Pico%20Micropython/main.py) file using Thonny.
* Since this file is saved as main.py inside Pico, it will automatically run at startup, i.e., It will run as soon as the board is powered.

## Usage
* The joystick can be used to switch between multiple options on the screen.
* Either of the 4 buttons can be used to select an option, which will then load the QR code.
* After the QR is loaded on screen, we may press any button to return back to the main menu.
* Current implementation allows upto 3 QR codes to be saved, however changes in the code can accomodate several more to be stored in this device.

## Snapshots
![](https://i.imgur.com/4GrSexl.jpeg)
![](https://i.imgur.com/9V6lAMO.jpeg)
![](https://i.imgur.com/uZ9ymey.jpeg)
