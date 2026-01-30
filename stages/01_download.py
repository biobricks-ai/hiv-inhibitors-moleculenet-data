import requests
import os

# Updated URL to DeepChem S3 bucket
url = "https://deepchemdata.s3-us-west-1.amazonaws.com/datasets/HIV.csv"
output_path = "download/HIV.csv"

def download_file(url, output_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(output_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

if __name__ == "__main__":
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    print(f"Downloading {url} to {output_path}...")
    download_file(url, output_path)
    print("Download complete.")
