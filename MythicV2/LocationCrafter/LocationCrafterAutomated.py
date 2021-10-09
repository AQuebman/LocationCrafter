import random
from logging import exception
from builtins import input
import sys

#Declaring Variables
Region_Descriptor = ''
Location_Size = ''
Location_PP = 0
Encounters_PP = 0
Objects_PP = 0
Region_Descriptor, Location_Size = input("Enter Wilderness, City, or Structure for region and Large or Small for location size    ").split()

def RegionDesc_LocationSize():   
    #Finding out from the user what region descriptor and location size is
    while True:
        try:
            print("\n")
            if Region_Descriptor.casefold() == "Wilderness".casefold() and Location_Size.casefold() == "Large".casefold():                     
                print("Region Descriptor: WILDERNESS  Location Size: LARGE")
                Wilderness_Descriptor_Table_Roll_One()
                break
            
            elif Region_Descriptor.casefold() == "Wilderness".casefold() and Location_Size.casefold() == "Small".casefold():
                print("Region Descriptor: WILDERNESS  Location Size: SMALL")
                Wilderness_Descriptor_Table_Roll_One()                
                break  
            
            elif Region_Descriptor.casefold() == "City".casefold() and Location_Size.casefold() == "Large".casefold():
                print("Region Descriptor: CITY  Location Size: LARGE")
                City_Descriptor_Table_Roll_One()
                break
            
            elif Region_Descriptor.casefold() == "City".casefold() and Location_Size.casefold() == "Small".casefold():
                print("Region Descriptor: CITY  Location Size: SMALL")
                City_Descriptor_Table_Roll_One()
                break
            
            elif Region_Descriptor.casefold() == "Structure".casefold() and Location_Size.casefold() == "Large".casefold():
                print("Region Descriptor: STRUCTURE  Location Size: LARGE")
                Structure_Descriptor_Table_Roll_One()
                break
            
            elif Region_Descriptor.casefold() == "Structure".casefold() and Location_Size.casefold() == "Small".casefold():
                print("Region Descriptor: STRUCTURE  Location Size: SMALL")
                Structure_Descriptor_Table_Roll_One()
                break
        
            else:
                print("Your entries are invalid try again")
        
        except ValueError as exception:
                print("Invalid Entries Try Again")
 

def Wilderness_Descriptor_Table_Roll_One():   
    #Rolling twice on the region descriptor tables and outputting result to the user         
    Wilderness_Region_Descriptor_Random_Roll_One = random.randint(1, 101)       
    while True:
        try:
            if Wilderness_Region_Descriptor_Random_Roll_One in range(1,6):
                Description_One = ("Dry and arid")
                print(Description_One)
                Wilderness_Descriptor_Table_Roll_Two()
                break
            
            elif Wilderness_Region_Descriptor_Random_Roll_One in range(6,11):
                Description_One = ("Wet")
                print(Description_One)
                Wilderness_Descriptor_Table_Roll_Two()
                break
            
            elif Wilderness_Region_Descriptor_Random_Roll_One in range(11,16):
                Description_One = ("Dense vegetation")
                print(Description_One)
                Wilderness_Descriptor_Table_Roll_Two()
                break
            
            elif Wilderness_Region_Descriptor_Random_Roll_One in range(16,21):
                Description_One = ("Rocky")
                print(Description_One)
                Wilderness_Descriptor_Table_Roll_Two()
                break
            
            elif Wilderness_Region_Descriptor_Random_Roll_One in range(21,26):
                Description_One = ("Lots of open space")
                print(Description_One)
                Wilderness_Descriptor_Table_Roll_Two()
                break
            
            elif Wilderness_Region_Descriptor_Random_Roll_One in range(26,31):
                Description_One = ("Sandy, dirty, or rough")
                print(Description_One)
                Wilderness_Descriptor_Table_Roll_Two()
                break
            
            elif Wilderness_Region_Descriptor_Random_Roll_One in range(31,36):
                Description_One = ("Barren")
                print(Description_One)
                Wilderness_Descriptor_Table_Roll_Two()
                break
            
            elif Wilderness_Region_Descriptor_Random_Roll_One in range(36,41):
                Description_One = ("Active natural elements, such as a volcano, waterfall, river, winds, rain, etc.")
                print(Description_One)
                Wilderness_Descriptor_Table_Roll_Two()
                break  
            
            elif Wilderness_Region_Descriptor_Random_Roll_One in range(41,46):
                Description_One = ("Hot")
                print(Description_One)
                Wilderness_Descriptor_Table_Roll_Two() 
                break   
            
            elif Wilderness_Region_Descriptor_Random_Roll_One in range(46,51):
                Description_One = ("Cold")
                print(Description_One)
                Wilderness_Descriptor_Table_Roll_Two()  
                break
            
            elif Wilderness_Region_Descriptor_Random_Roll_One in range(51,56):
                Description_One = ("Hilly or sloping")
                print(Description_One)
                Wilderness_Descriptor_Table_Roll_Two() 
                break  
            
            elif Wilderness_Region_Descriptor_Random_Roll_One in range(56,61):
                Description_One = ("Difficult to travel through")
                print(Description_One)
                Wilderness_Descriptor_Table_Roll_Two()
                break  
            
            elif Wilderness_Region_Descriptor_Random_Roll_One in range(61,66):
                Description_One = ("Plant life")
                print(Description_One)
                Wilderness_Descriptor_Table_Roll_Two()  
                break
            
            elif Wilderness_Region_Descriptor_Random_Roll_One in range(66,71):
                Description_One = ("Active animals")
                print(Description_One)
                Wilderness_Descriptor_Table_Roll_Two()  
                break
            
            elif Wilderness_Region_Descriptor_Random_Roll_One in range(71,76):
                Description_One = ("Mountainous")
                print(Description_One)
                Wilderness_Descriptor_Table_Roll_Two()
                break  
            
            elif Wilderness_Region_Descriptor_Random_Roll_One in range(76,81):
                Description_One = ("Cliffs")
                print(Description_One)
                Wilderness_Descriptor_Table_Roll_Two()  
                break
            
            elif Wilderness_Region_Descriptor_Random_Roll_One in range(81,86):
                Description_One = ("Dangerous -  the Region is obviously dangerous in some way")
                print(Description_One)
                Wilderness_Descriptor_Table_Roll_Two()  
                break
            
            elif Wilderness_Region_Descriptor_Random_Roll_One in range(86,91):
                Description_One = ("Body of water")
                print(Description_One)
                Wilderness_Descriptor_Table_Roll_Two()  
                break
            
            elif Wilderness_Region_Descriptor_Random_Roll_One in range(91,96):
                Description_One = ("Exotic - Something highly unusual about the region")
                print(Description_One)
                Wilderness_Descriptor_Table_Roll_Two()
                break  
        
            elif Wilderness_Region_Descriptor_Random_Roll_One in range(96,101):
                Meaning_Tables() 
                Wilderness_Descriptor_Table_Roll_Two()  
                break  
        
        except ValueError as exception:
                print("Invalid Entries Try Again")


def Wilderness_Descriptor_Table_Roll_Two():   
    #Rolling twice on the region descriptor tables and outputting result to the user         
    Wilderness_Region_Descriptor_Random_Roll_Two = random.randint(1,101)
    while True:
        try:
            if Wilderness_Region_Descriptor_Random_Roll_Two in range(1,6):
                Description_Two = ("Dry and arid")
                print(Description_Two)
                break
            
            elif Wilderness_Region_Descriptor_Random_Roll_Two in range(6,11):
                Description_Two = ("Wet")
                print(Description_Two)
                break
            
            elif Wilderness_Region_Descriptor_Random_Roll_Two in range(11,16):
                Description_Two = ("Dense vegetation")
                print(Description_Two)
                break
            
            elif Wilderness_Region_Descriptor_Random_Roll_Two in range(16,21):
                Description_Two = ("Rocky")
                print(Description_Two)
                break
            
            elif Wilderness_Region_Descriptor_Random_Roll_Two in range(21,26):
                Description_Two = ("Lots of open space")
                print(Description_Two)
                break
            
            elif Wilderness_Region_Descriptor_Random_Roll_Two in range(26,31):
                Description_Two = ("Sandy, dirty, or rough")
                print(Description_Two)
                break
            
            elif Wilderness_Region_Descriptor_Random_Roll_Two in range(31,36):
                Description_Two = ("Barren")
                print(Description_Two)
                break
            
            elif Wilderness_Region_Descriptor_Random_Roll_Two in range(36,41):
                Description_Two = ("Active natural elements, such as a volcano, waterfall, river, winds, rain, etc.")
                print(Description_Two)
                break  
            
            elif Wilderness_Region_Descriptor_Random_Roll_Two in range(41,46):
                Description_Two = ("Hot")
                print(Description_Two)
                break    
            
            elif Wilderness_Region_Descriptor_Random_Roll_Two in range(46,51):
                Description_Two = ("Cold")
                print(Description_Two)
                break  
            
            elif Wilderness_Region_Descriptor_Random_Roll_Two in range(51,56):
                Description_Two = ("Hilly or sloping")
                print(Description_Two)
                break   
            
            elif Wilderness_Region_Descriptor_Random_Roll_Two in range(56,61):
                Description_Two = ("Difficult to travel through")
                print(Description_Two)
                break  
            
            elif Wilderness_Region_Descriptor_Random_Roll_Two in range(61,66):
                Description_Two = ("Plant life")
                print(Description_Two)
                break  
            
            elif Wilderness_Region_Descriptor_Random_Roll_Two in range(66,71):
                Description_Two = ("Active animals")
                print(Description_Two)
                break  
            
            elif Wilderness_Region_Descriptor_Random_Roll_Two in range(71,76):
                Description_Two = ("Mountainous")
                print(Description_Two)
                break  
            
            elif Wilderness_Region_Descriptor_Random_Roll_Two in range(76,81):
                Description_Two = ("Cliffs")
                print(Description_Two)
                break  
            
            elif Wilderness_Region_Descriptor_Random_Roll_Two in range(81,86):
                Description_Two = ("Dangerous -  the Region is obviously dangerous in some way")
                print(Description_Two)
                break  
            
            elif Wilderness_Region_Descriptor_Random_Roll_Two in range(86,91):
                Description_Two = ("Body of water")
                print(Description_Two)
                break  
            
            elif Wilderness_Region_Descriptor_Random_Roll_Two in range(91,96):
                Description_Two = ("Exotic - Something highly unusual about the region")
                print(Description_Two)
                break  
            
            elif Wilderness_Region_Descriptor_Random_Roll_Two in range(96,101):
                Meaning_Tables()
                break       
            
            else:
                print("Your entries are invalid try again")
        except ValueError as exception:
                print("Invalid Entries Try Again")



def City_Descriptor_Table_Roll_One(): 
    #Rolling twice on the region descriptor tables and outputting result to the user         
    City_Region_Descriptor_Random_Roll_One = random.randint(1, 101)       
    while True:
        try:
            if City_Region_Descriptor_Random_Roll_One in range(1,6):
                Description_One = ("Sprawling and large")
                print(Description_One)
                City_Descriptor_Table_Roll_Two()
                break
            
            elif City_Region_Descriptor_Random_Roll_One in range(6,11):
                Description_One = ("Simple and sparse")
                print(Description_One)
                City_Descriptor_Table_Roll_Two()
                break
            
            elif City_Region_Descriptor_Random_Roll_One in range(11,16):
                Description_One = ("Modern")
                print(Description_One)
                City_Descriptor_Table_Roll_Two()
                break
            
            elif City_Region_Descriptor_Random_Roll_One in range(16,21):
                Description_One = ("Old")
                print(Description_One)
                City_Descriptor_Table_Roll_Two()
                break
            
            elif City_Region_Descriptor_Random_Roll_One in range(21,26):
                Description_One = ("Thriving or bustling")
                print(Description_One)
                City_Descriptor_Table_Roll_Two()
                break
            
            elif City_Region_Descriptor_Random_Roll_One in range(26,31):
                Description_One = ("Inactive or abandoned")
                print(Description_One)
                City_Descriptor_Table_Roll_Two()
                break
            
            elif City_Region_Descriptor_Random_Roll_One in range(31,36):
                Description_One = ("Quiet, sleepy")
                print(Description_One)
                City_Descriptor_Table_Roll_Two()
                break
            
            elif City_Region_Descriptor_Random_Roll_One in range(36,41):
                Wilderness_Descriptor_Table_Roll_Two()
                City_Descriptor_Table_Roll_Two()
                break  
            
            elif City_Region_Descriptor_Random_Roll_One in range(41,46):
                Description_One = ("Dangerous -  the Region is obviously dangerous in some way")
                print(Description_One)
                City_Descriptor_Table_Roll_Two() 
                break   
            
            elif City_Region_Descriptor_Random_Roll_One in range(46,51):
                Description_One = ("Well ordered and organized")
                print(Description_One)
                City_Descriptor_Table_Roll_Two()  
                break
            
            elif City_Region_Descriptor_Random_Roll_One in range(51,56):
                Description_One = ("In crisis - The City is experiencing an obvious crisis of some kind.")
                print(Description_One)
                City_Descriptor_Table_Roll_Two() 
                break  
            
            elif City_Region_Descriptor_Random_Roll_One in range(56,61):
                Description_One = ("Crumbling or run down")
                print(Description_One)
                City_Descriptor_Table_Roll_Two()
                break  
            
            elif City_Region_Descriptor_Random_Roll_One in range(61,66):
                Description_One = ("Wealthy and booming")
                print(Description_One)
                City_Descriptor_Table_Roll_Two()  
                break
            
            elif City_Region_Descriptor_Random_Roll_One in range(66,71):
                Description_One = ("Densely populated")
                print(Description_One)
                City_Descriptor_Table_Roll_Two()  
                break
            
            elif City_Region_Descriptor_Random_Roll_One in range(71,76):
                Description_One = ("Clean")
                print(Description_One)
                City_Descriptor_Table_Roll_Two()
                break  
            
            elif City_Region_Descriptor_Random_Roll_One in range(76,81):
                Description_One = ("Friendly")
                print(Description_One)
                City_Descriptor_Table_Roll_Two()  
                break
            
            elif City_Region_Descriptor_Random_Roll_One in range(81,86):
                Description_One = ("Hostile")
                print(Description_One)
                City_Descriptor_Table_Roll_Two()  
                break
            
            elif City_Region_Descriptor_Random_Roll_One in range(86,91):
                Description_One = ("Specific purpose - The City or Structure exists for a specific purpose that is evident.")
                print(Description_One)
                City_Descriptor_Table_Roll_Two()  
                break
            
            elif City_Region_Descriptor_Random_Roll_One in range(91,96):
                Description_One = ("Exotic - Something highly unusual about the region")
                print(Description_One)
                City_Descriptor_Table_Roll_Two()
                break  
            
            elif City_Region_Descriptor_Random_Roll_One in range(96,101):
                City_Descriptor_Table_Roll_Two()
                Meaning_Tables()   
                break  
        
        except ValueError as exception:
                print("Invalid Entries Try Again")

def City_Descriptor_Table_Roll_Two(): 
    #Rolling twice on the region descriptor tables and outputting result to the user         
    City_Region_Descriptor_Random_Roll_Two = random.randint(1,101)
    while True:
        try:
            if City_Region_Descriptor_Random_Roll_Two in range(1,6):
                Description_Two = ("Sprawling and large")
                print(Description_Two)
                break
            
            elif City_Region_Descriptor_Random_Roll_Two in range(6,11):
                Description_Two = ("Simple and sparse")
                print(Description_Two)
                break
            
            elif City_Region_Descriptor_Random_Roll_Two in range(11,16):
                Description_Two = ("Modern")
                print(Description_Two)
                break
            
            elif City_Region_Descriptor_Random_Roll_Two in range(16,21):
                Description_Two = ("Old")
                print(Description_Two)
                break
            
            elif City_Region_Descriptor_Random_Roll_Two in range(21,26):
                Description_Two = ("Thriving or bustling")
                print(Description_Two)
                break
            
            elif City_Region_Descriptor_Random_Roll_Two in range(26,31):
                Description_Two = ("Inactive or abandoned")
                print(Description_Two)
                break
            
            elif City_Region_Descriptor_Random_Roll_Two in range(31,36):
                Description_Two = ("Quiet, sleepy")
                print(Description_Two)
                break
            
            elif City_Region_Descriptor_Random_Roll_Two in range(36,41):
                Wilderness_Descriptor_Table_Roll_Two()
                break  
            
            elif City_Region_Descriptor_Random_Roll_Two in range(41,46):
                Description_Two = ("Dangerous -  the Region is obviously dangerous in some way")
                print(Description_Two)
                break    
            
            elif City_Region_Descriptor_Random_Roll_Two in range(46,51):
                Description_Two = ("Well ordered and organized")
                print(Description_Two)
                break  
            
            elif City_Region_Descriptor_Random_Roll_Two in range(51,56):
                Description_Two = ("In crisis - The City is experiencing an obvious crisis of some kind.")
                print(Description_Two)
                break   
            
            elif City_Region_Descriptor_Random_Roll_Two in range(56,61):
                Description_Two = ("Crumbling or run down")
                print(Description_Two)
                break  
            
            elif City_Region_Descriptor_Random_Roll_Two in range(61,66):
                Description_Two = ("Wealthy and booming")
                print(Description_Two)
                break  
            
            elif City_Region_Descriptor_Random_Roll_Two in range(66,71):
                Description_Two = ("Densely populated")
                print(Description_Two)
                break  
            
            elif City_Region_Descriptor_Random_Roll_Two in range(71,76):
                Description_Two = ("Clean")
                print(Description_Two)
                break  
            
            elif City_Region_Descriptor_Random_Roll_Two in range(76,81):
                Description_Two = ("Friendly")
                print(Description_Two)
                break  
            
            elif City_Region_Descriptor_Random_Roll_Two in range(81,86):
                Description_Two = ("Hostile")
                print(Description_Two)
                break  
            
            elif City_Region_Descriptor_Random_Roll_Two in range(86,91):
                Description_Two = ("Specific purpose - The City or Structure exists for a specific purpose that is evident.")
                print(Description_Two)
                break  
            
            elif City_Region_Descriptor_Random_Roll_Two in range(91,96):
                Description_Two = ("Exotic - Something highly unusual about the region")
                print(Description_Two)
                break  
            
            elif City_Region_Descriptor_Random_Roll_Two in range(96,101):
                Meaning_Tables()
                break    
               
            else:
                print("Your entries are invalid try again")
        except ValueError as exception:
                print("Invalid Entries Try Again")

