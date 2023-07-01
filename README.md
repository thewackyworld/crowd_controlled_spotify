# crowd_controlled_spotify
this is a program that can be used by cafes or restruants to have the costumers choose what song to be played, 
users can add in a song based on the name and artist then they can vote on songs that everyone else put up.
the song with the highest vote will go to the top of the list.
then the song with the highest votes will be added to the spotify queue of the restruant.

the program has a website made using the django framework that allows users to look at the song suggestion list
they add and vote on songs on that website.

then a python script takes that table in real time and arranges it by highest vote, then using the spotipy library it adds the song that 
is on the top of the list to the queue as the song that will play next. the program will only add the song when there is only 10 seconds left on
the already playing song (to give voters enough time to vote on the next song)


Run the server 
go to http://127.0.0.1:8000/list/
then run Spoopifying.py 
sign in to your spotify 
then play a song and it will do its thing
