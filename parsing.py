import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_and_parse():
    # 1. Mimic Drama Live's payload to get data
    url = "https://fgcode.org/232425" 
    payload = {"code": "232425"}
    response = requests.post(url, json=payload, verify=False)
    
    try:
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.HTTPError as e:
        print(f"Error: The server returned an HTTP error: {e}")
        print(f"Response text: {response.text}")
        return
    except ValueError: # Includes JSONDecodeError
        print("Error: The server did not return valid JSON. It might be down or experiencing issues.")
        print(f"Response text: {response.text}")
        return
    
    # 2. Convert raw JSON data to M3U format string
    m3u_content = "#EXTM3U\n"
    for channel in data.get('channels', []):
        m3u_content += f"#EXTINF:-1,{channel['name']}\n{channel['stream_url']}\n"
        
    # 3. Save to a file
    with open("iptv.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)

if __name__ == "__main__":
    fetch_and_parse()
