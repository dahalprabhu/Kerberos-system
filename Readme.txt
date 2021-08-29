In this implementaion of Kerberos Authentication, we use Flask API to create two servers.
The first is the KeyDistribution Center which consists of two modules. The first module is 
a Authentication Server which generates Ticket Granting Ticket upon user requests. 
The second module is Ticket Granting Server which grants tickets for the session. Finally, 
we have a file server which requires ticket from the Ticket Granting Server. It verifies the 
tickets and returns the requested file to the user.

DES is used as encryption algorithm in this implementaion.

To run the implementaion follow these steps:

1) Install the requirements from requirements.txt.
2) Run Key_Distribution.py found in Key_Distribution Folder.
3) Run Server.py found in Server Folder.
4) Run Client.py in Client Folder.
5) In Client.py the default username is prabhu while its password is 'prabhudahal333'. Enter this password.
6) Finally you can see messeges each server and finally the required file 'Sonnet.txt' 
   is printed as the output from the file server after being sucessfully authenticated. 