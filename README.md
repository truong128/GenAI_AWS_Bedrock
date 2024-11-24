# GenAI_AWS_Bedrock
This is the code snippet used to generate the image according to the "Prompt" request using AWS Bedrock services.

# Here is the step-by-step to run
## Step 1: Create an AWS account
## Step 2: Prepare any input image
## Step 3: Run on AWS CLI or API (need AWS configure if running API from local machine)
## Step 4: Run the Python script above

# Troubleshooting: If you encounter any errors related to permissions or models, you need to go to your account to set them up.
## 1. Go to the AWS Management Console
## 2. Search for "IAM" and go to the IAM service
## 3. Click on "Users" in the left sidebar
## 4. Find and click on your user "your IAM user"
## 5. Click on "Add permissions" button
## 6. Choose "Attach existing policies directly"
## 7. In the search box, type "Bedrock"
## 8. Look for and select AmazonBedrockFullAccess
## 9. Click "Next" and then "Add permissions"

# -> Alternatively, if you prefer using AWS CLI (AWS console), you can run:
aws iam attach-user-policy \
    --user-name "your-IAM user here" \
    --policy-arn arn:aws:iam::aws:policy/AmazonBedrockFullAccess
