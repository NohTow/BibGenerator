# BibGenerator
BibGenerator is a script used to generate .bib from a list of paper. 
It uses the API made available by DBPL (http://dblp.org/search/publ/api) to search for references given names contained in the list.

# Usage
Edit the liste.txt file to fill it with your papers names, one per line. Then, just run bibcreator.py by entering
```
python bibcreator.py
```
Then, each paper will be checked and, if multiple references are found, you will be asked to choose by entering the number next to the one you want to choose (or -1 if you want to choose none).

During this process, a file named "export.bib", which contained your references and some warnings if no reference has been found/added for a given paper.

This is to let you complete the .bib if needed, but if you want to suppress these warnings, just run the script using the option --warning=false as such : 
```
python bibcreator.py --warning=false
```