def Structure_Descriptor_Table_Roll_One(): 
    #Rolling twice on the region descriptor tables and outputting result to the user         
    Structure_Region_Descriptor_Random_Roll_One = random.randint(1, 101)       
    while True:
        try:
            
            if Structure_Region_Descriptor_Random_Roll_One in range(1,6):
                Description_One = ("Well made and tended")
                print(Description_One)
                Structure_Descriptor_Table_Roll_Two()
                break
            
            elif Structure_Region_Descriptor_Random_Roll_One in range(6,11):
                Description_One = ("Run down")
                print(Description_One)
                Structure_Descriptor_Table_Roll_Two()
                break
            
            elif Structure_Region_Descriptor_Random_Roll_One in range(11,16):
                Description_One = ("Busy")
                print(Description_One)
                Structure_Descriptor_Table_Roll_Two()
                break
            
            elif Structure_Region_Descriptor_Random_Roll_One in range(16,21):
                Description_One = ("Inactive or abandoned")
                print(Description_One)
                Structure_Descriptor_Table_Roll_Two()
                break
            
            elif Structure_Region_Descriptor_Random_Roll_One in range(21,26):
                Description_One = ("Ancient, of a bygone era")
                print(Description_One)
                Structure_Descriptor_Table_Roll_Two()
                break
            
            elif Structure_Region_Descriptor_Random_Roll_One in range(26,31):
                Description_One = ("Old")
                print(Description_One)
                Structure_Descriptor_Table_Roll_Two()
                break
            
            elif Structure_Region_Descriptor_Random_Roll_One in range(31,36):
                Description_One = ("Modern")
                print(Description_One)
                Structure_Descriptor_Table_Roll_Two()
                break
            
            elif Structure_Region_Descriptor_Random_Roll_One in range(36,41):
                Wilderness_Descriptor_Table_Roll_Two()
                Structure_Descriptor_Table_Roll_Two()
                break  
            
            elif Structure_Region_Descriptor_Random_Roll_One in range(41,46):
                Description_One = ("Simple or small")
                print(Description_One)
                Structure_Descriptor_Table_Roll_Two() 
                break   
            
            elif Structure_Region_Descriptor_Random_Roll_One in range(46,51):
                Description_One = ("Tall or large")
                print(Description_One)
                Structure_Descriptor_Table_Roll_Two()  
                break
            
            elif Structure_Region_Descriptor_Random_Roll_One in range(51,56):
                Description_One = ("Imposing")
                print(Description_One)
                Structure_Descriptor_Table_Roll_Two() 
                break  
            
            elif Structure_Region_Descriptor_Random_Roll_One in range(56,61):
                Description_One = ("Welcoming")
                print(Description_One)
                Structure_Descriptor_Table_Roll_Two()
                break  
            
            elif Structure_Region_Descriptor_Random_Roll_One in range(61,66):
                Description_One = ("Functional - the Structure itself is a type of machine.")
                print(Description_One)
                Structure_Descriptor_Table_Roll_Two()  
                break
            
            elif Structure_Region_Descriptor_Random_Roll_One in range(66,71):
                Description_One = ("Quiet")
                print(Description_One)
                Structure_Descriptor_Table_Roll_Two()  
                break
            
            elif Structure_Region_Descriptor_Random_Roll_One in range(71,76):
                Description_One = ("Sturdy")
                print(Description_One)
                Structure_Descriptor_Table_Roll_Two()
                break  
            
            elif Structure_Region_Descriptor_Random_Roll_One in range(76,81):
                Description_One = ("Dangerous")
                print(Description_One)
                Structure_Descriptor_Table_Roll_Two()  
                break
            
            elif Structure_Region_Descriptor_Random_Roll_One in range(81,86):
                Description_One = ("Occupied")
                print(Description_One)
                Structure_Descriptor_Table_Roll_Two()  
                break
            
            elif Structure_Region_Descriptor_Random_Roll_One in range(86,91):
                Description_One = ("Specific purpose - The Structure or Structure exists for a specific purpose that is evident.")
                print(Description_One)
                Structure_Descriptor_Table_Roll_Two()  
                break
            
            elif Structure_Region_Descriptor_Random_Roll_One in range(91,96):
                Description_One = ("Exotic - Something highly unusual about the region")
                print(Description_One)
                Structure_Descriptor_Table_Roll_Two()
                break  
        
            elif Structure_Region_Descriptor_Random_Roll_One in range(96,101):
                Structure_Descriptor_Table_Roll_Two()
                Meaning_Tables()   
                break  
        
        except ValueError as exception:
                print("Invalid Entries Try Again")

def Structure_Descriptor_Table_Roll_Two(): 
    #Rolling twice on the region descriptor tables and outputting result to the user         
    Structure_Region_Descriptor_Random_Roll_Two = random.randint(1,101)
    while True:
        try:
            if Structure_Region_Descriptor_Random_Roll_Two in range(1,6):
                Description_Two = ("Well made and tended")
                print(Description_Two)
                break
            
            elif Structure_Region_Descriptor_Random_Roll_Two in range(6,11):
                Description_Two = ("Run down")
                print(Description_Two)
                break
            
            elif Structure_Region_Descriptor_Random_Roll_Two in range(11,16):
                Description_Two = ("Busy")
                print(Description_Two)
                break
            
            elif Structure_Region_Descriptor_Random_Roll_Two in range(16,21):
                Description_Two = ("Inactive or abandoned")
                print(Description_Two)
                break
            
            elif Structure_Region_Descriptor_Random_Roll_Two in range(21,26):
                Description_Two = ("Ancient, of a bygone era")
                print(Description_Two)
                break
            
            elif Structure_Region_Descriptor_Random_Roll_Two in range(26,31):
                Description_Two = ("Old")
                print(Description_Two)
                break
            
            elif Structure_Region_Descriptor_Random_Roll_Two in range(31,36):
                Description_Two = ("Modern")
                print(Description_Two)
                break
            
            elif Structure_Region_Descriptor_Random_Roll_Two in range(36,41):
                Wilderness_Descriptor_Table_Roll_Two()
                break  
            
            elif Structure_Region_Descriptor_Random_Roll_Two in range(41,46):
                Description_Two = ("Simple or small")
                print(Description_Two)
                break    
            
            elif Structure_Region_Descriptor_Random_Roll_Two in range(46,51):
                Description_Two = ("Tall or large")
                print(Description_Two)
                break  
            
            elif Structure_Region_Descriptor_Random_Roll_Two in range(51,56):
                Description_Two = ("Imposing")
                print(Description_Two)
                break   
            
            elif Structure_Region_Descriptor_Random_Roll_Two in range(56,61):
                Description_Two = ("Welcoming")
                print(Description_Two)
                break  
            
            elif Structure_Region_Descriptor_Random_Roll_Two in range(61,66):
                Description_Two = ("Functional - the Structure itself is a type of machine.")
                print(Description_Two)
                break  
            
            elif Structure_Region_Descriptor_Random_Roll_Two in range(66,71):
                Description_Two = ("Quiet")
                print(Description_Two)
                break  
            
            elif Structure_Region_Descriptor_Random_Roll_Two in range(71,76):
                Description_Two = ("Sturdy")
                print(Description_Two)
                break  
            
            elif Structure_Region_Descriptor_Random_Roll_Two in range(76,81):
                Description_Two = ("Dangerous")
                print(Description_Two)
                break  
            
            elif Structure_Region_Descriptor_Random_Roll_Two in range(81,86):
                Description_Two = ("Occupied")
                print(Description_Two)
                break  
            
            elif Structure_Region_Descriptor_Random_Roll_Two in range(86,91):
                Description_Two = ("Specific purpose - The City or Structure exists for a specific purpose that is evident.")
                print(Description_Two)
                break  
            
            elif Structure_Region_Descriptor_Random_Roll_Two in range(91,96):
                Description_Two = ("Exotic - Something highly unusual about the region")
                print(Description_Two)
                break  
            
            elif Structure_Region_Descriptor_Random_Roll_Two in range(96,101):
                Meaning_Tables()
                break       
            
            else:
                print("Your entries are invalid try again")
        except ValueError as exception:
                print("Invalid Entries Try Again")

