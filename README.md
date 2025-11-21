<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Auto-YouTube Uploader with AI</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #f6d365, #fda085);
            color: #222;
            padding: 40px;
            line-height: 1.6;
        }
        h1, h2, h3 {
            color: #1a1a1a;
        }
        h1 {
            font-size: 3em;
            text-align: center;
            margin-bottom: 0.5em;
            text-shadow: 2px 2px #fff;
        }
        h2 {
            font-size: 2em;
            margin-top: 1.5em;
            border-bottom: 2px dashed #fff;
            padding-bottom: 0.3em;
        }
        p {
            font-size: 1.2em;
        }
        .feature {
            background: rgba(255, 255, 255, 0.2);
            padding: 15px;
            margin: 10px 0;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            transition: transform 0.3s ease;
        }
        .feature:hover {
            transform: scale(1.02);
            box-shadow: 0 6px 12px rgba(0,0,0,0.3);
        }
        ul {
            list-style-type: square;
            padding-left: 20px;
        }
        code {
            background: rgba(255,255,255,0.5);
            padding: 2px 5px;
            border-radius: 5px;
            font-size: 1em;
        }
        .tip {
            background: rgba(0,0,0,0.1);
            padding: 10px;
            border-left: 5px solid #fff;
            margin: 15px 0;
            border-radius: 8px;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            font-style: italic;
            color: #111;
        }
        .highlight {
            color: #fff;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>🚀 Auto-YouTube Uploader with AI</h1>
    
<p>Welcome to the future of content creation! This tool combines the power of <span class="highlight">AI-generated metadata</span> with seamless <span class="highlight">automatic YouTube uploading</span>. Now, even non-technical creators can have their videos uploaded with smart titles, descriptions, and hashtags — all in one click.</p>
    
<h2>✨ Features</h2>
    <div class="feature">
        <h3>AI-Generated Titles</h3>
        <p>Get catchy, SEO-friendly titles created automatically, so your videos stand out and attract more viewers.</p>
    </div>
    <div class="feature">
        <h3>Smart Video Descriptions</h3>
        <p>Your video descriptions are written to engage your audience, summarize the content, and boost discoverability.</p>
    </div>
    <div class="feature">
        <h3>Viral-Ready Hashtags</h3>
        <p>Automatically generate trending hashtags relevant to your content, giving your videos a better chance to go viral.</p>
    </div>
    <div class="feature">
        <h3>Automatic YouTube Upload</h3>
        <p>No more manual uploading! Videos are uploaded directly to your YouTube channel with the AI-generated metadata applied.</p>
    </div>
    
<h2>⚡ How It Works</h2>
    <p>This system has been designed for simplicity and speed:</p>
    <ul>
        <li>Provide your video file (MP4 or similar).</li>
        <li>The AI reads the video context and generates <strong>title, description, and hashtags</strong> automatically.</li>
        <li>The tool authenticates with your YouTube account securely using Google OAuth.</li>
        <li>Upload happens automatically, displaying progress and final video ID.</li>
    </ul>
    
<h2>🛠 No Technical Knowledge Needed</h2>
    <p>This is a **plug-and-play solution**:</p>
    <ul>
        <li>No command-line expertise required.</li>
        <li>No API keys management for end users (optional for future SaaS version).</li>
        <li>Fully automated workflow: just select a video and press upload.</li>
    </ul>
    
<div class="tip">
        <strong>Pro Tip:</strong> Future versions will integrate cloud uploads, so no local files are required at all — you could record on your phone and upload instantly via AI!
    </div>
    
<h2>🌟 Future Vision</h2>
    <p>Imagine a platform where creators can:</p>
    <ul>
        <li>Generate AI-powered content metadata for every platform: YouTube, Instagram, TikTok, and more.</li>
        <li>Upload directly from a mobile device or camera, without touching a PC.</li>
        <li>Track analytics and AI suggestions to optimize every post for reach and engagement.</li>
        <li>Empower youth creators globally to automate tedious work and focus on creative storytelling.</li>
    </ul>
    
<h2>🚀 Quick Start for Testing (Developers & Early Adopters)</h2>
    <p>1. Install Python 3.10+ and dependencies:</p>
    <pre><code>pip install npmai langchain_core pydantic google-api-python-client google-auth-oauthlib</code></pre>
    <p>2. Place your video file in the same folder.</p>
    <p>3. Make sure you have <code>client_secrets.json</code> from Google Cloud.</p>
    <p>4. Run the script: <code>python auto_youtube_upload.py</code></p>
    
<div class="tip">
        ⚠️ Note: On restricted networks (like corporate PCs), the YouTube API may be blocked. For full functionality, run on a network that allows Google API access.
    </div>
    
<h2>💡 Why This Tool Rocks</h2>
    <ul>
        <li>Save hours of manual uploading and research.</li>
        <li>Boost your video’s chance to go viral.</li>
        <li>Perfect for content creators, educators, and social activists.</li>
        <li>Scalable: can handle one video or hundreds automatically.</li>
    </ul>
    
<p class="footer">✨ Join the AI-driven future of content creation with Auto-YouTube Uploader. Let your videos fly higher, faster, and smarter! ✨</p>
</body>
</html>
