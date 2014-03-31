# Use this script for the laptop
import urllib2
import time
import os
def internet_on():
	print "Checking for internet connection..."
	try:
		response=urllib2.urlopen('http://74.125.224.72/',timeout=5)
		return True
	except urllib2.URLError as err: pass
	return False
	
def main():
	print " +----------------------------------------------------------------------------+"
	print "                                 Da Backup Box"
	print " +----------------------------------------------------------------------------+"
	x = raw_input("Do you wish to backup right now? (y/n): ")
	while x.upper() != "Y" and x.upper() != "N":
		x = raw_input("Huh? y or n: ")
	if x.upper() == "Y":
		if internet_on() == 0:
			print "Checking if you\'re home..."
			RuAtHome = os.system('NETSH WLAN SHOW INTERFACE SSID | findstr /r "TP-LINK_37A68Esss"') # Success code == 0, error code > 0
			ping = os.system('powershell.exe "Test-Connection -q 192.168.0.5 | Out-Null"') # Success code == 0, error code > 0 Is Out-Null really acceptable?! Does it actually work?!
			print ping
			print RuAtHome
			if ping == 1 and RuAtHome == 0:
				print 'Attempting to locally connect to RPi...'
				rsync = os.system("rsync -avuih --rsync-path='rsync --log-file=/mnt/disk1/Adam/rsync.log' --exclude '.dropbox*' --exclude 'desktop.ini' --delete --progress --chmod u+rwx -e 'ssh -p 1019 -i /cygdrive/c/Users/User/.ssh/id_rsa' '/cygdrive/c/Users/User/Dropbox/' pi@192.168.0.5:/mnt/disk1/Adam/Dropbox/")
			else:
				if ping == 0:
					print 'The server is currently unreachable.'
				if RuAtHome > 0:
					print 'Please try again later when you\'re home.'
		else:
			# note: for the following command to work, ensure you have rsync set in the PATH environment variable
			rsync = os.system("rsync -avuih --rsync-path='rsync --log-file=/mnt/disk1/Adam/rsync.log' --exclude '.dropbox*' --exclude 'desktop.ini' --delete --progress --chmod u+rwx -e 'ssh -p 1019 -i /cygdrive/c/Users/User/.ssh/id_rsa' '/cygdrive/c/Users/User/Dropbox/' pi@codaamok.servebeer.com:/mnt/disk1/Adam/Dropbox/")
	else:
		print "OK, will try again tomorrow"
	time.sleep(5)
			
main()