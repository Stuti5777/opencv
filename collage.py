# importing libraries 
import os 
import cv2 
from PIL import Image 

# Checking the current directory path 
print(os.getcwd()) 

# Folder which contains all the images 
# from which video is to be generated 
image_folder = r"/Users/YourUsername/Downloads/collage/newfolder2"  # Update to your macOS path

# Change working directory to the image folder
os.chdir(image_folder)

mean_height = 0
mean_width = 0

# Count number of images in the folder
num_of_images = len([file for file in os.listdir(image_folder) if file.endswith(('.jpg', '.jpeg', '.png'))])

for file in os.listdir(image_folder): 
    if file.endswith(('.jpg', '.jpeg', '.png')):
        im = Image.open(os.path.join(image_folder, file)) 
        width, height = im.size 
        mean_width += width 
        mean_height += height 

# Finding the mean height and width of all images. 
mean_width = int(mean_width / num_of_images) 
mean_height = int(mean_height / num_of_images) 

# Resizing all images to the same size
for file in os.listdir(image_folder): 
    if file.endswith(('.jpg', '.jpeg', '.png')): 
        im = Image.open(os.path.join(image_folder, file)) 
        imResize = im.resize((mean_width, mean_height), Image.LANCZOS) 
        imResize.save(file, 'JPEG', quality=95) 

# Video Generating function 
def generate_video(): 
    video_name = 'mygeneratedvideo.avi'
    
    # Get all image files
    images = [img for img in os.listdir(image_folder) if img.endswith(('.jpg', '.jpeg', '.png'))]
    print(images) 

    # Read the first image to set dimensions
    frame = cv2.imread(os.path.join(image_folder, images[0])) 
    height, width, layers = frame.shape 

    # Define the video codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # Use a codec compatible with Mac
    video = cv2.VideoWriter(video_name, fourcc, 1, (width, height)) 

    # Appending the images to the video one by one 
    for image in images: 
        video.write(cv2.imread(os.path.join(image_folder, image))) 
    
    # Release the video
    video.release() 

# Calling the generate_video function 
generate_video() 
