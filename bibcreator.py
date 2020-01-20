import requests as rq
import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--warning", help="Print if no entry has been found for a paper in the .bib", default="true")
    writer = BibTexWriter()
    liste = open("liste.txt","r")
    res = open("references.bib","w")
    line = liste.readline()
    while line:
        line = line.replace(" ","+").replace(",","")
        r = rq.post("http://dblp.org/search/publ/api?q="+line+"&format=bib")
        if(r.text != ""):
            db = BibDatabase()
            bib_database = bibtexparser.loads(r.text)
            #print(bib_database.entries[0])
            if(len(bib_database.entries) > 1):
                for i in range(0, len(bib_database.entries)):
                    print(str(i)+" : "+str(bib_database.entries[i]))
                choice = -2
                while(-1 > choice or choice > len(bib_database.entries)-1):
                    choice = int(input('Which reference do you want to add ? (-1 for none) : '))
                if(choice == -1 ):
                    print("No reference has been added for \""+line.replace("+"," ")+"\"")
                    if(parser.parse_args().warning == "true"):
                        res.write("WARNING : No reference added for \""+line.replace("+"," ")+"\"")

                else:
                    temp = []
                    temp.append(bib_database.entries[int(choice)]) 
                    print(temp)
                    db.entries = temp 
                    res.write(writer.write(db))  
            #if(bib.database.entries)
            else:
                temp = []
                temp.append(bib_database.entries[0])
                db.entries = temp
                print(db.entries[0])
                res.write(writer.write(db))
        else:
            print("No result found for \""+line.replace("+"," ")+"\"")
            if(parser.parse_args().warning == "true"):
                res.write("WARNING : No reference found for \""+line.replace("+"," ")+"\"")
        line = liste.readline()
        #res.write(r.text)
    
if __name__ == "__main__":
    main()
	
