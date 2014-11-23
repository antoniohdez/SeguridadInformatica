from sniffer import sniffer
from nmap import scan
import sys, subprocess

def print_menu():
	# Clear the screen
	subprocess.call('clear', shell=True)
	print "Final project"
	print "-" * 50
	print "\t Select an option:"
	print "\t\t1) Scan ports"
	print "\t\t2) Sniff traffic"
	print "\t\t3) Exit"
	print "-" * 50
	return int( raw_input("Option: ") )

def output_format():
	subprocess.call('clear', shell=True)
	print "-" * 50
	print "\t Select an option:"
	print "\t\t1) Console"
	print "\t\t2) txt file"
	print "\t\t3) Back"
	print "-" * 50
	return int( raw_input("Option: ") )	

while True:
	option = print_menu()

	while option != 3:
		format = output_format()
		subprocess.call('clear', shell=True)
		if option == 1:
			scan(format)
		elif option == 2:
			sniffer(format)
		elif option == 3:
			sys.exit()
		else:
			print "Invalid option"
		raw_input("Enter to continue")
		break
	if option == 3:
		sys.exit()