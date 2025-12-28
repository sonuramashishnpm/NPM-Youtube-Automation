from npmai import Ollama
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from moviepy.editor import VideoFileClip
import whisper
import json
import time
import os
import io

llms=input("Enter A.I from which you want to use  so select and write exact from here:-{'ChatGPT','Gemini'}:)
file=input("Enter your video file path")
thumbnail=input("Enter your thumbnail file path")

clip=VideoFileClip(file)

audio=clip.audio
audio.write_audiofile("temp.wav")

model=whisper.load_model("base")
result=model.transcribe("temp.wav")
text=result["text"]

llm = Ollama(model="llama3.2",temperature="0.8")

descriptionp = PromptTemplate(
    input_variables=["video_d"],
    template="""Hey you are a social media manager and you have to write the description about a video that you are going to uplaod note:note: please only write description no reply of contexts and you have these informations:{video_d}"""
)

hashtagsp = PromptTemplate(
    input_variables=["video_c"],
    template="""Hey you are a social media manager and you have to write the hastags that can be used in this video to rank and viral note: please only write hashtags no reply of contexts and you have these informations:{video_c}"""
)

titlep = PromptTemplate(
    input_variables=["t"],
    template="""Hey you are a social media manager and you have to write the title as per above contex{t} and de not respond for anything just generate a short title"""
)

descriptionr = descriptionp.format(
    video_d=text
)
hashtagsr = hashtagsp.format(
    video_c=text
)
titler = titlep.format(
    t="t"
)

resultd = llm.invoke(descriptionr)
time.sleep(5)
resulth = llm.invoke(hashtagsr)
time.sleep(3)
resultt = llm.invoke(titler)

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def get_youtube_service():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "client_secrets.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("youtube", "v3", credentials=creds)

def upload_video(file_path, description, tags, title,thumbnail_path):
    youtube = get_youtube_service()

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": "22"
        },
        "status": {"privacyStatus": "public"}
    }

    media = MediaFileUpload(file_path, chunksize=-1, resumable=True)

    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media
    )
    

    print("\nVideo is getting uploaded...")

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print("Uploaded:", int(status.progress() * 100), "%")

    print("\nUpload Complete!")
    print("Video ID:", response["id"])
    
    thumbnail=youtube.thumbnails.set(
        videoId=response["id"],
        media_body=thumbnail_path
        ).execute()

upload_video(
    file_path=file,
    description=resultd,
    tags=[resulth],
    title=resultt,
    thumbnail_path=thumbnail
)
