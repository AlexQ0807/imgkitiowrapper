import os
import base64
import unittest
from dotenv import load_dotenv

from imgkitiowrapper.operations import ImgKitOperations

load_dotenv()


class TestSQLAlchemyEngineWrapper(unittest.TestCase):
    IMAGEKITIO_PUBLIC_KEY = os.getenv("IMAGEKITIO_PUBLIC_KEY")
    IMAGEKITIO_PRIVATE_KEY = os.getenv("IMAGEKITIO_PRIVATE_KEY")
    IMAGEKITIO_URL_ENDPOINT = os.getenv("IMAGEKITIO_URL_ENDPOINT")
    imgkit_op = ImgKitOperations(public_key=IMAGEKITIO_PUBLIC_KEY,
                                 private_key=IMAGEKITIO_PRIVATE_KEY,
                                 url_endpoint=IMAGEKITIO_URL_ENDPOINT)

    def test_upload_image_url(self):
        try:
            image_url = "https://www.theartstory.org/images20/works/post_impressionism_1.jpg"

            upload_success = self.imgkit_op.upload_url(image_url, "post_impressionism_1",
                                                       upload_image_folder='/test_folder', tags=["testing"])

            self.assertTrue(upload_success)
        except Exception as e:
            print(e)
            self.assertTrue(False)

    def test_upload_image_base64(self):
        try:
            with open("sample_image.jpg", "rb") as image_file:
                img_base64 = base64.b64encode(image_file.read())

            upload_success = False
            if img_base64 is not None:
                upload_success = self.imgkit_op.upload_url(img_base64, "impressionism_2",
                                                           upload_image_folder='/test_folder', tags=["testing"])
            self.assertTrue(upload_success)
        except Exception as e:
            print(e)
            self.assertTrue(False)

    def test_get_folder_images(self):
        try:
            image_list = self.imgkit_op.get_all_images_in_folder(folder_path='/test_folder')
            image_urls = [img.url for img in image_list]
            print(image_urls)
            self.assertTrue(True)
        except Exception as e:
            print(e)
            self.assertTrue(False)

    def test_get_folder_images_filter_by_tags(self):
        try:
            image_list = self.imgkit_op.get_all_images_in_folder(folder_path='/test_folder', tags="testing")
            image_urls = [img.url for img in image_list]
            print(image_urls)
            self.assertTrue(True)
        except Exception as e:
            print(e)
            self.assertTrue(False)