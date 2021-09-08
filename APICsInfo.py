#**********************************************************************************
#    This script wil help the main program to store and print the APICs Info
#	 The script will Store the following information:
#		Name Node
#		Fabric ID
#		Fabric Domain Name
#		Fabric Node Mac Addr
#		Fabric S/N
#		Controller Model
#		Tunnel End Point (TEP) Address
#		Tunnel End Point (TEP) Address Pool
#		Control Plane MTU
#		Infra Vlan ID
#		Out Of Band (OOB) Address
#		Out Of Band (OOB) Network Mask
#		Out Of Band (OOB) Address Default Gateway
#**********************************************************************************

class APICsInfo:
    def __init__(self):
        nameNode = ""
        FabricID = ""
        FabricDomainName = ""
        FabricNodeMacAddr = ""
        FabricSN = ""
        ControllerModel = ""
        TunnelEndPointAddress = ""
        TunnelEndPointAddressPool = ""
        ControlPlaneMTU = ""
        InfraVlanID = ""
        OutOfBandAddress = ""
        OutOfBandNetworkMask = ""
        OutOfBandAddressDefaultGateway = ""
        FabricNodeState = ""

    #Variable for Node Name
    nameNode = ""

    #Variable for Fabric ID 
    FabricID = ""

    #Variable for Fabric Domain Name
    FabricDomainName = ""

    #Variable for Fabric Node Mac Address
    FabricNodeMacAddr = ""

    #Variable for Fabric Serial Number
    FabricSN = ""

    #Variable for Fabric APIC Node State
    FabricNodeState = ""

    #Variable for APIC Controller Model
    ControllerModel = ""

    #Variable for Tunnel End Point (TEP) Address
    TunnelEndPointAddress = ""

    #Variable for Tunnel End Point (TEP) Address Pool
    TunnelEndPointAddressPool = ""

    #Variable for Control Plane MTU
    ControlPlaneMTU = ""

    #Variable for Infraestructure Vlan ID
    InfraVlanID = ""

    #Variable for Out Of Band (OOB) IP Address
    OutOfBandAddress = ""

    #Variable for Out Of Band (OOB) Mask Address
    OutOfBandNetworkMask = ""

    #Variable for Out Of Band (OOB) Default Gateway
    OutOfBandAddressDefaultGateway = ""

    ##################################################################
    #Set Function section that set a specifig value to a self variable
    ##################################################################

    #Set function that set the APIC Name Node
    def setNameNode(self, nameNodeAux):
        self.nameNode = nameNodeAux

    #Set function that set the APIC Fabric ID
    def setFabricID(self, FabricIDAux):
        self.FabricID = FabricIDAux

    #Set function that set the APIC Fabric Domain Name
    def setFabricDomainName(self, FabricDomainNameAux):
        self.FabricDomainName = FabricDomainNameAux

    #Set function that set the APIC Fabric Mac Address
    def setFabricNodeMacAddr(self, FabricNodeMacAddrAux):
        self.FabricNodeMacAddr = FabricNodeMacAddrAux

    #Set function that set the APIC Fabric Serial Number
    def setFabricSN(self, FabricSNAux):
        self.FabricSN = FabricSNAux

    #Set function that set the APIC Fabric Node State
    def setFabricNodeState(self, FabricNodeStateAux):
        self.FabricNodeState = FabricNodeStateAux

    #Set function that set the APIC Controller Model
    def setControllerModel(self, ControllerModelAux):
        self.ControllerModel = ControllerModelAux

    #Set function that set the APIC Tunnel End Point Address
    def setTunnelEndPointAddress(self, TunnelEndPointAddressAux):
        self.TunnelEndPointAddress = TunnelEndPointAddressAux

    #Set function that set the APIC Tunnel End Point Address Pool
    def setTunnelEndPointAddressPool(self, TunnelEndPointAddressPool):
        self.TunnelEndPointAddressPool = TunnelEndPointAddressPool

    #Set function that set the APIC Control Plane MTU
    def setControlPlaneMTU(self, ControlPlaneMTUAux):
        self.ControlPlaneMTU = ControlPlaneMTUAux

    #Set function that set the APIC Infraestructure Vlan ID
    def setInfraVlanID(self, InfraVlanIDAux):
        self.InfraVlanID = InfraVlanIDAux

    #Set function that set the APIC Out Of Band IP Address
    def setOutOfBandAddress(self, OutOfBandAddressAux):
        self.OutOfBandAddress = OutOfBandAddressAux

    #Set function that set the APIC Out Of Band Network Mask
    def setOutOfBandNetworkMask(self, OutOfBandNetworkMaskAux):
        self.OutOfBandNetworkMask = OutOfBandNetworkMaskAux

    #Set function that set the APIC Out Of Band Default Gateway
    def setOutOfBandAddressDefaultGateway(self, OutOfBandAddressDefaultGatewayAux):
        self.OutOfBandAddressDefaultGateway = OutOfBandAddressDefaultGatewayAux

    #Method that put the default values in the variables
    def defaultValue(self):
        self.nameNode = ""
        self.FabricID = ""
        self.FabricDomainName = ""
        self.FabricNodeMacAddr = ""
        self.FabricSN = ""
        self.ControllerModel = ""
        self.TunnelEndPointAddress = ""
        self.TunnelEndPointAddressPool = ""
        self.ControlPlaneMTU = ""
        self.InfraVlanID = ""
        self.OutOfBandAddress = ""
        self.OutOfBandNetworkMask = ""
        self.OutOfBandAddressDefaultGateway = ""
        self.FabricNodeState = ""

    #Method that print all the APIC information
    def printAPICsValues(self):
        print ("   Node Name                           :      %s" % self.nameNode)
        print ("   Fabric ID                           :      %s" % self.FabricID)
        print ("   Fabric Domain Name                  :      %s" % self.FabricDomainName)
        print ("   Fabric Node Mac Addr                :      %s" % self.FabricNodeMacAddr)
        print ("   Fabric S/N                          :      %s" % self.FabricSN)
        print ("   Fabric Node State                   :      %s" % self.FabricNodeState)
        print ("   Controller Model                    :      %s" % self.ControllerModel)
        print ("   Tunnel End Point (TEP) Addr         :      %s" % self.TunnelEndPointAddress)
        print ("   TEP Pool                            :      %s" % self.TunnelEndPointAddressPool)
        print ("   Control Plane MTU                   :      %s" % self.ControlPlaneMTU)
        print ("   Infra Vlan ID                       :      %s" % self.InfraVlanID)
        print ("   Out Of Band (OOB) Addr              :      %s" % self.OutOfBandAddress)
        print ("   Out Of Band (OOB) Network Mask      :      %s" % self.OutOfBandNetworkMask)
        print ("   Out Of Band (OOB) Addr DG           :      %s" % self.OutOfBandAddressDefaultGateway)
