# Python-FacebookGaming-Scraper


It's supposed to get the following from a **main URL** and **videos URL** :

* Name 
* Followers 
* Likes on Page 
* Views on Video 
* Age of the Video
* Likes on Video 


and probably more to be added later.


The data this gets will be used in data science ... *eventually*.


Currently it outputs into a CSV the following : **Name | Followers | Page_Likes | Age_and_views | Video_Likes**.


In **Age_and_views** i currently have only the views ( which also need more processing , so it displays the full amount and no other characters ) but i plan to split 
**Age_and_views** into two collumns and have **Age** as a chart going down with **"a day ago"** (example element from the list ) = *1* and etc. but i'm still thinking about how i could implement something like this.


I'll also need to implement a click button function for a "infinitely" expanding playlist of sorts so i don't have nil values in the list.
