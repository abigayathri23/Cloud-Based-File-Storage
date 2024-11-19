from flask import Flask, request, jsonify, send_file
import boto3
from google.cloud import storage
import os

app = Flask(__name__)

# AWS S3 Configuration
AWS_BUCKET_NAME = "your-aws-bucket-name"
AWS_REGION = "your-region"
s3_client = boto3.client('s3', region_name=AWS_REGION)

# Google Cloud Storage Configuration
GCP_BUCKET_NAME = "your-gcp-bucket-name"
gcp_client = storage.Client()

# Upload File
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    cloud_provider = request.form.get('cloud_provider')

    if cloud_provider == 'aws':
        s3_client.upload_fileobj(file, AWS_BUCKET_NAME, file.filename)
        return jsonify({"message": f"File uploaded to AWS S3: {file.filename}"})

    elif cloud_provider == 'gcp':
        bucket = gcp_client.bucket(GCP_BUCKET_NAME)
        blob = bucket.blob(file.filename)
        blob.upload_from_file(file)
        return jsonify({"message": f"File uploaded to GCP: {file.filename}"})

    return jsonify({"error": "Invalid cloud provider"}), 400

# Download File
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    cloud_provider = request.args.get('cloud_provider')

    if cloud_provider == 'aws':
        s3_client.download_file(AWS_BUCKET_NAME, filename, filename)
        return send_file(filename, as_attachment=True)

    elif cloud_provider == 'gcp':
        bucket = gcp_client.bucket(GCP_BUCKET_NAME)
        blob = bucket.blob(filename)
        blob.download_to_filename(filename)
        return send_file(filename, as_attachment=True)

    return jsonify({"error": "Invalid cloud provider"}), 400

# Delete File
@app.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    cloud_provider = request.args.get('cloud_provider')

    if cloud_provider == 'aws':
        s3_client.delete_object(Bucket=AWS_BUCKET_NAME, Key=filename)
        return jsonify({"message": f"File deleted from AWS S3: {filename}"})

    elif cloud_provider == 'gcp':
        bucket = gcp_client.bucket(GCP_BUCKET_NAME)
        blob = bucket.blob(filename)
        blob.delete()
        return jsonify({"message": f"File deleted from GCP: {filename}"})

    return jsonify({"error": "Invalid cloud provider"}), 400

if __name__ == '__main__':
    app.run(debug=True)
