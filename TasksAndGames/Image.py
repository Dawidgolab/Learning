# Load image width/height
from PIL import Image

pathToImage = "k.jpg" # You new to add your own path to the image you want to display
newImage = Image.open(pathToImage)
print(f"Width: {newImage.width}")
print(f"Height: {newImage.height}")

#print(newImage.size)
