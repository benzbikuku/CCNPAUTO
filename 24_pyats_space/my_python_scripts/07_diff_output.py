from genie.utils.diff import Diff
import json
with open('/home/benz/CCNPAUTO/24_pyats_space/my_python_scripts/output1.info') as data:
	output1 = json.load(data)

with open('/home/benz/CCNPAUTO/24_pyats_space/my_python_scripts/output2.info') as data:
	output2 = json.load(data)
diff = Diff(output1, output2)
diff.findDiff()
print(diff)
