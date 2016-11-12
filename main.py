#Hydrocarbon Wiki v1

#Functionality:
#-Only does branch and straight-chain type hydrocarbons.
#-Has diagram creation.
#-Prefixes range from Meth- to Dec-.
#-Cyclo types are not implemented.

#import time

print("\t\tWelcome to the organic compounder\n(c) 2016\nPlease use organic molecules responsibly\n\n\n")

while True:
    compound = input("Type in your hydrocarbon!\nThis program will define it!\n>>")
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
            elif x  + "ane"== iterating_term:
                straight_chain = True
                suffix = "ane"
                prefix = x
            elif x  + "ene"== iterating_term:
                straight_chain = True
                suffix = "ene"
                prefix = x
            elif x  + "yne"== iterating_term:
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
        pring("(Error: bond position or branch position can't be 0)")
        continue
    else:
        pass
    #Interface
    print("Hydrocarbon: {}".format(name))
    print("Specs:")
    if branch_type == True:
        print("Branch-type hydrocarbon.")
    elif straight_chain == True:
        print("Straight-chain type hydrocarbon")
    print("Note: '3-' in the display means a triple bond")
    print("Hydrocarbon Structure:")
    bond_vertical = " | "
    double_bond_vertical = "| |"
    triple_bond_vertical = "(|)"
    bond_horizontal = "- -"
    double_bond_horizontal = "= ="
    triple_bond_horizontal = "3 -"
    bond_diagonal_left = "//" #for cyclos later.
    bond_diagonal_right = "\\\\"
    space_filler = "   "
    carbon_atom = " C "
    hydrogen_atom = " H "
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
    #Display
    layer1 = []
    layer2 = []
    layer3 = []
    layer4 = []
    layer5 = []
    layer6 = []
    layer7 = []
    layer8 = []
    layer9 = []
    layerX = []
    carbon_position_counter = 0
    while True:
        if carbon_value < 0 and suffix == "ene" and carbon_position_counter == carbon_value:
            layer5.append(carbon_atom + double_bond_horizontal)
            carbon_position_counter = carbon_position_counter + 1
        elif carbon_value < 0 and suffix == "ene" and carbon_position_counter == carbon_value:

        else:
            layer5.append(carbon_atom + bond_horizontal)
            carbon_position_counter = carbon_position_counter + 1
            layer5.append(carbon_atom)

