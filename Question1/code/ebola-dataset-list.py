# Script to query HDX for a list of datasets
# and return CSV table.

import sys
import csv
import yajl as json
import requests as r
from termcolor import colored as color

#librairie supplementaire
from bs4 import BeautifulSoup
import urllib
import datetime

# Fetch arguments from command line.
if __name__ == '__main__':
	if len(sys.argv) <= 1:
	    usage = '''
	    Please provide a CSV path.

	    python code/ebola-dataset-list.py {path/to/file.csv}

	    e.g.

	    python code/ebola-dataset-list.py data/data.csv
	    '''
	    print(usage)
	    sys.exit(1)

	csv_path = sys.argv[1]

# Get list of datasets form HDX.
def getDatasetListforTag(num_table = None, l = None, verbose = False):


	print "----------------------------------"

	page=soup = BeautifulSoup(urllib.urlopen("http://missingmigrants.iom.int/latest-global-figures").read())
	tables=soup.find_all("table")
	lesrecords=[]
	count_table=0
	for table in tables:#recuperation des tables
		count_table+=1
		if count_table==num_table:#la table demander
			trs=table.find_all("tr")
			ligne=[]
			for tr in trs:
				ligne=[]
				for td in tr.find_all("td"):
					value=""
					if td.span!=None:
						if td.span.span!=None:
							value=td.span.span.get_text()
						else:
							value=td.span.get_text()
					else:
						value=0
					if value=="-":
						value=0
					ligne.append(value)
				ligne.append("http://missingmigrants.iom.int/latest-global-figures")
				ligne.append("methodology")
				ligne.append(datetime.datetime.now())
				ligne.append("")
				ligne.append("")
				ligne.append("")



				lesrecords.append(ligne)


	d=True

	if d is True:
		m = color("SUCCESS", "green", attrs=['bold'])
		n = color((len(lesrecords)-1), "blue", attrs=['dark'])
		print "%s : processing %s records." % (m, n)

        f = csv.writer(open(l, "w"))

        # Write headers.
        f.writerow(["","January", "February", "March", "April","May", "June", "July", "August", "September", "October","November","December","Month not specified","Total","source","methodology", "date of dataset", "location", "caveats",  "comments"])

        # Write records.
        record_counter = 0
        for record in lesrecords:
			#print (dataset)
			record_counter += 1
			try:
			    f.writerow(record)

			except Exception as e:
				err = color("ERROR", "red", attrs=['bold'])
				rec = color(record_counter, "yellow", attrs=['bold'])
				print "%s : record %s failed to write." % (err, rec)
				f.writerow([
			    	"NA",
			    	"NA",
			    	"NA",
			    	"NA",
			    	"NA",
			    	"NA",
			    	"NA",
			    	"NA",
			    	"NA",
			    	"NA"
			    	])

				# Printing more detailed error messages.
				if verbose is True:
					print e

	print "----------------------------------"
	print "************* %s ***************" % (color("DONE", "blue", attrs=['blink','bold']))
	print "----------------------------------"


# Running the function.
getDatasetListforTag(2, csv_path, verbose = False)
