# pop_europe
A ML approach to figuring out where people live.


This code estimates the population density in high resolution over EU using sentinel-2 data supplemented with Sentinel-1 and nightlight data. 

I created this project as a starting point for two groups of student groups in an ML course. They have since worked more on the code and developed and tested alternative approaches. The students tested various CNN based approaches and variations on the clustering+regression approach in this project. The most promising of the CNN based results seemed to be based on ResNet-50. Unfortunately the CNN based approach cannot generate super-resolution outputs and is rather computationally expensive. For those reasons i prefer the simpler old school methods. 


The R2 of predicted population is 0.75-0.8 so far, which is not that great (depending on how training data are selected and which bands are included). -But with "rescaling" this is still very useful if you trust the coarse resolution census data used as inputs. The main difficulties seem to be extremely dense city centers and industrial areas. 

Ideas for improvement:
* More types of data.
* non-linear modelling. (Issue: linear has been chosen because formula transferring between the pixel function and area average function is trivial - this is an issue because we only have "ground truth" as area averages.)



Feel free to contact me if you want to collaborate on this. 


![Result](figures/population_estimates.png)
Top row: S2 rgb
Middle row: per pixel pop density
Bottom row: pop density per ha (gaussian smooth of middle row)


# Input data: 
* Population density in 1km resolution from https://ec.europa.eu/eurostat/web/gisco/geodata/grids
* Sentinel-2 multiband images in 20m resolution.
* Sentinel-1 VV/VH images on same grid
* VIIRS Lunar Gap-Filled BRDF Nighttime Lights Daily (resampled to same grid.)


# Approach
* unsupervised clustering of S2 multiband (after a PCA/ICA transform)
* Bounded linear regression to determine the relative pop density in each cluster.
* (optional) rescale to force a match to census data.


# Scripts: 
* populationgrid.ipynb: script to convert the GISCO 1km population data to a geotiff.
* ee.ipynb: a script that downloads a set of random 5x5 km Sentinel-2 tiles in 20m resolution using earthengine. 
* Clustering: the script that does clustering and regression. 






