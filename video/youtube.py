#!/usr/bin/env python3

from flask import current_app, request, url_for
import requests
from yt_dlp import YoutubeDL
from contextlib import redirect_stdout
from pathlib import Path
from io import BytesIO

@current_app.route("/wiimc/", methods=["GET"])
def get_yt_video_list():
    args = request.args
    keys = args.keys()

    url = "https://y.com.sb/api/v1/"
    query_params = {}

    if "q" in keys:
        url += "search"
        query_params["q"] = args.get("q", "")

    elif "trending" in keys:
        url += "trending"

    else:
        url += "popular"

    api_response = requests.get(url, params=query_params)

    response = "[Playlist]\n"

    if api_response.status_code == requests.codes.ok:
        for index, entry in enumerate(api_response.json()):
            response += f"File{index}=http://192.168.1.34{url_for('get_yt_video_data', q=entry.get('videoId'))}\n"
            response += f"Title{index}={entry.get('title')}\n"
            response += f"Length{index}={entry.get('lengthSeconds')}\n"

    print(response)
    return response

@current_app.route("/video/youtube/", methods=["GET"])
def get_yt_video_data():
    video_id = request.args.get("q", "")
    buffer = BytesIO()

    with redirect_stdout(buffer), YoutubeDL(current_app.config["YT_DLP_CONFIG"]) as yt:
        yt.download([video_id])

    return buffer.getvalue()
