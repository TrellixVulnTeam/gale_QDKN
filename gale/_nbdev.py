# AUTOGENERATED BY NBDEV! DO NOT EDIT!

__all__ = ["index", "modules", "custom_doc_links", "git_url"]

index = {"setup_logger": "00_core.utils.logger.ipynb",
         "log_main_process": "00_core.utils.logger.ipynb",
         "subplots": "00a_core.utils.visualize.ipynb",
         "show_image": "00a_core.utils.visualize.ipynb",
         "show_titled_image": "00a_core.utils.visualize.ipynb",
         "show_images": "00a_core.utils.visualize.ipynb",
         "imshow_tensors": "00a_core.utils.visualize.ipynb",
         "Registry.__doc__": "00b_core.utils.structures.ipynb",
         "Registry.register.__doc__": "00b_core.utils.structures.ipynb",
         "Registry.get.__doc__": "00b_core.utils.structures.ipynb",
         "ACTIVATION_REGISTRY": "00b_core.utils.structures.ipynb",
         "ACTIVATION_REGISTRY.__doc__": "00b_core.utils.structures.ipynb",
         "IMAGE_CLASSIFIER_BACKBONES": "00b_core.utils.structures.ipynb",
         "IMAGE_CLASSIFIER_BACKBONES.__doc__": "00b_core.utils.structures.ipynb",
         "IMAGE_CLASSIFIER_HEADS": "00b_core.utils.structures.ipynb",
         "IMAGE_CLASSIFIER_HEADS.__doc__": "00b_core.utils.structures.ipynb",
         "META_ARCH_REGISTRY": "00b_core.utils.structures.ipynb",
         "META_ARCH_REGISTRY.__doc__": "00b_core.utils.structures.ipynb",
         "OPTIM_REGISTRY": "00b_core.utils.structures.ipynb",
         "OPTIM_REGISTRY.__doc__": "00b_core.utils.structures.ipynb",
         "SCHEDULER_REGISTRY": "00b_core.utils.structures.ipynb",
         "SCHEDULER_REGISTRY.__doc__": "00b_core.utils.structures.ipynb",
         "DatasetCatalog": "00b_core.utils.structures.ipynb",
         "norm_types": "01_core.nn.utils.ipynb",
         "bn_types": "01_core.nn.utils.ipynb",
         "init_default": "01_core.nn.utils.ipynb",
         "cond_init": "01_core.nn.utils.ipynb",
         "apply_leaf": "01_core.nn.utils.ipynb",
         "apply_init": "01_core.nn.utils.ipynb",
         "set_bn_eval": "01_core.nn.utils.ipynb",
         "trainable_params": "01_core.nn.utils.ipynb",
         "params": "01_core.nn.utils.ipynb",
         "maybe_convert_to_onehot": "01_core.nn.utils.ipynb",
         "worker_init_fn": "01_core.nn.utils.ipynb",
         "LOSS_REGISTRY": "01a_core.nn.losses.ipynb",
         "LOSS_REGISTRY.__doc__": "01a_core.nn.losses.ipynb",
         "LabelSmoothingCrossEntropy": "01a_core.nn.losses.ipynb",
         "BinarySigmoidFocalLoss": "01a_core.nn.losses.ipynb",
         "FocalLoss": "01a_core.nn.losses.ipynb",
         "build_loss": "01a_core.nn.losses.ipynb",
         "Ranger": "02_core.nn.optim.optimizers.ipynb",
         "RangerGC": "02_core.nn.optim.optimizers.ipynb",
         "SGDP": "02_core.nn.optim.optimizers.ipynb",
         "AdamP": "02_core.nn.optim.optimizers.ipynb",
         "LRMultiplier": "02a_core.nn.optim.lr_schedulers.ipynb",
         "CosineLR": "02a_core.nn.optim.lr_schedulers.ipynb",
         "FlatCosScheduler": "02a_core.nn.optim.lr_schedulers.ipynb",
         "WarmupParamScheduler": "02a_core.nn.optim.lr_schedulers.ipynb",
         "WarmupCosineLR": "02a_core.nn.optim.lr_schedulers.ipynb",
         "WarmupLinearLR": "02a_core.nn.optim.lr_schedulers.ipynb",
         "WarmupConstantLR": "02a_core.nn.optim.lr_schedulers.ipynb",
         "WarmupStepLR": "02a_core.nn.optim.lr_schedulers.ipynb",
         "Configurable": "03_core.classes.ipynb",
         "GaleModule": "03_core.classes.ipynb",
         "OptimSchedBuilder": "03_core.classes.ipynb",
         "OptimSchedBuilder.prepare_optimization_config": "03_core.classes.ipynb",
         "OptimSchedBuilder.build_optimizer": "03_core.classes.ipynb",
         "OptimSchedBuilder.build_lr_scheduler": "03_core.classes.ipynb",
         "GaleTask": "03_core.classes.ipynb",
         "GaleTask.shared_step": "03_core.classes.ipynb",
         "GaleTask.training_step": "03_core.classes.ipynb",
         "GaleTask.validation_step": "03_core.classes.ipynb",
         "GaleTask.test_step": "03_core.classes.ipynb",
         "GaleTask.setup_optimization": "03_core.classes.ipynb",
         "GaleTask.configure_optimizers": "03_core.classes.ipynb",
         "has_pool_type": "04_classification.modelling.backbones.ipynb",
         "prepare_backbone": "04_classification.modelling.backbones.ipynb",
         "filter_weight_decay": "04_classification.modelling.backbones.ipynb",
         "ImageClassificationBackbone": "04_classification.modelling.backbones.ipynb",
         "TimmBackboneBase": "04_classification.modelling.backbones.ipynb",
         "ResNetBackbone": "04_classification.modelling.backbones.ipynb",
         "ImageClassificationHead": "04a_classification.modelling.heads.ipynb",
         "FullyConnectedHead": "04a_classification.modelling.heads.ipynb",
         "FastaiHead": "04a_classification.modelling.heads.ipynb",
         "GeneralizedImageClassifier": "04b_classification.modelling.meta_arch.common.ipynb",
         "ViT": "04b_classification.modelling.meta_arch.vit.ipynb",
         "pil_loader": "05_classification.data.common.ipynb",
         "cv2_loader": "05_classification.data.common.ipynb",
         "denormalize": "05_classification.data.common.ipynb",
         "show_image_batch": "05_classification.data.common.ipynb",
         "DatasetDict": "05_classification.data.common.ipynb",
         "ClassificationMapper": "05_classification.data.common.ipynb",
         "ClassificationDataset": "05_classification.data.common.ipynb",
         "FolderParser": "05_classification.data.common.ipynb",
         "PandasParser": "05_classification.data.common.ipynb",
         "CSVParser": "05_classification.data.common.ipynb",
         "imagenet_stats": "05a_classification.data.transforms.ipynb",
         "cifar_stats": "05a_classification.data.transforms.ipynb",
         "mnist_stats": "05a_classification.data.transforms.ipynb",
         "imagenet_no_augment_transform": "05a_classification.data.transforms.ipynb",
         "imagenet_augment_transform": "05a_classification.data.transforms.ipynb",
         "aug_transforms": "05a_classification.data.transforms.ipynb",
         "register_torchvision_dataset": "05b_classification.data.build.ipynb",
         "register_dataset_from_folders": "05b_classification.data.build.ipynb",
         "register_dataset_from_df": "05b_classification.data.build.ipynb",
         "build_classification_loader_from_config": "05b_classification.data.build.ipynb",
         "folder2df": "06_collections.pandas.ipynb",
         "split_dataframe_into_stratified_folds": "06_collections.pandas.ipynb",
         "get_dataframe_fold": "06_collections.pandas.ipynb",
         "get_dataset_labeling": "06_collections.pandas.ipynb",
         "dataframe_labels_2_int": "06_collections.pandas.ipynb",
         "split_dataframe_train_test": "06_collections.pandas.ipynb",
         "format_time": "06a_collections.callbacks.notebook.ipynb",
         "html_progress_bar": "06a_collections.callbacks.notebook.ipynb",
         "text_to_html_table": "06a_collections.callbacks.notebook.ipynb",
         "NotebookProgressBar": "06a_collections.callbacks.notebook.ipynb",
         "NotebookTrainingTracker": "06a_collections.callbacks.notebook.ipynb",
         "NotebookProgressCallback": "06a_collections.callbacks.notebook.ipynb",
         "EMACallback": "06b_collections.callbacks.ema.ipynb"}

modules = ["core/utils/logger.py",
           "core/utils/visualize.py",
           "core/utils/structures.py",
           "core/nn/utils.py",
           "core/nn/losses.py",
           "core/nn/optim/optimizers.py",
           "core/nn/optim/lr_schedulers.py",
           "core/classes.py",
           "classification/modelling/backbones.py",
           "classification/modelling/heads.py",
           "classification/modelling/meta_arch/common.py",
           "classification/modelling/meta_arch/vit.py",
           "classification/data/common.py",
           "classification/data/transforms.py",
           "classification/data/build.py",
           "collections/pandas.py",
           "collections/callbacks/notebook.py",
           "collections/callbacks/ema.py"]

doc_url = "https://benihime91.github.io/gale/"

git_url = "https://github.com/benihime91/gale/tree/master/"

def custom_doc_links(name): return None
