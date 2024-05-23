import json
import requests
import os

book_id = "010_002_0000455414"

# Function to download an image from a URL and save it locally
def download_image(url, folder):
    try:
        response = requests.get(url)
        response.raise_for_status()
        # Extract image name from the URL
        image_name = url.split("/")[-1]
        # Create the full path to save the image
        image_path = os.path.join(folder, image_name)
        # Write the image data to a file
        with open(image_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {image_name}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

# Read the JSON file
root_api = "./results/" + book_id
with open(root_api + "/book.json", 'r') as file:
    image_urls = json.load(file)

# Directory to save the images
output_folder = root_api + "/book"
os.makedirs(output_folder, exist_ok=True)

# Download each image
for url in image_urls:
    download_image(url, output_folder)