#Tables for when 96-100 is rolled for the Region Descriptors Table    
def Meaning_Tables(): 
    while True:
        try:
            Meaning_Tables_Random_Roll_Two = random.randint(1,101)
            Meaning_Tables_Random_Roll_One = random.randint(1,101)
            
            if Meaning_Tables_Random_Roll_One == 1:
                Description_One = ("Description Meaning: Abnormally")
                print(Description_One)
                break
            
            elif Meaning_Tables_Random_Roll_One == 2:
                Description_One = ("Description Meaning: Adventurously")
                print(Description_One)
                break
            
            elif Meaning_Tables_Random_Roll_One == 3:
                Description_One = ("Description Meaning: Aggressively")
                print(Description_One)
                break
            
            elif Meaning_Tables_Random_Roll_One == 4:
                Description_One = ("Description Meaning: Angrily")
                print(Description_One)
                break
            
            elif Meaning_Tables_Random_Roll_One == 5:
                Description_One = ("Description Meaning: Anxiously")
                print(Description_One)
                break
            
            elif Meaning_Tables_Random_Roll_One == 6:
                Description_One = ("Description Meaning: Awkwardly")
                print(Description_One)
                break
            
            elif Meaning_Tables_Random_Roll_One == 7:
                Description_One = ("Description Meaning: Beautifully")
                print(Description_One)
                break       
            
            elif Meaning_Tables_Random_Roll_One == 8:
                Description_One = ("Description Meaning: Bleakly")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 9:
                Description_One = ("Description Meaning: Boldly")
                print(Description_One)
                break   
            
            elif Meaning_Tables_Random_Roll_One == 10:
                Description_One = ("Description Meaning: Bravely")
                print(Description_One)
                break 
            
            elif Meaning_Tables_Random_Roll_One == 11:
                Description_One = ("Description Meaning: Busily")
                print(Description_One)
                break   
            
            elif Meaning_Tables_Random_Roll_One == 12:
                Description_One = ("Description Meaning: Calmly")
                print(Description_One)
                break     
            
            elif Meaning_Tables_Random_Roll_One == 13:
                Description_One = ("Description Meaning: Carefully")
                print(Description_One)
                break         
            
            elif Meaning_Tables_Random_Roll_One == 14:
                Description_One = ("Description Meaning: Carelessly")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 15:
                Description_One = ("Description Meaning: Cautiously")
                print(Description_One)
                break      
            
            elif Meaning_Tables_Random_Roll_One == 16:
                Description_One = ("Description Meaning: Ceaselessly")
                print(Description_One)
                break   
            
            elif Meaning_Tables_Random_Roll_One == 17:
                Description_One = ("Description Meaning: Cheerfully")
                print(Description_One)
                break   
           
            elif Meaning_Tables_Random_Roll_One == 18:
                Description_One = ("Description Meaning: Combatively")
                print(Description_One)
                break      
            
            elif Meaning_Tables_Random_Roll_One == 19:
                Description_One = ("Description Meaning: Coolly")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 20:
                Description_One = ("Description Meaning: Crazily")
                print(Description_One)
                break    
            
            elif Meaning_Tables_Random_Roll_One == 21:
                Description_One = ("Description Meaning: Curiously")
                print(Description_One)
                break 
            
            elif Meaning_Tables_Random_Roll_One == 22:
                Description_One = ("Description Meaning: Daintily")
                print(Description_One)
                break        
            
            elif Meaning_Tables_Random_Roll_One == 23:
                Description_One = ("Description Meaning: Dangerously")
                print(Description_One)
                break   
            
            elif Meaning_Tables_Random_Roll_One == 24:
                Description_One = ("Description Meaning: Defiantly")
                print(Description_One)
                break 
            
            elif Meaning_Tables_Random_Roll_One == 25:
                Description_One = ("Description Meaning: Deliberately")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 26:
                Description_One = ("Description Meaning: Delightfully")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 27:
                Description_One = ("Description Meaning: Dimly")
                print(Description_One)
                break   
            
            elif Meaning_Tables_Random_Roll_One == 28:
                Description_One = ("Description Meaning: Efficiently")
                print(Description_One)
                break     
            
            elif Meaning_Tables_Random_Roll_One == 29:
                Description_One = ("Description Meaning: Energetically")
                print(Description_One)
                break    
            
            elif Meaning_Tables_Random_Roll_One == 30:
                Description_One = ("Description Meaning: Enormously")
                print(Description_One)
                break     
            
            elif Meaning_Tables_Random_Roll_One == 31:
                Description_One = ("Description Meaning: Enthusiastically")
                print(Description_One)
                break   
            
            elif Meaning_Tables_Random_Roll_One == 32:
                Description_One = ("Description Meaning: Excitedly")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 33:
                Description_One = ("Description Meaning: Fearfully")
                print(Description_One)
                break    
            
            elif Meaning_Tables_Random_Roll_One == 34:
                Description_One = ("Description Meaning: Ferociously")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 35:
                Description_One = ("Description Meaning: Fiercely")
                print(Description_One)
                break       
            
            elif Meaning_Tables_Random_Roll_One == 36:
                Description_One = ("Description Meaning: Foolishly")
                print(Description_One)
                break    
            
            elif Meaning_Tables_Random_Roll_One == 37:
                Description_One = ("Description Meaning: Fortunately")
                print(Description_One)
                break   
            
            elif Meaning_Tables_Random_Roll_One == 38:
                Description_One = ("Description Meaning: Frantically")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 39:
                Description_One = ("Description Meaning: Freely")
                print(Description_One)
                break   
            
            elif Meaning_Tables_Random_Roll_One == 40:
                Description_One = ("Description Meaning: Frighteningly")
                print(Description_One)
                break   
            
            elif Meaning_Tables_Random_Roll_One == 41:
                Description_One = ("Description Meaning: Fully")
                print(Description_One)
                break     
            
            elif Meaning_Tables_Random_Roll_One == 42:
                Description_One = ("Description Meaning: Generously")
                print(Description_One)
                break 
            
            elif Meaning_Tables_Random_Roll_One == 43:
                Description_One = ("Description Meaning: Gently")
                print(Description_One)
                break    
            
            elif Meaning_Tables_Random_Roll_One == 44:
                Description_One = ("Description Meaning: Gladly")
                print(Description_One)
                break 
            
            elif Meaning_Tables_Random_Roll_One == 45:
                Description_One = ("Description Meaning: Gracefully")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 46:
                Description_One = ("Description Meaning: Gratefully")
                print(Description_One)
                break  
           
            elif Meaning_Tables_Random_Roll_One == 47:
                Description_One = ("Description Meaning: Happily")
                print(Description_One)
                break    
            
            elif Meaning_Tables_Random_Roll_One == 48:
                Description_One = ("Description Meaning: Hastily")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 49:
                Description_One = ("Description Meaning: Healthily")
                print(Description_One)
                break   
            
            elif Meaning_Tables_Random_Roll_One == 50:
                Description_One = ("Description Meaning: Helpfully")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 51:
                Description_One = ("Description Meaning: Helplessly")
                print(Description_One)
                break   
            
            elif Meaning_Tables_Random_Roll_One == 52:
                Description_One = ("Description Meaning: Hopelessly")
                print(Description_One)
                break    
            
            elif Meaning_Tables_Random_Roll_One == 53:
                Description_One = ("Description Meaning: Innocently")
                print(Description_One)
                break 
            
            elif Meaning_Tables_Random_Roll_One == 54:
                Description_One = ("Description Meaning: Intensely")
                print(Description_One)
                break 
            
            elif Meaning_Tables_Random_Roll_One == 55:
                Description_One = ("Description Meaning: Interestingly")
                print(Description_One)
                break   
            
            elif Meaning_Tables_Random_Roll_One == 56:
                Description_One = ("Description Meaning: Irritatingly")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 57:
                Description_One = ("Description Meaning: Jovially")
                print(Description_One)
                break    
            
            elif Meaning_Tables_Random_Roll_One == 58:
                Description_One = ("Description Meaning: Joyfully")
                print(Description_One)
                break 
            
            elif Meaning_Tables_Random_Roll_One == 59:
                Description_One = ("Description Meaning: Judgementally")
                print(Description_One)
                break 
            
            elif Meaning_Tables_Random_Roll_One == 60:
                Description_One = ("Description Meaning: Kindly")
                print(Description_One)
                break 
            
            elif Meaning_Tables_Random_Roll_One == 61:
                Description_One = ("Description Meaning: Kookily")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 62:
                Description_One = ("Description Meaning: Lazily")
                print(Description_One)
                break 
            
            elif Meaning_Tables_Random_Roll_One == 63:
                Description_One = ("Description Meaning: Lightly")
                print(Description_One)
                break    
            
            elif Meaning_Tables_Random_Roll_One == 64:
                Description_One = ("Description Meaning: Loosely")
                print(Description_One)
                break   
            
            elif Meaning_Tables_Random_Roll_One == 65:
                Description_One = ("Description Meaning: Loudly")
                print(Description_One)
                break    
           
            elif Meaning_Tables_Random_Roll_One == 66:
                Description_One = ("Description Meaning: Lovingly")
                print(Description_One)
                break   
            
            elif Meaning_Tables_Random_Roll_One == 67:
                Description_One = ("Description Meaning: Loyally")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 68:
                Description_One = ("Description Meaning: Majestically")
                print(Description_One)
                break 
            
            elif Meaning_Tables_Random_Roll_One == 69:
                Description_One = ("Description Meaning: Meaningfully")
                print(Description_One)
                break   
            
            elif Meaning_Tables_Random_Roll_One == 70:
                Description_One = ("Description Meaning: Mechanically")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 71:
                Description_One = ("Description Meaning: Miserably")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 72:
                Description_One = ("Description Meaning: Mockingly")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 73:
                Description_One = ("Description Meaning: Mysteriously")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 74:
                Description_One = ("Description Meaning: Naturally")
                print(Description_One)
                break   
            
            elif Meaning_Tables_Random_Roll_One == 75:
                Description_One = ("Description Meaning: Neatly")
                print(Description_One)
                break   
            
            elif Meaning_Tables_Random_Roll_One == 76:
                Description_One = ("Description Meaning: Nicely")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 77:
                Description_One = ("Description Meaning: Oddly")
                print(Description_One)
                break     
            
            elif Meaning_Tables_Random_Roll_One == 78:
                Description_One = ("Description Meaning: Offensively")
                print(Description_One)
                break    
           
            elif Meaning_Tables_Random_Roll_One == 79:
                Description_One = ("Description Meaning: Officially")
                print(Description_One)
                break      
            
            elif Meaning_Tables_Random_Roll_One == 80:
                Description_One = ("Description Meaning: Partially")
                print(Description_One)
                break
            
            elif Meaning_Tables_Random_Roll_One == 81:
                Description_One = ("Description Meaning: Peacefully")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 82:
                Description_One = ("Description Meaning: Perfectly")
                print(Description_One)
                break   
           
            elif Meaning_Tables_Random_Roll_One == 83:
                Description_One = ("Description Meaning: Playfully")
                print(Description_One)
                break   
            
            elif Meaning_Tables_Random_Roll_One == 84:
                Description_One = ("Description Meaning: Politely")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 85:
                Description_One = ("Description Meaning: Positively")
                print(Description_One)
                break    
            
            elif Meaning_Tables_Random_Roll_One == 86:
                Description_One = ("Description Meaning: Powerfully")
                print(Description_One)
                break
            
            elif Meaning_Tables_Random_Roll_One == 87:
                Description_One = ("Description Meaning: Quaintly")
                print(Description_One)
                break   
           
            elif Meaning_Tables_Random_Roll_One == 88:
                Description_One = ("Description Meaning: Quarrelsomely")
                print(Description_One)
                break    
            
            elif Meaning_Tables_Random_Roll_One == 89:
                Description_One = ("Description Meaning: Quietly")
                print(Description_One)
                break     
           
            elif Meaning_Tables_Random_Roll_One == 90:
                Description_One = ("Description Meaning: Roughly")
                print(Description_One)
                break    
            
            elif Meaning_Tables_Random_Roll_One == 91:
                Description_One = ("Description Meaning: Rudely")
                print(Description_One)
                break  
           
            elif Meaning_Tables_Random_Roll_One == 92:
                Description_One = ("Description Meaning: Ruthlessly")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 93:
                Description_One = ("Description Meaning: Slowly")
                print(Description_One)
                break   
            
            elif Meaning_Tables_Random_Roll_One == 94:
                Description_One = ("Description Meaning: Softly")
                print(Description_One)
                break 
           
            elif Meaning_Tables_Random_Roll_One == 95:
                Description_One = ("Description Meaning: Swiftly")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 96:
                Description_One = ("Description Meaning: Threateningly")
                print(Description_One)
                break 
           
            elif Meaning_Tables_Random_Roll_One == 97:
                Description_One = ("Description Meaning: Very")
                print(Description_One)
                break      
           
            elif Meaning_Tables_Random_Roll_One == 98:
                Description_One = ("Description Meaning: Violently")
                print(Description_One)
                break 
            
            elif Meaning_Tables_Random_Roll_One == 99:
                Description_One = ("Description Meaning: Wildly")
                print(Description_One)
                break  
            
            elif Meaning_Tables_Random_Roll_One == 100:
                Description_One = ("Description Meaning: Yieldingly")
                print(Description_One)
                break                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            
            else:
                print("Your entries are invalid try again")
        except ValueError as exception:
                print("Invalid Entries Try Again") 
                
    while True:
        try:
                if Meaning_Tables_Random_Roll_Two == 1:
                    Description_Two = ("Description Meaning #2: Abandoned")
                    print(Description_Two)
                    break
                
                elif Meaning_Tables_Random_Roll_Two == 2:
                    Description_Two = ("Description Meaning #2: Abnormal")
                    print(Description_Two)
                    break
                
                elif Meaning_Tables_Random_Roll_Two == 3:
                    Description_Two = ("Description Meaning #2: Amusing")
                    print(Description_Two)
                    break
                
                elif Meaning_Tables_Random_Roll_Two == 4:
                    Description_Two = ("Description Meaning #2: Ancient")
                    print(Description_Two)
                    break
                
                elif Meaning_Tables_Random_Roll_Two == 5:
                    Description_Two = ("Description Meaning #2: Aromatic")
                    print(Description_Two)
                    break
                
                elif Meaning_Tables_Random_Roll_Two == 6:
                    Description_Two = ("Description Meaning #2: Average")
                    print(Description_Two)
                    break
                
                elif Meaning_Tables_Random_Roll_Two == 7:
                    Description_Two = ("Description Meaning #2: Beautiful")
                    print(Description_Two)
                    break       
                
                elif Meaning_Tables_Random_Roll_Two == 8:
                    Description_Two = ("Description Meaning #2: Bizarre")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 9:
                    Description_Two = ("Description Meaning #2: Classy")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 10:
                    Description_Two = ("Description Meaning #2: Clean")
                    print(Description_Two)
                    break 
                
                elif Meaning_Tables_Random_Roll_Two == 11:
                    Description_Two = ("Description Meaning #2: Cold")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 12:
                    Description_Two = ("Description Meaning #2: Colorful")
                    print(Description_Two)
                    break     
                
                elif Meaning_Tables_Random_Roll_Two == 13:
                    Description_Two = ("Description Meaning #2: Creepy")
                    print(Description_Two)
                    break         
                
                elif Meaning_Tables_Random_Roll_Two == 14:
                    Description_Two = ("Description Meaning #2: Cute")
                    print(Description_Two)
                    break  
               
                elif Meaning_Tables_Random_Roll_Two == 15:
                    Description_Two = ("Description Meaning #2: Damaged")
                    print(Description_Two)
                    break      
                
                elif Meaning_Tables_Random_Roll_Two == 16:
                    Description_Two = ("Description Meaning #2: Dark")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 17:
                    Description_Two = ("Description Meaning #2: Defeated")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 18:
                    Description_Two = ("Description Meaning #2: Delicate")
                    print(Description_Two)
                    break      
                
                elif Meaning_Tables_Random_Roll_Two == 19:
                    Description_Two = ("Description Meaning #2: Delightful")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 20:
                    Description_Two = ("Description Meaning #2: Dirty")
                    print(Description_Two)
                    break    
                
                elif Meaning_Tables_Random_Roll_Two == 21:
                    Description_Two = ("Description Meaning #2: Disagreeable")
                    print(Description_Two)
                    break 
                
                elif Meaning_Tables_Random_Roll_Two == 22:
                    Description_Two = ("Description Meaning #2: Disgusting")
                    print(Description_Two)
                    break        
                
                elif Meaning_Tables_Random_Roll_Two == 23:
                    Description_Two = ("Description Meaning #2: Drab")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 24:
                    Description_Two = ("Description Meaning #2: Dry")
                    print(Description_Two)
                    break 
                
                elif Meaning_Tables_Random_Roll_Two == 25:
                    Description_Two = ("Description Meaning #2: Dull")
                    print(Description_Two)
                    break  
               
                elif Meaning_Tables_Random_Roll_Two == 26:
                    Description_Two = ("Description Meaning #2: Empty")
                    print(Description_Two)
                    break  
               
                elif Meaning_Tables_Random_Roll_Two == 27:
                    Description_Two = ("Description Meaning #2: Enormous")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 28:
                    Description_Two = ("Description Meaning #2: Exotic")
                    print(Description_Two)
                    break     
               
                elif Meaning_Tables_Random_Roll_Two == 29:
                    Description_Two = ("Description Meaning #2: Faded")
                    print(Description_Two)
                    break    
                
                elif Meaning_Tables_Random_Roll_Two == 30:
                    Description_Two = ("Description Meaning #2: Familiar")
                    print(Description_Two)
                    break     
                
                elif Meaning_Tables_Random_Roll_Two == 31:
                    Description_Two = ("Description Meaning #2: Fancy")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 32:
                    Description_Two = ("Description Meaning #2: Fat")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 33:
                    Description_Two = ("Description Meaning #2: Feeble")
                    print(Description_Two)
                    break    
                
                elif Meaning_Tables_Random_Roll_Two == 34:
                    Description_Two = ("Description Meaning #2: Feminine")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 35:
                    Description_Two = ("Description Meaning #2: Festive")
                    print(Description_Two)
                    break       
                
                elif Meaning_Tables_Random_Roll_Two == 36:
                    Description_Two = ("Description Meaning #2: Flawless")
                    print(Description_Two)
                    break    
                
                elif Meaning_Tables_Random_Roll_Two == 37:
                    Description_Two = ("Description Meaning #2: Fresh")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 38:
                    Description_Two = ("Description Meaning #2: Full")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 39:
                    Description_Two = ("Description Meaning #2: Glorious")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 40:
                    Description_Two = ("Description Meaning #2: Good")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 41:
                    Description_Two = ("Description Meaning #2: Graceful")
                    print(Description_Two)
                    break     
                
                elif Meaning_Tables_Random_Roll_Two == 42:
                    Description_Two = ("Description Meaning #2: Hard")
                    print(Description_Two)
                    break 
                
                elif Meaning_Tables_Random_Roll_Two == 43:
                    Description_Two = ("Description Meaning #2: Harsh")
                    print(Description_Two)
                    break    
                
                elif Meaning_Tables_Random_Roll_Two == 44:
                    Description_Two = ("Description Meaning #2: Healthy")
                    print(Description_Two)
                    break 
                
                elif Meaning_Tables_Random_Roll_Two == 45:
                    Description_Two = ("Description Meaning #2: Heavy")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 46:
                    Description_Two = ("Description Meaning #2: Historical")
                    print(Description_Two)
                    break  
               
                elif Meaning_Tables_Random_Roll_Two == 47:
                    Description_Two = ("Description Meaning #2: Horrible")
                    print(Description_Two)
                    break    
                
                elif Meaning_Tables_Random_Roll_Two == 48:
                    Description_Two = ("Description Meaning #2: Important")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 49:
                    Description_Two = ("Description Meaning #2: Interesting")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 50:
                    Description_Two = ("Description Meaning #2: Juvenile")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 51:
                    Description_Two = ("Description Meaning #2: Lacking")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 52:
                    Description_Two = ("Description Meaning #2: Lame")
                    print(Description_Two)
                    break    
                
                elif Meaning_Tables_Random_Roll_Two == 53:
                    Description_Two = ("Description Meaning #2: Large")
                    print(Description_Two)
                    break 
                
                elif Meaning_Tables_Random_Roll_Two == 54:
                    Description_Two = ("Description Meaning #2: Lavish")
                    print(Description_Two)
                    break 
                
                elif Meaning_Tables_Random_Roll_Two == 55:
                    Description_Two = ("Description Meaning #2: Lean")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 56:
                    Description_Two = ("Description Meaning #2: Less")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 57:
                    Description_Two = ("Description Meaning #2: Lethal")
                    print(Description_Two)
                    break    
                
                elif Meaning_Tables_Random_Roll_Two == 58:
                    Description_Two = ("Description Meaning #2: Lonely")
                    print(Description_Two)
                    break 
                
                elif Meaning_Tables_Random_Roll_Two == 59:
                    Description_Two = ("Description Meaning #2: Lovely")
                    print(Description_Two)
                    break 
                
                elif Meaning_Tables_Random_Roll_Two == 60:
                    Description_Two = ("Description Meaning #2: Macabre")
                    print(Description_Two)
                    break 
                
                elif Meaning_Tables_Random_Roll_Two == 61:
                    Description_Two = ("Description Meaning #2: Magnificent")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 62:
                    Description_Two = ("Description Meaning #2: Masculine")
                    print(Description_Two)
                    break 
                
                elif Meaning_Tables_Random_Roll_Two == 63:
                    Description_Two = ("Description Meaning #2: Mature")
                    print(Description_Two)
                    break    
                
                elif Meaning_Tables_Random_Roll_Two == 64:
                    Description_Two = ("Description Meaning #2: Messy")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 65:
                    Description_Two = ("Description Meaning #2: Mighty")
                    print(Description_Two)
                    break    
                
                elif Meaning_Tables_Random_Roll_Two == 66:
                    Description_Two = ("Description Meaning #2: Military")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 67:
                    Description_Two = ("Description Meaning #2: Modern")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 68:
                    Description_Two = ("Description Meaning #2: Extravagant")
                    print(Description_Two)
                    break 
                
                elif Meaning_Tables_Random_Roll_Two == 69:
                    Description_Two = ("Description Meaning #2: Mundane")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 70:
                    Description_Two = ("Description Meaning #2: Mysterious")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 71:
                    Description_Two = ("Description Meaning #2: Natural")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 72:
                    Description_Two = ("Description Meaning #2: Nondescript")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 73:
                    Description_Two = ("Description Meaning #2: Odd")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 74:
                    Description_Two = ("Description Meaning #2: Pale")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 75:
                    Description_Two = ("Description Meaning #2: Petite")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 76:
                    Description_Two = ("Description Meaning #2: Poor")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 77:
                    Description_Two = ("Description Meaning #2: Powerful")
                    print(Description_Two)
                    break     
                
                elif Meaning_Tables_Random_Roll_Two == 78:
                    Description_Two = ("Description Meaning #2: Quaint")
                    print(Description_Two)
                    break    
                
                elif Meaning_Tables_Random_Roll_Two == 79:
                    Description_Two = ("Description Meaning #2: Rare")
                    print(Description_Two)
                    break      
                
                elif Meaning_Tables_Random_Roll_Two == 80:
                    Description_Two = ("Description Meaning #2: Reassuring")
                    print(Description_Two)
                    break
                
                elif Meaning_Tables_Random_Roll_Two == 81:
                    Description_Two = ("Description Meaning #2: Remarkable")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 82:
                    Description_Two = ("Description Meaning #2: Rotten")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 83:
                    Description_Two = ("Description Meaning #2: Rough")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 84:
                    Description_Two = ("Description Meaning #2: Ruined")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 85:
                    Description_Two = ("Description Meaning #2: Rustic")
                    print(Description_Two)
                    break    
                
                elif Meaning_Tables_Random_Roll_Two == 86:
                    Description_Two = ("Description Meaning #2: Scary")
                    print(Description_Two)
                    break
                
                elif Meaning_Tables_Random_Roll_Two == 87:
                    Description_Two = ("Description Meaning #2: Simple")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 88:
                    Description_Two = ("Description Meaning #2: Small")
                    print(Description_Two)
                    break    
                
                elif Meaning_Tables_Random_Roll_Two == 89:
                    Description_Two = ("Description Meaning #2: Smelly")
                    print(Description_Two)
                    break     
                
                elif Meaning_Tables_Random_Roll_Two == 90:
                    Description_Two = ("Description Meaning #2: Smooth")
                    print(Description_Two)
                    break    
                
                elif Meaning_Tables_Random_Roll_Two == 91:
                    Description_Two = ("Description Meaning #2: Soft")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 92:
                    Description_Two = ("Description Meaning #2: Strong")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 93:
                    Description_Two = ("Description Meaning #2: Tranquil")
                    print(Description_Two)
                    break   
                
                elif Meaning_Tables_Random_Roll_Two == 94:
                    Description_Two = ("Description Meaning #2: Ugly")
                    print(Description_Two)
                    break 
                
                elif Meaning_Tables_Random_Roll_Two == 95:
                    Description_Two = ("Description Meaning #2: Valuable")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 96:
                    Description_Two = ("Description Meaning #2: Warlike")
                    print(Description_Two)
                    break 
                
                elif Meaning_Tables_Random_Roll_Two == 97:
                    Description_Two = ("Description Meaning #2: Warm")
                    print(Description_Two)
                    break      
                
                elif Meaning_Tables_Random_Roll_Two == 98:
                    Description_Two = ("Description Meaning #2: Watery")
                    print(Description_Two)
                    break 
                
                elif Meaning_Tables_Random_Roll_Two == 99:
                    Description_Two = ("Description Meaning #2: Weak")
                    print(Description_Two)
                    break  
                
                elif Meaning_Tables_Random_Roll_Two == 100:
                    Description_Two = ("Description Meaning #2: Young")
                    print(Description_Two)
                    break                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                else:
                    print("Your entries are invalid try again")
        except ValueError as exception:
                    print("Invalid Entries Try Again")


