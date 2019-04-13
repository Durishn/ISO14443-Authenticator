ISO14443A-Authenticator
======

Introduction
------------
This repo contains all necessary code to unlock (NOT LOGIN) a Mac OS user by scanning an ISO1443 (MiFare) tag as authentication using an Arduino, PN532 RFID Reader, and some Python.

It connects to an Arduino Uno with a PN532 RFID reader (or shiled) connected over USB to your computer. The Arduino passes the UID of the tag over serial at 115200 baud. A Python script listens at that port, and matches the first 5 digits of the UID to the valid keys it has stored in `config.py` - it does not store the entire UID of the card for security purposes. Upon match it unfreezes any screensaver that might be running and enters the password found in `config.py` to the login window. Viola, logged in!

Is it secure? No. My OSx pass is literally stored in plain text in the config, not great form for sure. But I keep most of my files, systems and processes seperate with various users and encryptions so I'm not too-too worried. Point being, use caution if you choose to implement this. 


Instructions
------------
1. Plug your PN532 into your Arduino Uno
2. Run `bash findtty.sh` & wait until the program prompts you to plug in your Arduino (this little script is courtesy of [Jerry Davis](https://gist.github.com/lanhed/dcb652c83f032fea31c9)). Remember the output of this script.
3. Open your Arduino editor and upload `read_NDEF_id.ino` to your Uno. Open the serial monitor and set it to 115200 baud. After a few seconds try scanning a tag, if you see the UID then your good. Log the UID of all tags you want to validate
4. Open `config.py` and enter the first 6 digits of the UID of all valid tags, your OSx password, and your port from step 2
5. Run `python NFC_Authenticator.py` and try scanning a tag - you should see some output confirming validation
6. Try turning on your screensaver or locking your screen and scanning your tag, it should now work.
7. Now just setup the program to run on login either through an Automation task or seperate script (I setup a directory and bash script for progs that run on login)
