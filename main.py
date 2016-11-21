#Organic Compound Analyser V2
#Features:
#Branch-type, straight-chain and cyclo types are implemented to this version.
#Also includes Alcohols
#No proper imaging system...yet
#Has a feature to scan for allotropes of a formula.
#Cleaner code, easier to debug.
#A proper menu

import re
import math

print("""Welcome to the organic compounder V.2
        (c) 2016
        Please use organic molecules responsibly\n""")

#Defined vars
prefixes = ["meth", "eth", "prop", "but", "pent", "hex", "hept", "oct", "non", "dec", " "]
bnd = "-"
dble_bnd = "="
trpl_bnd = "?"
side_bnd1 = "/"
side_bnd2 = "\\"
dble_side_bnd = "/2"
dble_side_bnd2 = "\\2"
trpl_side_bnd = "/3"
trpl_side_bnd2 = "\\3"

def odd_cyclo (x, y):
    horizontal_joint = "--"
    vertical_joint = "|"
def scan(compound):
    while True:
        name = compound
        compound = compound + " "
        compound = list(compound.lower())
        iterating_term = ""
        prefix = ""
        suffix = ""
        prefix_list = ["meth", "eth", "prop", "but", "pent", "hex", "hept", "oct", "non", "dec"]
        num_indicator = 0
        branch_value = 0
        carbon_value = 0
        carbon_atom_value = 0
        straight_chain = False
        branch_type = False
        #Iterating loop to define the sections of the hydrocarbon.
        for x in compound:
            if x == "-":
                    pass
            try:
                numberA = int(x)
                num_indicator = num_indicator + 1
                if num_indicator == 0:
                    carbon_value = carbon_value + numberA
                elif num_indicator == 1:
                    branch_value = branch_value + carbon_value
                    carbon_value = numberA
                else:
                    print("Malfunctioning...")
            except:
                if x == "-":
                    pass
                else:
                    iterating_term = iterating_term + x
            for x in prefix_list:
                if x + "yl" == iterating_term:
                    branch_type = True
                elif x  + "ane" == iterating_term:
                    straight_chain = True
                    suffix = "ane"
                    prefix = x
                elif x  + "ene" == iterating_term:
                    straight_chain = True
                    suffix = "ene"
                    prefix = x
                elif x  + "yne" == iterating_term:
                    straight_chain = True
                    suffix = "yne"
                    prefix = x
        #Idiot-proof.
        if branch_type and straight_chain == False:
            print("Malfunctioning...")
            break
        elif branch_type == True:
            pass
        elif straight_chain == True:
            pass
        elif suffix == "ene" or "yne" and carbon_value < 2:
            print("This is not a valid hydrocarbon. Try again.")
            print("(Error: -ene or -yne suffixes can't have less than 2 carbon atoms.)")
            continue
        elif carbon_value or branch_value == 0:
            print("This is not a valid hydrocarbon. Try again.")
            print("(Error: bond position or branch position can't be 0)")
            continue
        else:
            pass
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
        #Interface
        print("Hydrocarbon: {}".format(name))
        print("Specs:")
        if branch_type == True:
            print("Branch-type hydrocarbon.")
        elif straight_chain == True:
            print("Straight-chain type hydrocarbon")
        print("Note: '3-' in the display means a triple bond")
        #setting up values
        value_carbon = 0
        value_hydrogen = 0
        single_bond_value = 0
        double_bond_value = 0
        triple_bond_value = 0
        #Prefix values
        if prefix == "meth":
            value_carbon = value_carbon + 1
        elif prefix == "eth":
            value_carbon = value_carbon + 2
        elif prefix == "prop":
            value_carbon = value_carbon + 3
        elif prefix == "but":
            value_carbon = value_carbon + 4
        elif prefix == "pent":
            value_carbon = value_carbon + 5
        elif prefix == "hex":
            value_carbon = value_carbon + 6
        elif prefix == "hept":
            value_carbon = value_carbon + 7
        elif prefix == "oct":
            value_carbon = value_carbon + 8
        elif prefix == "non":
            value_carbon = value_carbon + 9
        elif prefix == "dec":
            value_carbon = value_carbon + 10
        #Detemining value_hydrogen
        if suffix == "ane":
            value_hydrogen = value_carbon * 2 + 2
            single_bond_value = single_bond_value + value_hydrogen + value_carbon - 1
        elif suffix == "ene":
            value_hydrogen = value_carbon * 2
            double_bond_value = double_bond_value + 1
            single_bond_value = single_bond_value + value_hydrogen + value_carbon - 2
        elif suffix == "yne":
            value_hydrogen = value_carbon * 2 - 2
            single_bond_value = single_bond_value + value_hydrogen + value_carbon - 2

            
def allotropes():
    atoms = {}
    compounds = []
    formula = input("Type in your formula, this program will find it's allotropes!\n>>")
    display = input("Do you want an advanced view for each of your allotropes? (Y/n)\n>>")
    
    if display.upper() == "Y" or display == "":
        display = True
    else:
        display = False
        
    #Make a list of parts
    atoms["C"] = int((re.search(r'C\d+', formula).group()).strip("C"))
    atoms["H"] = int((re.search(r'H\d+', formula).group()).strip("H"))
    
    #Start with straight alkane, # of hydrogens always * 2 + 2 than carbon
    if atoms["C"] * 2 + 2 == atoms["H"]:
        compounds.append("%sane" % prefixes[atoms["C"]])
    
    #Check that alkenes and alkynes have at least 2 atoms
    if atoms["C"] >= 2:    
        #Next straight alkene, # of hydrogens always * 2 than carbon
        if atoms["C"] * 2 == atoms["H"]:
            typ = "e"
            
        #Lastly straight alkyne, # of hydrogens always * 2 - 2 than carbon
        if atoms["C"] * 2 - 2 == atoms["H"]:
            typ = "y"
        
        if typ:
            for i in range(1, math.floor(atoms["C"]/2) + 1):
                compounds.append("%s%s%sne" % (str(i) + "-", prefixes[atoms["C"]], typ))
        
        
    if not compounds:
        print("No organic molecules can be made using the formula %s" % formula)
        return
        
    for compound in compounds:
        if display:
            scan(compound)
        else:
            print(compound)
    print("\n\n")
    
#Menu
while True:
    sector = input("""Which sector would you like to use?
    [F]ind all the allotropes of a formula
    [S]can an organic compound to find all about it
>>""")
    #Navigation to each sector
    if sector.lower() == "f":
        allotropes()
        
    elif sector.lower() == "s":
        compound = input("Name your compound, and we will scan it and draw it:\t")
        scan(compound)
        
#Moved the vars to the top