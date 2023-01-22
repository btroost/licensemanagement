#code2.py   #alternative code1
import xml.dom.minidom
import csv
import os
import codecs
import io

def code3():
    #This code reeds the license key and returns a list per trigram.
    print("Started")
    
    file = "License Key LKO2109741 Details.txt"
    f = open("in_test/"+file, "rt")
    data=[]
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
            data.append(row)
            row=[]
    f.close()

    outputfile = open("out/"+file+"_out.csv", "w")
    for row in data:
        outputfile.write(row[0])
        outputfile.write(";")
        outputfile.write(row[1])
        outputfile.write(";")
        outputfile.write(row[2])
        outputfile.write("\n")
    outputfile.close()
    print("Finished")
    print ("Outputfile: " + outputfile.name)

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