def Known_Elements(): 
#Asking the user for any known elements and then outputting the answer to the console
    known = []
    i = 1
    while i < 99:
        a = input("\n""List any known elements for this area:  ")
        known.append(a)
        i+=1
        if a == '':
            break
    known = list(filter(None, known))    
    print(str(known))
    Area_Location(known)
    
def Area_Location(known):
    if Location_Size.casefold() == "LARGE".casefold():
            Large_Location(known)
    elif Location_Size.casefold() == "Small".casefold():
            Small_Location(known)

def Large_Location(known):        
    Large_Location_Die = random.randint(1, 11)
    global Location_PP
    global Encounters_PP
    global Objects_PP
    Large_Location_Die = Large_Location_Die + Location_PP

    while True:
        try:
            if Large_Location_Die in range(1,6):
                print("LARGE LOCATION = Expected - what you most expect for this category at this time")
                Location_PP = Location_PP + 1
                Encounters(known)
            
            elif Large_Location_Die in range(6,9):
                print("LARGE LOCATION = Expected - what you most expect for this category at this time")
                Location_PP = Location_PP + 1
                Encounters(known)
            
            elif Large_Location_Die in range(9,11): 
                print("LARGE LOCATION = Random - Location inspired by the following random element descriptors")             
                Location_Element_Descriptors()
                Location_PP = Location_PP + 1
                Encounters(known) 
            
            elif Large_Location_Die in range(11, 12):
                Location_PP = Location_PP + 1
                Large_Location_Number_11 = input("Is this a Known area or Random Location?  ").casefold()
                if Large_Location_Number_11.casefold() == "Known".casefold() and (str(known)) != '[]':
                        print(str(known))
                        KnownInput = input("Pick which known applies  ").casefold()
                        while KnownInput not in known:
                            print("Known selection not in list")
                            KnownInput = input("Pick a known that applies  ").casefold()
                        else:
                            print("Location:  ", end='') 
                            (print(KnownInput))
                            Encounters(known)
                            
                elif (str(known)) == '[]' and Large_Location_Number_11.casefold() == "Known".casefold():
                    print("No Known is Available, defaulting to expected")
                    print("LARGE LOCATION = Expected - what you most expect for this category at this time")
                    Encounters(known) 
                        
                elif Large_Location_Number_11.casefold() == "Random".casefold():
                    Location_Element_Descriptors()
                    Encounters(known)
            
            elif Large_Location_Die in range(12, 13):
                Location_PP = Location_PP + 1
                Large_Location_Number_12 = input("Is this a Known area or Expected Location?  ").casefold()
                
                if Large_Location_Number_12.casefold() == "Known".casefold() and (str(known)) != '[]':
                    print(str(known))
                    KnownInput = input("Pick which known applies  ").casefold()
                    while KnownInput not in known:
                        print("Known selection not in list")
                        KnownInput = input("Pick a known that applies  ").casefold()
                    else:
                        print("LOCATION:  ", end='')
                        (print(KnownInput))
                        Encounters(known)
                
                elif (str(known)) == '[]'and Large_Location_Number_12.casefold() == "Known".casefold():
                    print("No Known is Available, defaulting to expected")
                    print("LARGE LOCATION = Expected - what you most expect for this category at this time")
                    Encounters(known)
                    
                elif Large_Location_Number_12.casefold() == "Expected".casefold():
                    print("LARGE LOCATION = Expected - what you most expect for this category at this time")
                    Encounters(known)
            
            elif Large_Location_Die in range(13, 14): 
                #PP gets added in the special elements table             
                Special_Element_Table(known)
            
            elif Large_Location_Die in range(14, 16):
                Large_Location_Number_14_15 = input("Is there more to explore of this area, Yes or No?").casefold()
                if Large_Location_Number_14_15.casefold() == "yes".casefold():
                    Location_PP = Location_PP + 1
                    Encounters_PP = Encounters_PP + 1
                    Objects_PP = Objects_PP + 1
                    print("LARGE LOCATION: EXPECTED")
                    print("ENCOUNTERS: EXPECTED")
                    print("OBJECTS: EXPECTED")
                    Large_Location_Die = random.randint(1, 11) +Location_PP
                else:
                    print("Location is complete, exiting program")
                    sys. exit()
            
            elif Large_Location_Die in range(16, 999):
                print("LARGE LOCATION = Expected - what you most expect for this category at this time")
                Location_PP = Location_PP - 6
                Encounters(known)
            else:
                print("Your entries are invalid try again")                
        except ValueError as exception:
                print("Invalid Entries Try Again")


#Small Location Area Elements Table
def Small_Location(known):
    Small_Location_Die = random.randint(1, 11)
    global Location_PP
    global Encounters_PP
    global Objects_PP
    Small_Location_Die = Small_Location_Die + Location_PP

    while True:
        try:
            if Small_Location_Die in range(1,6):
                print("SMALL LOCATION = Expected - what you most expect for this category at this time")
                Location_PP = Location_PP + 1
                Encounters(known)
            
            elif Small_Location_Die in range(6,9):
                print("SMALL LOCATION = Expected - what you most expect for this category at this time")
                Location_PP = Location_PP + 1
                Encounters(known)
            
            elif Small_Location_Die in range(9,11): 
                print("SMALL LOCATION = Random - Location inspired by the following random element descriptors")             
                Location_Element_Descriptors()
                Location_PP = Location_PP + 1
                Encounters(known) 
            
            elif Small_Location_Die in range(11, 12):
                Location_PP = Location_PP + 1
                Small_Location_Number_11 = input("Is this a Known area or Random Location?  ").casefold()
                if Small_Location_Number_11.casefold() == "Known".casefold() and (str(known)) != '[]':
                        print(str(known))
                        KnownInput = input("Pick which known applies  ").casefold()
                        while KnownInput not in known:
                            print("Known selection not in list")
                            KnownInput = input("Pick a known that applies  ").casefold()
                        else:
                            print("Location:  ", end='') 
                            (print(KnownInput))
                            Encounters(known)
                            
                elif (str(known)) == '[]'and Small_Location_Number_11.casefold() == "Known".casefold():
                    print("No Known is Available, defaulting to expected")
                    print("SMALL LOCATION = Expected - what you most expect for this category at this time")
                    Encounters(known) 
                        
                elif Small_Location_Number_11.casefold() == "Random".casefold():
                    Location_Element_Descriptors()
                    Encounters(known)
            
            elif Small_Location_Die in range(12, 13):
                Small_Location_Number_12 = input("Is there more to explore of this area, Yes or No?").casefold()
                if Small_Location_Number_12.casefold() == "yes".casefold():
                    Location_PP = Location_PP + 1
                    Encounters_PP = Encounters_PP + 1
                    Objects_PP = Objects_PP + 1
                    print("SMALL LOCATION: EXPECTED")
                    print("ENCOUNTERS: EXPECTED")
                    print("OBJECTS: EXPECTED")
                    Small_Location_Die = random.randint(1, 11) +Location_PP
                else:
                    print("Location is complete, exiting program")
                    sys. exit()    
                    
            elif Small_Location_Die in range(13, 14):
                Location_PP = Location_PP + 1
                Small_Location_Number_13 = input("Is this a Known area or Special Location?  ")     
                
                if Small_Location_Number_13.casefold() == "Known".casefold() and (str(known)) != '[]':
                        print(str(known))
                        KnownInput = input("Pick which known applies  ").casefold()
                        while KnownInput not in known:
                            print("Known selection not in list")
                            KnownInput = input("Pick a known that applies  ").casefold()
                        else:
                            print("Location:  ", end='') 
                            (print(KnownInput))
                            Encounters(known)
                            
                elif (str(known)) == '[]':
                    print("No Known is Available, defaulting to special")    
                    #PP gets added in the special elements table             
                    Special_Element_Table(known)
                
                elif Small_Location_Number_13.casefold() == "Special".casefold():
                    #PP gets added in the special elements table             
                    Special_Element_Table(known)
                    
                    
            elif Small_Location_Die in range(14, 16):
                Small_Location_Number_14_16 = input("Is there more to explore of this area, Yes or No?").casefold()
                if Small_Location_Number_14_16.casefold() == "yes".casefold():
                    Location_PP = Location_PP + 1
                    Encounters_PP = Encounters_PP + 1
                    Objects_PP = Objects_PP + 1
                    print("SMALL LOCATION: EXPECTED")
                    print("ENCOUNTERS: EXPECTED")
                    print("OBJECTS: EXPECTED")
                    Small_Location_Die = random.randint(1, 11) +Location_PP
                else:
                    print("Location is complete, exiting program")
                    sys. exit()    
                    
            elif Small_Location_Die in range(16, 999):
                print("SMALL LOCATION = Expected - what you most expect for this category at this time")
                Location_PP = Location_PP - 6
                Encounters(known)         

            else:
                print("Your entries are invalid try again")                
        except ValueError as exception:
                print("Invalid Entries Try Again") 

#Encounters Area Elements Table
def Encounters(known):
    Encounters_Element_Die = random.randint(1, 11)
    global Encounters_PP       
    Encounters_Element_Die = Encounters_Element_Die + Encounters_PP
    while True:
        try:
            if Encounters_Element_Die in range(1,6):
                print("ENCOUNTERS = None - There is no encounter element")
                Encounters_PP  = Encounters_PP + 1
                Objects(known)
            
            elif Encounters_Element_Die in range(6,9):
                print("ENCOUNTERS = Expected - what you most expect for this category at this time")
                Encounters_PP = Encounters_PP + 1
                Objects(known)
                
            elif Encounters_Element_Die in range(9,11):
                print("ENCOUNTERS = Random - Location inspired by the following random element descriptors")             
                Location_Element_Descriptors()
                Encounters_PP = Encounters_PP + 1
                Objects(known)
                
            elif Encounters_Element_Die in range(11, 12):
                Encounters_PP = Encounters_PP + 1
                Encounters_Element_Die_11 = input("Is this a Known area or Random Location?  ").casefold()
                if Encounters_Element_Die_11.casefold() == "Known".casefold() and (str(known)) != '[]':
                        print(str(known))
                        KnownInput = input("Pick which known applies  ").casefold()
                        while KnownInput not in known:
                            print("Known selection not in list")
                            KnownInput = input("Pick a known that applies  ").casefold()
                        else:
                            print("Location:  ", end='') 
                            (print(KnownInput))
                            Objects(known)
                            
                elif (str(known)) == '[]' and Encounters_Element_Die_11.casefold() == "Known".casefold():
                    print("No Known is Available, defaulting to expected")
                    print("ENCOUNTERS = Expected - what you most expect for this category at this time")
                    Objects(known) 
                        
                elif Encounters_Element_Die_11.casefold() == "Random".casefold():
                    Encounters_Element_Descriptors()
                    Objects(known)   
            
            elif Encounters_Element_Die in range(12, 13):
                print("ENCOUNTERS = None - There is no encounter element")
                Encounters_PP  = Encounters_PP + 1
                Objects(known)
                    
            elif Encounters_Element_Die in range(13, 14):
                Encounters_PP = Encounters_PP + 1
                Encounters_Element_Number_13 = input("Is this a Known area or Special Location?  ")     
                
                if Encounters_Element_Number_13.casefold() == "Known".casefold() and (str(known)) != '[]':
                        print(str(known))
                        KnownInput = input("Pick which known applies  ").casefold()
                        while KnownInput not in known:
                            print("Known selection not in list")
                            KnownInput = input("Pick a known that applies  ").casefold()
                        else:
                            print("ENCOUNTER:  ", end='') 
                            (print(KnownInput))
                            Objects(known)
                            
                elif (str(known)) == '[]':
                    print("No Known is Available, defaulting to special")    
                    #PP gets added in the special elements table             
                    Encounter_Special_Element_Table(known)
                
                elif Encounters_Element_Number_13.casefold() == "Special".casefold():
                    #PP gets added in the special elements table             
                    Encounter_Special_Element_Table(known)
                    
            elif Encounters_Element_Die in range(14, 16):
                print("ENCOUNTERS = Expected - what you most expect for this category at this time")
                Encounters_PP = Encounters_PP + 1
                Objects(known)
                
            elif Encounters_Element_Die in range(16, 999):
                print("ENCOUNTERS = Expected - what you most expect for this category at this time")
                Encounters_PP = Encounters_PP - 6
                Objects(known)
                  
            else:
                print("Your entries are invalid try again")
        except ValueError as exception:
                print("Invalid Entries Try Again")

#Objects Area Elements Table
def Objects(known):
    Objects_Element_Die = random.randint(1, 11)
    global Objects_PP
    Objects_Element_Die = Objects_Element_Die + Objects_PP
    while True:
        try:
            if Objects_Element_Die in range(1,6):
                print("OBJECTS = None - There is no object element")
                Objects_PP  = Objects_PP + 1
                input("\n Press a key when ready to move to the next area \n")
                Area_Location(known)
            
            elif Objects_Element_Die in range(6,9):
                print("OBJECTS = Expected - what you most expect for this category at this time")
                Objects_PP = Objects_PP + 1
                input("\n Press a key when ready to move to the next area \n")
                Area_Location(known)
                
            elif Objects_Element_Die in range(9,11):
                print("OBJECTS = Random - Location inspired by the following random element descriptors")             
                Objects_Element_Descriptors()
                Objects_PP = Objects_PP + 1
                input("\n Press a key when ready to move to the next area \n")
                Area_Location(known)
                
            elif Objects_Element_Die in range(11, 12):
                Objects_PP = Objects_PP + 1
                Objects_Element_Die_11 = input("Is this a Known area or Random Location?  ").casefold()
                if Objects_Element_Die_11.casefold() == "Known".casefold() and (str(known)) != '[]':
                        print(str(known))
                        KnownInput = input("Pick which known applies  ").casefold()
                        while KnownInput not in known:
                            print("Known selection not in list")
                            KnownInput = input("Pick a known that applies  ").casefold()
                        else:
                            print("Location:  ", end='') 
                            (print(KnownInput))
                            input("\n Press a key when ready to move to the next area \n")
                            Area_Location(known)
                            
                elif (str(known)) == '[]' and Objects_Element_Die_11.casefold() == "Known".casefold():
                    print("No Known is Available, defaulting to expected")
                    print("Object = Expected - what you most expect for this category at this time")
                    input("\n Press a key when ready to move to the next area \n")
                    Area_Location(known) 
                        
                elif Objects_Element_Die_11.casefold() == "Random".casefold():
                    Objects_Element_Descriptors()
                    input("\n Press a key when ready to move to the next area \n")
                    Area_Location(known)   
            
            elif Objects_Element_Die in range(12, 13):
                print("OBJECT = None - There is no object element")
                Objects_PP  = Objects_PP + 1
                input("\n Press a key when ready to move to the next area \n")                
                Area_Location(known)
                    
            elif Objects_Element_Die in range(13, 14):
                Objects_PP = Objects_PP + 1
                Objects_Element_Number_13 = input("Is this a Known area or Special Location?  ")     
                
                if Objects_Element_Number_13.casefold() == "Known".casefold() and (str(known)) != '[]':
                        print(str(known))
                        KnownInput = input("Pick which known applies  ").casefold()
                        while KnownInput not in known:
                            print("Known selection not in list")
                            KnownInput = input("Pick a known that applies  ").casefold()
                        else:
                            print("OBJECT:  ", end='') 
                            (print(KnownInput))
                            input("\n Press a key when ready to move to the next area \n")                            
                            Area_Location(known)
                            
                elif (str(known)) == '[]':
                    print("No Known is Available, defaulting to special")    
                    #PP gets added in the special elements table             
                    Objects_Special_Element_Table(known)
                
                elif Objects_Element_Number_13.casefold() == "Special".casefold():
                    #PP gets added in the special elements table             
                    Objects_Special_Element_Table(known)
                    
            elif Objects_Element_Die in range(14, 16):
                print("OBJECTS = Expected - what you most expect for this category at this time")
                Objects_PP = Objects_PP + 1
                input("\n Press a key when ready to move to the next area \n \n")                
                Area_Location(known)
                
            elif Objects_Element_Die in range(16, 999):
                print("OBJECTS = Expected - what you most expect for this category at this time")
                Objects_PP = Objects_PP - 6
                input("\n Press a key when ready to move to the next area \n \n")                
                Area_Location(known)
                  
            else:
                print("Your entries are invalid try again")
        except ValueError as exception:
                print("Invalid Entries Try Again")     
                
                
