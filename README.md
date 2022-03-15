# weather service

This is the test for backend developers.

Please do not push your solution to a publicly available repo.

# Introduction

This is a Python/Flask API to get a forecast for London during Oct 2017.

# Environment set up

Checkout the code and set up the service ready for development as follows:

    # Set up the package to run in development mode:
    python setup.py develop

    # Running the webapp locally reloading when changes are made:
    FLASK_APP=app.py FLASK_ENV=development flask run

    # Optional: Running any test you might choose to write:
    pytest -sv


# Check the service is running after set up

When the app is running you can do the following curl request:

    curl http://localhost:5000/ping
    {
      "name": "weatherservice",
      "status": "ok",
      "version": "1.0.0"
    }


# Pair-programming tasks

In the first 30 minutes you are expected to complete the following tasks:
- Implement the get forecast endpoint.
- Build and run the flask application inside a docker container and verify the
  endpoint is working as expected, using a curl request

In the final 15 minutes of the interview:
- Discuss the interview questions.


## Get forecast endpoint behaviour

The task is to implement the get_forecast() inside backend.py, returing data to
implement the following GET requests

### A GET request for a known date and time

    curl http://<host:ip>/<city>/<date>/<hour minute>/

    curl http://localhost:5000/london/20171018/1500/
    {
        "description": "light rain",
        "humidity": "100%",
        "pressure": 1015.55,
        "temperature": 290.44
    }

### A GET request for an unknown date and time

    curl http://localhost:5000/london/21171005/2200/
    {
      "message": "No data for 2117-10-05 22:00",
      "status": "error"
    }


## Questions for interview

Please prepare answers for these questions in advance of the interview.

- How would you return data for a request between two data points in the dummy data.
- How will you scale the weather service to handle increasing load.
  - For example, scaling the systems to 1k Requests Per Minute (RPM) and then 5k RPM.
- Where do you think the bottlenecks lie in scaling such a system?
- How do you ensure that the API response time is always within tolerable range?
- What if any data storage would you use as the backend for the weather service?
  - If you had a storage backend, how would it scale?

Optional question:

- How might we minimise the use of the system resources (cloud hosting costs)?
  - The system should still be able to scale as needed.
