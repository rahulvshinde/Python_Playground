# import requests
# import json
#
# report = []
# def print_hierachy(employee_id):
#     employee = requests.get('http://www.linkedin.corp/api/employee/%s' % employee_id)
#     if employee.status == 200:
#         print employee['name'], employee['title']
#         result = json.load(employee.json)
#         for report in result['reports']:
#             print_hierachy(report)
#     return 0
#
# print_hierachy(100)


import requests
import json
def print_employee_hierarchy(id, tab_size=0):
    # get info using requests
    # parse the info to get: name, title, reports
    # for every id in reports -> recurse print_emp_hierarchy(id)

    resp = requests.get("http://www.linkedin.corp/api/employee/%s" % id)
    resp_json = json(resp)
    # resp_json.get("name")
    name = resp_json["name"]
    title = resp_json["title"]
    reports = resp_json["reports"]

    for _ in range(tab_size):
        print "\t",
    print "%s - %s" % (name, title)

    if not reports:
        return

    tab_size += 1

    for id in reports:
        print_employee_hierarchy(id, tab_size)
print_employee_hierarchy(100, 0)