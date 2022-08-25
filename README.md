# Virtual Machines reservationsystem
        
        Assume you are the administrator of a cloud which hosts some finite number of Virtual Machines. Users of your cloud can borrow or check-out VMs for use. Once they are done using it, they can check-in the VM back. Once a VM is checked in, as an administrator, you should perform some cleanup on the VM and then return it back to the pool of VMs.

 # How to run the project 

  1. install required packages using following command 
  
     ``` pip3 install -r requirements.txt ```
     
  2. run the application using following command
  
     ``` python app.py ```
     
  3. TO checkin and chekout
    i. Checkin VM 
        ```
            curl http://localhost:5000/checkin/<USER_NAME> 
        e.g.
              curl http://localhost:5000/checkin/pavan
        ```
     ii. Checkout VM
        ``` 
             curl http://localhost:5000/checkout/<USER_NAME> 
        e.g.
              curl http://localhost:5000/checkout/pavan
        ```
