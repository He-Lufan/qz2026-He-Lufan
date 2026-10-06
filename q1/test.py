def analyze_log(filepath):
    import json
    class Format(dict):
            def __str__(self):
                return json.dumps(self, indent=4, ensure_ascii=False)
    try:
        l=[]
        l_update=[]
        with open(filepath,"r",encoding="utf-8") as f:
            for line in f:
                l.append(line)
        for s in l:
            d=json.loads(s)
            l_update.append(d)                          #把日志转换成了可处理的含字典的列表
                              
        total=len(l_update)                             #关于total
            
        by_level={}                                     #关于level
        for i in range(len(l_update)):
            if l_update[i]["level"] not in by_level:
                by_level[l_update[i]["level"]]=1
            else:
                by_level[l_update[i]["level"]]+=1
            
        by_user={}                                       #关于user
        for i in range(len(l_update)):
            if l_update[i]["user"] not in by_user:
                by_user[l_update[i]["user"]]=1
            else:
                by_user[l_update[i]["user"]]+=1
            
        for i in range(len(l_update)):                   #关于last error
            if l_update[i]["level"]=="ERROR":
                last_error=l_update[i]["message"]
            
        r={
                  "total":total,
                  "by_level":by_level,
                  "by_user":by_user,
                  "last_error":last_error
                  }                                       #统计了字典
        final_result=Format(r)            
        return final_result   
     
    except (FileNotFoundError,UnboundLocalError):
        r={"total":0,"by_level":{},
           "by_user":{},"last_error":None}
        final_result=Format(r)            
        return final_result


result = analyze_log("empty.jsonl")
print(result)
print(result["total"])        
print(result["by_level"])     
print(result["by_user"])      
print(result["last_error"])   
