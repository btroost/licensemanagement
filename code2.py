#code2.py   #alternative code1
import xml.dom.minidom
import csv
import os
import codecs
import io

def code2():
    outputfile = open("out/results_dslsprd-2022-11-09.csv", "w")
# Get the list of all files and directories
#    path = "C://Users//Vanshi//Desktop//gfg"
    path = "inprd"
    dir_list = os.listdir(path)
#    print("Files and directories in '", path, "' :")
    # prints all files
#    print(dir_list)
    for file in dir_list:
#        print (file)

#    filename = "LicenseServer20221031074122.log"
        file = "inprd/"+file
#    LicenseServer20221107083922
#LicenseServer20221031074122.log
        f = open(file, "rt")
#    data=[]
        row=[]
        for x in f:
            #    print(x)
            if (x.find("Grant!!") > 0):
                q=x.rpartition("Grant!!")
                row.append(q[1].strip())
                r=q[2].rsplit("!")
                outputfile.write(r[0]+","+r[6]+","+r[7]+","+r[8]+"\n")

    outputfile.close()
    print("Finished")
    #        print(r[7])
    #        print(r[8])

    #    if (x.find("Detachment") > 0):
    #        print(x)
    #    if (x.find("TimeOut") > 0):
    #        print(x)

def code3():
    file = "License Key LKO2109741 Details.txt"
    f = open(file, "rt")
    data=[]
#    row=["Config"+";Quantity" + ";TargetID"]
#    data.append(row)
    row=[]
    for x in f:
        if x.find("Configurations") > 0:
            q=x.rpartition("Products")
            row.append(q[2].strip())
        if x.find("Quantity") > 0:
            q=x.rpartition("Quantity")
            row.append(q[2].strip())
        if x.find("Target ID") > 0:
            q=x.rpartition("Target ID")
            row.append(q[2].strip())
        if x.find("SerialNumber") > 0:
        #    row.append("newline")
            data.append(row)
            row=[]
    f.close()

#    for i in data:
#        print (i[0]+";"+i[1])

    outputfile = open(file+"_out.csv", "w")
    for row in data:
        outputfile.write(row[0])
        outputfile.write(";")
        outputfile.write(row[1])
        outputfile.write(";")
        outputfile.write(row[2])
        outputfile.write("\n")
    outputfile.close()


def code4():
    # This code reads a series of DSLS logfiles and returns structured usage data
    path = "in_2312"
    outputfile = open("out/output_"+path+".csv", "w")
    sep = ";"

    # Get the list of all files and directories
    dir_list = os.listdir(path)

    print("Started")
    for file in dir_list:
        file = path +"/"+file
        row=[]

        with io.open(file, 'r', encoding='windows-1252') as f:
            for x in f:
                if (x.find("Grant!!") > 0):
                    q=x.rpartition("Grant!!")
                    r=q[2].rsplit("!")
                    rx=r[6].split("(")
                    t=q[0].split(" ")
                    outputfile.write("Grant!!"+sep+r[0]+sep+rx[0]+sep+r[7]+sep+r[8]+sep+t[0]+sep+t[1]+"\n")
                if (x.find("TimeOut!!") > 0):
                    q=x.rpartition("TimeOut!!")
                    r=q[2].rsplit("!")
                    rx=r[6].split("(")
                    t=q[0].split(" ")
                    outputfile.write("TimeOut!!"+sep+r[0]+sep+rx[0]+sep+r[7]+sep+r[8]+sep+t[0]+sep+t[1]+"\n")
                if (x.find("Detachment!!") > 0):
                    q=x.rpartition("Detachment!!")
                    r=q[2].rsplit("!")
                    rx=r[6].split("(")
                    t=q[0].split(" ")
                    outputfile.write("Detachment!!"+sep+r[0]+sep+rx[0]+sep+r[7]+sep+r[8]+sep+t[0]+sep+t[1]+"\n")
            f.close()
    print ("returned outputfile: " + outputfile.name)
    outputfile.close()
    print("Finished")
