# Serverless Landat NDVI AWS Lambda Function

This lambda function takes a set of lat/long coordinates and returns a list of dates and ndvi values

## Setting up the environment

This repository uses the Serverless Framework to build, run, and test a GIS API that runs on AWS Lambda on the Python 3.8 runtime. In order to test locally you will need to install Python 3.8. We recommend using pyenv to manage Python installations, but it's not required.

#### Install Python 3.8 using pyenv (Optional)

Pyenv is a useful tool for managing multiple Python installations with different versions.

- Install [pyenv](https://github.com/pyenv/pyenv#installation). Check for any instructions at the end of the install logsand restart your terminal after you're done.

- Run `pyenv install 3.8.2` in your terminal to install Python 3.8. Now when you run `pyenv versions` you should see `3.8.2` in your list of Python installations. Try `pyenv install -l` to see a full list of versions you can install. Check out the full pyenv README for more information.

- Run `pyenv local 3.8.2` to set the Python version for this directory to your 3.8 installation.

### Install dependencies

- Install Python 3.8

- Install [pipenv](https://pipenv.pypa.io/en/latest/): `pip install pipenv`. Pipenv is a tool for managing Python environments. It creates virtual environments for you and manages dependencies. And it plays well with pyenv!

- Install [nodejs](https://nodejs.org/en/) if you don't have it already. Choose the LTS version.

- Install the [Serverless Framework](https://serverless.com/framework/docs/getting-started/) with `npm install -g serverless`.

- Install serverless dependencies: `npm install`

- Install Python dependencies: `pipenv install`


## Run a local API

Spin up a local API to test against. Use `pipenv run` to use the virtual environment for the project.

```pipenv run serverless offline```

You should see something like this:

```
offline: Starting Offline: dev/us-east-1.
offline: Offline [http for lambda] listening on http://localhost:3002

   ┌───────────────────────────────────────────────────────────────────────────────┐
   │                                                                               │
   │   GET | http://localhost:3000/dev/landat-ndvi                                 │
   │   POST | http://localhost:3000/2015-03-31/functions/landat-ndvi/invocations   │
   │                                                                               │
   └───────────────────────────────────────────────────────────────────────────────┘

offline: [HTTP] server ready: http://localhost:3000 🚀
offline: 
offline: Enter "rp" to replay the last request
```

Test your offline API with curl:

```bash
curl http://localhost:3000/dev/landat-ndvi/\?lng\=-82.8\&lat\=35.8
```

You should get a response that looks something like:

```bash
["20000108,54", "20000116,53", "20000124,52", "20000201,51", "20000209,50", ...
```

## Deploying

Deploy your API:

```bash
# Deploy to beta
pipenv run serverless deploy --stage beta

# Deploy to prod
pipenv run serverless deploy --stage prod
```

The expected result should be similar to:

```bash
Serverless: Generating requirements.txt from Pipfile...
Serverless: Parsed requirements.txt from Pipfile in /...
Serverless: Using static cache of requirements found at /...
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
curl https://995z88gokc.execute-api.us-east-1.amazonaws.com/beta/landat-ndvi\?args\=-82.49633789062501,35.58138418324621
```

Expected Results (Truncated in the middle)
```
["20000108,53", "20000116,52", "20000124,52", "20000201,51", ........... "20171209,55", "20171217,52", "20171225,48", "20180102,49"]
```
