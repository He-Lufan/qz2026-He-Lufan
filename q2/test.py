import json                             #测试 从 JSON 文件加载用户，覆盖当前数据；                                         
class UserManager:                      #从文件加载后，后续添加用户的 id 应接续已加载的最大 id
    def __init__(self):                 #这两项功能
        self.user_dict={}
        self.i=1

    def add_user(self,name,age):
        user={"id":self.i,"name":name,"age":age}
        self.user_dict[self.i]=user
        self.i+=1
        print(user)

    def save_to_json(self,d):
        with open("test.json","w",encoding="utf-8") as f:
            json.dump(self.user_dict,f,ensure_ascii=False)

    def load_from_json(self,s):  
        with open("test.json","r",encoding="utf-8") as f:
            self.user_dict=json.load(f)
        for k in range(1,len(self.user_dict)):
            if self.user_dict[str(k)]["id"]>self.user_dict[str(k+1)]["id"]:
                self.i=self.user_dict[str(k)]["id"]+1
                k+=1
            else:
                self.i=self.user_dict[str(k+1)]["id"]+1
                k+=1
        print(self.user_dict)

"""
um = UserManager()
um.add_user("张三", 18)
um.add_user("李四", 20)
"""
um2=UserManager()
um2.load_from_json("test.json")
um2.add_user("五娃",10)
um2.save_to_json("test.json")