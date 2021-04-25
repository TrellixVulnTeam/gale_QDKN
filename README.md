# PyTorch Gale



## Installation

You can install PyTorch Gale from source

```bash
git clone https://github.com/benihime91/gale
cd gale
pip install .
```

If you plan to develop PyTorch Gale yourself you can use an editable install 
```bash
git clone https://github.com/benihime91/gale
pip install -e "gale[dev]"
```

## Introduction
PyTorch Gale tasks allow you to train models using `PyTorch Image Models` models, use Hydra to hotswap models, optimizers or schedulers and leverage all the advances features that Lightning has to offer, including custom Callbacks, Loggers, Accelerators and high performance scaling with minimal changes.

This project was started as a way to collect interesting techniques dotted throughout Kaggle competitions and varous deep learning forums which have been usefull in training accuracte deep learning models for Computer Vision Tasks. 

Currently PyTorch Gale only supports Image Classification. The final goal is to be able to support both Object Detection and Image Segmentation hopefully.

PyTorch Gale is beta software. The project is under active development and our APIs are subject to change in future releases. The current API of PyTorch Gale is highly inspired from [Detectron 2](https://github.com/facebookresearch/detectron2).

## How To Learn
The best way to learn PyTorch Gale is to go through the documentation. You should probably get familiar with [PyTorch](https://pytorch.org/) and [PyTorch Lightning](https://pytorch-lightning.readthedocs.io/en/latest/). Next, go through [Hydra docs](https://hydra.cc/docs/next/intro) and [PyTorch Image Models](https://github.com/rwightman/pytorch-image-models)

## Contributions
Have a question? Found a bug? Missing a specific feature? Ran into a problem? Feel free to file a new issue or PR with respective title and description. If you already found a solution to your problem, don't hesitate to share it. Suggestions for new best practices and tricks are always welcome!

After you clone this repository, please run `nbdev_install_git_hooks` in your terminal. This sets up git hooks, which clean up the notebooks to remove the extraneous stuff stored in the notebooks (e.g. which cells you ran) which causes unnecessary merge conflicts.
