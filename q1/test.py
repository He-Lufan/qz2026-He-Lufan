import json
l=[]
l_update=[]
with open("app.jsonl","r",encoding="utf-8") as f:
    for line in f:
        l.append(line)
print(l)
for s in l:
    d=json.loads(s)
    l_update.append(d)
print(l_update)                                 #把日志转换成了可处理的含字典的列表

total=len(l_update)                             #关于total
print(total)

by_level={}                                     #关于level
for i in range(len(l_update)):
    if l_update[i]["level"] not in by_level:
        by_level[l_update[i]["level"]]=1
    else:
        by_level[l_update[i]["level"]]+=1
print(by_level)

by_user={}                                       #关于user
for i in range(len(l_update)):
    if l_update[i]["user"] not in by_user:
        by_user[l_update[i]["user"]]=1
    else:
        by_user[l_update[i]["user"]]+=1
print(by_user)

for i in range(len(l_update)):                   #关于last error
    if l_update[i]["level"]=="ERROR":
        last_error=l_update[i]["message"]
print(last_error)

result={
          "total":total,
          "by_level":by_level,
          "by_user":by_user,
          "last_error":last_error
          }
print(result)                                     #统计了字典

formatted_json = json.dumps(result,indent=4,ensure_ascii=False)
print(formatted_json)                             #调整了格式
"""result = analyze_log("app.jsonl")"""