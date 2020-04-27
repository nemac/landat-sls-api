# Serverless Landat NDVI AWS Lambda Function

This lambda function takes a set of lat/long coordinates and returns a list of dates and ndvi values

### Setting up the environment

This repository uses the Serverless Framework to build, run, and test a GIS API that runs on AWS Lambda on the Python 3.8 runtime. In order to test locally you will need to install Python 3.8. We recommend using pyenv to manage Python installations, but it's not required.


#### Installing Python 3.8 using pyenv (Optional)

- Install [pyenv](https://github.com/pyenv/pyenv#installation).

- Follow any instructions at the end of the install logs.

- Restart your terminal.

- Run `pyenv install 3.8.2` in your terminal to install Python 3.8. Now when you run `pyenv versions` you should see `3.8.2` in your list of Python installations. Try `pyenv install -l` to see a full list of versions you can install. Check out the full pyenv README for more information about using pyenv.


### Setting up a virtual environment (Recommended)

A virtual environment is a Python abstraction that allows you to create an isolated Python environment. There are many different ways to set up virtual environments. However you do it, we highly recommend using virtual environments for all of your Python projects.

Here's a few ways to set up virtual environements:

- [Pipenv](https://pipenv.pypa.io/en/latest/) is a well-supported environment manager. It plays nicely with pyenv as well. Once Pipenv is installed run `pipenv install -r requirements.txt` to set up your virtual environment and install dependencies.

- If you're using pyenv on Linux or macOS, you can use the [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv#pyenv-virtualenv) pyenv plugin.

- You could use the built-in Python module [venv](https://docs.python.org/3/library/venv.html). If you're using pyenv you will want to run `pyenv global 3.8.2` before setting up your virtualenv.

- There's also the classic [virtualenv](https://virtualenv.pypa.io/en/latest/) library. If you go this route you might want to check out the popular tool [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/stable/).


### Install dependencies

- Install [nodejs](https://nodejs.org/en/) if you don't have it already. Make sure to choose the LTS version.

- Install the [Serverless Framework](https://serverless.com/framework/docs/getting-started/) using npm: `npm install -g serverless`.

- Unless you're using Pipenv, you'll need to activate your virtual environment (see the documentation for your virtual environment manager). Once you've activated your environment, run `pip install -r requirements.txt`. If you're using pipenv then the install command you used above does this for you.

- Install serverless dependencies: `npm install`


### Run a local API

You can spin up a local API to test against by running:

```serverless offline```

You should see something like this:

```bash
Serverless: Starting Offline: dev/us-east-1.

Serverless: Routes for landat-ndvi:
Serverless: GET /landat-ndvi
Serverless: POST /{apiVersion}/functions/landat-ndvi-dev-landat-ndvi/invocations

Serverless: Offline [HTTP] listening on http://localhost:3000
Serverless: Enter "rp" to replay the last request
```

Test your offline API with curl:

```bash
curl http://localhost:3000/landat-ndvi/\?lng\=-82.8\&lat\=35.8
```

You should get a response that looks something like:

```bash
["20000108,54", "20000116,53", "20000124,52", "20000201,51", "20000209,50", ...
```

### Deploying

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
