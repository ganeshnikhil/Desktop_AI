# Adapted from OpenAI's Vision example 
import base64
import cv2 
from src.BRAIN.lm_ai import client  # point to local server 
from PIL import Image 


def resize_image(image_path , require_width=336 , require_height=336):
    with Image.open(image_path) as img:
        width, height = img.size
        if height <= require_height and width <= require_width:
            return True 
        try:
            img = img.resize((require_width, require_height), Image.ANTIALIAS)
            img.save(image_path)
            print(f"Image saved to {image_path}, size: {require_width}x{require_height}")
        except Exception as e:
            print(e)
            return False 
        return True 
    
def capture_image_and_save(image_path="captured_image.png"):
    # Initialize the camera
    cap = cv2.VideoCapture(0)  # 0 is the default camera

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return None 

    try:
        # Capture a single frame
        ret, frame = cap.read()

        if ret:
            # Save the image in PNG format
            cv2.imwrite(image_path, frame)
            print(f"Image captured and saved as {image_path}")
            return image_path 
        else:
            print("Error: Could not capture image.")
            return None 
    finally:
        # Release the camera
        cap.release()
        cv2.destroyAllWindows()

def detect_object(image_path , model="Lewdiculous/Eris_PrimeV4-Vision-32k-7B-GGUF-IQ-Imatrix"):
    # Ask the user for a path on the filesystem:
    # Read the image and encode it to base64:
    
    if not resize_image(image_path):
        print("Failed to resize image.")
        return None 
    
    
    base64_image = ""
    try:
        image = open(image_path.replace("'", ""), "rb").read()
        base64_image = base64.b64encode(image).decode("utf-8")
    except:
        print("Couldn't read the image. Make sure the path is correct and the file exists.")
        exit()

    completion = client.chat.completions.create(
        model= model,
        messages=[
        {
        "role": "system",
        "content": "This is a chat between a user and an assistant. The assistant is helping the user to describe an image.",
        },
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "What’s in this image?.ingnore the human in background"},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                },
            },
        ],
        }
    ],
    max_tokens=20000,
    stream=True
    )
    
    
    result = []
    for chunk in completion:
        if chunk.choices[0].delta.content:
            token = chunk.choices[0].delta.content
            print(token , end="", flush=True)
            result.append(token)
    if result:
        return result 
    

# if __name__ == "__main__":
#     image = capture_image_and_save()
    
#image = capture_image_and_save()