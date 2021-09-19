import sys
import csv
from configparser import ConfigParser

ini = ConfigParser()
ini.read('config_nnf_assembler_test.ini')

#Find all keys in the INI file to build a row template and
#include a "game" field to store the section name.
rowTemplate = {}
for sec in ini.sections():
   for key,value in ini.items(sec):
       rowTemplate[key] = value
print(rowTemplate)

#Write to csv file
f = open('config_nnf_assembler_test.csv', 'w')

for sec in ini.sections():
   row = rowTemplate.copy()
   f.write("%s,%s\n"%(sec,''))
   for key,value in ini.items(sec):
       f.write("%s,%s\n"%(key,row[key]))


f.close()

