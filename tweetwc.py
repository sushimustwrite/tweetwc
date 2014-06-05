#############
#
# Copyright 2014 sushimustwrite
# This script is licensed under the MIT License. http://opensource.org/licenses/MIT
#
#############

'''Counts the words of your tweets. Run this script with: python tweetswc.py yourtextfile.txt'''

import csv
from sys import argv

MY_FILE = "/path/to/your/tweets.csv"

txtfile = argv

def parse(raw_file, delimiter):
    
    #open csv
    opened_file = open(raw_file)
    
    csv_data = csv.reader(opened_file,delimiter=delimiter)

    wcfile = open(argv[1], 'w') #open my text file
    
    #grab specific value in csv file (the one with the tweet)
    for row in csv_data:
        if row[6] != '':  
            continue
        
        else:
            wcfile.write(row[5]+'\n') #write the row number containing the tweet to wcfile
            
    
    #close files
    opened_file.close()
    wcfile.close()

def main():
    parse(MY_FILE,",")

if __name__ == "__main__":
    main()
