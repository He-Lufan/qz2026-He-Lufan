import json
class UserManager:
    def __init__(self):
        self.user_dict={}
        self.i=1
        
    def add_user(self,name,age):
        user={"id":self.i,"name":name,"age":age}
        self.user_dict[self.i]=user
        self.i+=1
        print(user)
      
    def get_user(self,id):
        try:
            print(self.user_dict[id])
        except KeyError:
            print(None)

    def update_age(self,id,age):
        self.user_dict[id]["age"]=age
        print("True")

    def remove_user(self,id):
        try:
            del self.user_dict[id]
            print("True")
        except KeyError:
            print(False)
    
    def list_users(self):
        user_list=[]
        for user in self.user_dict:
            user_list.append(self.user_dict[user])
        print(user_list)

    def save_to_json(self,d):
        with open("users.json","w",encoding="utf-8") as f:
            json.dump(self.user_dict,f,ensure_ascii=False)

    def load_from_json(self,s):  
        with open("users.json","r",encoding="utf-8") as f:
            self.user_dict=json.load(f)
        for k in range(1,len(self.user_dict)):                                 #覆盖和取最大值的功能
            if self.user_dict[str(k)]["id"]>self.user_dict[str(k+1)]["id"]:
                self.i=self.user_dict[str(k)]["id"]+1
                k+=1
            else:
                self.i=self.user_dict[str(k+1)]["id"]+1
                k+=1




um = UserManager()
um.add_user("张三", 18)
um.add_user("李四", 20) 
um.get_user(1) 
um.get_user(99) 
um.update_age(1, 19)
um.remove_user(2)
um.remove_user(2)
um.list_users() 
um.save_to_json("users.json")
um2 = UserManager()
um2.load_from_json("users.json")
um2.list_users()