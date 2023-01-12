# Import Module
from googleapiclient.discovery import build

# Create YouTube Object
youtube = build('youtube', 'v3',
				developerKey='Enter API key')

ch_request = youtube.channels().list(
	part='statistics',
	id='Enter Channel ID')

# Channel Information
ch_response = ch_request.execute()

sub = ch_response['items'][0]['statistics']['subscriberCount']
vid = ch_response['items'][0]['statistics']['videoCount']
views = ch_response['items'][0]['statistics']['viewCount']

print("Total Subscriber:- ", sub)
print("Total Number of Videos:- ", vid)
print("Total Views:- ", views)
