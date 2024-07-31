# RiiTube
A way to watch YouTube on your Wii with WiiMC.

The code is extremely simple. All it does is:

1. For YouTube, uses Inviduous API to search for videos, or browse trending or popular videos (probably tech-related because that's what Inviduous tends to grab). Or uses the Vimeo or Dailymotion API.
2. Returns a playlist file in WiiMC format.
3. Uses yt-dlp to download video file, and proxies that to the Wii.

# Credits
- [@larsenv](https://github.com/larsenv): Original code.
- [@MatiasMFM2001](https://github.com/larsenv): Flask refactoring and dockerizing app.
