# :package_name

This repo details an attempt to use the [DINO](https://github.com/facebookresearch/dino) self-supervised training method on a dataset of chest x-rays. The resulting embeddings will then be used with the k-nn algorithm to attempt to detect diseases such as fractures from a small sample of labelled images.


## Install

Clone the repo and run the following commands to install the necessary libraries

``` bash
pip install virtualenv
virtualenv virtualenv
virtualenv/bin/activate # This is for linux machines. The activate file will be in a different location on different systems
pip install -r requirements.txt
```

## Usage
