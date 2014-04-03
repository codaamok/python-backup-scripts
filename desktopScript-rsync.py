# Use this script for the desktop
import datetime
import time
import os
os.system("cls")
def main():
	print " +----------------------------------------------------------------------------+"
	print " |                               Da Backup Box                                |"
	print " +----------------------------------------------------------------------------+"
	print " +  Before you backup, it is wise to ensure you're not downloading, uploading +"
	print " +  or transferring to/from the server. Doing any of those during backup      +"
	print " +  will give you a very slow experience. This is because of the bandwidth    +"
	print " +  limitations that the RPi has when using USB & Ethernet together.          +"
	print " +----------------------------------------------------------------------------+"
	x = raw_input("    Do you wish to backup right now? (y/n): ")
	while x.upper() != "Y" and x.upper() != "N":
		x = raw_input("    U WOT M8? y or n: ")
	print " +----------------------------------------------------------------------------+"
	if x.upper() == "Y":
		print "    Checking if server is online..."
		ping = os.system('powershell.exe "Test-Connection -q 192.168.0.5 | Out-Null"') # Success code == 0, error code > 0 Is Out-Null really acceptable?! Does it actually work?!
		if ping == 0:
			print '    Connection OK, initiating backup...'
			startTime = datetime.datetime.now()
			command = os.system("rsync -avuih --rsync-path='rsync --log-file=/mnt/disk1/Adam/Dropbox-rsync/rsync.log' --exclude '.dropbox*' --exclude 'desktop.ini' --exclude 'Thumbs.db' --delete --progress --chmod u+rwx -e 'ssh -p 1019 -i /cygdrive/c/Users/Adam/.ssh/id_rsa' '/cygdrive/c/Users/Adam/Dropbox/' username@domain.com::/path/to/directory")
			finishTime = datetime.datetime.now() - startTime
		else:
			print '    Connection failed, quiting...'
	else:
		print "    OK, will try again tomorrow."
	print("Total time: " + str(finishTime))
	time.sleep(5)
			
main()