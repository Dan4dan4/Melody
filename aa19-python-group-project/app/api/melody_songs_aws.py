import boto3
import botocore
import os
import uuid

BUCKET_NAME = os.environ.get("S3_BUCKET")
S3_LOCATION = f"https://{BUCKET_NAME}.s3.amazonaws.com/"
ALLOWED_EXTENSIONS = {"mp3", "wav", "ogg", "m4a"}

s3 = boto3.client(
   "s3",
   aws_access_key_id=os.environ.get("S3_KEY"),
   aws_secret_access_key=os.environ.get("S3_SECRET")
)

def get_unique_filename(filename):
    ext = filename.rsplit(".", 1)[1].lower()
    unique_filename = uuid.uuid4().hex
    return f"{unique_filename}.{ext}"


def upload_file_to_s3(file, acl="public-read"):
    try:
        s3.upload_fileobj(
            file,
            BUCKET_NAME,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type,
                "Metadata": {
                    "x-amz-meta-Content-Type": file.content_type
                }
            }
        )
    except Exception as e:
        # in case the s3 upload fails
        return {"errors": str(e)}

    return {"url": f"{S3_LOCATION}{file.filename}"}


def remove_file_from_s3(audio_url):
    # AWS needs the audio file name, not the URL
    key = audio_url.rsplit("/", 1)[1]
    print(key)
    try:
        s3.delete_object(
        Bucket=BUCKET_NAME,
        Key=key
        )
    except Exception as e:
        return { "errors": str(e) }
    return True

def validate_audio_file(filename):
    """
    Validate file extension for audio files
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS