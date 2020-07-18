import requests
import json
def get_emp(id,depth=0):
    emp=requests.get("https://api.linkedin.com/v1/employee/%s" % id)
    if emp.status == 200:
        emp_json = json(emp)
        name = emp_json["name"]
        title = emp_json["title"]
        reports = emp_json["reports"]
        if not reports:
            return
        for _ in range(depth):
            print "\t",
            print "%s-%s"%(name,title)
        depth+=1
        for id in reports:
            get_emp(id,depth)

get_emp("A123456789",0)