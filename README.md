

# Deep Learning for emojis with VS Code Tools for AI

Semantic representations for emoji understanding used to build a recipe prediction model see: [blog](https://blogs.technet.microsoft.com/machinelearning/2018/04/24/deep-learning-for-emojis-with-vs-code-tools-for-ai/)

## Prerequisites

The prerequisites to run this example are as follows:

1. Visual Studio Code Tools for AI is integrated with Azure Machine Learning. Make sure that you have properly installed [Azure Machine Learning Workbench] by following the [Install and create Quickstart](https://docs.microsoft.com/en-us/azure/machine-learning/preview/quickstart-installation)

2. This example could be run on any compute context. If you are running it in a remote environment it is recommended to have access to an Azure Blob Storage Account to store intermediary files. See how to create and manage your storage account [here](https://docs.microsoft.com/en-us/azure/storage/common/storage-create-storage-account?toc=%2fazure%2fstorage%2fblobs%2ftoc.json)

## Create a new project

1. Clone this repo to your local machine to /Emoji2recipe
2. Open the project with Visual Studio Code. You should have access to the VS Code tools for AI if you have successfully installed Azure Machine Learning Workbench.(See instructions above)

## Setup compute environment (Optional)

### Setup remote VM as execution target
```
az ml computetarget attach --name "my_dsvm" --address "my_dsvm_ip_address" --username "my_name" --password "my_password" --type remotedocker
```
### Configure my_dsvm.compute
```
baseDockerImage: microsoft/mmlspark:plus-gpu-0.7.91
nvidiaDocker: true
```
### Configure my_dsvm.runconfig
To push models to Azure Blob Storage, add your storage account details to your .runconfig file:

```
EnvironmentVariables:
  "STORAGE_ACCOUNT_NAME": "<YOUR_AZURE_STORAGE_ACCOUNT_NAME>"
  "STORAGE_ACCOUNT_KEY": "<YOUR_AZURE_STORAGE_ACCOUNT_KEY>"
Framework: Python
```

For more info on Azure ML Workbench compute targets see [documentation](https://docs.microsoft.com/en-us/azure/machine-learning/preview/how-to-create-dsvm-hdi).

### Prepare compute environment

```
az ml experiment -c prepare my_dsvm
```

## Download data and embeddings
Download the [word2vec](https://code.google.com/archive/p/word2vec/) embeddings and [emoji2vec](https://github.com/uclmr/emoji2vec) embeddings and update respective paths in config.py.

## Preprocess data and build your own model

```
az ml experiment submit -c local Emoji2recipe/preprocess.py
```

## Predict recipes

```
az ml experiment submit -c local Emoji2recipe/score.py
```
## Get cooking!

The result generated in the previous step will show you a recipe with the title and instructions!

# Credits

The dataset used for the experiments is available [here](https://eightportions.com/datasets/Recipes/). Special thanks to Ryan Lee for curating this and making this available.

Special thanks to Ben Eisner, Tim Rocktaschel and the team from UCL for making the pre-trained emoji embeddings available.

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
