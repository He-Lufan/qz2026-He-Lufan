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
        self.user_list=[]
        for user in self.user_dict:
            self.user_list.append(self.user_dict[user])
        print(self.user_list)

    def save_to_json(self,d):
        with open("users.json","w",encoding="utf-8") as f:
            json.dump(self.user_list,f,ensure_ascii=False)

    def load_from_json(self,s):  
        with open("users.json","r",encoding="utf-8") as f:
             load=json.load(f)
        print(load)




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