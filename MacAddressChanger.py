import subprocess
import optparse
import re


def parser_function():
    parser=optparse.OptionParser()
    parser.add_option('-i','--interface',dest='interface',help="Enter the interface for changing the MacAdress")
    parser.add_option('-m','--macaddress',dest='macaddress',help="Enter the MacAdress that need to be updated")
    (option,args)=parser.parse_args()
    interface=option.interface
    macaddress=option.macaddress
    old_mac =first_result(interface)
    print(f"Current_Mac:{old_mac}")
    macchanger(interface,macaddress)
    new_mac=ChangedMac(interface)
    print(f"Changed__mac:{new_mac}")
    if (old_mac==new_mac):
       print("Not changed ")
    else:
        print("MacAddress Changed Successfully")
    
def macchanger(interface,macaddress):
    subprocess.call(["ifconfig",interface,'down'])
    subprocess.call(["ifconfig",interface,'hw','ether',macaddress])
    subprocess.call(["ifconfig",interface,'up'])


def first_result(interface):
    first_output=subprocess.check_output(['ifconfig',interface],text=True)
    before_mac=re.search('\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',first_output)
    if before_mac:
        return f"{before_mac.group(0)}"
        

#def checkingoutput(interface):
 #   output=subprocess.check_output(['ifconfig',interface],text=True)
  #  return first_result(output,interface)

def ChangedMac(interface):
    After_mac=subprocess.check_output(['ifconfig',interface],text=True)
    New_Mac=re.search('\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',After_mac)
    return f"{New_Mac.group(0)}"
    

parser_function()





