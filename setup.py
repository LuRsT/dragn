import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    # Project
    name="dragn",
    version="0.0.2",
    description="A library to emulate rolling dice",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lurst/dragn",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
    ],
    # Author
    author="Gil Goncalves",
    author_email="lursty@gmail.com",
    # Code
    packages=setuptools.find_packages(),
)
