import os, sys
file_path = '/scratch2/NCEPDEV/marine/Jong.Kim/mom6-tools/mom6_tools'
sys.path.append(os.path.dirname(file_path))

from mom6_tools.MOM6grid import MOM6grid
from mom6_tools.latlon_analysis import time_mean_latlon
from mom6_tools.m6plot import xyplot
import matplotlib.pyplot as plt
import warnings
import xarray as xr
import argparse

# required arg
parser = argparse.ArgumentParser()
parser.add_argument('-grid', required=True)
parser.add_argument('-data', required=True)               
args = parser.parse_args()

print(f'Loading grid... {args.grid}')
print(f'Loading data... {args.data}')

nc = xr.open_mfdataset(args.data, decode_times=False)
grd= MOM6grid(args.grid)
grd.area_t=grd.Ah
xyplot(nc.SST[0,:,:].to_masked_array(),grd.geolon,grd.geolat,save='sst.png')

