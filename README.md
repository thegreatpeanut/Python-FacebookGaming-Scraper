# Python-FacebookGaming-Scraper


It's supposed to get the following from a **main URL** and **videos URL** :

* Name 
* Followers 
* Likes on Page 
* Views on Video 
* Likes on Video 


and probably more to be added later.



Currently it outputs into a CSV the following : **Name | Followers | Page_Likes | Views | Video_Likes**.

Then you can output the csv data into a postgresql DB.

Added a login module ( must make a user_password.txt in the root folder ) .

Cleaned the code a little bit , made all the main parts of the code into methods.

Will begin working on a gui asap.

Paths will break eventually, looking into adding a user input request for paths if necessary.

Tried using m. and mbasic. versions of facebook . They're somehow worse than the default new interface.

**Names of people in your friend list that like a video you're scraping will show in the Video_Likes list** ( YAY ) , had to do a remove all characters except K ( looking for another solution since if there 1*mil* or more likes the code will break )

Tried using a new account but that does not get the new interface ... 


Will be looking to add a gui to this script


-- Work in progress --
