import setuptools


setuptools.setup(
    name="parakeet",
    author="Anshaj Goyal",
    version="1.0",
    description="Parakeet paraphraser",
    long_description="A paraphraser is a tool that is used to rewriting a piece of text in order to make it easier to understand. The tool is based on the Seq2Seq model, which is a neural network that is used to learn the structure of a text. The Seq2Seq model is trained on a large dataset of texts, and the paraphraser is able to use this information to generate a new piece of text that is easier to understand.",
    url="https://github.com/leetanshaj/Parakeet.git",
    packages=setuptools.find_packages(),
    install_requires=['simpletransformers', 'sklearn', 'sentence_transformers', 'Levenshtein'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: Apache 2.0",
        "Operating System :: OS Independent",
    ],
)