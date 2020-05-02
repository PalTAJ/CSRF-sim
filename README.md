# CSRF-sim
##Task: 
######Demonstrate a cross-site request forgery attack between a malicious server and a client.

we have two folder - legit_site and fake_site


legit site will be a website used by clients, its an online storage system mangement flask app i created for another class.
to run it:
go to src directory and open terminal/cmd/powershell
type: python main.py run-api
then go to your browser and navigate to: http://localhost:5000
it will lead to a login menu, use any user login data from control.py 
you can check and test it after logining in.


fake_site will be used by an adversary to steal your accounts info using CSRF attack.
how to run:
go to fake_site directory
go to src directory and open terminal/cmd/powershell
type python app.py 
then go to your browser and navigate to: http://localhost:5005
you will see a cat picture ik.

simualtion:

both sites should be up while doing this, so dont quit any of the terminals.
first, login to the storage system and go to my profile and check the password, it should be 123456

second, when you login a session token is saved and allow you to stay logged in for 24 hours giving the condition 
that the client do not logout.

third, lets say the user recives an email containing a link for a site, our cat website, he clicks it and tries it out.

four, when he click the button there, a jquiry post request will be sent to the storage house site, from the client side
so if he is logged in, his session will be there and it will accept any request from the client.

five, the request we sent changes the current loggedin user password to hacker123 and the site logoff the client from the site
when he tries to login to it, password 123456 wont work because it has been changed to hacker123.

i tested this scenario locally.


 - note that for this simulation i disabled db, so dont expect it to work here.
 
 
