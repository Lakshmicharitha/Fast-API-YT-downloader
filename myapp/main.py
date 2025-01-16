from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pytube import YouTube
import os
import yt_dlp

# Initialize the FastAPI app
app = FastAPI()

# Allow CORS for frontend running on localhost:3000 (adjust as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://fast-api-yt-downloader-1.onrender.com"],  # Allow frontend from localhost:3000
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

cur_dir = os.getcwd()

@app.post("/download")
def download_video(link: str = Form(...)):
    youtube_dl_options = {
        "format": "best",
        "outtmpl": os.path.join(cur_dir,f"Video-{link[-11:]}.mp4")
    }
    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        ydl.download([link])
    return {"status":"Download started"}

if __name__ == "__main__":
    import uvicorn
    # Run the app on localhost and port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)