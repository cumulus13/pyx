from pyboxapi import BoxApi
import  sys

folder_id=1720362018
box_api = BoxApi(client_id = 'mz3m6rw1ur45nj1n2156mvs8jylu7pat ', client_secret = 'nd4jwkfNkYzAr5zIXM1f4SmMlus2Qwm5')

# Allow the client_id above access to whatever account you specify here.
# The reason you need to provide a username and password is for the OAuth2 flow and
# because the access_tokens only live for 1 hour and refresh token for 14 days.
box_api.obtain_access_token(username = 'hadi.attaqwa@gmail.com', password = 'blackid-licface-xxxnuxer13')

# Alternatively set the access_token yourself
box_api.set_access_token(token="zAcyZBNtzYHv5p2KFwcJzaGIu8e4Q3Ho")

#items = box_api.get_folders_items(folder_id=1720362018)

#f = open('example.csv')
#files = {
#  'example.csv' : f
#}

# Updating a file
#box_api.create_files_content(file_id = box_file['id'], parent_id=folder_id, name=str(sys.argv[1]), files=sys.argv[1])

# Uploading a new file
box_api.create_file_content(parent_id=folder_id, name=str(sys.argv[1]), files=sys.argv[1])