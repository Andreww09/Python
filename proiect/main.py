import sys
import time

from Comparator import Comparator

# the timer for rechecking the given locations
DELAY = 5

try:
    assert len(sys.argv) == 3, f"Invalid number of arguments, expected 3, got{len(sys.argv)}"
    comparator = Comparator(sys.argv[1], sys.argv[2])
    # initially the locations are synchronized
    comparator.run(False)
    while True:
        time.sleep(DELAY)
        # check for changes
        comparator.run(True)
except Exception as e:
    print(e)
