import boto3
import calendar
import json
import os
import rasterio
import re
from Config import *
from rasterio.session import AWSSession
from rasterio.vrt import WarpedVRT

print('loading function')

# Create an S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
  bucket_name = os.environ['BUCKET_NAME'] # From AWS Lambda environment variable
  try:
    bucket_objects = []
    # List all objects in bucket and put it into a list
    for key in s3.list_objects(Bucket=bucket_name)['Contents']:
      bucket_objects.append(key['Key'])
    regex = re.compile('.*\.xml')
    tifs = [i for i in bucket_objects if not regex.match(i)] # remove all xmls and walk away with only tifs

    # Open each tif from object store and grab the ndvi value for a lat/long point
    ndviValues = []
    for tif in tifs:
      times = []
      # Extract the year from the tif file
      year = int(tif[4:8])
      dates_file = LEAP_DATES_FILE if calendar.isleap(year) else NONLEAP_DATES_FILE
      f = open(dates_file)
      dates = [ x.rstrip('\n') for x in f.readlines() ]
      f.close()
      times = [ '' + str(year) + x for x in dates ]
      # The last timepoint rolls over to the next year
      times[-1] = '' + str(year+1) + times[-1][4:]
      datasource = "s3://%s/%s" % (bucket_name, tif)
      with rasterio.Env(AWSSession(boto3.Session()), AWS_VIRTUAL_HOSTING=False) as env:
        with rasterio.open(datasource) as src:
          with WarpedVRT(src, crs='EPSG:4326') as vrt:
            args = event['queryStringParameters']['args']
            arglist = args.split(",")
            print(arglist)
            lon = float(arglist[0])
            lat = float(arglist[1])
            coords = [(lon, lat)]
            result_gen = vrt.sample(coords, list(range(1, 47)))
            for i, v in enumerate(next(result_gen)):
              ndviValues.append("%s,%s" % (times[i],v))
   
    return {
      'statusCode': 200,
      'body': json.dumps(ndviValues)
    }

  except:
    print('Something went wrong!')
    return {
      'statusCode': 400,
      'body': json.dumps('Error!')
    }
