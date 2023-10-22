from imagekitio import ImageKit
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions
from imagekitio.models.ListAndSearchFileRequestOptions import ListAndSearchFileRequestOptions

class ImgKitOperations:
    imagekit = None

    def __init__(self, private_key, public_key, url_endpoint):
        try:
            self.imagekit = ImageKit(
                private_key=private_key,
                public_key=public_key,
                url_endpoint=url_endpoint
            )
        except Exception as e:
            raise e

    def get_all_images_in_folder(self, folder_path='/', tags: str = ""):
        try:
            options = ListAndSearchFileRequestOptions(
                path=folder_path,
            )
            if len(tags) > 0:
                options.tags = tags

            result = self.imagekit.list_files(options=options)

            return result.list

        except Exception as e:
            raise e

    def upload_url(self, image_url, upload_image_name, upload_image_folder="/", tags: list = None,
                   use_unique_file_name: bool = False, is_private_file: bool = False):

        try:
            if self.imagekit is not None:

                options = UploadFileRequestOptions(
                    use_unique_file_name=use_unique_file_name,
                    folder=upload_image_folder,
                    is_private_file=is_private_file,
                )

                if tags is not None and len(tags) > 0:
                    options.tags = tags

                res = self.imagekit.upload_file(file=image_url,
                                                file_name=upload_image_name,
                                                options=options)

                if res.response_metadata:
                    return 200 <= res.response_metadata.http_status_code <= 299
                else:
                    return False
        except Exception as e:
            raise e
