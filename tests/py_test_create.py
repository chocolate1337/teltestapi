from tavern.core import run
from logging import config
import yaml

with open("log_spec.yaml", "r") as log_spec_file:
    config.dictConfig(yaml.load(log_spec_file))


success = run("test.tavern.yaml", {})

if not success:
    print("Error running tests")
