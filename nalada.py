#import random
def pocit(nalada):

    nalada = str(input("jak se dnes cítíš?"))

    #nalada = random.choice(nalada)

    print("mám se", nalada)

    if nalada == "dobře":
        print("tak to rád slyším")
    elif nalada == "špatně":
        print("tak to mě mrzí")
    else:
        print("tak to joooo")
pocit("nalada")

