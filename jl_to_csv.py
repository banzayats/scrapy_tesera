#!/usr/bin/env python

import unicodecsv as csv
import json, sys

def main():
    if len(sys.argv) != 3:
        sys.exit("No json and/or csv file given")
		
    jsonpath = sys.argv[1]
    csvpath = sys.argv[2]
	
    jsonfile = open(jsonpath, "r")
	
    with open(csvpath, 'wb') as f:
	for i, item in enumerate(jsonfile):
            msg = json.loads(item)
	    w = csv.DictWriter(f,msg.keys())
            if i == 0:
                w.writeheader()
            w.writerow(msg)  
			
if __name__ == "__main__":
    main()
