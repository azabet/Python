"""
This module plots a world map of countries' attribute.
It takes a list of countries and their corresponding values.
Written by Amir Zabet @ 2014/05/13
"""

import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from matplotlib.colorbar import ColorbarBase

def plot(countries,values,label='',verbose=False):
    """
    Usage: worldmap.plot(countries, values, label)
    """
    countries_shp = shpreader.natural_earth(resolution='110m',category='cultural',
                                            name='admin_0_countries')
    ## Create a plot
    fig = plt.figure()
    ax = plt.axes(projection=ccrs.PlateCarree())
    ## Create a colormap
    cmap = plt.get_cmap('RdYlGn_r')
    val = values[np.isfinite(values)]
    mean = val.mean()
    std = val.std()
    norm = Normalize(vmin=0,vmax=mean+2*std)
    smap = ScalarMappable(norm=norm,cmap=cmap)
    ax2 = fig.add_axes([0.3, 0.9, 0.4, 0.05])
    cbar = ColorbarBase(ax2,cmap=cmap,norm=norm,orientation='horizontal')
    cbar.set_label(label)
    ## Add countries to the map
    for country in shpreader.Reader(countries_shp).records():
        countrycode = country.attributes['adm0_a3']
        countryname = country.attributes['name_long']
        ## Check for country code consistency
        if countrycode == 'SDS': #South Sudan
           countrycode = 'SSD'
        elif countrycode == 'ROU': #Romania
           countrycode = 'ROM'
        elif countrycode == 'COD': #Dem. Rep. Congo
           countrycode = 'ZAR'
        elif countrycode == 'KOS': #Kosovo
           countrycode = 'KSV'
        if countrycode in countries:
           val = values[countries==countrycode]
           if np.isfinite(val):
              color = smap.to_rgba(val)
           else:
              color = 'grey'
        else:
           color = 'w'
           if verbose:
              print("No data available for "+countrycode+": "+countryname)
        ax.add_geometries(country.geometry,ccrs.PlateCarree(),facecolor=color,label=countryname)
    plt.show()
