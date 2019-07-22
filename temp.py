from linkedin_api import Linkedin
import json

# Authenticate using any Linkedin account credentials
api = Linkedin('vishalamca@gmail.com', 'Prince@123')


# GET all connected profiles (1st, 2nd and 3rd degree) of a given profile


connections=api.search_people(connection_of ='vishala-maddineni-62392656',network_depth ='F',limit=100)

first_degree=[]

for item in connections:
  # if (item['distance'] == 'DISTANCE_1'):
       # Increment the existing user's count.
       first_degree.append(item)

querry=[]

for item in first_degree:
  data = {}
  value = item['urn_id']
  retrieve=api.get_profile(value)
  name=retrieve['firstName']+' '+retrieve['lastName']
  experience=retrieve['experience']
  skills=retrieve['skills']
  link='https://www.linkedin.com/in/'+item['public_id']+'/'
  data['name'] = name
  data['link']=link
  data['skills']=skills
  data['experience']=experience
  querry.append(data)

with open('connections.txt', 'w') as file:
     file.write(json.dumps(first_degree))

with open('profileDetails.txt', 'w') as file:
     file.write(json.dumps(querry))
