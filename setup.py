import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="knn-classifier-dmartinez", # Replace with your own username
    version="0.0.2",
    author="David Martinez",
    author_email="author@example.com",
    description="A simple brute-force approach to knn classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/unburied/k_nearest_neighbors",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)