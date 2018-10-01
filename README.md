# sharex-uploader

Python flask based sharex-uploader with one master password. No compression. Self-Hosted.
Includes web-gui for manual upload.

#Sharex custom uploader config:

`{
  "DestinationType": "ImageUploader, TextUploader, FileUploader",
  "RequestURL": "YOURDOMAIN.COM/upload",
  "FileFormName": "file",
  "Arguments": {
    "password": "YOUR_MASTER_PASSWORD"
  },
  "ResponseType": "RedirectionURL"
}`