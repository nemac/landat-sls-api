# Serverless Landat NDVI

This lambda function takes a set of lat/long coordinates and returns a list of dates and ndvi values

## Setup

In order to deploy the function simply run

```bash
serverless deploy
```

The expected result should be similar to:

```bash
Serverless: Generating requirements.txt from Pipfile...
Serverless: Parsed requirements.txt from Pipfile in /Users/jbliss/landat-ndvi/.serverless/requirements.txt...
Serverless: Using static cache of requirements found at /Users/jbliss/Library/Caches/serverless-python-requirements/1b64de819e599fff2506e5351b26bdd8092db40d01e8c3b85ebb91cd06bc7031_slspyc ...
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Injecting required Python packages to package...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service landat-ndvi.zip file to S3 (48.17 MB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
..............
Serverless: Stack update finished...
Service Information
service: landat-ndvi
stage: dev
region: us-east-1
stack: landat-ndvi-dev
resources: 11
api keys:
  None
endpoints:
  GET - https://995z88gokc.execute-api.us-east-1.amazonaws.com/dev/landat-ndvi
functions:
  landat-ndvi: landat-ndvi-dev-landat-ndvi
layers:
  None
Serverless: Run the "serverless" command to setup monitoring, troubleshooting and testing.
```

Sample Use Case
```
curl https://995z88gokc.execute-api.us-east-1.amazonaws.com/dev/landat-ndvi\?args\=-82.49633789062501,35.58138418324621
```

Expected Results (Truncated in the middle)
```
["20000108,53", "20000116,52", "20000124,52", "20000201,51", ........... "20171209,55", "20171217,52", "20171225,48", "20180102,49"]
```
