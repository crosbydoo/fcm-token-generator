# FCM TOKEN GENERATOR

This tool will generate a new fcm token for your project. this tool work on new legacy you can read on below for the detail.
Tool can generate token access that used for test fcm through postman or https.

## New Legacy Must Read

- [2024 Firebase Cloud Messaging Legacy](https://firebase.google.com/docs/cloud-messaging/migrate-v1?hl=en&authuser=2&_gl=1*1mafz7a*_ga*MTg4MzY3MDAxNS4xNzE2NzQ1OTI1*_ga_CW55HF8NVT*MTcyMDY3OTgxMS40OC4xLjE3MjA2Nzk4NjcuNC4wLjA.): Update for new legacy official from Firebase byGoogle.

## Prerequisites

Before you begin, ensure you have the following installed:

- Lates Python
- Google Firebase Plugin

## Get Started

1. Clone the repository:

   ```bash
   git clone https://github.com/crosbydoo/fcm-token-generator.git
   ```

2. Navigate to the project directory and install depedencies

   ```bash
   pip install google-oauth
   ```

3. Set up your Firebase credentials

   - Obtain your adminsdk from firebase console
   - How to obtain ? Go project settings -> Service Accounts -> Admin SDK -> Generate new provate Key

4. Adjust the path of adminsdk.json
   In main.py on the SERVICE_ACCOUNT_FILE variable please adjust with your adminsdk.json path.

5. Run the script

   ```bash
   python main.py
   ```

## OTHER WAYS TO USE

you can use google-colab to run and obtain the access token.

### How to use with Google Colab

1. just go to your google colab
2. please ensure you have upload the adminsdk.json
3. adding this code
   ```bash
   from google.colab import files
   ```
4. how to get the path your adminsdk.json in colab ? Just click right and copy path . very simple right ?
5. just run the script and you will get the access token