#Special Elements Table for when a Special Area Element is rolled
def Special_Element_Table(known):
    global Encounters_PP  
    global Objects_PP
    global Location_PP
    while True:
        try:
            Special_Element_Roll_One = random.randint(1,101)
            if Special_Element_Roll_One in range (1,11):
                
                if Location_Size.casefold() == "LARGE".casefold():
                    Location_PP = Location_PP + 1
                    print("SUPERSIZE: Enhance this Area Element:")
                    Special_Element_Large_Location(known)
                    Encounters(known)
                
                elif Location_Size.casefold() == "Small".casefold():
                    Location_PP = Location_PP + 1
                    print("SUPERSIZE: Enhance this Area Element:")
                    Special_Element_Small_Location(known)
                    Encounters(known)
            
            if Special_Element_Roll_One in range (11, 21):
                
                if Location_Size.casefold() == "LARGE".casefold():
                    Location_PP = Location_PP + 1
                    print("BARELY THERE: Minimize this Area Element:")
                    Special_Element_Large_Location(known)
                    Encounters(known)
                
                elif Location_Size.casefold() == "Small".casefold():
                    Location_PP = Location_PP + 1
                    print("BARELY THERE: Minimize this Area Element:")
                    Special_Element_Small_Location(known)
                    Encounters(known)
                    
            if Special_Element_Roll_One in range(21, 31):
                
                if Location_Size.casefold() == "LARGE".casefold():
                    Location_PP = Location_PP + 1
                    print("THIS IS BAD: This Area Element is BAD for the PC's:")
                    Special_Element_Large_Location(known)
                    Encounters(known)
                
                elif Location_Size.casefold() == "Small".casefold():
                    Location_PP = Location_PP + 1
                    print("THIS IS BAD: This Area Element is BAD for the PC's:")
                    Special_Element_Small_Location(known)
                    Encounters(known)
            
            if Special_Element_Roll_One in range(31, 41):
                
                if Location_Size.casefold() == "LARGE".casefold():
                    Location_PP = Location_PP + 1
                    print("THIS IS GOOD: This Area Element is GOOD for the PC's:")
                    Special_Element_Large_Location(known)
                    Encounters(known)
                
                elif Location_Size.casefold() == "Small".casefold():
                    Location_PP = Location_PP + 1
                    print("THIS IS GOOD: This Area Element is GOOD for the PC's:")
                    Special_Element_Small_Location(known)
                    Encounters(known)
            
            if Special_Element_Roll_One in range(41, 51):
                
                if Location_Size.casefold() == "LARGE".casefold():
                    Location_PP = Location_PP + 1
                    print("MULTIELEMENT: Two elements combine to make up this area:")
                    Special_Element_Large_Location(known)
                    Special_Element_Large_Location(known)
                    Encounters(known)
                
                elif Location_Size.casefold() == "Small".casefold():
                    Location_PP = Location_PP + 1
                    print("MULTIELEMENT: Two elements combine to make up this area:")
                    Special_Element_Small_Location(known)
                    Special_Element_Small_Location(known)
                    Encounters(known)
            
            if Special_Element_Roll_One in range(51, 66):
                if Location_Size.casefold() == "LARGE".casefold():
                    Location_PP = Location_PP + 1
                    print("EXIT HERE: This area contains an exit or an Expected Element")
                    Encounters(known)
                    
                elif Location_Size.casefold() == "Small".casefold():
                    Location_PP = Location_PP + 1
                    print("EXIT HERE: This area contains an exit or an Expected Element")
                    Encounters(known)
                    
            if Special_Element_Roll_One in range(66, 81):
                if Location_Size.casefold() == "LARGE".casefold():
                    Location_PP = Location_PP + 1
                    print("RETURN: This area contains a connection to another area or is an Expected Element")
                    Encounters(known)
                    
                elif Location_Size.casefold() == "Small".casefold():
                    Location_PP = Location_PP + 1
                    print("RETURN: This area contains a connection to another area or is an Expected Element")
                    Encounters(known)
                    
            if Special_Element_Roll_One in range(81, 91):
                if Location_Size.casefold() == "LARGE".casefold():
                    print("GOING DEEPER(+3 PP): Expected - what you most expect for this category at this time")
                    Location_PP = Location_PP + 3
                    Encounters(known) 
                elif Location_Size.casefold() == "Small".casefold():
                    print("GOING DEEPER(+3 PP): Expected - what you most expect for this category at this time")
                    Location_PP = Location_PP + 3
                    Encounters(known) 
                    
            if Special_Element_Roll_One in range(91, 101):
                if Location_Size.casefold() == "LARGE".casefold():
                    print("COMMON GROUND(-3 PP): Expected - what you most expect for this category at this time")
                    Location_PP = Location_PP -3
                    Encounters(known)
                elif Location_Size.casefold() == "Small".casefold():                    
                    print("COMMON GROUND(-3 PP): Expected - what you most expect for this category at this time")
                    Location_PP = Location_PP -3
                    Encounters(known)  
            else:
                print("Your entries are invalid try again")
        except ValueError as exception:
                print("Invalid Entries Try Again")
                


def Encounter_Special_Element_Table(known):
    global Encounters_PP  
    global Objects_PP
    global Location_PP
    while True:
            try:
                Special_Element_Roll_One = random.randint(1,101)
                if Special_Element_Roll_One in range (1,11):
                    
                    if Location_Size.casefold() == "LARGE".casefold():
                        Encounters_PP = Encounters_PP + 1
                        print("SUPERSIZE: Enhance this Encounter Element:")
                        Special_Element_Large_Location(known)
                        Objects(known)
                    
                    elif Location_Size.casefold() == "Small".casefold():
                        Encounters_PP = Encounters_PP + 1
                        print("SUPERSIZE: Enhance this Encounter Element:")
                        Special_Element_Small_Location(known)
                        Objects(known)
                
                if Special_Element_Roll_One in range (11, 21):
                    
                    if Location_Size.casefold() == "LARGE".casefold():
                        Encounters_PP = Encounters_PP + 1
                        print("BARELY THERE: Minimize this Encounter Element:")
                        Special_Element_Large_Location(known)
                        Objects(known)
                    
                    elif Location_Size.casefold() == "Small".casefold():
                        Encounters_PP = Encounters_PP + 1
                        print("BARELY THERE: Minimize this Encounter Element:")
                        Special_Element_Small_Location(known)
                        Objects(known)
                        
                if Special_Element_Roll_One in range(21, 31):
                    
                    if Location_Size.casefold() == "LARGE".casefold():
                        Encounters_PP = Encounters_PP + 1
                        print("THIS IS BAD: This Encounter Element is BAD for the PC's:")
                        Special_Element_Large_Location(known)
                        Objects(known)
                    
                    elif Location_Size.casefold() == "Small".casefold():
                        Encounters_PP = Encounters_PP + 1
                        print("THIS IS BAD: This Encounter Element is BAD for the PC's:")
                        Special_Element_Small_Location(known)
                        Objects(known)
                
                if Special_Element_Roll_One in range(31, 41):
                    
                    if Location_Size.casefold() == "LARGE".casefold():
                        Encounters_PP = Encounters_PP + 1
                        print("THIS IS GOOD: This Encounter Element is GOOD for the PC's:")
                        Special_Element_Large_Location(known)
                        Objects(known)
                    
                    elif Location_Size.casefold() == "Small".casefold():
                        Encounters_PP = Encounters_PP + 1
                        print("THIS IS GOOD: This Encounter Element is GOOD for the PC's:")
                        Special_Element_Small_Location(known)
                        Objects(known)
                
                if Special_Element_Roll_One in range(41, 51):
                    
                    if Location_Size.casefold() == "LARGE".casefold():
                        Encounters_PP = Encounters_PP + 1
                        print("MULTIELEMENT: Two elements combine to make up this Encounter:")
                        Special_Element_Large_Location(known)
                        Special_Element_Large_Location(known)
                        Objects(known)
                    
                    elif Location_Size.casefold() == "Small".casefold():
                        Encounters_PP = Encounters_PP + 1
                        print("MULTIELEMENT: Two elements combine to make up this Encounter:")
                        Special_Element_Small_Location(known)
                        Special_Element_Small_Location(known)
                        Objects(known)
                
                if Special_Element_Roll_One in range(51, 66):
                    if Location_Size.casefold() == "LARGE".casefold():
                        Encounters_PP = Encounters_PP + 1
                        print("EXIT HERE: This Encounter contains an exit or an Expected Element")
                        Objects(known)
                        
                    elif Location_Size.casefold() == "Small".casefold():
                        Encounters_PP = Encounters_PP + 1
                        print("EXIT HERE: This Encounter contains an exit or an Expected Element")
                        Objects(known)
                        
                if Special_Element_Roll_One in range(66, 81):
                    if Location_Size.casefold() == "LARGE".casefold():
                        Encounters_PP = Encounters_PP + 1
                        print("RETURN: This Encounter contains a connection to another Encounter or is an Expected Element")
                        Objects(known)
                        
                    elif Location_Size.casefold() == "Small".casefold():
                        Encounters_PP = Encounters_PP + 1
                        print("RETURN: This Encounter contains a connection to another Encounter or is an Expected Element")
                        Objects(known)
                        
                if Special_Element_Roll_One in range(81, 91):
                    if Location_Size.casefold() == "LARGE".casefold():
                        print("GOING DEEPER(+3 PP): Expected - what you most expect for this category at this time")
                        Encounters_PP = Encounters_PP + 3
                        Objects(known)
                        
                    elif Location_Size.casefold() == "Small".casefold():
                        print("GOING DEEPER(+3 PP): Expected - what you most expect for this category at this time")
                        Encounters_PP = Encounters_PP + 3
                        Objects(known) 
                        
                if Special_Element_Roll_One in range(91, 101):
                    if Location_Size.casefold() == "LARGE".casefold():
                        print("COMMON GROUND(-3 PP): Expected - what you most expect for this category at this time")
                        Encounters_PP = Encounters_PP -3
                        Objects(known)
                        
                    elif Location_Size.casefold() == "Small".casefold():                    
                        print("COMMON GROUND(-3 PP): Expected - what you most expect for this category at this time")
                        Encounters_PP = Encounters_PP -3
                        Objects(known)  
                else:
                    print("Your entries are invalid try again")
            except ValueError as exception:
                    print("Invalid Entries Try Again")

def Objects_Special_Element_Table(known):
    global Encounters_PP  
    global Objects_PP
    global Location_PP
    while True:
            try:
                Special_Element_Roll_One = random.randint(1,101)
                if Special_Element_Roll_One in range (1,11):
                    
                    if Location_Size.casefold() == "LARGE".casefold():
                        Objects_PP = Objects_PP + 1
                        print("SUPERSIZE: Enhance this Object Element:")
                        Special_Element_Large_Location(known)
                        input("\n Press a key when ready to move to the next area \n")                        
                        Area_Location(known)
                    
                    elif Location_Size.casefold() == "Small".casefold():
                        Objects_PP = Objects_PP + 1
                        print("SUPERSIZE: Enhance this Object Element:")
                        Special_Element_Small_Location(known)
                        input("\n Press a key when ready to move to the next area \n")                        
                        Area_Location(known)
                
                if Special_Element_Roll_One in range (11, 21):
                    
                    if Location_Size.casefold() == "LARGE".casefold():
                        Objects_PP = Objects_PP + 1
                        print("BARELY THERE: Minimize this Object Element:")
                        Special_Element_Large_Location(known)
                        input("\n Press a key when ready to move to the next area \n")                        
                        Area_Location(known)
                    
                    elif Location_Size.casefold() == "Small".casefold():
                        Objects_PP = Objects_PP + 1
                        print("BARELY THERE: Minimize this Object Element:")
                        Special_Element_Small_Location(known)
                        input("\n Press a key when ready to move to the next area \n")                         
                        Area_Location(known)
                        
                if Special_Element_Roll_One in range(21, 31):
                    
                    if Location_Size.casefold() == "LARGE".casefold():
                        Objects_PP = Objects_PP + 1
                        print("THIS IS BAD: This Object Element is BAD for the PC's:")
                        Special_Element_Large_Location(known)
                        input("\n Press a key when ready to move to the next area \n")                         
                        Area_Location(known)
                    
                    elif Location_Size.casefold() == "Small".casefold():
                        Objects_PP = Objects_PP + 1
                        print("THIS IS BAD: This Object Element is BAD for the PC's:")
                        Special_Element_Small_Location(known)
                        input("\n Press a key when ready to move to the next area \n")                         
                        Area_Location(known)
                
                if Special_Element_Roll_One in range(31, 41):
                    
                    if Location_Size.casefold() == "LARGE".casefold():
                        Objects_PP = Objects_PP + 1
                        print("THIS IS GOOD: This Object Element is GOOD for the PC's:")
                        Special_Element_Large_Location(known)
                        input("\n Press a key when ready to move to the next area \n")                         
                        Area_Location(known)
                    
                    elif Location_Size.casefold() == "Small".casefold():
                        Objects_PP = Objects_PP + 1
                        print("THIS IS GOOD: This Object Element is GOOD for the PC's:")
                        Special_Element_Small_Location(known)
                        input("\n Press a key when ready to move to the next area \n")                         
                        Area_Location(known)
                
                if Special_Element_Roll_One in range(41, 51):
                    
                    if Location_Size.casefold() == "LARGE".casefold():
                        Objects_PP = Objects_PP + 1
                        print("MULTIELEMENT: Two elements combine to make up this Object:")
                        Special_Element_Large_Location(known)
                        Special_Element_Large_Location(known)
                        input("\n Press a key when ready to move to the next area \n")                         
                        Area_Location(known)
                    
                    elif Location_Size.casefold() == "Small".casefold():
                        Objects_PP = Objects_PP + 1
                        print("MULTIELEMENT: Two elements combine to make up this Object:")
                        Special_Element_Small_Location(known)
                        Special_Element_Small_Location(known)
                        input("\n Press a key when ready to move to the next area \n")                         
                        Area_Location(known)
                
                if Special_Element_Roll_One in range(51, 66):
                    if Location_Size.casefold() == "LARGE".casefold():
                        Objects_PP = Objects_PP + 1
                        print("EXIT HERE: This Object contains an exit or an Expected Element")
                        input("\n Press a key when ready to move to the next area \n")                         
                        Area_Location(known)
                        
                    elif Location_Size.casefold() == "Small".casefold():
                        Objects_PP = Objects_PP + 1
                        print("EXIT HERE: This Object contains an exit or an Expected Element")
                        input("\n Press a key when ready to move to the next area \n")                         
                        Area_Location(known)
                        
                if Special_Element_Roll_One in range(66, 81):
                    if Location_Size.casefold() == "LARGE".casefold():
                        Objects_PP = Objects_PP + 1
                        print("RETURN: This Object contains a connection to another Object or is an Expected Element")
                        input("\n Press a key when ready to move to the next area \n")                         
                        Area_Location(known)
                        
                    elif Location_Size.casefold() == "Small".casefold():
                        Objects_PP = Objects_PP + 1
                        print("RETURN: This Object contains a connection to another Object or is an Expected Element")
                        input("\n Press a key when ready to move to the next area \n")                         
                        Area_Location(known)
                        
                if Special_Element_Roll_One in range(81, 91):
                    if Location_Size.casefold() == "LARGE".casefold():
                        print("GOING DEEPER(+3 PP): Expected - what you most expect for this category at this time")
                        Objects_PP = Objects_PP + 3
                        input("\n Press a key when ready to move to the next area \n")                         
                        Area_Location(known)
                        
                    elif Location_Size.casefold() == "Small".casefold():
                        print("GOING DEEPER(+3 PP): Expected - what you most expect for this category at this time")
                        Objects_PP = Objects_PP + 3
                        input("\n Press a key when ready to move to the next area \n")                         
                        Area_Location(known) 
                        
                if Special_Element_Roll_One in range(91, 101):
                    if Location_Size.casefold() == "LARGE".casefold():
                        print("COMMON GROUND(-3 PP): Expected - what you most expect for this category at this time")
                        Objects_PP = Objects_PP -3
                        input("\n Press a key when ready to move to the next area \n")                         
                        Area_Location(known)
                        
                    elif Location_Size.casefold() == "Small".casefold():                    
                        print("COMMON GROUND(-3 PP): Expected - what you most expect for this category at this time")
                        Objects_PP = Objects_PP -3
                        input("\n Press a key when ready to move to the next area \n")                         
                        Area_Location(known)  
                else:
                    print("Your entries are invalid try again")
            except ValueError as exception:
                    print("Invalid Entries Try Again")

