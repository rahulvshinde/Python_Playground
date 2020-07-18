"""Write a script which parses /var/log/messages and generates a CSV with two columns: minute, number_of_messages
"""
import re

log_filename = "log.log"
csv_filename = "counts.csv"
time_count = {}

output = {}
#Parse out the timedate stamp Jan 20 05:22:37 to capture two groups 1.) Jan 20 05:22 2.) log output e.g.
#R: cs3:  The cool service on fakehost does not appear to be communicating with the cool
regex = re.compile(r'^(\w+ \d+ \d+:\d+):\d+ \w+ .*$')
with open(log_filename, "r") as myfile:
    for log_line in myfile:
        match = regex.match(log_line)
        # print match.group(1)
        if match.group(1) in output:
            output[match.group(1)] += 1
        else:
            output.update({match.group(1):1})
with open("counts.csv", 'w') as csvf:
    csvf.write("minute, number_of_messages")
    for timestamp in sorted(output.keys()):
        print(timestamp, output[timestamp])
        csvf.write("{},{}".format(timestamp, output[timestamp]))