import os
import sys

from dotenv import load_dotenv

load_dotenv()
"""
Loading shared scripts for unittest
This prevents throwing errors when unit test is running without logging code mounted in utils/
"""
test_path = os.path.abspath("../shared_utils/unittest")
sys.path.insert(0, test_path)
