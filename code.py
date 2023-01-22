#code.py  -- main code page for functions
import xml.dom.minidom
import csv


def code1():
    ## need input files:
    # 1)Dassault licenses.csv
    # 2)DSLS license rules
    # 3)Installed quantity on license server
    # data set:
    #   [0]-license assets data[0]
    #   [1]-License key info LKO Dassault
    #   [2]-license access rules
    #   --[0] network,
    #   --[1] network group,
    #   --[2] trigrams (create single list?)
    #   [3] -Processed assetlist
    #   [4] -Processed licensekey inf? of processed trigrams
    #   [5] -Processed accessrules
    #
    #*****************************************
    #    data1 = openfile1("DassaultLicenses.csv")
    #    data = openfile2("DSLS-Authorization_rules--userbased2.xml")

    #** Get datafiles
    GlobalTagetID="KKZ-42661C6F695667C0"  # ="FSN-42A8108E79C537A0"
    sep = ";"

    Assets ="in_test/Licenties - 19 augustus-mod.csv"  #DassaultLicenses.csv"
    AssetsOut ="out/Licenties - 19 augustus-mod_out.csv"  #DassaultLicenses.csv"
    LicenseKeys="in_test/License Key LKO2071370 Details.txt" #License Key LKO2072356 Details.txt"  #License Key LKO2037228 Details.txt"
    LicenseKeysOut="out/License Key LKO2071370 Details_out.csv" #License Key LKO2072356 Details.txt"  #License Key LKO2037228 Details.txt"


    data=[]
    #***** open files ***** #
    data.append(openassets(Assets))
    data.append(openlicensekeys(LicenseKeys)) #v5 april
    #data.append(openaccessrules("DSLS-Authorization_rules--userbased2.xml"))

    #*****Process data in files *****#
    data.append(processassets(data[0],GlobalTagetID))
    data.append(processlicensekey(data[1],GlobalTagetID))
    #data.append(processacl(data))

    #***** create combined tables *****#
    debug = False
    if debug:

        # ***** Print results *****#
        #    for set in data:
        #        print("***** New list, length = " + str(len(set)) + " *****")
        #        for row in set:
        #            print (row)

        dataset=2
        print("***** Specific list, length = " + str(len(data[dataset])) + " *****")
        for row in data[dataset]:
                print(row)
        dataset=3
        print("***** Specific list, length = " + str(len(data[dataset])) + " *****")
        for row in data[dataset]:
                print(row)


    outputfile = open(AssetsOut, "w")
    for row in data[2]:
        for element in row:
            outputfile.write(element)
            outputfile.write(sep)
        outputfile.write("\n")
    outputfile.close()
    print ("OutputFile: " +outputfile.name)

    outputfile = open(LicenseKeysOut, "w")
    for row in data[3]:
        for element in row:
            outputfile.write(element)
            outputfile.write(sep)
        outputfile.write("\n")
    outputfile.close()
    print ("OutputFile: " +outputfile.name)

    print("Finished")

def openassets(filein):
    data=[]
    with open(filein) as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=';')
        i=0
        for row in csvReader:
            #skip header
            if i > 0:
                data.append(row)
            i = i+1
    return data

def openlicensekeys(file):
    f = open(file, "rt")
    data=[]
    row=[]
    for x in f:
        if x.find("Certificate:") > 0:
            q=x.rpartition("Portfolio")
            row.append(q[2].strip())

        if x.find("Configurations") > 0:
            q=x.rpartition("Products")
            row.append(q[2].strip())

        if x.find("Target ID") > 0:
            q=x.rpartition("Target ID")
            row.append(q[2].strip())

        if x.find("Quantity") > 0:
            q=x.rpartition("Quantity")
            row.append(q[2].strip())

        if x.find("SerialNumber") > 0:
            row.append("newline")
            data.append(row)
            row=[]

    return data

def openaccessrules(filein):
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

def processassets(datain,GlobalTagetID):
    #** list of special keys.
    #--first value is special key
    #--next values are the contents of the special keys.
    list = [
    ["ZAD", "HD2", "KT1", "FS1"],
    ["ZAM", "HD2", "KT1", "FS1","AMG"],  #etc.
    ["ZAC","CD3", "KT1","FS1"]]

    # 1 collect trigrams per targetID and split special keys
    targetID = GlobalTagetID #"KKZ-42661C6F695667C0"
    #
    newdata = []
#    newdata = ["A","B","AAA","D","E",GlobalTagetID,"G","H","I","J","K","L","M","N","O","P","Q"]
    header = ["A","B","AAA","D","E",GlobalTagetID,"G","H","I","J","K","L","M","N","O","P","Q"]
    newdata.append(header)
    for rows in datain:
        validrow = False
        for items in rows:
            if targetID in items:
                specialkey = False
                for items in list:
                    if rows[2] == items[0]:
                        specialkey = True
                        for x in range(1,len(items)):
                            nrow = rows.copy()
                            nrow[2] = items[x]
                            newdata.append(nrow)
                if specialkey == False:
                    newdata.append(rows)


    # 2 consolidate on site and trigram
    # add key to sort:
    for rows in newdata:
        rows.append(rows[2])
