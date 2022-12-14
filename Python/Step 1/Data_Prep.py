
#----------------------- Step 1 

# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Data_Prep.py
# Created on: 2022-08-21 14:47:35.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: Data_Prep <NHDFlowline> <PRISM_ppt_30yr_normal_4kmM3_annual_asc_asc> <NHDWaterbody> <WBD_Subwatershed_selection> 
# Description: 
# ---------------------------------------------------------------------------


# You will need to have ArcGIS licence to run this script

# Import arcpy module

import arcpy

# Script arguments
NHDFlowline = arcpy.GetParameterAsText(0)
if NHDFlowline == '#' or not NHDFlowline:
    NHDFlowline = "NHDFlowline" # provide a default value if unspecified

PRISM_ppt_30yr_normal_4kmM3_annual_asc_asc = arcpy.GetParameterAsText(1)
if PRISM_ppt_30yr_normal_4kmM3_annual_asc_asc == '#' or not PRISM_ppt_30yr_normal_4kmM3_annual_asc_asc:
    PRISM_ppt_30yr_normal_4kmM3_annual_asc_asc = "PRISM_ppt_30yr_normal_4kmM3_annual_asc.asc" # provide a default value if unspecified

NHDWaterbody = arcpy.GetParameterAsText(2)
if NHDWaterbody == '#' or not NHDWaterbody:
    NHDWaterbody = "NHDWaterbody" # provide a default value if unspecified

WBD_Subwatershed_selection = arcpy.GetParameterAsText(3)
if WBD_Subwatershed_selection == '#' or not WBD_Subwatershed_selection:
    WBD_Subwatershed_selection = "WBD_Subwatershed selection" # provide a default value if unspecified

# Local variables:
elev_cm__2_ = "elev_cm"
DEM = "c:\\Users\\r_sigdel\\documents\\ArcGIS\\Default.gdb\\DEM"  # Please change the working directory
Watershed_Boundary = "C:\\Users\\r_sigdel\\Documents\\ArcGIS\\Default.gdb\\Watershed_Boundary"   # Please change the working directory
DEM_Result01 = "C:\\Users\\r_sigdel\\Documents\\ArcGIS\\Default.gdb\\DEM_Result01"   # Please change the working directory
PRISM_ppt_30yr_normal_4kmM3_ = "C:\\Users\\r_sigdel\\Documents\\ArcGIS\\Default.gdb\\PRISM_ppt_30yr_normal_4kmM3_"   # Please change the working directory
PRISM_clip_location1 = "C:\\Users\\r_sigdel\\Documents\\ArcGIS\\Default.gdb\\PRISM_clip_location1"  # Please change the working directory
NHDWaterbody_1_Project = "C:\\Users\\r_sigdel\\Documents\\ArcGIS\\Default.gdb\\NHDWaterbody_1_Project"  # Please change the working directory
Waterbody_clip1 = "C:\\Users\\r_sigdel\\Documents\\ArcGIS\\Default.gdb\\Waterbody_clip1"  # Please change the working directory
NHD_Flow = "C:\\Users\\r_sigdel\\Documents\\ArcGIS\\Default.gdb\\NHD_Flow" # Please change the working directory
NHD_Clip_Result01 = "C:\\Users\\r_sigdel\\Documents\\ArcGIS\\Default.gdb\\NHD_Clip_Result01" # Please change the working directory
NHD_Clip_Result__3_ = NHD_Clip_Result01
CumulativeArea = "CumulativeArea"
NHD_Clip_Result__2_ = NHD_Clip_Result__3_
NHD_Clip_Result__5_ = NHD_Clip_Result__2_

# Process: Raster Calculator
arcpy.gp.RasterCalculator_sa("\"%elev_cm (2)%\"/100", DEM)

# Process: Project (2)
arcpy.Project_management(WBD_Subwatershed_selection, Watershed_Boundary, "PROJCS['NAD_1983_Albers',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Albers'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['central_meridian',-96.0],PARAMETER['Standard_Parallel_1',29.5],PARAMETER['Standard_Parallel_2',45.5],PARAMETER['latitude_of_origin',23.0],UNIT['Meter',1.0]],VERTCS['Unknown VCS',VDATUM['Unknown'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['User_Defined_Unit',0.01]]", "", "GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "NO_PRESERVE_SHAPE", "", "NO_VERTICAL")

# Process: Clip
arcpy.Clip_management(DEM, "-2639279.9632896 1147606.05910667 -1386691.27938268 2641621.22492985", DEM_Result01, Watershed_Boundary, "", "ClippingGeometry", "NO_MAINTAIN_EXTENT")

# Process: Project Raster
arcpy.ProjectRaster_management(PRISM_ppt_30yr_normal_4kmM3_annual_asc_asc, PRISM_ppt_30yr_normal_4kmM3_, "PROJCS['NAD_1983_Albers',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Albers'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['central_meridian',-96.0],PARAMETER['Standard_Parallel_1',29.5],PARAMETER['Standard_Parallel_2',45.5],PARAMETER['latitude_of_origin',23.0],UNIT['Meter',1.0]],VERTCS['Unknown VCS',VDATUM['Unknown'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['User_Defined_Unit',0.01]]", "NEAREST", "4676.7657753533 4676.7657753533", "", "", "GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "NO_VERTICAL")

# Process: Clip (3)
arcpy.Clip_management(PRISM_ppt_30yr_normal_4kmM3_, "-2639279.9632896 1147606.05910667 -1386691.27938268 2641621.22492985", PRISM_clip_location1, Watershed_Boundary, "", "ClippingGeometry", "NO_MAINTAIN_EXTENT")

# Process: Project (3)
arcpy.Project_management(NHDWaterbody, NHDWaterbody_1_Project, "PROJCS['NAD_1983_Albers',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Albers'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['central_meridian',-96.0],PARAMETER['Standard_Parallel_1',29.5],PARAMETER['Standard_Parallel_2',45.5],PARAMETER['latitude_of_origin',23.0],UNIT['Meter',1.0]],VERTCS['Unknown VCS',VDATUM['Unknown'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['User_Defined_Unit',0.01]]", "", "GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "NO_PRESERVE_SHAPE", "", "NO_VERTICAL")

# Process: Clip (4)
arcpy.Clip_analysis(NHDWaterbody_1_Project, Watershed_Boundary, Waterbody_clip1, "")

# Process: Project
arcpy.Project_management(NHDFlowline, NHD_Flow, "PROJCS['NAD_1983_Albers',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Albers'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['central_meridian',-96.0],PARAMETER['Standard_Parallel_1',29.5],PARAMETER['Standard_Parallel_2',45.5],PARAMETER['latitude_of_origin',23.0],UNIT['Meter',1.0]],VERTCS['Unknown VCS',VDATUM['Unknown'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['User_Defined_Unit',0.01]]", "", "GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "NO_PRESERVE_SHAPE", "", "NO_VERTICAL")

# Process: Clip (2)
arcpy.Clip_analysis(NHD_Flow, Watershed_Boundary, NHD_Clip_Result01, "")

# Process: Join Field
arcpy.JoinField_management(NHD_Clip_Result01, "COMID", CumulativeArea, "ComID", "OID;ComID;TotDASqKM;DivDASqKM")

# Process: Add Field
arcpy.AddField_management(NHD_Clip_Result__3_, "CUMDRAINAG", "FLOAT", "12", "2", "", "", "NULLABLE", "REQUIRED", "")

# Process: Calculate Field
arcpy.CalculateField_management(NHD_Clip_Result__2_, "CUMDRAINAG", "[TotDASqKM]", "VB", "")

