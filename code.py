#code.py  -- main code page for functions
import xml.dom.minidom


def code1():
    ## need input files:
    # 1)Dassault licenses.csv
    # 2)DSLS license rules
    # 3)Installed quantity on license server
    #*****************************************
    data = openfile1()
    data = openfile2("DSLS-Authorization_rules--userbased2.xml")

    for set in data:
        for row in set:
            print (row)

def openfile1():
    f1 = open("DassaultLicenses.csv")
    print(f1.read())

def openfile2(filein):
    f2 = xml.dom.minidom.parse(filein)
#    print("start")

    ##get IP Ranges in table iprangedata
    #***************************************************
    iprangestag = f2.getElementsByTagName("ipranges")
    iprangesIn=[]
    if iprangestag.length > 0:
        ipranges = iprangestag[0].getElementsByTagName("iprange")

        print ("there are %d ipranges:" % ipranges.length)
        for elements in ipranges:
            iprangedata=[]
            iprangedata.append(elements.getAttribute("range"))
            iprangedata.append(elements.getAttribute("id"))
            iprangesIn.append(iprangedata)
    else:
        print ("there are 0 ipranges:")

    ##get IP Rangegroups in table iprangegroupdata
    #***************************************************
    iprangegroupstag = f2.getElementsByTagName("iprangegroups")
    iprangegroupsIn=[]
    if iprangegroupstag.length > 0:
        iprangegroups = iprangegroupstag[0].getElementsByTagName("iprangegroup")

        print ("there are %d iprangegroups:" % iprangegroups.length)
        for elements in iprangegroups:
            iprangegroupdata=[]
            iprangegroupdata.append(elements.getAttribute("id"))
            iprangegroupdata.append(elements.childNodes[1].childNodes[0].nodeValue)
            iprangegroupdata.append(elements.childNodes[3].getAttribute("id"))
            iprangegroupdata.append(elements.childNodes[5].data)
            iprangegroupsIn.append(iprangegroupdata)
    else:
        print ("there are 0 iprangegroups:")

    ##get editor licensefeatures in table trigrams
    #***************************************************
    editortag = f2.getElementsByTagName("editor")
    trigrams=[]
    for elements in editortag:
        if elements.getAttribute("name")=="Dassault Systemes V5":
            model = elements.getElementsByTagName("model")
            for elements in model:
                if elements.getAttribute("type") == "ConcurrentUser":
                    trigramsV5 = elements.getElementsByTagName("feature")

    print ("there are %d trigram rules for V5:" % trigramsV5.length)
    trigramsIn=[]

    if trigramsV5.length >0:
        for element in trigramsV5:
            trigramdata = []
            trigramdata.append(element.getAttribute("name"))
            trigramdata.append(element.childNodes[1].nodeName)
            trigramdata.append(element.childNodes[1].getAttribute("ruletype"))
            trigramdata.append(element.childNodes[1].childNodes[1].childNodes[0].nodeValue)
            trigramdata.append(element.childNodes[1].childNodes[3].getAttribute("quantity"))
            trigramdata.append(element.childNodes[1].childNodes[3].getAttribute("id"))
            trigramdata.append(element.childNodes[1].childNodes[5].data)
            trigramsIn.append(trigramdata)

    dataset = []
    dataset.append(iprangesIn)
    dataset.append(iprangegroupsIn)
    dataset.append(trigramsIn)
    return dataset


def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)
