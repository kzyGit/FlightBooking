import os
import cloudinary
import uuid


def cloudinary_config():
    """ Cloudinary configuration settings """
    return cloudinary.config(
        cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
        api_key=os.getenv('CLOUDINARY_API_KEY'),
        api_secret=os.getenv('CLOUDINARY_API_SECRET')
    )


def upload_images(image):
    """ Uploads an imaged to cloudinary """
    cloudinary_config()
    name = image.name.split(".")
    filename = name[0] + str(uuid.uuid4())
    return cloudinary.uploader.upload(image, public_id=filename,
                                      folder='FlightSpace')
