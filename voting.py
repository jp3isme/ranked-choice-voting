# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 18:18:24 2020

@author: John-Michael
"""
import csv
import os
import sys, getopt

def main(argv):
   dirname = os.path.dirname(__file__)
   inputfile = ''
   
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
   except getopt.GetoptError:
      print ('votes.py -i <inputfile>')
      sys.exit(2)
   if len(opts) == 0:
      print ('votes.py -i <inputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('votes.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
         
   print ('Input file is ' + inputfile)
   scores = {}
   
   filepath = os.path.join(dirname, inputfile)
   with open(filepath, "r", encoding="UTF-8-sig") as votes:
        csv_reader = csv.reader(votes, delimiter='\t')
        next(csv_reader) # skip header
        for row in csv_reader:
            choice = len(row) -1 # first choice gets most points
            for item in row[1:]:
                if item in scores:
                    scores[item] += choice
                else:
                    scores[item] = choice
                choice -= 1 # each choice lower gets one fewer point

   scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
   for i in scores:
    	print(i[1], i[0])

if __name__ == "__main__":
   main(sys.argv[1:])


