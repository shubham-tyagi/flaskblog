import os

class Config(object):
    SECRET_KEY = os.environ.get ('SECRET_KEY') or 'you-will-never-guess'
    # The first term looks for the value of an environment variable, also called SECRET_KEY. The second term, 
    # is just a hardcoded string.
    #  This is a pattern that you will see me repeat often for configuration variables.