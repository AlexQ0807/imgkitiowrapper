import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='imgkitiowrapper',
    version='0.0.1',
    author='Alex Q',
    author_email='alex.quan0807@gmail.com',
    description='Personal Wrapper for Image Kit IO operations',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['imgkitiowrapper'],
    install_requires=[
        'imagekitio'
    ],
)