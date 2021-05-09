import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="text2text",
    version="0.1.2",
    author="Artit Wangperawong",
    author_email="artitw@gmail.com",
    description="Text2Text: Multilingual text transformer to generate translations, summarizations, questions and variations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/artitw/text2text",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='multilingual cross-lingual bert natural language processin nlp nlg text generation question summary summarization translation data augmentation science machine learning colab',
    install_requires=[
        'torch',
        'tqdm',
        'numpy',
        'sentencepiece',
        'transformers'
    ],
)