def analyze_log(filepath):
    import json
    from pprint import pprint
    
    r_0={"total":0,"by_level":{},"by_user":{},"last_error":None}
    try:
        l=[]
        l_update=[]
        with open(filepath,"r",encoding="utf-8") as f:
            for line in f:
                l.append(line)
        for s in l:
            try:
                d=json.loads(s)
                l_update.append(d)   
            except json.JSONDecodeError:
                continue                                #把日志转换成了可处理的含字典的列表
                              
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
        final_result=r 
                   
     
    except (FileNotFoundError,UnboundLocalError):
         final_result=r_0
    finally:
        pprint(final_result,indent=4,sort_dicts=False,width=1)
        return final_result        


result = analyze_log("empty.jsonl")
print(result["total"])        
print(result["by_level"])     
print(result["by_user"])      
print(result["last_error"])   
