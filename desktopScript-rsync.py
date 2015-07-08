import datetime
import time
import os
os.system("cls")
def main():
	lineBreak()
	print " |                            Raspberry Pi Backup                             |"
	lineBreak()
	print " +  Before you backup, it is wise to ensure you're not downloading, uploading +"
	print " +  or transferring to/from the RPi. Doing any of those during backup         +"
	print " +  will give you a very slow experience. This is because of the bandwidth    +"
	print " +  limitations that the RPi has when using USB & Ethernet together.          +"
	lineBreak()
	x = raw_input("    Do you wish to backup right now? (y/n): ")
	while x.upper() != "Y" and x.upper() != "N":
		x = raw_input("    Please enter y or n: ")
	lineBreak()
	if x.upper() == "Y":
		print "    Checking if RPi is online..."
		ping = testConnection()
		if ping == 0:
			print '    Connection OK, initiating backup...'
			finishTime = rsync()
		else:
			print "    Can not establish connection to RPi, quitting..."
	else:
		print "    OK, will try again tomorrow."
	print("Total time: " + str(finishTime))
	time.sleep(5)

def lineBreak():
	print " +----------------------------------------------------------------------------+"

def testConnection():
	ping = os.system('powershell.exe "Test-Connection -q 192.168.0.125 | Out-Null"')
	return ping

def rsync():
	startTime = datetime.datetime.now()
	os.system("rsync -rvuih --rsync-path='rsync --log-file=/media/exthdd1/rsync.log' --delete --progress -e 'ssh -p 1019 -i /cygdrive/c/Users/Adam/.ssh/private-passphrase' '/cygdrive/c/Users/Adam/Desktop' pi@192.168.0.125:/media/exthdd1/backup/")
	finishTime = datetime.datetime.now() - startTime
	return finishTime
	
main()