This repo wraps [@gkossakowski's covid-19 repo](https://github.com/gkossakowski/covid-19/) into a script that pulls the most recent data and sends it via a collection of `\n` separated JSON records into provided URL.

## Parameters

There are several environment properties that control the execution of the script:

* `URL` - the actual URL where the POST is being sent (required)
* `ALL` - when set to True, not only the today's data but also all historical data are being sent
* `MAX_RECORDS_IN_POST` - number of records to include in a single request
* `VERBOSE` - when set to True, the sent contents is being printed out on the console too

## Running locally

Make sure the Python requirements are met (`pip3 install -r requiremets.txt`) and run following command

`URL="https://MY_URL" ./update-and-push.sh`

This will first process the notebook script and update CSV with current variables and then push the data to your URL

## Running as a Docker image

To build image:

`docker build -t covid19 .`

To run image:

`docker run -e URL="https://MY_URL" -e VERBOSE=True covid19`

To run image with all historical data being sent:

`docker run -e URL="https://MY_URL" -e VERBOSE=True -e ALL=True covid19`
