import json
import sys
import yaml


y = yaml.safe_load(sys.stdin)

print(json.dumps(y))
