import cv2
# Read the image from file
image = cv2.imread('image.jpeg')
# Display the image in a window
cv2.imshow('Image', image)
# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

# Load the image
image = cv2.imread('image.jpeg')
# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Save the grayscale image
cv2.imwrite('gray_image Santiago Medrano0103.jpeg ', gray_image)

# Load the image
image = cv2.imread('image.jpeg ')
# Resize the image to 300x200
resized_image = cv2.resize(image, (300, 200))
# Save the resized image
cv2.imwrite('resized_image Santiago Medrano0103.jpg', resized_image)

# Load the image
image = cv2.imread('image.jpeg ')
# Get the image's height and width
(h, w) = image.shape[:2]
# Define the center of the image
center = (w // 2, h // 2)
# Rotation matrix
matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
# Perform the rotation
rotated_image = cv2.warpAffine(image, matrix, (w, h))
# Save the rotated image
cv2.imwrite('rotated_image Santiago Medrano0103.jpg  ', rotated_image)

# Load the image
image = cv2.imread('image.jpeg  ')
# Apply Gaussian Blur
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
# Save the blurred image
cv2.imwrite('blurred_image Santiago Medrano0103.jpg ', blurred_image)

# Load the image
image = cv2.imread('image.jpeg ')
# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Apply Canny edge detector
edges = cv2.Canny(gray_image, 100, 200)
# Save the edges image
cv2.imwrite('edges Santiago Medrano0103.jpg', edges)

# Load the image
image = cv2.imread('image.jpeg')
# Draw a rectangle
cv2.rectangle(image, (50, 50), (200, 200), (255, 0, 0), 3)
# Add text to the image
cv2.putText(image, 'OpenCV Santiago Medrano0103 ', (60, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
# Save the output image
cv2.imwrite('output_image Santiago Medrano0103.jpg ', image)

# Load the image
image = cv2.imread('image.jpeg ', 0)
# Apply thresholding
_, thresh_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
# Save the thresholded image
cv2.imwrite('threshold_image Santiago Medrano0103.jpg', thresh_image)

# Load the image
image = cv2.imread('image.jpeg')
# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Find edges
edges = cv2.Canny(gray_image, 100, 200)
# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Draw contours on the original image
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
# Save the output image with contours
cv2.imwrite('contours_image Santiago Medrano0103.jpg', image)

