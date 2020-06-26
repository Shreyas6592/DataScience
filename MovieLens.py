import pandas as pd

#Format - UserID::MovieID::Rating::Timestamp
rat = pd.read_csv('ratings.dat',sep="::",names =["UserID", "MovieID", "Rating", "TimeStampNetAvg"],engine='python')    

rat.head() 
print(rat.shape) 

#Format - MovieID::Title::Genres
mov = pd.read_csv('movies.dat',sep="::",names =["MovieID","Title","Genres"],engine='python')  

mov.head()
print(mov.shape)
        
#Format -  UserID::Gender::Age::Occupation::Zip-code        
        
usr = pd.read_csv('users.dat',sep='::',names=["UserID","Gender","Age","Occupation","Zip-code"],engine='python')
usr.head()    
print(usr.shape)

#MovieID Title UserID Age Gender Occupation Rating
