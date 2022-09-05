"""
Part 2:
Create a copy of your script from part 1 and modify it to be a functioning script tool (both a toolbox and .py component)
Script should take arguments (input defibrillators and buildings, output data, and extent to use)
Submit both the .tbx and the .py file
Note: I should be able to run the script tool without modifying the script at all to update paths
"""
import arcpy

defibs = arcpy.GetParameterAsText(0)  #r"C:\Users\student\OneDrive - University of Redlands\GIS 467_667 SP 22\GIS 467 Assignment 7\campus.gdb\defibrillators"
buildings = arcpy.GetParameterAsText(1) #r"C:\Users\student\OneDrive - University of Redlands\GIS 467_667 SP 22\GIS 467 Assignment 7\campus.gdb\buildings"
output = arcpy.GetParameterAsText(2) #r"C:\Users\student\OneDrive - University of Redlands\GIS 467_667 SP 22\GIS 467 Assignment 7\campus.gdb\output"

#rest of code
with arcpy.EnvManager(extent=buildings):
    arcpy.analysis.CreateThiessenPolygons(defibs, 
                                          output)