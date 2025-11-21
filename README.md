# NPM-Youtube-Automation
🚀 Auto-YouTube Uploader with AI Metadata Generator

Welcome to Auto-YouTube Uploader, the ultimate tool for content creators who want AI-powered titles, descriptions, hashtags and seamless video uploads in one click!

✨ Features

AI-generated metadata using npmai + LangChain:

Smart, catchy titles

Viral-ready hashtags

Engaging video descriptions

Automatic YouTube upload via YouTube Data API v3

Handles OAuth securely with client_secrets.json

Fully Python-based, single-file, easy to run

⚡ How It Works

Generate video metadata using AI (Gemini model).

Authenticate with YouTube (OAuth).

Upload video with auto-assigned title, description, hashtags, and public visibility.

Display upload progress and video ID in console.

🛠 Requirements

Python 3.10+

Libraries: npmai, langchain_core, pydantic, google-api-python-client, google-auth-oauthlib, google-auth-httplib2

client_secrets.json (Google OAuth credentials)

video.mp4 (or any video file to upload)

🚀 Quick Start

Clone or download this script.

Install dependencies:

pip install npmai langchain_core pydantic google-api-python-client google-auth-oauthlib


Place client_secrets.json & your video in the same folder.

Run:

python your_script_name.py


Watch the console for AI-generated metadata and upload progress.

💡 Pro Tips

Run on a network that allows YouTube and Google API access.

First run requires Google OAuth authentication; subsequent runs use token.json.

Customize prompts for titles, hashtags, descriptions to match your channel style.

🌟 Why It’s Awesome

Save hours of manual YouTube uploading

Make your videos SEO-friendly and viral-ready

All-in-one AI + automation solution for creators

Unleash the power of AI and let your content fly! 🚀
Note:-#Here user just need to enter detail about video in short and video will be uplaoded to their respective yotube channel we are making it non tech friendly also.
