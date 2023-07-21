# Image-Caption-Generator

This repository contains code and resources for image caption generator using deep learning models. The project aims to develop accurate and efficient models for describing an image in words by the model.

## Table of Contents
 - [Introduction](#introduction)
 - [Installation](#installation)
 - [Usage](#usage)
 - [Dataset](#dataset)
 - [Model Training](#model-training)
 - [Contributing](#contributing)
 - [License](#license)

## Introduction

The Image Caption Generator is a deep learning based project that automatically generates captions for images using state-of-the-art computer vision techniques and natural language processing models.

## Features

 - Automatic image captioning using deep learning models.
 - Pre-trained models for caption generation.
 - Support for various image formats.

## Installation

1. Clone the repository to your local machine:
```shell
git clone https://github.com/ArnabKumarRoy02/Image-Caption-Generator.git
```

2. Install the required dependencies:

```shell
pip install -r requirements.txt
```

## Usage

1. Make sure you have the required dependencies installed.
2. Run the `app.py` script to test it:
```shell
flask run
```
3. Optionally, you can fine-tune or train your own models using the provided dataset and scripts.

## Dataset

The Image Caption Generator uses the [Flickr8k](https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_Dataset.zip) dataset for training. Make sure to download the dataset or use your own dataset for training.

## Pre-trained Models

We provide pre-trained models that can be use for generating captions without the need for training. You can download the pre-trained models from the following links:
 - [Xception Model](weights.h5)
 - [EfficientNetB0 Model](model.h5)

## Contributing

Contributions to this project are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE)

## Acknowledgments

 - The Image Caption Generator project is built upon the works of several open-source libraries and research papers. We acknowledge the contributions of the research community and the creators of the datasets used in this project.
