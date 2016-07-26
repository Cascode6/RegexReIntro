import re

FILE = "darmik.txt"


# Here, we initialize our search patterns. Think of these as a first filter level 
darmok = re.compile("darmok", re.IGNORECASE)
enterprise = re.compile("enterprise", re.IGNORECASE)


picardLines = re.compile('KIRK')

# same name, different place
rikerLines = re.compile('anakin:', re.IGNORECASE)
rikerNamed = re.compile(': anakin', re.IGNORECASE)

# non-digit characters
syn = re.compile(r'\{')
tax = re.compile(r'\}')



# Our Example Function
def parse():
    # open your file to parse it! Regex works with strings
    with open(FILE, "r") as f:
        text = f.read()

        # Calling match will determine if the beginning of the string matches the pattern called
        title = darmok.match(text)
        if title:
            print(title.span()) #prints the starting and ending index in the string
            print(title.group()) #prints the search term
        else:
            print("title Not Found!")

        # If it doesn't: 
        title = enterprise.match(text)
        if title:
            print(title.span())
            print(title.group())
        else:
            print("title Not Found!")

        # Search will scan the whole document, not stopping at the beginning of the string
        thisEpisode = enterprise.search(text)
        if thisEpisode:
            print(thisEpisode.span())
            print(thisEpisode.group())
        else:
            print("Enterprise Not Found!")
        
        
        # Findall will return all instances matching the pattern:
        wrongLines = picardLines.findall(text)
        if wrongLines:
            pass
            # print(wrongLines)
        else:
            print("Must've been Kirk")

        # To replace them, we use the search pattern, our desired replacement, and pass in the string we want changed

        text = re.sub(picardLines, "PICARD", text)
        print(text[271:277])

        
        # to find the index of the first pattern match
        otherWrongLines = rikerLines.findall(text)
        if otherWrongLines:
            text = re.sub(rikerLines, "RIKER:", text)
            print(text[534:540])
        else:
            print("Must've been Anakin")
        
        justWrongName = rikerNamed.search(text).span()
        if justWrongName:
            text = re.sub(rikerNamed, ": Riker", text)
            print(text[3494:3502])
        else:
            print("Must've been Anakin")


        if syn.findall(text):
            text = re.sub(syn, "[", text)
        
        if tax.findall(text):
            text = re.sub(tax, "]", text)



        # Important note: calling "sub" on the text won't change the original document!
        # To save our changes to the file, we have to write it to file:
        with open("darmokCorrected.txt", "w") as d:
            d.write(text)
        
        f.close()
        d.close()


# a good example of when to use re and regex rather than the native string searches
phonePattern = re.compile(r'''
                # don't match beginning of string, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    ''', re.VERBOSE)

parse()