import cv2
import pygame

# Initialize pygame for sound
pygame.mixer.init()
click_sound = pygame.mixer.Sound("bab.mp3")  # Replace with your sound file path

# Function to read the first line of a text file
def read_first_line(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
    return first_line

# Function to modify the first line of a text file
def modify_first_line(file_path, new_first_line):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Modify the first line
    lines[0] = new_first_line + '\n'
    
    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)
        
# Callback function to handle mouse clicks
def count_clicks(event, x, y, flags, param):
    global click_count, displaying_alternate
    if event == cv2.EVENT_LBUTTONDOWN:
        click_count += 1
        displaying_alternate = True
        click_sound.play()  # Play sound effect on click
    elif event == cv2.EVENT_LBUTTONUP:
        displaying_alternate = False



# Example usage
file_path = 'count.txt'

# Read the first line
count_ori = read_first_line(file_path)
count_ori = int(count_ori)

# Initialize click count and image display state
click_count = count_ori
displaying_alternate = False

# Load the images
img_path_original = "close.png"  # Replace with your original image path
img_path_alternate = "open.png"  # Replace with your alternate image path
img_original = cv2.imread(img_path_original)
img_alternate = cv2.imread(img_path_alternate)

# Check if the images are loaded
if img_original is None or img_alternate is None:
    print("Error loading images.")
    exit()

# Define Tiffany blue color
tiffany_blue = (181, 186, 10)  # BGR format

# Create a window and set the mouse callback function
cv2.namedWindow("Taylor")
cv2.setMouseCallback("Taylor", count_clicks)



while True:
    # Select the image to display
    if displaying_alternate:
        img_to_display = img_alternate
    else:
        img_to_display = img_original

    # Add text to the image
    img_with_text = img_to_display.copy()
    height, width, _ = img_with_text.shape
    
    # Calculate text size and position
    text1 = "TAYLOR"
    text2 = f"Count: {click_count}"
    font_scale = 14  # Adjust font size as needed
    thickness = 40   # Adjust thickness as needed
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    # Calculate size of the text to center it
    (text_width1, text_height1), _ = cv2.getTextSize(text1, font, font_scale, thickness)
    (text_width2, text_height2), _ = cv2.getTextSize(text2, font, font_scale, thickness)
    
    # Center text horizontally at the top
    text_x1 = (width - text_width1) // 2
    text_y1 = text_height1 + 80  # Add some padding from the top
    text_x2 = (width - text_width2) // 2
    text_y2 = text_y1 + text_height1 + 80  # Add some padding between lines
    
    # Put the text on the image
    cv2.putText(img_with_text, text1, (text_x1, text_y1), font, font_scale, tiffany_blue, thickness, cv2.LINE_AA)
    cv2.putText(img_with_text, text2, (text_x2, text_y2), font, font_scale, tiffany_blue, thickness, cv2.LINE_AA)

    # Display the image
    cv2.imshow("Taylor", img_with_text)

    # Wait for user input
    key = cv2.waitKey(1) & 0xFF

    # Exit if the user presses 'q'
    if key == ord('q'):
        break

new_count = str(click_count)
modify_first_line(file_path, new_count)

# Verify the change
updated_first_line = read_first_line(file_path)
# print("Updated First Line:", updated_first_line)
# Clean up

cv2.destroyAllWindows()
pygame.quit()