def Special_Element_Large_Location(known):        
    Large_Location_Die = random.randint(1, 11)
    global Location_PP
    Large_Location_Die = Large_Location_Die + Location_PP
    while True:
        try:
            if Large_Location_Die in range(1,6):
                print("SPECIAL TABLE Large Location = Expected - what you most expect for this category at this time")
                break
            
            elif Large_Location_Die in range(6,9):
                print("SPECIAL TABLE Large Location = Expected - what you most expect for this category at this time")
                break
            
            elif Large_Location_Die in range(9,11): 
                print("SPECIAL TABLE Random - Location inspired by the following random element descriptors")             
                Location_Element_Descriptors()
                break
            
            elif Large_Location_Die in range(11, 12):
                Large_Location_Number_11 = input("SPECIAL TABLE: Is this a Known area or Random Location?  ").casefold()   
                if Large_Location_Number_11.casefold() == "Known".casefold() and (str(known)) != '[]':
                        print(str(known))
                        KnownInput = input("Pick which known applies  ").casefold()
                        while KnownInput not in known:
                            print("Known selection not in list")
                            KnownInput = input("Pick a known that applies  ").casefold()
                        else:
                            print("SPECIAL LARGE LOCATION:  ", end='')  
                            (print(KnownInput))
                            break  
                                
                elif (str(known)) == '[]' and Large_Location_Number_11.casefold() == "Known".casefold():
                    print("No Known is Available, defaulting to expected")
                    print("LARGE LOCATION = Expected - what you most expect for this category at this time")
                    break
                    
                elif Large_Location_Number_11.casefold() == "Random".casefold():
                    Location_Element_Descriptors()
                    break
            
            elif Large_Location_Die in range(12, 13):
                Large_Location_Number_12 = input("SPECIAL TABLE: Is this a Known area or Expected Location?  ").casefold() 
                if Large_Location_Number_12.casefold() == "Known".casefold():
                    print(str(known))
                    KnownInput = input("Pick which known applies  ").casefold()
                    while KnownInput not in known:
                        print("Known selection not in list")
                        KnownInput = input("Pick a known that applies  ").casefold()
                    else:
                        print("SPECIAL LARGE LOCATION:  ", end='')
                        (print(KnownInput))
                        break  
                             
                elif Large_Location_Number_12.casefold() == "Expected".casefold():
                    print("SPECIAL TABLE: Large Location = Expected - what you most expect for this category at this time")
                    break
            
            elif Large_Location_Die in range(13, 14):
                    print("SPECIAL TABLE: Large Location = Expected - what you most expect for this category at this time")
                    break
            
            elif Large_Location_Die in range(14, 16):
                Large_Location_Number_14_15 = input("Is there more to explore of this area, Yes or No?").casefold()
                if Large_Location_Number_14_15.casefold() == "yes".casefold():
                    print("LARGE LOCATION: EXPECTED")
                    print("ENCOUNTERS: EXPECTED")
                    print("OBJECTS: EXPECTED")
                    break
                else:
                    print("Location is completed, exiting program")
                    sys. exit()
            
            elif Large_Location_Die in range(16, 999):
                print("LARGE LOCATION = Expected - what you most expect for this category at this time")
                break
            
            else:
                print("Your entries are invalid try again")                
        except ValueError as exception:
                print("Invalid Entries Try Again")
                
def Special_Element_Small_Location(known):
    Small_Location_Die = random.randint(1, 11)
    global Location_PP
    global Encounters_PP
    global Objects_PP
    Small_Location_Die = Small_Location_Die + Location_PP

    while True:
        try:
            if Small_Location_Die in range(1,6):
                print("SMALL LOCATION = Expected - what you most expect for this category at this time")
                Location_PP = Location_PP + 1
                Encounters(known)
            
            elif Small_Location_Die in range(6,9):
                print("SMALL LOCATION = Expected - what you most expect for this category at this time")
                Location_PP = Location_PP + 1
                Encounters(known)
            
            elif Small_Location_Die in range(9,11): 
                print("SMALL LOCATION = Random - Location inspired by the following random element descriptors")             
                Location_Element_Descriptors()
                Location_PP = Location_PP + 1
                Encounters(known) 
            
            elif Small_Location_Die in range(11, 12):
                Location_PP = Location_PP + 1
                Small_Location_Number_11 = input("Is this a Known area or Random Location?  ").casefold()
                if Small_Location_Number_11.casefold() == "Known".casefold() and (str(known)) != '[]':
                        print(str(known))
                        KnownInput = input("Pick which known applies  ").casefold()
                        while KnownInput not in known:
                            print("Known selection not in list")
                            KnownInput = input("Pick a known that applies  ").casefold()
                        else:
                            print("Location:  ", end='') 
                            (print(KnownInput))
                            Encounters(known)
                            
                elif (str(known)) == '[]' and Small_Location_Number_11.casefold() == "Known".casefold():
                    print("No Known is Available, defaulting to expected")
                    print("SMALL LOCATION = Expected - what you most expect for this category at this time")
                    Encounters(known) 
                        
                elif Small_Location_Number_11.casefold() == "Random".casefold():
                    Location_Element_Descriptors()
                    Encounters(known)
            
            elif Small_Location_Die in range(12, 13):
                Small_Location_Number_12 = input("Is there more to explore of this area, Yes or No?").casefold()
                if Small_Location_Number_12.casefold() == "yes".casefold():
                    Location_PP = Location_PP + 1
                    Encounters_PP = Encounters_PP + 1
                    Objects_PP = Objects_PP + 1
                    print("SMALL LOCATION: EXPECTED")
                    print("ENCOUNTERS: EXPECTED")
                    print("OBJECTS: EXPECTED")
                    Small_Location_Die = random.randint(1, 11) +Location_PP
                else:
                    print("Location is complete, exiting program")
                    sys. exit()    
                    
            elif Small_Location_Die in range(13, 14):
                Location_PP = Location_PP + 1
                Small_Location_Number_13 = input("Is this a Known area or Special Location?  ")     
                
                if Small_Location_Number_13.casefold() == "Known".casefold() and (str(known)) != '[]':
                        print(str(known))
                        KnownInput = input("Pick which known applies  ").casefold()
                        while KnownInput not in known:
                            print("Known selection not in list")
                            KnownInput = input("Pick a known that applies  ").casefold()
                        else:
                            print("Location:  ", end='') 
                            (print(KnownInput))
                            Encounters(known)
                            
                elif (str(known)) == '[]':
                    print("No Known is Available, defaulting to special element which becomes expected on the special element table")    
                    print("SPECIAL TABLE: Small Location = Expected - what you most expect for this category at this time")
                    break
                
                elif Small_Location_Number_13.casefold() == "Special".casefold():
                    print("SPECIAL TABLE: Large Location = Expected - what you most expect for this category at this time")
                    break
                    
            elif Small_Location_Die in range(14, 16):
                Small_Location_Number_14_16 = input("Is there more to explore of this area, Yes or No?").casefold()
                if Small_Location_Number_14_16.casefold() == "yes".casefold():
                    Location_PP = Location_PP + 1
                    Encounters_PP = Encounters_PP + 1
                    Objects_PP = Objects_PP + 1
                    print("SMALL LOCATION: EXPECTED")
                    print("ENCOUNTERS: EXPECTED")
                    print("OBJECTS: EXPECTED")
                    Small_Location_Die = random.randint(1, 11) +Location_PP
                else:
                    print("Location is complete, exiting program")
                    sys. exit()    
                    
            elif Small_Location_Die in range(16, 999):
                print("SMALL LOCATION = Expected - what you most expect for this category at this time")
                Location_PP = Location_PP - 6
                Encounters(known)         

            else:
                print("Your entries are invalid try again")                
        except ValueError as exception:
                print("Invalid Entries Try Again") 

#Similar to Meaning Tables, two random rolls on the random Element Descriptor's table for Locations
def Location_Element_Descriptors():
    while True:
        try:
            Location_Random_Element_Descriptors_Roll_One = random.randint(1,101)
            Location_Random_Element_Descriptors_Roll_Two = random.randint(1,101)
            
            if Location_Random_Element_Descriptors_Roll_One == 1:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Abandoned")
                print(Random_Element_Descriptor_One)
                break
            
            elif Location_Random_Element_Descriptors_Roll_One == 2:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Amusing")
                print(Random_Element_Descriptor_One)
                break
            
            elif Location_Random_Element_Descriptors_Roll_One == 3:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Ancient")
                print(Random_Element_Descriptor_One)
                break
            
            elif Location_Random_Element_Descriptors_Roll_One == 4:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Aromatic")
                print(Random_Element_Descriptor_One)
                break
            
            elif Location_Random_Element_Descriptors_Roll_One == 5:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Beautiful")
                print(Random_Element_Descriptor_One)
                break
            
            elif Location_Random_Element_Descriptors_Roll_One == 6:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Bleak")
                print(Random_Element_Descriptor_One)
                break
            
            elif Location_Random_Element_Descriptors_Roll_One == 7:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Average")
                print(Random_Element_Descriptor_One)
                break       
            
            elif Location_Random_Element_Descriptors_Roll_One == 8:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Bizarre")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 9:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Calm")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 10:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Classy")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Location_Random_Element_Descriptors_Roll_One == 11:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Clean")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 12:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Colorful")
                print(Random_Element_Descriptor_One)
                break     
            
            elif Location_Random_Element_Descriptors_Roll_One == 13:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Creepy")
                print(Random_Element_Descriptor_One)
                break         
            
            elif Location_Random_Element_Descriptors_Roll_One == 14:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Cold")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 15:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Cute")
                print(Random_Element_Descriptor_One)
                break      
            
            elif Location_Random_Element_Descriptors_Roll_One == 16:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Damaged")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 17:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Dangerous")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 18:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Dark")
                print(Random_Element_Descriptor_One)
                break      
            
            elif Location_Random_Element_Descriptors_Roll_One == 19:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Dirty")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 20:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Delightful")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Location_Random_Element_Descriptors_Roll_One == 21:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Drab")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Location_Random_Element_Descriptors_Roll_One == 22:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Disgusting")
                print(Random_Element_Descriptor_One)
                break        
            
            elif Location_Random_Element_Descriptors_Roll_One == 23:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Enormous")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 24:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Dry")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Location_Random_Element_Descriptors_Roll_One == 25:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Empty")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 26:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Enormous")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 27:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Exotic")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 28:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Fortunate")
                print(Random_Element_Descriptor_One)
                break     
            
            elif Location_Random_Element_Descriptors_Roll_One == 29:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Familiar")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Location_Random_Element_Descriptors_Roll_One == 30:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Frightening")
                print(Random_Element_Descriptor_One)
                break     
            
            elif Location_Random_Element_Descriptors_Roll_One == 31:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Full")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 32:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Fancy")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 33:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Festive")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Location_Random_Element_Descriptors_Roll_One == 34:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Harsh")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 35:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Horrible")
                print(Random_Element_Descriptor_One)
                break       
            
            elif Location_Random_Element_Descriptors_Roll_One == 36:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Important")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Location_Random_Element_Descriptors_Roll_One == 37:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Helpful")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 38:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Lavish")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 39:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Magnificent")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 40:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Intense")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 41:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Messy")
                print(Random_Element_Descriptor_One)
                break     
            
            elif Location_Random_Element_Descriptors_Roll_One == 42:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Military")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Location_Random_Element_Descriptors_Roll_One == 43:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Loud")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Location_Random_Element_Descriptors_Roll_One == 44:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Modern")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Location_Random_Element_Descriptors_Roll_One == 45:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Majestic")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 46:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Meaningful")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 47:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Extravagant")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Location_Random_Element_Descriptors_Roll_One == 48:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Mundane")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 49:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Mysterious")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 50:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Natural")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 51:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Odd")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 52:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Official")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Location_Random_Element_Descriptors_Roll_One == 53:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Peaceful")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Location_Random_Element_Descriptors_Roll_One == 54:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Small")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Location_Random_Element_Descriptors_Roll_One == 55:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Positive")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 56:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Reassuring")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 57:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Quaint")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Location_Random_Element_Descriptors_Roll_One == 58:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Quiet")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Location_Random_Element_Descriptors_Roll_One == 59:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Ruined")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Location_Random_Element_Descriptors_Roll_One == 60:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Rustic")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Location_Random_Element_Descriptors_Roll_One == 61:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Simple")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 62:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Threatening")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Location_Random_Element_Descriptors_Roll_One == 63:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Smelly")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Location_Random_Element_Descriptors_Roll_One == 64:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Tranquil")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 65:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Warm")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Location_Random_Element_Descriptors_Roll_One == 66:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Watery")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 67:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Negative")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 68:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Enclosed")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Location_Random_Element_Descriptors_Roll_One == 69:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Domestic")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 70:
                Random_Element_Descriptor_One = ("\tLocation Random Element: New")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 71:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Open")
                print(Random_Element_Descriptor_One)
                break  
         
            elif Location_Random_Element_Descriptors_Roll_One == 72:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Safe")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 73:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Expected")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 74:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Unexpected")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 75:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Strange")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 76:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Active")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 77:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Inactive")
                print(Random_Element_Descriptor_One)
                break     
            
            elif Location_Random_Element_Descriptors_Roll_One == 78:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Harmful")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Location_Random_Element_Descriptors_Roll_One == 79:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Primitive")
                print(Random_Element_Descriptor_One)
                break      
            
            elif Location_Random_Element_Descriptors_Roll_One == 80:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Protection")
                print(Random_Element_Descriptor_One)
                break
            
            elif Location_Random_Element_Descriptors_Roll_One == 81:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Unusual")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 82:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Bright")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 83:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Ornate")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 84:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Atmosphere")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 85:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Sounds")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Location_Random_Element_Descriptors_Roll_One == 86:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Resourceful")
                print(Random_Element_Descriptor_One)
                break
            
            elif Location_Random_Element_Descriptors_Roll_One == 87:
                Random_Element_Descriptor_One = ("\tLocation Random Element:  Purposeful")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 88:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Personal")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Location_Random_Element_Descriptors_Roll_One == 89:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Exclusive")
                print(Random_Element_Descriptor_One)
                break     
            
            elif Location_Random_Element_Descriptors_Roll_One == 90:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Intriguing")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Location_Random_Element_Descriptors_Roll_One == 91:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Echo")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 92:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Unsteady")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 93:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Moving")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Location_Random_Element_Descriptors_Roll_One == 94:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Cluttered")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Location_Random_Element_Descriptors_Roll_One == 95:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Storage")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 96:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Confusing")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Location_Random_Element_Descriptors_Roll_One == 97:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Lonely")
                print(Random_Element_Descriptor_One)
                break      
            
            elif Location_Random_Element_Descriptors_Roll_One == 98:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Long")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Location_Random_Element_Descriptors_Roll_One == 99:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Tall")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Location_Random_Element_Descriptors_Roll_One == 100:
                Random_Element_Descriptor_One = ("\tLocation Random Element: Artistic")
                print(Random_Element_Descriptor_One)
                break                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            
            else:
                print("Your entries are invalid try again")
        except ValueError as exception:
                print("Invalid Entries Try Again") 
                
    while True:
        try:
                if Location_Random_Element_Descriptors_Roll_Two == 1:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Abandoned")
                    print(Random_Element_Descriptor_Two)
                    break
                
                elif Location_Random_Element_Descriptors_Roll_Two == 2:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Amusing")
                    print(Random_Element_Descriptor_Two)
                    break
                
                elif Location_Random_Element_Descriptors_Roll_Two == 3:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Ancient")
                    print(Random_Element_Descriptor_Two)
                    break
                
                elif Location_Random_Element_Descriptors_Roll_Two == 4:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Aromatic")
                    print(Random_Element_Descriptor_Two)
                    break
                
                elif Location_Random_Element_Descriptors_Roll_Two == 5:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Beautiful")
                    print(Random_Element_Descriptor_Two)
                    break
               
                elif Location_Random_Element_Descriptors_Roll_Two == 6:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Bleak")
                    print(Random_Element_Descriptor_Two)
                    break
                
                elif Location_Random_Element_Descriptors_Roll_Two == 7:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Average")
                    print(Random_Element_Descriptor_Two)
                    break       
                
                elif Location_Random_Element_Descriptors_Roll_Two == 8:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Bizarre")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 9:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Calm")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 10:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Classy")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Location_Random_Element_Descriptors_Roll_Two == 11:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Clean")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 12:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Colorful")
                    print(Random_Element_Descriptor_Two)
                    break     
                
                elif Location_Random_Element_Descriptors_Roll_Two == 13:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Creepy")
                    print(Random_Element_Descriptor_Two)
                    break         
                
                elif Location_Random_Element_Descriptors_Roll_Two == 14:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Cold")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 15:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Cute")
                    print(Random_Element_Descriptor_Two)
                    break      
                
                elif Location_Random_Element_Descriptors_Roll_Two == 16:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Damaged")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 17:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Dangerous")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 18:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Dark")
                    print(Random_Element_Descriptor_Two)
                    break      
                
                elif Location_Random_Element_Descriptors_Roll_Two == 19:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Dirty")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 20:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Delightful")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Location_Random_Element_Descriptors_Roll_Two == 21:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Drab")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Location_Random_Element_Descriptors_Roll_Two == 22:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Disgusting")
                    print(Random_Element_Descriptor_Two)
                    break        
                
                elif Location_Random_Element_Descriptors_Roll_Two == 23:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Enormous")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 24:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Dry")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Location_Random_Element_Descriptors_Roll_Two == 25:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Empty")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 26:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Enormous")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 27:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Exotic")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 28:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Fortunate")
                    print(Random_Element_Descriptor_Two)
                    break     
                
                elif Location_Random_Element_Descriptors_Roll_Two == 29:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Familiar")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Location_Random_Element_Descriptors_Roll_Two == 30:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Frightening")
                    print(Random_Element_Descriptor_Two)
                    break     
                
                elif Location_Random_Element_Descriptors_Roll_Two == 31:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Full")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 32:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Fancy")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 33:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Festive")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Location_Random_Element_Descriptors_Roll_Two == 34:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Harsh")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 35:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Horrible")
                    print(Random_Element_Descriptor_Two)
                    break       
                
                elif Location_Random_Element_Descriptors_Roll_Two == 36:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Important")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Location_Random_Element_Descriptors_Roll_Two == 37:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Helpful")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 38:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Lavish")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 39:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Magnificent")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 40:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Intense")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 41:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Messy")
                    print(Random_Element_Descriptor_Two)
                    break     
                
                elif Location_Random_Element_Descriptors_Roll_Two == 42:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Military")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Location_Random_Element_Descriptors_Roll_Two == 43:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Loud")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Location_Random_Element_Descriptors_Roll_Two == 44:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Modern")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Location_Random_Element_Descriptors_Roll_Two == 45:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Majestic")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 46:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Meaningful")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 47:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Extravagant")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Location_Random_Element_Descriptors_Roll_Two == 48:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Mundane")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 49:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Mysterious")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 50:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Natural")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 51:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Odd")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 52:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Official")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Location_Random_Element_Descriptors_Roll_Two == 53:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Peaceful")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Location_Random_Element_Descriptors_Roll_Two == 54:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Small")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Location_Random_Element_Descriptors_Roll_Two == 55:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Positive")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 56:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Reassuring")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 57:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Quaint")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Location_Random_Element_Descriptors_Roll_Two == 58:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Quiet")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Location_Random_Element_Descriptors_Roll_Two == 59:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Ruined")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Location_Random_Element_Descriptors_Roll_Two == 60:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Rustic")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Location_Random_Element_Descriptors_Roll_Two == 61:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Simple")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 62:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Threatening")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Location_Random_Element_Descriptors_Roll_Two == 63:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Smelly")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Location_Random_Element_Descriptors_Roll_Two == 64:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Tranquil")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 65:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Warm")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Location_Random_Element_Descriptors_Roll_Two == 66:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Watery")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 67:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Negative")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 68:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Enclosed")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Location_Random_Element_Descriptors_Roll_Two == 69:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Domestic")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 70:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: New")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 71:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Open")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 72:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Safe")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 73:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Expected")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 74:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Unexpected")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 75:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Strange")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 76:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Active")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 77:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Inactive")
                    print(Random_Element_Descriptor_Two)
                    break     
                
                elif Location_Random_Element_Descriptors_Roll_Two == 78:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Harmful")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Location_Random_Element_Descriptors_Roll_Two == 79:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Primitive")
                    print(Random_Element_Descriptor_Two)
                    break      
                
                elif Location_Random_Element_Descriptors_Roll_Two == 80:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Protection")
                    print(Random_Element_Descriptor_Two)
                    break
                
                elif Location_Random_Element_Descriptors_Roll_Two == 81:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Unusual")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 82:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Bright")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 83:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Ornate")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 84:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Atmosphere")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 85:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Sounds")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Location_Random_Element_Descriptors_Roll_Two == 86:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Resourceful")
                    print(Random_Element_Descriptor_Two)
                    break
                
                elif Location_Random_Element_Descriptors_Roll_Two == 87:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Purposeful")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 88:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Personal")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Location_Random_Element_Descriptors_Roll_Two == 89:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Exclusive")
                    print(Random_Element_Descriptor_Two)
                    break     
                
                elif Location_Random_Element_Descriptors_Roll_Two == 90:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Intriguing")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Location_Random_Element_Descriptors_Roll_Two == 91:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Echo")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 92:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Unsteady")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 93:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Moving")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Location_Random_Element_Descriptors_Roll_Two == 94:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Cluttered")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Location_Random_Element_Descriptors_Roll_Two == 95:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Storage")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 96:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Confusing")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Location_Random_Element_Descriptors_Roll_Two == 97:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Lonely")
                    print(Random_Element_Descriptor_Two)
                    break      
                
                elif Location_Random_Element_Descriptors_Roll_Two == 98:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Long")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Location_Random_Element_Descriptors_Roll_Two == 99:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Tail")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Location_Random_Element_Descriptors_Roll_Two == 100:
                    Random_Element_Descriptor_Two = ("\tLocation Random Element #2: Artistic")
                    print(Random_Element_Descriptor_Two)
                    break                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                
                else:
                    print("Your entries are invalid try again")
        except ValueError as exception:
                    print("Invalid Entries Try Again")

