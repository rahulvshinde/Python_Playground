log_filename = "m.txt"
csv_filename = "counts.csv"
time_count = {}

# # Read log messages
# def readlogs(log_filename):
#     with open(log_filename, 'r') as logf:
#         for line in logf.readlines():
#             time = line.split(" ")
#             # print time
#             # hr_min = time[2][:-3]
#             # print hr_min
#             combined_time = time[0] + " " + time[1] + " " + time[2][:-3]
#             print (combined_time)
#             if combined_time in time_count:
#                 time_count[combined_time] += 1
#             else:
#                 time_count.update({combined_time: 1})
#         # print (time_count.keys())
#     writelogs(time_count)
# # Create CSV file
# def writelogs(time_count):
#     with open(csv_filename, 'w') as csvf:
#         csvf.write("minute, number_of_messages")
#         for timestamp in sorted(time_count.keys()):
#             csvf.write("{},{}".format(timestamp, time_count[timestamp]))
#     with open(csv_filename, "r") as csvfile:
#         for line in csvfile.readlines():
#             print(line)
# readlogs(log_filename)


#!/usr/bin/python
#
import re

output = {}
#Parse out the timedate stamp Jan 20 05:22:37 to capture two groups 1.) Jan 20 05:22 2.) log output e.g.
#R: cs3:  The cool service on fakehost does not appear to be communicating with the cool
regex = re.compile(r'^(\w+ \d+ \d+:\d+):\d+ \w+ .*$')
with open("m.txt", "r") as myfile:
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
