import requests

def fetch_and_parse():
    # 1. Mimic Drama Live's payload to get data
    url = "https://fgcode.org/232425" 
    payload = {"code": "232425"}
    response = requests.post(url, json=payload).json()
    
    # 2. Convert raw JSON data to M3U format string
    m3u_content = "#EXTM3U\n"
    for channel in response.get('channels', []):
        m3u_content += f"#EXTINF:-1,{channel['name']}\n{channel['stream_url']}\n"
        
    # 3. Save to a file
    with open("iptv.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)

if __name__ == "__main__":
    fetch_and_parse()