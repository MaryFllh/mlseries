import os
import sys

"""
Loading shared scripts for unittest
This prevents throwing errors when unit test is running without logging code mounted in utils/
"""
logger_path = os.path.abspath("./shared_utils/unittest")
sys.path.insert(0, logger_path)


# Change directory to /ml because the ml code runs from /ml as root dir and this allows the calls to loading the model, etc. to be successful
os.chdir(os.getcwd() + "/ml")
