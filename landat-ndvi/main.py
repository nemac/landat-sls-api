import calendar
import json
import os
import rasterio
from Config import *
from pyproj import CRS, Transformer

def lambda_handler(event, context):
  bucket_name = os.environ['BUCKET_NAME'] # From AWS Lambda environment variable
  tifs = LANDAT_NDVI_FILES
  ndviValues = []
  from_crs = CRS("epsg:4326")
  transformer = Transformer.from_crs("epsg:4326", LANDAT_TIF_PROJECTION, always_xy=True)
  try:
    lng = float(event['queryStringParameters']['lng'])
    lat = float(event['queryStringParameters']['lat'])
    x,y = transformer.transform(lng, lat)
    coords = [(x, y)]
    for tif in tifs:
      times = []
      # Extract the year from the tif file
      year = int(tif[4:8])
      dates_list = LEAP_DATES_LIST if calendar.isleap(year) else NONLEAP_DATES_LIST
      times = [ '' + str(year) + x for x in dates_list ]
      # The last timepoint rolls over to the next year
      times[-1] = '' + str(year+1) + times[-1][4:]
      datasource = "s3://%s/%s" % (bucket_name, tif)
      with rasterio.open(datasource) as src:
        result = src.sample(coords)
        for i, v in enumerate(next(result)):
          ndviValues.append('%s,%s' % (times[i],v))
   
    return {
      'statusCode': 200,
      'body': json.dumps(ndviValues),
      "headers": {
        "Content-Type": 'application/json',
        "Access-Control-Allow-Origin": "*"
      }
    }

  except Exception as e: 
    print('exception is: ' + e)
    return {
      'statusCode': 400,
      'body': json.dumps(e)
    }
