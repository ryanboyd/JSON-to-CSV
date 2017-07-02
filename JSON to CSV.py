'''

  .o oOOOOOOOo                                            OOOo
   Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
   OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
   OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
   `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
   .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
   OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
  oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
 oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
   Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
   :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
   .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                     `$"  `OOOO' `O"Y ' `OOOO'  o             .
   .                  .     OP"          : o     .
                            :

JSON to CSV Converter
        Coded by Ryan L. Boyd
        The University of Texas at Austin

*This script was built for Python 2.7
*This script does not require any additional packages

        
Fill in the appropriate directory for the JSON_FileDir variable
Then run this script. It will batch convert all files to CSV format
'''

import os
import json
import csv

#set the directory from which you will read .txt files
JSON_FileDir = "X:/Directory with JSON Files/"

#make sure that it ends with a trailing slash so that
#you know that it's there for future directory use in the script
if JSON_FileDir.endswith("/") == False:
        JSON_FileDir += "/"

#create an output directory within TextFileDir
if not os.path.exists(JSON_FileDir + "CSV/"):
    os.makedirs(JSON_FileDir + "CSV/")



#initialize variables of note

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            a = ''
            try:
                a = str(x)
            except:
                a = x.encode('ascii', 'ignore').decode('ascii')
            
            out[str(name[:-1])] = a

    flatten(y)
    return out


header_keys = []

#this first time goes through and figures out all of the keys in the entire dataset
print('Determining complete key list....')


for filename in os.listdir(JSON_FileDir):
        #make sure that you're only reading .json files
        if filename.endswith(".json") == True:


                #set up your reader
                with open(JSON_FileDir + filename) as JSON_File:

                        #read in the file, converting linebreaks to spaces
                        dataset = json.loads(JSON_File.read())
                        
                        
                        flat_data = flatten_json(dataset)

                        keys = flat_data.keys()

                        for key in keys:

                                if key not in header_keys:
                                        header_keys.append(key)



#now we go back through and convert all of it to a CSV

with open(JSON_FileDir + "CSV/CSV_Output.csv", 'wb') as outgoing:

        writer = csv.writer(outgoing)

        header = ['Filename']
        header.extend(header_keys)

        writer.writerow(header)


        for filename in os.listdir(JSON_FileDir):
        #make sure that you're only reading .json files
                if filename.endswith(".json") == True:


                        Data_row = ['']*len(header_keys)

                        #set up your reader
                        with open(JSON_FileDir + filename) as JSON_File:

                                #read in the file, converting linebreaks to spaces
                                dataset = json.loads(JSON_File.read())
                                
                                #print the status
                                print("Currently working on: " + filename)

                                flat_data = flatten_json(dataset)

                                for key in flat_data.keys():
                                        Data_row[header_keys.index(key)] = flat_data[key]

                        Data_final = [filename]

                        Data_final.extend(Data_row)

                        writer.writerow(Data_final)

                                        

print('Complete!')                                        

                                        
