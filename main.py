#Organic Compound Analyser V2
#Features:
#Branch-type, straight-chain and cyclo types are implemented to this version.
#Also includes Alcohols
#No proper imaging system...yet
#Has a feature to scan for allotropes of a formula.
#Cleaner code, easier to debug.
#A proper menu

import re

print("""Welcome to the organic compounder V.2
        (c) 2016
        Please use organic molecules responsibly""")

#Defined lists
prefixes = ["meth", "eth", "prop", "but", "pent", "hex", "hept", "oct", "non", "dec", " "]

def scan(compound):
    compound = list(compound)
    moleculeType = ""
    #Compound Iteration
    #1. Test for normal Alk-
    if compound[0].isdigit() == True:
        moleculeType = "Alk"
        iterating_term = ""
        for x in compound:
            if x == "-":
                pass
            elif x.isdigit() == True:
                pass
            else:
                iterating_term = iterating_term + x
        for x in prefix_list:
            if x  + "ane" == iterating_term:
                moleculeType = moleculeType + "ane"
            elif x  + "ene" == iterating_term:
                moleculeType = moleculeType + "ene"
            elif x  + "yne" == iterating_term:
                moleculeType = moleculeType + "yne"
    else:
        print("Type not included in system yet...")
        return

def allotropes():
    atoms = {}
    compounds = []
    formula = input("Type in your formula, this program will find it's allotropes!\n>>")
    display = input("Do you want an advanced view for each of your allotropes? (Y/n)")
    
    if display.upper() == "Y" or display == "":
        display = True
    else:
        display = False
        
    #Make a list of parts    
    atoms["C"] = int(re.findall(r'C\d+', formula).strip("С"))
    atoms["H"] = int(re.findall(r'H\d+', formula).strip("H"))
    
    #Start with straight alkane, # of hydrogens always * 2 + 2 than carbon
    if atoms["C"] * 2 + 2 == atoms["H"]:
        type = "a"
        
    #Next straight alkene, # of hydrogens always * 2 than carbon
    if atoms["C"] * 2 == atoms["H"]:
        type = "e"
        
    #Lastly straight alkyne, # of hydrogens always * 2 - 2 than carbon
    if atoms["C"] * 2 - 2 == atoms["H"]:
        type = "y"
    
    #Add straight molecule to list, there can be only one
    compounds.append("%s%sne" % (prefixes, type))
        
        
        
    if not compounds:
        print("No organic molecules can be made using the formula %s" % formula)
        return
        
    for compound in compounds:
        if display:
            scan(compound)
        else:
            print(compound)
    
#Menu
while True:
    sector = input("Which sector would you like to use?\n
    \t[F]ind all the allotropes of a formula\n
    \t[S]can an organic compound to find all about it")
    #Navigation to each sector
    if sector.lower() == "f":
        allotropes()
        
    elif sector.lower() == "s":
        scan(input("Type in your compound and this program will define it!\n>>") + " ")
        
