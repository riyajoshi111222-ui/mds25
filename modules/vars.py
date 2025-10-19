#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "27962072"))
API_HASH = environ.get("API_HASH", "a37e33a05ec3b9321751dec49fdb9829")
BOT_TOKEN = environ.get("BOT_TOKEN", "8107257529:AAHiauOoPAH9LVqrQ11mb-K7NB1wS87k2Po")

OWNER = int(environ.get("OWNER", "787410221"))
CREDIT = environ.get("CREDIT", "ARJUN 𝘽𝙊𝙏𝙎")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '787410221').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '787410221').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
api_url = "http://master-api-v3.vercel.app/"
api_token = "eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MTY1MDE5MTMzLCJvcmdJZCI6NzMxMDMwLCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTk0MTQxODQwMzEiLCJuYW1lIjoiVmloYWFuIiwiZW1haWwiOiJyaXlham9zaGkxMTEyMjJAZ21haWwuY29tIiwiaXNGaXJzdExvZ2luIjp0cnVlLCJkZWZhdWx0TGFuZ3VhZ2UiOiJFTiIsImNvdW50cnlDb2RlIjoiSU4iLCJpc0ludGVybmF0aW9uYWwiOjAsImlzRGl5Ijp0cnVlLCJsb2dpblZpYSI6Ik90cCIsImZpbmdlcnByaW50SWQiOiJiZTFlMTc4OS0xZmFiLTQ0ODYtOGI5Zi03YTgwOTNjYmU5ZjAiLCJpYXQiOjE3NjA4NjU2NjksImV4cCI6MTc2MTQ3MDQ2OX0.O0j6P1b4F8Vp7Dj2P3Fz8WfbmNlzg82nNZMBXm4-jlhLbnzRQgymnZrRtdUu8fte"
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.



