#Inference engine
#Author: Joshua DeNio
#Date: 04/01/2020
#Description: This is the main inference engine for the weather hazards app.

#Imports
import Region
#import Gui_interface

"""
Function name:
Description:
Input:
Output:
Preconditions:
Postconditions:
"""
def inference_engine(region_id, image, region_list):

    hazards = []
    adjacent_regions = []

    # Make the set of adjacent regions to region ( use getter for adjacent regions)
    adjacent_regions = region_list[region_id].get_adjacent_regions()

    # Check image for hazards (check_image returns a list of hazards)
    hazards = check_image(image)

    # Issue a hazard warning if there is a hazard in our selected region

    # Test to see if the condition will spread to any adjacent regions
    #   if so call a recursive call on the region and pass in the region_id,
    #   image and region_list and call for each adjacent region.

    print("Finished")


"""
Function name:
Description:
Input:
Output:
Preconditions:
Postconditions:
"""
def check_image(image):

    hazards = []

    #Call tensorflow functionality to check the image for fire: if found add hazard

    #Call tensorflow functionality to check the image for snow: if found add hazard

    #Call tensorflow functionality to check the image for flooding: if found add hazard

    #Call tensorflow functionality to check the image for storms: if found add hazard

    return hazards

def main():

    #List to store regions
    region_list = []
    #The number of regions we want can be changed by user input
    number_of_regions = 20

    #Get user input for number of regions from GUI


    #Generate regions and populate the list
    for x in range(number_of_regions):

        #Get the regions name from GUI
        name = "temp"
        new_region = Region(name)

    #Set the x,y coordinants of all regions

    #Adjust conditions if needed

    # Run the inerence engine
    
main()