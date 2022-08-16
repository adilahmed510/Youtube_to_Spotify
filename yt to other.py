#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install google-api-python-client
pip install spotipy


# In[ ]:


api_key= "AIzaSyBYFWk02YwfEkUAzimLGsxBkWVBS0Te7PY"


# In[1]:


api_key= "AIzaSyBYFWk02YwfEkUAzimLGsxBkWVBS0Te7PY"
from googleapiclient.discovery import build
yt= build("youtube","v3",developerKey= api_key)

## p_items= yt.playlists().list(part="snippet", channelId= "UCFzxZ3a7pw7hVJ2Tx5Ogqfw")
## p_req=p_items.execute()
## print(req)

## to get playlist id from diff playlists

##for item in p_req["items"]:
    ##print("Play list Id:",item["id"])
    ##for names of playlist
    ##print("Play list name:", item["snippet"]["title"])
    ##print()
#nextPageToken=None 
#while True :

pl_id= "PLqc472hFAQgrzcUEQLKiNHeX1lc7zM9ao"
p_songs=yt.playlistItems().list(part="contentDetails", playlistId= pl_id,maxResults=50)
p_req=p_songs.execute()
#print(p_req)

## get video ids of all the items in playlist
vid_lst=[]
for i in p_req["items"]:
    v_id= i["contentDetails"]["videoId"]
    vid_lst.append(v_id)
    #print (v_id)
csep_vlist=','.join(vid_lst)
#nextPageToken= p_req["nextPageToken"]
#print (nextPageToken)
#if nextPageToken== None:
    #break

#video details(Titles) in a list 
v_titles=[]
v_deets=yt.videos().list(part='snippet', id=csep_vlist)
vdeets_req= v_deets.execute()
#print(vdeets_req)
for i in vdeets_req["items"]:
    v_titles.append(i["snippet"]["title"])
print(v_titles)

########Done With YOUTUBE!!!!


# In[8]:


import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.client import Spotify

#scope = "user-library-read"
#token="BQCGVfcD6kkKwLbC0HvEoqODdTpTOfHhgdc0aFx14UXvs-_so6bJDAlSR0ccjDQX_lfFDehC9Nl7BzZ8Wue4j8F0IsMUKPIhEKhJhVLHy5lcU7uBMYTWH8Bvd2b2XbYIuvk3y8L9K_YdslYAWf6oiDgFR7HSQ5v3xXcewMt299oZiZ-I6NlIMTWeYUNoFKyDMIvFa_0NYDsvdCdu9PKA9oWX9rhEcDJnLMLaTaA"

#sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id="ffd7784b2b694b0b8eee2eea6bcc6ff8", client_secret= "ecd91e37a6f04c7fa0b72ffd0571e8dd", redirect_uri="http://localhost/"))


#results = sp.current_user_saved_tracks()
#for idx, item in enumerate(results['items']):
  #  track = item['track']
   # print(idx, track['artists'][0]['name'], " – ", track['name'])

cid ="ffd7784b2b694b0b8eee2eea6bcc6ff8" 
secret = "ecd91e37a6f04c7fa0b72ffd0571e8dd"
rdrct_uri="http://localhost/"
scope="playlist-modify-public"
auth_manager=SpotifyOAuth( client_id=cid, client_secret=secret, redirect_uri=rdrct_uri, scope=scope)


#urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
sp = spotipy.Spotify(auth_manager=auth_manager)

#artist = sp.artist(urn)
#print(artist)
#user = sp.user('plamere')
#print(user)

srch= sp.search(q= "ghetto akon", type="track", limit=1)
#for i in srch["tracks"]["items"]:
 #   v_id= i["uri"]
  #  print()
   # print(v_id)
#print(v_titles)
#c=0

### Getting spotify ids(uris) of songs from youtube.
uri_lst=[]
for i in v_titles:
    srch= sp.search(q= i, type="track", limit=1)
    for i in srch["tracks"]["items"]:
        v_id= i["uri"]
        #print(v_id)
        uri_lst.append(v_id)
    #print (i)
    #c=c+1
    #if c==2:
     #   break
#print(uri_lst)
#comma seperated uti list
csep_uris= ",".join(uri_lst)
#print(csep_uris)


##getiing playlist and ids

#pid='6oyJvuDQBVzXXa0sElISSE'
pname=input("Enter playlist name")
plst=sp.current_user_playlists()
#print(plst)
for i in plst["items"]:
    if pname== i["name"]:
        pid=i['id']
print(pid)


## Adding songs to playlist by its ids
plitms= sp.playlist_items(playlist_id=pid)
print(plitms)
pladd= sp.playlist_add_items(playlist_id =pid, items= csep_uris)
print(plitms)


# In[ ]:




