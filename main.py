# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("11:06 AM", "2:02",'thurSday'))


# Run unit tests automatically
main(module='test_module', exit=False)