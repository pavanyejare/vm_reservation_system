#!/usr/bin/env python3
import json, os, sys

def save_db(data):
    with open("vm_status.json", "w") as file:
        json.dump(data,file)
    file.close

def read_db():
    if os.path.isfile('./vm_status.json') and os.path.getsize('./vm_status.json') > 0:
      with open("vm_status.json", "r") as file:
        data=json.load(file)
      file.close
    else:
        data=[]
    return data
   
def vm_allocation(user):
    inventory=read_db()
    #print(inventory)
    if inventory:
       for i in inventory:
        if i['USER'] == user:
            #data="ERROR: VM - ",i["id"], "allready assigned to - ", user
            #print (data)
            return ("ERROR: VM - ",i["id"], "allready assigned to - ", user)
       for i in range(1,101):  
            check=next((x for x in inventory if x["id"] == i),None)
            flag=0
            if not check:
                new_vm={'id':i, 'USER':user}
                inventory.insert(i-1,new_vm)
                save_db(inventory)
                return ("INFO: New VM id : ", i,"assigned to user : ",user , "IP of vm = 192.168.1.", i)
                flag=1
                break
       if not flag:
        data="DEBUG : VM not available please try later .....(:) "
    else:
        inventory.insert(0,{'id':1, 'USER':user})
        save_db(inventory)
        return ("INFO: New VM id : 1 assigned to user : ",user , "IP of vm = 192.168.1.1")
    

def del_vm(user):
   inventory=read_db()
   flag=0
   for i in range(len(inventory)):
      if inventory[i]['USER'] == user:
        del inventory[i]
        flag=1
        break
   save_db(inventory)
   if not flag:
    return ('INFO: User ', user ,' not found')
   else:
    return ("INFO: user deleted successfully ", user)
def login():
   user = input("Enter Username : ")
   vm_allocation(user)

#login()
#del_vm()
