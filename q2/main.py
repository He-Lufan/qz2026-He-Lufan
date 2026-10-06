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

    
um = UserManager()
um.add_user("张三", 18)
um.add_user("李四", 20) 
um.get_user(1) 
um.get_user(99) 