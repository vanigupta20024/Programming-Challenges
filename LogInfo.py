# GHC Codepath Sandbox - 6
# Module SE101
# HARD

'''
Output:
{'WARNING': {'403': {'Forbidden': {'No token in request parameters': 1}}}, 
'ERROR': {'500': {'Server Error': {'int is not subscriptable': 2}}}, 
'INFO': {'200': {'OK': {'Login Successful': 1, 'User sent a message': 1}}}}
'''


import time
start = time.time()

def logInfo(logs):
    logs_dict = {}
    for log in logs:
        l = log.replace("[", "").replace("]", "").split()
        msg = l[0]
        num = l[1]
        err_typ = ""
        err_msg = ""
        if l[2] == "OK":
            err_msg = " ".join(l).split("OK")[-1].strip()
            err_typ = "OK"
        else:
            err_msg = " ".join(l).split(":")[-1].strip()
            temp1 = " ".join(l).split(":")[0]
            err_typ = " ".join(temp1.split()[2:])
        if msg in logs_dict.keys():
            if num in logs_dict[msg].keys():
                if err_typ in logs_dict[msg][num].keys():
                    if err_msg in logs_dict[msg][num][err_typ].keys():
                        logs_dict[msg][num][err_typ][err_msg] += 1
                    else:
                        logs_dict[msg][num][err_typ][err_msg] = 1
                else:
                    logs_dict[msg][num] = {err_typ : {err_msg : 1}}
            else:
                logs_dict[msg] = {num : {err_typ : {err_msg : 1}}}
        else:
            logs_dict[msg] = {num : {err_typ : {err_msg : 1}}}

    return logs_dict


l = [
'[WARNING] 403 Forbidden: No token in request parameters',
'[ERROR] 500 Server Error: int is not subscriptable',
'[INFO] 200 OK Login Successful',
'[INFO] 200 OK User sent a message',
'[ERROR] 500 Server Error: int is not subscriptable'
]

print(logInfo(l))
print(time.time() - start)
