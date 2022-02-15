# weather service

This is the test for backend developers. The test for frontend developers is [here](https://github.com/SuperCarers/weather-service-frontend)

Please do not push your solution to a publicly available repo.

# Introduction

This is a Python/Flask service which provides an API to get a forecast for a
given city.

The service requires an API key from [openweathermap](https://www.openweathermap.org)
(free registration required). This API"s backend uses the Open Weather API
endpoint https://openweathermap.org/forecast5.


# Getting it running

The implementation of this service has some problems that need to be fixed
before it will run. Once the project has been set up you should be able to run
the service by calling:

    # Set up the package to run in development mode:
    python setup.py develop

    # Running any test you might choose to do:
    pytest -sv

    # Running the webapp locally:
    FLASK_APP=app.py flask run


# Existing API

I would like to make the following calls against this web service using "curl".
The submitted result will be put through automated testing to verify the API
is working.

When the service is running it can be checked using the ping endpoint:

    curl http://localhost:5000/ping
    {
      "name": "weatherservice",
      "status": "ok",
      "version": "1.0.0"
    }

The weather endpoint has the form:

    curl http://<host:ip>/<city>/<date>/<hour minute>/

    curl http://localhost:5000/london/20171005/2200/
    {
        "description": "broken clouds",
        "humidity": "66%",
        "pressure": 1027.51,
        "temperature": "285.25"
    }

The service also supports recovering just the fields: description, humidity,
pressure & temperature:

    curl http://<host:ip>/<city>/<date>/<hour minute>/<field>/

    curl http://localhost:5000/london/20171005/2200/humidity/
    {
      "humidity": "66%"
    }

    curl http://localhost:5000/london/20171005/2200/temperature/
    {
      "temperature": "285.25"
    }


When no data is found for the date and time given the API will respond with:

    curl http://localhost:5000/london/21171005/2200/temperature
    {
      "message": "No data for 2117-10-05 22:00",
      "status": "error"
    }


# Pair-programming tasks

- What is your testing approach? (We prefer pytest)?
- Get the implementation working using the dummy data.
- Implement a way to return the temperature in Fahrenheit, Kelvin or Celcius.
- Convert to using the openweathermap service to retrieve real data.
- Create a docker container which can be configured with the API key.
- Run the docker container and verify the API.

# Questions for interview

Please prepare answers for these questions in advance of the interview.

- What would you approach to returning data be if a request is made between two times that the https://openweathermap.org/forecast5 data set supports.
- How will you scale the weather service to handle increasing load.
- How would you measure the weather service response handling?
- What if any data storage would you use as the backend for the weather service?
- If you had a storage backend, how would it scale?
