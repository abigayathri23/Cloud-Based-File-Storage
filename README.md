## MINI PROJECT IN CLOUD COMPUTING
Cloud-Based File Storage
This project implements a simple cloud-based file storage system that allows users to upload, download, and delete files using AWS S3. The backend is developed using Flask (Python), and the frontend provides an easy-to-use interface for interacting with the system.

## Features
Upload Files: Users can upload files to a cloud storage system (AWS S3).
Download Files: Users can retrieve previously uploaded files.
Delete Files: Users can delete files from the cloud storage.
Prerequisites
Before setting up the project, ensure you have the following:
## AWS
AWS Account: You will need an AWS account to use S3 for file storage.
AWS S3 Bucket: You must create an S3 bucket in your AWS account to store the files.
Python 3.x: The backend is developed in Python 3.
AWS CLI: Used for authentication with AWS services.
Flask: A Python web framework for running the backend server.
Boto3: AWS SDK for Python to interact with AWS S3.

## FRONT END OUTPUT
![Front End](D:\Screenshots\Front End.png)

## Setup
1. Clone the Repository
Begin by cloning this repository to your local machine.

2. Install Dependencies
Set up the required dependencies for the project, which include Python libraries like Flask and Boto3. It is recommended to use a virtual environment to manage dependencies.

3. Configure AWS
Before running the application, configure your AWS CLI to authenticate with AWS services. This will store your AWS credentials securely.

You will also need to create an AWS S3 bucket where files will be uploaded, downloaded, and deleted. Ensure that you have the necessary IAM permissions to perform these operations (such as s3:PutObject, s3:GetObject, and s3:DeleteObject).

4. Backend Setup
The backend is implemented using Flask. It provides endpoints for uploading, downloading, and deleting files. The backend interacts with AWS S3 using the Boto3 library, which is an SDK provided by AWS.

5. Frontend Setup
The frontend is a simple HTML form that allows users to interact with the backend. It provides input fields for selecting files to upload and buttons to trigger download and delete operations.

6. Running the Project
Once all dependencies are installed and configuration is complete, you can run the backend server. The server will handle API requests to interact with S3 for file upload, download, and deletion.

The frontend can be opened in any modern web browser. It will allow users to perform operations on the cloud storage by interacting with the backend.

7. API Endpoints
POST /upload: Uploads a file to S3.
GET /download: Downloads a file from S3.
DELETE /delete: Deletes a file from S3.
Troubleshooting
AWS Configuration: If the AWS credentials are not configured correctly, you may encounter authentication errors.
Permissions: Make sure your AWS IAM user or role has the required permissions to access S3 and perform the necessary actions (upload, download, delete).
Bucket Region: Double-check that the region specified in the backend code matches the region of your S3 bucket.
