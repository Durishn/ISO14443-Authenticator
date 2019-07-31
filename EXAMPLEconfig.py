class Config:

	#FILL IN CURRENT PORT FOR SERIAL INPUT (ARDUINO), SEE FINDTTY.SH
	BAUDRATE = 9600
	PORT = '/dev/*FILL IN PORT*'

	# FILL IN FIRST 8 CHARACTERS OF UID... OR DONT...
	# LESS CHARACTERS MEANS A LITTLE LESS SECURITY BUT ALSO MEANS THIS PROGRAM
	# WON'T KNOW THE FULL UID OF YOUR TAG - ERGO KEEPS OTHER VALIDATIONS SAFE
	VALID_UIDS = ["FILL IN VALID KEY #1","FILL IN VALID KEY #2"]

	# PASSWORD FOR YOUR COMPUTER
	MAC_PASS = 'FILL IN PASSWORD'