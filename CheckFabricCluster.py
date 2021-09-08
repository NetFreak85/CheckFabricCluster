# coding=utf-8
#***********************************************************************************************************************#
#    This script help you to perform a complete Application Centric Infrastructure (ACI) fabric cluster Values Check    #
#	 The script will provide you the following information:                                                             #
#		Name Node                                                                                                       #
#		Fabric ID                                                                                                       #
#		Fabric Domain Name                                                                                              #
#		Fabric Node Mac Addr                                                                                            #
#		Fabric S/N                                                                                                      #
#		Controller Model                                                                                                #
#		Tunnel End Point (TEP) Address                                                                                  #
#		Tunnel End Point (TEP) Address Pool                                                                             #
#		Control Plane MTU                                                                                               #
#		Infra Vlan ID                                                                                                   #
#		Out Of Band (OOB) Address                                                                                       #
#		Out Of Band (OOB) Network Mask                                                                                  #
#		Out Of Band (OOB) Address Default Gateway                                                                       #
#                                                                                                                       #
# 		This info will help you when you need to install a new APIC in the Fabric                                       #
#                                                                                                                       #
#   --usage:                                                                                                            #
#             ./CheckFabricCluster.py                                                                                   #
#         or  python CheckFabricCluster.sh                                                                              #
#                                                                                                                       #
# date:  7/09/2021 Created                                                                                              #
#***********************************************************************************************************************#

import requests
import json
import getCookie
import Constant
from APICsInfo import APICsInfo

def printAux():
	print("+---------------------------------------------------------------+")

#Get Resquest to APICs and return a json object
def get_request(url, cookie):
	r = requests.get(url, cookies=cookie, verify=False)
	json_obj = json.loads(r.content)
	return json_obj

#Method that show all the APICs info
def ShowControllersFabric(apicIP, cookie):
	
	#Calls to the Cisco APIC API 
	fabricNode = get_request('https://%s/api/node/class/fabricNode.json?&order-by=fabricNode.modTs|desc' % apicIP, cookie)
	topSystem = get_request('https://%s/api/node/class/topSystem.json?&order-by=topSystem.modTs|desc' % apicIP, cookie)
	infraCont = get_request('https://%s/api/node/class/infraCont.json?&order-by=infraCont.modTs|desc' % apicIP, cookie)
	
	#We create a new object in the APIC Class in order to manage better the object in the APIC API
	APIC = APICsInfo()

	#Print the number of Controllers in the Fabric
	printAux()
	print("   Number of Controllers in the Fabric :   %s" % infraCont['imdata'][1]['infraCont']['attributes']['size'])
	printAux()

	#Loop that Print the APICs Info
	for i in range(0,int(fabricNode['totalCount'])):
			if fabricNode['imdata'][i]['fabricNode']['attributes']['role'] == "controller":
		
				#Set the API Values in the APICsInfo Class
				APIC.setNameNode(fabricNode['imdata'][i]['fabricNode']['attributes']['name'])
				APIC.setFabricID(fabricNode['imdata'][i]['fabricNode']['attributes']['id'])
				APIC.setControllerModel(fabricNode['imdata'][i]['fabricNode']['attributes']['model'])
				APIC.setTunnelEndPointAddress(fabricNode['imdata'][i]['fabricNode']['attributes']['address'])

				#Reach more information about the APIC in other API Tree
				for k in range(0,int(topSystem['totalCount'])):
						if topSystem['imdata'][k]['topSystem']['attributes']['id'] == fabricNode['imdata'][i]['fabricNode']['attributes']['id']:
							
							#Last call in the APIC API, we will find the Infraestructure Vlan ID in this call
							infraVlanVar = get_request('https://%s/api/node/mo/topology/pod-1/node-%s/sys/lldp/inst.json?query-target=self' % (apicIP, topSystem['imdata'][k]['topSystem']['attributes']['id']), cookie)
							
							#Store more information about the APICs in the APICsInfo Class
							APIC.setTunnelEndPointAddressPool(topSystem['imdata'][k]['topSystem']['attributes']['tepPool'])
							APIC.setFabricDomainName(topSystem['imdata'][k]['topSystem']['attributes']['fabricDomain'])
							APIC.setFabricNodeMacAddr(topSystem['imdata'][k]['topSystem']['attributes']['fabricMAC'])
							APIC.setFabricSN(topSystem['imdata'][k]['topSystem']['attributes']['serial'])
							APIC.setControlPlaneMTU(topSystem['imdata'][k]['topSystem']['attributes']['controlPlaneMTU'])
							APIC.setInfraVlanID(infraVlanVar['imdata'][0]['lldpInst']['attributes']['infraVlan'])
							APIC.setOutOfBandAddress(topSystem['imdata'][k]['topSystem']['attributes']['oobMgmtAddr'])
							APIC.setOutOfBandNetworkMask(topSystem['imdata'][k]['topSystem']['attributes']['oobMgmtAddrMask'])
							APIC.setOutOfBandAddressDefaultGateway(topSystem['imdata'][k]['topSystem']['attributes']['oobMgmtGateway'])
							APIC.setFabricNodeState(topSystem['imdata'][k]['topSystem']['attributes']['state'])

							#Print the APIC Information with a specific order
							APIC.printAPICsValues()

							#Reset the variables in the Class
							APIC.defaultValue()							
				printAux()

#Main program
if __name__ == '__main__':

    cookie = getCookie.get_cookie(Constant.apic, Constant.User, Constant.Password)	
    ShowControllersFabric(Constant.apic,cookie)
