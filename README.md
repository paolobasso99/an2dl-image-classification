# Image Classification challange AN2DL Politecnico di Milano 2022
This is the model that I used in the [Image Classification challange](https://web.archive.org/web/20221129163804/https://codalab.lisn.upsaclay.fr/competitions/8522) of the course "Artificial Neural Networks and Deep Learning" course held at Politecnico di Milano in 2022.

The challange consisted on the classification of 8 different plant species from photos with the dimensions `(96, 96, 3)`. The model me and my team developed uses the transfer learning approach with `ConvNeXtLarge` as the base model.

Our team arrived **first** in the challange, reaching an **accuracy of 95.48**, you can check the results [here](https://codalab.lisn.upsaclay.fr/competitions/8522#results).

## Models details
For more dettails about the model check the [Report](report/Report.pdf). Briefly, we used the following techniques:
1. Transfer Learning with `ConvNeXtLarge` model
2. CutMix and MixUp data augmentation techniques
3. Standard data augmentation (flip, rotate, zoom)
4. Test-Time data augmentation (self-ensemble technique)
5. Class weighting

## Running the code
### Requirements
This project uses [Poetry](https://python-poetry.org/docs/basic-usage/) to manage dependecies, you can see how to install Poetry [here](https://python-poetry.org/docs/#installation).

### Set up
1. Download the dataset from [here](https://drive.google.com/file/d/1uaK_kzFDFelW9z4Voceb5jiX-MdR-4Fa/view?usp=share_link) and save the `zip` inside the `data` folder.
2. Create Poetry virtual environment `poetry install`
3. Activate virtual environment
