import re

example='''ashokjain

								Newbie

 Offline
								Activity: 4









(WTB) looking for old Mining rig 100- 180 mhs

Today at 09:03:10 AM
  #1




Hi,I am looking for old Mining rig , probably from 100 to 180 mhsI just want old as wanted to try mining....Nvidia or and any gpu , Mumbai , Pune seller most prefer



















 





1516528023

       Hero Member

 Offline
       Posts: 1516528023



Ignore







1516528023

1516528023


        #2




1516528023











Report to moderator







 









NastyFans - The UNOFFICIAL Nasty Mining Fan Club







Advertised sites are not endorsed by the Bitcoin Forum. They may be unsafe, untrustworthy, or illegal in your jurisdiction. Advertise here.








abdullahsurati

								Newbie

 Offline
								Activity: 27










Re: (WTB) looking for old Mining rig 100- 180 mhs

Today at 09:10:29 AM
  #2




Quote from: ashokjain on Today at 09:03:10 AMHi,I am looking for old Mining rig , probably from 100 to 180 mhsI just want old as wanted to try mining....Nvidia or and any gpu , Mumbai , Pune seller most preferI can build for you a new one, consisting of 1050Ti's.I live in Mumbai.WhatsApp me if you want to know more - 9167100326"
'''


numbr=re.findall(r'\d{10}',example)

print len(numbr)