#        rows.append(str(rows[4] + "-" + rows[2]))  # for licenses per usagescope
    newdata.sort(reverse=False, key=sortkey)

    key = ""
    xlist = []
    xline = []
    for rows in newdata:
        if rows[17] == key:
            xline[3] = str(int(xline[3]) + int(rows[3]))
        else:
            xline=rows.copy()
            key = rows[17]
            if ((len (newdata) == 1) or (key != "")):
                xlist.append(xline)
    return xlist

def processlicensekey(datain,GlobalTagetID):
    # collect trigrams per targetID and split special keys
    newdata = []
    newrow=[]
    targetID = GlobalTagetID  #"FSN-42A8108E79C537A0"  #KKZ-42661C6F695667C0"
    for rows in datain:
        if rows[2] == targetID:
            # clean license configuration before processing
            r=rows[1].strip()
            if r.find("Shareable") > 0:
                type = "SHA"
            else:
                type="CFG"

            r=r.replace("(Shareable)","")
            r=r.replace("(Configuration)","")
            r=r.replace("(Named User)","")
            r=r.replace("(System)","")

            r=r.replace("(Token-Based)","")
            r=r.replace("(Single Add-On)","")

            #(Token-Based)
            #(Single Add-On)
            r=r.replace(" ","")

            r=r.replace("DASMS-BASE","XSE")
            r=r.replace("DASMS-AF","XFE")

            rows.append(r)
            rows.append(type)

            # Each trigram to get its own row
            i=len(r)
            if i >3:   #split in single trigrams
                j=int((i)/3)
                for k in range(j):
                    newrow = []
                    trigram=r[k*3+0]+r[k*3+1]+r[k*3+2]
                    newrow.append(trigram)
                    newrow.append(rows[6])
                    newrow.append(rows[3])
                    newrow.append(rows[0])
                    newrow.append(rows[2])
                    newdata.append(newrow)
            else:
                newrow=[]
                newrow.append(r)
                newrow.append(rows[6])
                newrow.append(rows[3])
                newrow.append(rows[0])
                newrow.append(rows[2])
                newdata.append(newrow)

    ## to do:split ZOM, ZOH, DASMS-AF (XAF), DASMS-BASE (XSE)

    #create key and sort
    for rows in newdata:
        if rows[2].find("V5") > 0:
            rows.append(rows[0] + "_V5_" + rows [4] + "_"  + rows [3])
        else:
            rows.append(rows[0] + "_V6_"  +  rows [4] + "_" + rows [3])
    newdata.sort(key=sortkey)

    # consolidate trigrams
    key = ""
    nwlist = []
    nwline = []
    for rows in newdata:
        if rows[-1] == key:
            nwline[2] = str(int(nwline[2]) + int(rows[2]))
        else:
            nwline=rows.copy()
            key = rows[-1]
            if ((len (newdata) == 1) or (key != "")):
                nwlist.append(nwline)
    # add keys to assets

    return nwlist

def processacl(datain):
    #process accesruledata
    dataset=[]
    r=[]
    #datain[2][2] is accessrules, trigrams
    for rows in datain[2][2]:  #2 is trigram
        i=len(rows[0])
        if i >3:   #split in single trigrams
            x=rows[0].replace("-","")
            j=int((i-1)/3)
            for k in range(j):
                r=rows.copy()
                r[0]=x[k*3+0]+x[k*3+1]+x[k*3+2]
                dataset.append(r)
        else:
            dataset.append(rows)

    #append key to sort
    for row in dataset:
        row.append((row[6].strip()) + "-"+  row[0])

    dataset.sort(key=sortkey)

    # consolidate per trigram and site
    key = ""
    nwlist = []
    nwline = []
    for rows in dataset:
        if rows[7] == key:
            nwline[4] = str(int(nwline[4]) + int(rows[4]))
        else:
            nwline=rows.copy()
            key = rows[7]
            if ((len (dataset) == 1) or (key != "")):
                nwlist.append(nwline)

    #    Append to assetlist
    # create newlist, 1a is assets not in acl + assets = acl
    newlist = []
    newrow = []

    for asset in datain[3]:
        newrow = asset.copy()
        for acl in nwlist:
            if asset[5]== acl[7]:
                newrow.append(acl[4])
                newrow.append(str(int(asset[3])-int(acl[4])))
        newlist.append(newrow)

    # 1b assets in acl not in assetlist
    for acl in nwlist:
        match = False
        for asset in datain[3]:
            if asset[5]== acl[7]:
                match =True
        if match == False:
            newrow=[]
            newrow.append("abc"+acl[0])
            newrow.append(acl[0])
            newrow.append(acl[6])
            newrow.append(acl[4])
            newrow.append("ServerID")
            newrow.append(acl[3])
            newrow.append(acl[7])

            newlist.append(newrow)

    #    for row in newlist:
    #        print(row)
    return newlist

def sortkey(e):
        return (e)[-1]

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)
