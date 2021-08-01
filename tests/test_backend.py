from weather_service import backend


def test_get_forecast(log, app):
    """Example test set up so candidate won't have to waste time trying to
    get this to work.

    """
    # Setup needed for testing with a flask application:
    with app.app_context():
        # Flask app context using code goes here E.g. backend.get_forecast(...)
        pass

    assert True is False
