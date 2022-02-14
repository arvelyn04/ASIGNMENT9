import json

myjsonfile=open('resume.json','r')
jsondata=myjsonfile.read()

obj=json.loads(jsondata)

print("BASIC INFORMATION:")

print("Name:"+str(obj ["NAME"]))
print("Label:"+str(obj ["LABEL"]))
print("Email:"+str(obj ["EMAIL"]))
print("Contact Number:"+str(obj ["CONTACT NUMBER"]))
print("URL:"+str(obj ["URL"]))
print("Address:"+str(obj ["ADDRESS"]))
print("Postal Code:"+str(obj ["POSTAL CODE"]))


print("PERSONAL INFORMATION:")

print("Age:"+str(obj ["AGE"]))
print("Gender:"+str(obj ["GENDER"]))
print("Civil Status:"+str(obj ["CIVIL STATUS"]))
print("Nationality:"+str(obj ["NATIONALITY"]))
print("Height:"+str(obj ["HEIGHT"]))
print("Weight:"+str(obj ["WEIGHT"]))


print("BACKGROUND:")

print("Name of the Company:"+str(obj ["NAME OF THE COMPANY"]))
print("Position:"+str(obj ["POSITION"]))
print("Company's URL:"+str(obj ["COMPANY'S URL"]))
print("Start Date:"+str(obj ["START DATE"]))
print("End Date:"+str(obj ["END DATE"]))


print("PROFILE:")

print("Profile 1:"+str(obj ["PROFILE1"]))
print("Profile 2:"+str(obj ["PROFILE2"]))
print("Profile 3:"+str(obj ["PROFILE3"]))
print("Profile 4:"+str(obj ["PROFILE4"]))
print("Profile 5:"+str(obj ["PROFILE5"]))



print("EDUCATIONAL ATTAINMENT:")

print("Elementary:"+str(obj ["ELEMENTARY"]))
print("Secondary:"+str(obj ["SECONDARY"]))
print("Senior-High:"+str(obj ["SENIOR-HIGH"]))
print("Tertiary:"+str(obj ["TERTIARY"]))


print("SKILLS:")

print("Skills:"+str(obj ["SKILLS"]))
print("Level:"+str(obj ["LEVEL"]))
print("Keywords:"+str(obj ["KEYWORDS"]))


print("LANGUAGES:")

print("Languages:"+str(obj ["LANGUAGES"]))