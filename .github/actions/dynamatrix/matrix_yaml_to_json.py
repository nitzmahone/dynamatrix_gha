import json
import yaml

# FIXME: this is subject to code injection; sanity check required
y = yaml.safe_load("""${{ inputs.matrixstr }}""")
print(json.dumps(y))