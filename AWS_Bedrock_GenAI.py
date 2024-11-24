import boto3
import base64
import json
from PIL import Image
import io

session = boto3.Session(region_name='us-east-1')
bedrock = session.client(service_name='bedrock-runtime')

def encode_image(image_path):
 with open(image_path, "rb") as image_file:
 return base64.b64encode(image_file.read()).decode('utf-8')

def decode_image(base64_string):
 image_data = base64.b64decode(base64_string)
 return Image.open(io.BytesIO(image_data))

def change_background(input_image_path, prompt, negative_prompt, output_image_path):
 
 base64_image = encode_image(input_image_path)

 request_body = {
 "taskType": "OUTPAINTING",
 "outPaintingParams": {
 "text": prompt,
 "negativeText": negative_prompt,
 "maskPrompt": "background",
 "image": base64_image,
 "outPaintingMode": "PRECISE"
 },
 "imageGenerationConfig": {
 "numberOfImages": 1,
 "quality": "standard",
 "cfgScale": 8.0,
 "seed": 42
 }
 }

 response = bedrock.invoke_model(
 body=json.dumps(request_body),
 modelId="amazon.titan-image-generator-v2:0",
 contentType="application/json",
 accept="application/json"
 )

 response_body = json.loads(response['body'].read())
 
 generated_image_base64 = response_body['images'][0]
 generated_image = decode_image(generated_image_base64)

 generated_image.save(output_image_path)
 print(f"Generated image saved to {output_image_path}")

input_image_path = "/Users/truong/Documents/3_AWS_AI_ML/Angels.jpg"
output_image_path = "/Users/truong/Documents/3_AWS_AI_ML/GenAI_Angels.jpg"

hashtag#prompt for Fuji Mountain
background_prompt = """
Mount Fuji in soft morning light, snow-capped peaks against a serene pastel sky. 
Cherry blossoms frame the scene, creating a dreamy Japanese landscape. Wispy clouds 
embrace the mountain slopes. Soft, ethereal lighting with subtle pink and purple hues. 
Peaceful and traditionally Japanese, maintaining soft focus for foreground prominence.
"""

negative_prompt = """
Urban elements, buildings, power lines, tourists, vehicles, text, logos, harsh lighting, 
oversaturated colors, heavy clouds, dark shadows, busy elements, modern structures
"""

change_background(input_image_path, background_prompt, negative_prompt, output_image_path)