def Encounters_Element_Descriptors():
    while True:
        try:
            Encounter_Random_Element_Descriptors_Roll_One = random.randint(1,101)
            Encounter_Random_Element_Descriptors_Roll_Two = random.randint(1,101)
            
            if Encounter_Random_Element_Descriptors_Roll_One == 1:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Abnormal")
                print(Random_Element_Descriptor_One)
                break
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 2:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Aggressive")
                print(Random_Element_Descriptor_One)
                break
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 3:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Angry")
                print(Random_Element_Descriptor_One)
                break
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 4:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Anxious")
                print(Random_Element_Descriptor_One)
                break
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 5:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Beautiful")
                print(Random_Element_Descriptor_One)
                break
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 6:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Average")
                print(Random_Element_Descriptor_One)
                break
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 7:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Bold")
                print(Random_Element_Descriptor_One)
                break       
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 8:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Busy")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 9:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Calm")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 10:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Careless")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 11:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Cautious")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 12:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Cheerful")
                print(Random_Element_Descriptor_One)
                break     
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 13:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Combative")
                print(Random_Element_Descriptor_One)
                break         
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 14:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Bizarre")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 15:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Crazy")
                print(Random_Element_Descriptor_One)
                break      
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 16:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Curious")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 17:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Dangerous")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 18:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Defiant")
                print(Random_Element_Descriptor_One)
                break      
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 19:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Classy")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 20:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Delightful")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 21:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Creepy")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 22:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Energetic")
                print(Random_Element_Descriptor_One)
                break        
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 23:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Enormous")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 24:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Excited")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 25:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Fearful")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 26:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Ferocious")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 27:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Foolish")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 28:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Fortunate")
                print(Random_Element_Descriptor_One)
                break     
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 29:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Frantic")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 30:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Frightening")
                print(Random_Element_Descriptor_One)
                break     
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 31:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Cute")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 32:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Generous")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 33:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Gentle")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 34:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Glad")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 35:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Graceful")
                print(Random_Element_Descriptor_One)
                break       
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 36:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Happy")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 37:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Helpful")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 38:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Helpless")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 39:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Innocent")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 40:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Intense")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 41:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Lazy")
                print(Random_Element_Descriptor_One)
                break     
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 42:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Defeated")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 43:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Loud")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 44:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Loyal")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 45:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Majestic")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 46:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Disgusting")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 47:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Enormous")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 48:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Miserable")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 49:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Mysterious")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 50:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Feeble")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 51:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Odd")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 52:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Official")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 53:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Peaceful")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 54:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Playful")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 55:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Positive")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 56:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Powerful")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 57:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Exotic")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 58:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Familiar")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 59:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Slow")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 60:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Horrible")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 61:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Swift")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 62:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Threatening")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 63:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Violent")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 64:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Wild")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 65:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Important")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 66:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Lonely")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 67:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Mighty")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 68:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Military")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 69:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Mundane")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 70:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Powerful")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 71:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Reassuring")
                print(Random_Element_Descriptor_One)
                break  
         
            elif Encounter_Random_Element_Descriptors_Roll_One == 72:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Small")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 73:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Smelly")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 74:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Strong")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 75:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Watery")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 76:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Weak")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 77:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Ambush")
                print(Random_Element_Descriptor_One)
                break     
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 78:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Harmful")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 79:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Trap")
                print(Random_Element_Descriptor_One)
                break      
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 80:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Friend")
                print(Random_Element_Descriptor_One)
                break
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 81:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Foe")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 82:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Negative")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 83:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Evil")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 84:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Animal")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 85:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Expected")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 86:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Unexpected")
                print(Random_Element_Descriptor_One)
                break
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 87:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Strange")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 88:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Armed")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 89:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Active")
                print(Random_Element_Descriptor_One)
                break     
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 90:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Inactive")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 91:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Multiple")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 92:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Single")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 93:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Primitive")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 94:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Unusual")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 95:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Fast")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 96:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Hidden")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 97:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Natural")
                print(Random_Element_Descriptor_One)
                break      
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 98:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Quiet")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 99:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Unnatural")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Encounter_Random_Element_Descriptors_Roll_One == 100:
                Random_Element_Descriptor_One = ("\tEncounter Random Element: Resourceful")
                print(Random_Element_Descriptor_One)
                break                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            
            else:
                print("Your entries are invalid try again")
        except ValueError as exception:
                print("Invalid Entries Try Again") 
                
    while True:
        try:
                if Encounter_Random_Element_Descriptors_Roll_Two == 1:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Abnormal")
                    print(Random_Element_Descriptor_Two)
                    break
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 2:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Aggressive")
                    print(Random_Element_Descriptor_Two)
                    break
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 3:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Angry")
                    print(Random_Element_Descriptor_Two)
                    break
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 4:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Anxious")
                    print(Random_Element_Descriptor_Two)
                    break
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 5:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Beautiful")
                    print(Random_Element_Descriptor_Two)
                    break
               
                elif Encounter_Random_Element_Descriptors_Roll_Two == 6:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Average")
                    print(Random_Element_Descriptor_Two)
                    break
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 7:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Bold")
                    print(Random_Element_Descriptor_Two)
                    break       
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 8:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Busy")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 9:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Calm")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 10:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Careless")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 11:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Cautious")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 12:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Cheerful")
                    print(Random_Element_Descriptor_Two)
                    break     
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 13:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Combative")
                    print(Random_Element_Descriptor_Two)
                    break         
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 14:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Bizarre")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 15:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Crazy")
                    print(Random_Element_Descriptor_Two)
                    break      
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 16:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Curious")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 17:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Dangerous")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 18:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Defiant")
                    print(Random_Element_Descriptor_Two)
                    break      
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 19:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Classy")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 20:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Delightful")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 21:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Creepy")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 22:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Energetic")
                    print(Random_Element_Descriptor_Two)
                    break        
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 23:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Enormous")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 24:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Excited")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 25:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Fearful")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 26:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Ferocious")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 27:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Foolish")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 28:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Fortunate")
                    print(Random_Element_Descriptor_Two)
                    break     
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 29:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Frantic")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 30:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Frightening")
                    print(Random_Element_Descriptor_Two)
                    break     
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 31:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Cute")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 32:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Generous")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 33:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Gentle")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 34:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Glad")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 35:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Graceful")
                    print(Random_Element_Descriptor_Two)
                    break       
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 36:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Happy")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 37:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Helpful")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 38:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Helpless")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 39:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Innocent")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 40:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Intense")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 41:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Lazy")
                    print(Random_Element_Descriptor_Two)
                    break     
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 42:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Defeated")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 43:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Loud")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 44:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Loyal")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 45:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Majestic")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 46:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Disgusting")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 47:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Enormous")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 48:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Miserable")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 49:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Mysterious")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 50:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Feeble")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 51:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Odd")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 52:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Official")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 53:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Peaceful")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 54:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Playful")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 55:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Positive")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 56:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Powerful")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 57:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Exotic")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 58:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Familiar")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 59:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Slow")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 60:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Horrible")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 61:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Swift")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 62:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Threatening")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 63:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Violent")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 64:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Wild")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 65:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Important")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 66:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Lonely")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 67:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Mighty")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 68:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Military")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 69:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Mundane")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 70:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Powerful")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 71:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Reassuring")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 72:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Small")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 73:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Smelly")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 74:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Strong")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 75:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Watery")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 76:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Weak")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 77:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Ambush")
                    print(Random_Element_Descriptor_Two)
                    break     
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 78:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Harmful")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 79:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Trap")
                    print(Random_Element_Descriptor_Two)
                    break      
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 80:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Friend")
                    print(Random_Element_Descriptor_Two)
                    break
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 81:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Foe")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 82:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Negative")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 83:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Evil")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 84:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Animal")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 85:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Expected")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 86:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Unexpected")
                    print(Random_Element_Descriptor_Two)
                    break
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 87:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Strange")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 88:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Armed")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 89:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Active")
                    print(Random_Element_Descriptor_Two)
                    break     
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 90:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Inactive")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 91:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Multiple")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 92:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Single")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 93:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Primitive")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 94:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Unusual")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 95:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Fast")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 96:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Hidden")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 97:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Natural")
                    print(Random_Element_Descriptor_Two)
                    break      
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 98:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Quiet")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 99:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Unnatural")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Encounter_Random_Element_Descriptors_Roll_Two == 100:
                    Random_Element_Descriptor_Two = ("\tEncounter Random Element #2: Resourceful")
                    print(Random_Element_Descriptor_Two)
                    break                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                
                else:
                    print("Your entries are invalid try again")
        except ValueError as exception:
                    print("Invalid Entries Try Again")


