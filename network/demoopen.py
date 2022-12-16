import os
output_command = os.popen("netstat -nb").read()
print(output_command)