# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/05a_classification.data.transforms.ipynb (unless otherwise specified).

__all__ = ['imagenet_stats', 'cifar_stats', 'mnist_stats', 'imagenet_stats', 'cifar_stats', 'mnist_stats',
           'imagenet_no_augment_transform', 'imagenet_augment_transform', 'aug_transforms']

# Cell
from typing import *

import albumentations as A
import numpy as np
import torchvision.transforms as T
from timm.data.auto_augment import auto_augment_transform, rand_augment_transform
from timm.data.constants import IMAGENET_DEFAULT_MEAN, IMAGENET_DEFAULT_STD
from timm.data.transforms import RandomResizedCropAndInterpolation, _pil_interp
from torch import Tensor

# Cell
imagenet_stats = (IMAGENET_DEFAULT_MEAN, IMAGENET_DEFAULT_STD)
cifar_stats = ([0.491, 0.482, 0.447], [0.247, 0.243, 0.261])
mnist_stats = ([0.15, 0.15, 0.15], [0.15, 0.15, 0.15])

#nbdev_comment _all_ = ["imagenet_stats", "cifar_stats", "mnist_stats"]

# Cell
def imagenet_no_augment_transform(
    size: Union[Sequence, int] = 224, interpolation: str = "bilinear"
) -> T.Compose:
    """
    The default image transform without data augmentation.

    It is often useful for testing models on Imagenet.
    It sequentially resizes the image and takes a central cropping.
    """
    interpolation = _pil_interp(interpolation)
    tfl = [T.Resize(size, _pil_interp(interpolation)), T.CenterCrop(size)]
    return T.Compose(tfl)

# Cell
def imagenet_augment_transform(
    size: int = 224,
    scale: Optional[float] = None,
    ratio: Optional[float] = None,
    interpolation: str = "random",
    hflip: Union[float, bool] = 0.5,
    vflip: Union[float, bool] = False,
    color_jitter: Union[Sequence, float] = 0.4,
    auto_augment: Optional[str] = None,
    mean: Optional[Sequence[float]] = IMAGENET_DEFAULT_MEAN,
) -> T.Compose:
    """
    The default image transform with data augmentation.It is often useful for training models on Imagenet.

    Adapted from: https://github.com/rwightman/pytorch-image-models/blob/master/timm/data/transforms_factory.py
    """

    scale = tuple(scale or (0.08, 1.0))  # default imagenet scale range
    ratio = tuple(ratio or (3.0 / 4.0, 4.0 / 3.0))  # default imagenet ratio range

    transforms = [
        RandomResizedCropAndInterpolation(size, scale, ratio, interpolation),
    ]

    if hflip and hflip > 0:
        transforms.append(T.RandomHorizontalFlip(p=hflip))
    if vflip and vflip > 0.0:
        transforms.append(T.RandomVerticalFlip(p=vflip))

    if auto_augment:
        assert isinstance(auto_augment, str)
        if isinstance(size, (tuple, list)):
            size_min = min(size)
        else:
            size_min = size

        aa_params = dict(
            translate_const=int(size_min * 0.45),
            img_mean=tuple([min(255, round(255 * x)) for x in mean]),
        )

        if interpolation and interpolation != "random":
            aa_params["interpolation"] = _pil_interp(interpolation)
        if auto_augment.startswith("rand"):
            transforms += [rand_augment_transform(auto_augment, aa_params)]
        else:
            transforms += [auto_augment_transform(auto_augment, aa_params)]

    elif color_jitter is not None:
        # color jitter is enabled when not using AA
        if isinstance(color_jitter, (list, tuple)):
            # color jitter should be a 3-tuple/list if spec brightness/contrast/saturation
            # or 4 if also augmenting hue
            assert len(color_jitter) in (3, 4)
        else:
            # if it's a scalar, duplicate for brightness, contrast, and saturation, no hue
            color_jitter = (float(color_jitter),) * 3
        transforms += [T.ColorJitter(*color_jitter)]
    return T.Compose(transforms)

# Cell
def aug_transforms(
    presize: int = 260,
    size: int = 224,
    interpolation: int = 1,
    hflip: Union[float, bool] = 0.5,
    vflip: Union[float, bool] = False,
    max_lighting: Union[float, bool] = 0.2,
    p_lighting: float = 0.75,
    max_rotate: Union[float, int, bool] = 10.0,
    p_rotate: float = 0.5,
    max_warp: Union[float, bool] = 0.2,
    p_affine: float = 0.75,
    pad_mode: str = "reflect",
    mult: float = 1.0,
    xtra_tfms: Optional[List] = None,
) -> A.Compose:
    """
    Utility func to easily create a list of flip, rotate, zoom, lighting transforms.
    Inspired from : https://docs.fast.ai/vision.augment.html#aug_transforms
    """
    max_rotate, max_lighting, max_warp = (
        np.array([max_rotate, max_lighting, max_warp]) * mult
    )
    transforms = [
        A.Resize(presize, presize, interpolation=interpolation, always_apply=True)
    ]
    if hflip:
        transforms += [A.HorizontalFlip(p=hflip)]
    if vflip:
        transforms += [A.VerticalFlip(p=vflip)]
    if max_rotate:
        transforms += [
            A.Rotate(limit=max_rotate, interpolation=interpolation, p=p_rotate)
        ]
    if max_warp:
        transforms += [A.IAAAffine(scale=max_warp, p=p_affine, mode=pad_mode)]
    if max_lighting:
        transforms += [A.RandomBrightness(max_lighting, p=p_lighting)]
        transforms += [A.RandomContrast(max_lighting, p=p_lighting)]
    if xtra_tfms is not None:
        transforms += [xtra_tfms]

    transforms += [
        A.RandomResizedCrop(size, size, interpolation=interpolation, always_apply=True)
    ]
    return A.Compose(transforms)