def Objects_Element_Descriptors():
    while True:
        try:
            Object_Random_Element_Descriptors_Roll_One = random.randint(1,101)
            Object_Random_Element_Descriptors_Roll_Two = random.randint(1,101)
            
            if Object_Random_Element_Descriptors_Roll_One == 1:
                Random_Element_Descriptor_One = ("\tObject Random Element: Amusing")
                print(Random_Element_Descriptor_One)
                break
            
            elif Object_Random_Element_Descriptors_Roll_One == 2:
                Random_Element_Descriptor_One = ("\tObject Random Element: Ancient")
                print(Random_Element_Descriptor_One)
                break
            
            elif Object_Random_Element_Descriptors_Roll_One == 3:
                Random_Element_Descriptor_One = ("\tObject Random Element: Aromatic")
                print(Random_Element_Descriptor_One)
                break
            
            elif Object_Random_Element_Descriptors_Roll_One == 4:
                Random_Element_Descriptor_One = ("\tObject Random Element: Average")
                print(Random_Element_Descriptor_One)
                break
            
            elif Object_Random_Element_Descriptors_Roll_One == 5:
                Random_Element_Descriptor_One = ("\tObject Random Element: Beautiful")
                print(Random_Element_Descriptor_One)
                break
            
            elif Object_Random_Element_Descriptors_Roll_One == 6:
                Random_Element_Descriptor_One = ("\tObject Random Element: Bizarre")
                print(Random_Element_Descriptor_One)
                break
            
            elif Object_Random_Element_Descriptors_Roll_One == 7:
                Random_Element_Descriptor_One = ("\tObject Random Element: Classy")
                print(Random_Element_Descriptor_One)
                break       
            
            elif Object_Random_Element_Descriptors_Roll_One == 8:
                Random_Element_Descriptor_One = ("\tObject Random Element: Colorful")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 9:
                Random_Element_Descriptor_One = ("\tObject Random Element: Creepy")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 10:
                Random_Element_Descriptor_One = ("\tObject Random Element: Cute")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Object_Random_Element_Descriptors_Roll_One == 11:
                Random_Element_Descriptor_One = ("\tObject Random Element: Damaged")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 12:
                Random_Element_Descriptor_One = ("\tObject Random Element: Delicate")
                print(Random_Element_Descriptor_One)
                break     
            
            elif Object_Random_Element_Descriptors_Roll_One == 13:
                Random_Element_Descriptor_One = ("\tObject Random Element: Disgusting")
                print(Random_Element_Descriptor_One)
                break         
            
            elif Object_Random_Element_Descriptors_Roll_One == 14:
                Random_Element_Descriptor_One = ("\tObject Random Element: Cold")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 15:
                Random_Element_Descriptor_One = ("\tObject Random Element: Empty")
                print(Random_Element_Descriptor_One)
                break      
            
            elif Object_Random_Element_Descriptors_Roll_One == 16:
                Random_Element_Descriptor_One = ("\tObject Random Element: Enormous")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 17:
                Random_Element_Descriptor_One = ("\tObject Random Element: Dangerous")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 18:
                Random_Element_Descriptor_One = ("\tObject Random Element: Exotic")
                print(Random_Element_Descriptor_One)
                break      
            
            elif Object_Random_Element_Descriptors_Roll_One == 19:
                Random_Element_Descriptor_One = ("\tObject Random Element: Deliberate")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 20:
                Random_Element_Descriptor_One = ("\tObject Random Element: Delightful")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Object_Random_Element_Descriptors_Roll_One == 21:
                Random_Element_Descriptor_One = ("\tObject Random Element: Faded")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Object_Random_Element_Descriptors_Roll_One == 22:
                Random_Element_Descriptor_One = ("\tObject Random Element: Familiar")
                print(Random_Element_Descriptor_One)
                break        
            
            elif Object_Random_Element_Descriptors_Roll_One == 23:
                Random_Element_Descriptor_One = ("\tObject Random Element: Enormous")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 24:
                Random_Element_Descriptor_One = ("\tObject Random Element: Fancy")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Object_Random_Element_Descriptors_Roll_One == 25:
                Random_Element_Descriptor_One = ("\tObject Random Element: Hard")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 26:
                Random_Element_Descriptor_One = ("\tObject Random Element: Heavy")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 27:
                Random_Element_Descriptor_One = ("\tObject Random Element: Horrible")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 28:
                Random_Element_Descriptor_One = ("\tObject Random Element: Fortunate")
                print(Random_Element_Descriptor_One)
                break     
            
            elif Object_Random_Element_Descriptors_Roll_One == 29:
                Random_Element_Descriptor_One = ("\tObject Random Element: Important")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Object_Random_Element_Descriptors_Roll_One == 30:
                Random_Element_Descriptor_One = ("\tObject Random Element: Frightening")
                print(Random_Element_Descriptor_One)
                break     
            
            elif Object_Random_Element_Descriptors_Roll_One == 31:
                Random_Element_Descriptor_One = ("\tObject Random Element: Large")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 32:
                Random_Element_Descriptor_One = ("\tObject Random Element: Lethal")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 33:
                Random_Element_Descriptor_One = ("\tObject Random Element: Magnificent")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Object_Random_Element_Descriptors_Roll_One == 34:
                Random_Element_Descriptor_One = ("\tObject Random Element: Military")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 35:
                Random_Element_Descriptor_One = ("\tObject Random Element: Modern")
                print(Random_Element_Descriptor_One)
                break       
            
            elif Object_Random_Element_Descriptors_Roll_One == 36:
                Random_Element_Descriptor_One = ("\tObject Random Element: Extravagant")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Object_Random_Element_Descriptors_Roll_One == 37:
                Random_Element_Descriptor_One = ("\tObject Random Element: Helpful")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 38:
                Random_Element_Descriptor_One = ("\tObject Random Element: Mundane")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 39:
                Random_Element_Descriptor_One = ("\tObject Random Element: Natural")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 40:
                Random_Element_Descriptor_One = ("\tObject Random Element: Powerful")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 41:
                Random_Element_Descriptor_One = ("\tObject Random Element: Rare")
                print(Random_Element_Descriptor_One)
                break     
            
            elif Object_Random_Element_Descriptors_Roll_One == 42:
                Random_Element_Descriptor_One = ("\tObject Random Element: Light")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Object_Random_Element_Descriptors_Roll_One == 43:
                Random_Element_Descriptor_One = ("\tObject Random Element: Loud")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Object_Random_Element_Descriptors_Roll_One == 44:
                Random_Element_Descriptor_One = ("\tObject Random Element: Reassuring")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Object_Random_Element_Descriptors_Roll_One == 45:
                Random_Element_Descriptor_One = ("\tObject Random Element: Majestic")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 46:
                Random_Element_Descriptor_One = ("\tObject Random Element: Meaningful")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 47:
                Random_Element_Descriptor_One = ("\tObject Random Element: Mechanical")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Object_Random_Element_Descriptors_Roll_One == 48:
                Random_Element_Descriptor_One = ("\tObject Random Element: Ruined")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 49:
                Random_Element_Descriptor_One = ("\tObject Random Element: Mysterious")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 50:
                Random_Element_Descriptor_One = ("\tObject Random Element: New")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 51:
                Random_Element_Descriptor_One = ("\tObject Random Element: Odd")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 52:
                Random_Element_Descriptor_One = ("\tObject Random Element: Official")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Object_Random_Element_Descriptors_Roll_One == 53:
                Random_Element_Descriptor_One = ("\tObject Random Element: Small")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Object_Random_Element_Descriptors_Roll_One == 54:
                Random_Element_Descriptor_One = ("\tObject Random Element: Smelly")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Object_Random_Element_Descriptors_Roll_One == 55:
                Random_Element_Descriptor_One = ("\tObject Random Element: Positive")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 56:
                Random_Element_Descriptor_One = ("\tObject Random Element: Powerful")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 57:
                Random_Element_Descriptor_One = ("\tObject Random Element: Smooth")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Object_Random_Element_Descriptors_Roll_One == 58:
                Random_Element_Descriptor_One = ("\tObject Random Element: Valuable")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Object_Random_Element_Descriptors_Roll_One == 59:
                Random_Element_Descriptor_One = ("\tObject Random Element: Warm")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Object_Random_Element_Descriptors_Roll_One == 60:
                Random_Element_Descriptor_One = ("\tObject Random Element: Soft")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Object_Random_Element_Descriptors_Roll_One == 61:
                Random_Element_Descriptor_One = ("\tObject Random Element: Watery")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 62:
                Random_Element_Descriptor_One = ("\tObject Random Element: Threatening")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Object_Random_Element_Descriptors_Roll_One == 63:
                Random_Element_Descriptor_One = ("\tObject Random Element: Weapon")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Object_Random_Element_Descriptors_Roll_One == 64:
                Random_Element_Descriptor_One = ("\tObject Random Element: Useful")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 65:
                Random_Element_Descriptor_One = ("\tObject Random Element: Clothing")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Object_Random_Element_Descriptors_Roll_One == 66:
                Random_Element_Descriptor_One = ("\tObject Random Element: Travel")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 67:
                Random_Element_Descriptor_One = ("\tObject Random Element: Tool")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 68:
                Random_Element_Descriptor_One = ("\tObject Random Element: Negative")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Object_Random_Element_Descriptors_Roll_One == 69:
                Random_Element_Descriptor_One = ("\tObject Random Element: Communication")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 70:
                Random_Element_Descriptor_One = ("\tObject Random Element: Food")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 71:
                Random_Element_Descriptor_One = ("\tObject Random Element: Domestic")
                print(Random_Element_Descriptor_One)
                break  
         
            elif Object_Random_Element_Descriptors_Roll_One == 72:
                Random_Element_Descriptor_One = ("\tObject Random Element: Artistic")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 73:
                Random_Element_Descriptor_One = ("\tObject Random Element: Expected")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 74:
                Random_Element_Descriptor_One = ("\tObject Random Element: Unexpected")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 75:
                Random_Element_Descriptor_One = ("\tObject Random Element: Strange")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 76:
                Random_Element_Descriptor_One = ("\tObject Random Element: Resource")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 77:
                Random_Element_Descriptor_One = ("\tObject Random Element: Fuel")
                print(Random_Element_Descriptor_One)
                break     
            
            elif Object_Random_Element_Descriptors_Roll_One == 78:
                Random_Element_Descriptor_One = ("\tObject Random Element: Harmful")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Object_Random_Element_Descriptors_Roll_One == 79:
                Random_Element_Descriptor_One = ("\tObject Random Element: Energy")
                print(Random_Element_Descriptor_One)
                break      
            
            elif Object_Random_Element_Descriptors_Roll_One == 80:
                Random_Element_Descriptor_One = ("\tObject Random Element: Multiple")
                print(Random_Element_Descriptor_One)
                break
            
            elif Object_Random_Element_Descriptors_Roll_One == 81:
                Random_Element_Descriptor_One = ("\tObject Random Element: Single")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 82:
                Random_Element_Descriptor_One = ("\tObject Random Element: Unusual")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 83:
                Random_Element_Descriptor_One = ("\tObject Random Element: Bright")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 84:
                Random_Element_Descriptor_One = ("\tObject Random Element: Ornate")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 85:
                Random_Element_Descriptor_One = ("\tObject Random Element: Broken")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Object_Random_Element_Descriptors_Roll_One == 86:
                Random_Element_Descriptor_One = ("\tObject Random Element: Liquid")
                print(Random_Element_Descriptor_One)
                break
            
            elif Object_Random_Element_Descriptors_Roll_One == 87:
                Random_Element_Descriptor_One = ("\tObject Random Element: Personal")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 88:
                Random_Element_Descriptor_One = ("\tObject Random Element: Intriguing")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Object_Random_Element_Descriptors_Roll_One == 89:
                Random_Element_Descriptor_One = ("\tObject Random Element: Active")
                print(Random_Element_Descriptor_One)
                break     
            
            elif Object_Random_Element_Descriptors_Roll_One == 90:
                Random_Element_Descriptor_One = ("\tObject Random Element: Inactive")
                print(Random_Element_Descriptor_One)
                break    
            
            elif Object_Random_Element_Descriptors_Roll_One == 91:
                Random_Element_Descriptor_One = ("\tObject Random Element: Garbage")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 92:
                Random_Element_Descriptor_One = ("\tObject Random Element: Useless")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 93:
                Random_Element_Descriptor_One = ("\tObject Random Element: Primitive")
                print(Random_Element_Descriptor_One)
                break   
            
            elif Object_Random_Element_Descriptors_Roll_One == 94:
                Random_Element_Descriptor_One = ("\tObject Random Element: Desired")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Object_Random_Element_Descriptors_Roll_One == 95:
                Random_Element_Descriptor_One = ("\tObject Random Element: Healing")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 96:
                Random_Element_Descriptor_One = ("\tObject Random Element: Hidden")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Object_Random_Element_Descriptors_Roll_One == 97:
                Random_Element_Descriptor_One = ("\tObject Random Element: Prized")
                print(Random_Element_Descriptor_One)
                break      
            
            elif Object_Random_Element_Descriptors_Roll_One == 98:
                Random_Element_Descriptor_One = ("\tObject Random Element: Flora")
                print(Random_Element_Descriptor_One)
                break 
            
            elif Object_Random_Element_Descriptors_Roll_One == 99:
                Random_Element_Descriptor_One = ("\tObject Random Element: Moving")
                print(Random_Element_Descriptor_One)
                break  
            
            elif Object_Random_Element_Descriptors_Roll_One == 100:
                Random_Element_Descriptor_One = ("\tObject Random Element: Confusing")
                print(Random_Element_Descriptor_One)
                break                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            
            else:
                print("Your entries are invalid try again")
        except ValueError as exception:
                print("Invalid Entries Try Again") 
                
    while True:
        try:
                if Object_Random_Element_Descriptors_Roll_Two == 1:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Amusing")
                    print(Random_Element_Descriptor_Two)
                    break
                
                elif Object_Random_Element_Descriptors_Roll_Two == 2:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Ancient")
                    print(Random_Element_Descriptor_Two)
                    break
                
                elif Object_Random_Element_Descriptors_Roll_Two == 3:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Aromatic")
                    print(Random_Element_Descriptor_Two)
                    break
                
                elif Object_Random_Element_Descriptors_Roll_Two == 4:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Average")
                    print(Random_Element_Descriptor_Two)
                    break
                
                elif Object_Random_Element_Descriptors_Roll_Two == 5:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Beautiful")
                    print(Random_Element_Descriptor_Two)
                    break
               
                elif Object_Random_Element_Descriptors_Roll_Two == 6:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Bizarre")
                    print(Random_Element_Descriptor_Two)
                    break
                
                elif Object_Random_Element_Descriptors_Roll_Two == 7:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Classy")
                    print(Random_Element_Descriptor_Two)
                    break       
                
                elif Object_Random_Element_Descriptors_Roll_Two == 8:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Colorful")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 9:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Creepy")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 10:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Cute")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Object_Random_Element_Descriptors_Roll_Two == 11:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Damaged")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 12:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Delicate")
                    print(Random_Element_Descriptor_Two)
                    break     
                
                elif Object_Random_Element_Descriptors_Roll_Two == 13:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Disgusting")
                    print(Random_Element_Descriptor_Two)
                    break         
                
                elif Object_Random_Element_Descriptors_Roll_Two == 14:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Cold")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 15:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Empty")
                    print(Random_Element_Descriptor_Two)
                    break      
                
                elif Object_Random_Element_Descriptors_Roll_Two == 16:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Enormous")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 17:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Dangerous")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 18:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Exotic")
                    print(Random_Element_Descriptor_Two)
                    break      
                
                elif Object_Random_Element_Descriptors_Roll_Two == 19:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Deliberate")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 20:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Delightful")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Object_Random_Element_Descriptors_Roll_Two == 21:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Faded")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Object_Random_Element_Descriptors_Roll_Two == 22:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Familiar")
                    print(Random_Element_Descriptor_Two)
                    break        
                
                elif Object_Random_Element_Descriptors_Roll_Two == 23:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Enormous")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 24:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Fancy")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Object_Random_Element_Descriptors_Roll_Two == 25:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Hard")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 26:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Heavy")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 27:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Horrible")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 28:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Fortunate")
                    print(Random_Element_Descriptor_Two)
                    break     
                
                elif Object_Random_Element_Descriptors_Roll_Two == 29:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Important")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Object_Random_Element_Descriptors_Roll_Two == 30:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Frightening")
                    print(Random_Element_Descriptor_Two)
                    break     
                
                elif Object_Random_Element_Descriptors_Roll_Two == 31:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Large")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 32:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Lethal")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 33:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Magnificent")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Object_Random_Element_Descriptors_Roll_Two == 34:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Military")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 35:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Modern")
                    print(Random_Element_Descriptor_Two)
                    break       
                
                elif Object_Random_Element_Descriptors_Roll_Two == 36:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Extravagant")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Object_Random_Element_Descriptors_Roll_Two == 37:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Helpful")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 38:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Mundane")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 39:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Natural")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 40:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Powerful")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 41:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Rare")
                    print(Random_Element_Descriptor_Two)
                    break     
                
                elif Object_Random_Element_Descriptors_Roll_Two == 42:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Light")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Object_Random_Element_Descriptors_Roll_Two == 43:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Loud")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Object_Random_Element_Descriptors_Roll_Two == 44:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Reassuring")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Object_Random_Element_Descriptors_Roll_Two == 45:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Majestic")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 46:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Meaningful")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 47:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Mechanical")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Object_Random_Element_Descriptors_Roll_Two == 48:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Ruined")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 49:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Mysterious")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 50:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: New")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 51:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Odd")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 52:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Official")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Object_Random_Element_Descriptors_Roll_Two == 53:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Small")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Object_Random_Element_Descriptors_Roll_Two == 54:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Smelly")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Object_Random_Element_Descriptors_Roll_Two == 55:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Positive")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 56:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Powerful")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 57:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Smooth")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Object_Random_Element_Descriptors_Roll_Two == 58:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Valuable")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Object_Random_Element_Descriptors_Roll_Two == 59:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Warm")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Object_Random_Element_Descriptors_Roll_Two == 60:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Soft")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Object_Random_Element_Descriptors_Roll_Two == 61:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Watery")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 62:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Threatening")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Object_Random_Element_Descriptors_Roll_Two == 63:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Weapon")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Object_Random_Element_Descriptors_Roll_Two == 64:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Useful")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 65:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Clothing")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Object_Random_Element_Descriptors_Roll_Two == 66:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Travel")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 67:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Tool")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 68:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Negative")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Object_Random_Element_Descriptors_Roll_Two == 69:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Communication")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 70:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Food")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 71:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Domestic")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 72:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Artistic")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 73:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Expected")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 74:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Unexpected")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 75:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Strange")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 76:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Resource")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 77:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Fuel")
                    print(Random_Element_Descriptor_Two)
                    break     
                
                elif Object_Random_Element_Descriptors_Roll_Two == 78:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Harmful")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Object_Random_Element_Descriptors_Roll_Two == 79:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Energy")
                    print(Random_Element_Descriptor_Two)
                    break      
                
                elif Object_Random_Element_Descriptors_Roll_Two == 80:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Multiple")
                    print(Random_Element_Descriptor_Two)
                    break
                
                elif Object_Random_Element_Descriptors_Roll_Two == 81:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Single")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 82:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Unusual")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 83:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Bright")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 84:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Ornate")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 85:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Broken")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Object_Random_Element_Descriptors_Roll_Two == 86:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Liquid")
                    print(Random_Element_Descriptor_Two)
                    break
                
                elif Object_Random_Element_Descriptors_Roll_Two == 87:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Personal")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 88:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Intriguing")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Object_Random_Element_Descriptors_Roll_Two == 89:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Active")
                    print(Random_Element_Descriptor_Two)
                    break     
                
                elif Object_Random_Element_Descriptors_Roll_Two == 90:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Inactive")
                    print(Random_Element_Descriptor_Two)
                    break    
                
                elif Object_Random_Element_Descriptors_Roll_Two == 91:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Garbage")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 92:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Useless")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 93:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Primitive")
                    print(Random_Element_Descriptor_Two)
                    break   
                
                elif Object_Random_Element_Descriptors_Roll_Two == 94:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Desired")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Object_Random_Element_Descriptors_Roll_Two == 95:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Healing")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 96:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Hidden")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Object_Random_Element_Descriptors_Roll_Two == 97:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Prized")
                    print(Random_Element_Descriptor_Two)
                    break      
                
                elif Object_Random_Element_Descriptors_Roll_Two == 98:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Flora")
                    print(Random_Element_Descriptor_Two)
                    break 
                
                elif Object_Random_Element_Descriptors_Roll_Two == 99:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Moving")
                    print(Random_Element_Descriptor_Two)
                    break  
                
                elif Object_Random_Element_Descriptors_Roll_Two == 100:
                    Random_Element_Descriptor_Two = ("\tObject Random Element #2: Confusing")
                    print(Random_Element_Descriptor_Two)
                    break                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                
                else:
                    print("Your entries are invalid try again")
        except ValueError as exception:
                    print("Invalid Entries Try Again")

if __name__ == '__main__':
    RegionDesc_LocationSize()
    Known_Elements()