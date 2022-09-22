# Post-Wildfire Debris-Flow Runout Modeling

Debris flows are a major natural hazard in mountainous regions, particularly in the aftermath of wildfires. This project estimates potential debris-flow runout length based on topographic parameters derived from widely available geospatial data on elevation, hydrography, and
precipitation. The underlying model is the average channel slope model developed by Prochaska et al. (2008). Model performance was tested using 34 observed debris flows across seven states with runout lengths provided by the US Landslide Inventory or measured from georeferenced aerial imagery, resulting in an average root mean square error of 0.049, with errors ranging from -0.83 to 0.41. For more details on the GIS workflow, and to access the Python and R scripts used to generate these modeling results, see [https://github.com/riverscience/Debris_Flow_Modelling].


Note the following caveats:

 

* The model used here is applicable only to non-volcanic debris flows, not to lahars or flows that deposit within a canyon.
* The model was developed using data from moderately sized debris flows (1000 to 10,000 metric tonnes mass) and is not applicable to very large debris flows.
* The model is based solely on topography and does not account for differences in material properties.
* These modeling results are for research purposes only. This work is preliminary and subject to revision.


References
Prochaska, A.B., P.M. Santi, J.D. Higgins, and S.H. Cannon. 2008. Debris-flow runout
predictions based on the average channel slope (ACS).
