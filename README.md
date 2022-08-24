# Virtual Machines reservationsystem

* How to run the project 

  1. install required packages using following command 
     ``` pip3 install -t requirements.txt ```
  2. run the application using following command
     ``` python app.py ```
  3. TO checkin and chekout

      i. Checkin VM 
        ``` curl http://localhost:5000/checkin/<USER_NAME> 
             e.g.
              curl http://localhost:5000/checkin/pavan
         ```
      ii. Checkout VM
          ``` curl http://localhost:5000/checkout/<USER_NAME> 
             e.g.
              curl http://localhost:5000/checkout/pavan
         ```
         