#Organic Compound Analyser V2
#Features:
#Branch-type, straight-chain and cyclo types are implemented to this version.
#Also includes Alcohols
#No proper imaging system...yet
#Has a feature to scan for allotropes of a formula.
#Cleaner code, easier to debug.
#A proper menu

print("\t\tWelcome to the organic compounder V.2\n
(c) 2016\n
Please use organic molecules responsibly\n\n\n")

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
    formula = input("Type in your formula, this program will find it's allotropes!\n>>")
    display = input("Do you want an advanced view for each of your allotropes? (Y/n)")
    if display.upper() == "Y" or display == "":
        display = True
    else:
        display = False
    #Make a list of parts    
    formulalist = formula.split("C")
    formulalist = formulalist[0].split("H") + formulalist
    #Start with straight alkane
    
    
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
        
