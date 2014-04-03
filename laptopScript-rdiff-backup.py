# Use this script for the laptop
import urllib2
import datetime
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
		if internet_on() == 0:
			print "    Checking if you\'re home..."
			RuAtHome = os.system('NETSH WLAN SHOW INTERFACE SSID | findstr /r "TP-LINK_37A68E"') # Success code == 0, error code > 0
			ping = os.system('powershell.exe "Test-Connection -q 192.168.0.5 | Out-Null"') # Success code == 0, error code > 0 Is Out-Null really acceptable?! Does it actually work?!
			print ping
			print RuAtHome
			if ping == 1 and RuAtHome == 0:
				print '    Connection OK, initiating backup...'
				transfer = os.system('rdiff-backup --terminal-verbosity=5 --exclude "**.dropbox**" --exclude "**.ini**" --remote-schema "ssh -C %s -p1019 rdiff-backup --server" C:/Users/Adam/Dropbox username@domain.com::/path/to/directory')
				eleteOld = os.system('rdiff-backup --remove-older-than 2W --remote-schema "ssh %s -p1019 rdiff-backup --server" username@domain.com::/path/to/directory')
			else:
				if ping == 0:
					print '    The server is currently unreachable.'
				elif RuAtHome > 0:
					print '    Please try again later when you\'re home.'
		else:
			transfer = os.system('rdiff-backup --terminal-verbosity=5 --exclude "**.dropbox**" --exclude "**.ini**" --remote-schema "ssh -C %s -p1019 rdiff-backup --server" C:/Users/Adam/Dropbox username@domain.com::/path/to/directory')
			eleteOld = os.system('rdiff-backup --remove-older-than 2W --remote-schema "ssh %s -p1019 rdiff-backup --server" username@domain.com::/path/to/directory')
	else:
		print "    OK, will try again tomorrow."
	# To do: output total time and read relevant parts from logs
	time.sleep(5)
			
main()