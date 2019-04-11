/**************************************************************************/
/*! 
    This will connect to a PN532 RFID reader to read ISO14443A or ISO14443A
    cards or tags. It retrieves the UID and passes the data over serial at 
    115200 baud
   
    Author: Nic Durish
    Email: dev@nicdurish.ca
*/
/**************************************************************************/
#include <Wire.h>
#include <PN532_I2C.h>
#include <PN532.h>
#include <NfcAdapter.h>
  
//Properly connect to PN  
PN532_I2C pn532i2c(Wire);
PN532 nfc(pn532i2c);
  
void setup(void) {

  //Begin Serial connection to find PN532 board
  Serial.begin(115200);
  nfc.begin();
  uint32_t versiondata = nfc.getFirmwareVersion();
  if (! versiondata) {
    Serial.print("Didn't find PN53x board");
    while (1); // halt
  }
  
  // Print board info
  Serial.print("Found chip PN5"); Serial.println((versiondata>>24) & 0xFF, HEX); 
  Serial.print("Firmware ver. "); Serial.print((versiondata>>16) & 0xFF, DEC); 
  Serial.print('.'); Serial.println((versiondata>>8) & 0xFF, DEC);
  
  // Set the max number of retry attempts to read from a card
  nfc.setPassiveActivationRetries(0xFF);
  
  // configure board to read RFID tags
  nfc.SAMConfig();
  Serial.println("done");
}

void loop(void) {
  boolean success;
  uint8_t uid[] = { 0, 0, 0, 0, 0, 0, 0 };  // Buffer to store the returned UID
  uint8_t uidLength;                        // Length of the UID (4 or 7 bytes depending on ISO14443A card type)
  String uidString = "";  

  // Wait for an ISO14443A tag.  When one is found 'uid' and 'uidLength' will be populated
  success = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A, &uid[0], &uidLength);
  if (success) {
    for (uint8_t i=0; i < uidLength; i++) {
      uidString = uidString + String(uid[i], HEX);
    }

    // Print UID to serial and wait 1s
    Serial.println(uidString);
    delay(1000);
  }
}
