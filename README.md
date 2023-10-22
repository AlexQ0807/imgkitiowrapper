## Wrapper for Imagekit.IO (Private)
<hr>

### Setup
```
pip install git+https://github.com/AlexQ0807/imgkitiowrapper.git
```


### Example

```
image_url = "<image_url_to_upload>"

upload_success = self.imgkit_op.upload_url(image_url, "test_image",
                                           upload_image_folder='/test_folder', 
                                           tags=["test"])

```