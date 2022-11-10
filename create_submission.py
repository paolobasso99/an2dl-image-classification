import os
from distutils.dir_util import copy_tree
from shutil import make_archive, rmtree

import typer
from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn


def main():
    # Check folders
    if not os.path.isdir('models'):
        print("The models path does not exists")
        raise typer.Exit(code=1)
    if not os.path.isdir('submission'):
        os.mkdir('submission')
    if not os.path.isdir('submissions_archives'):
        os.mkdir('submissions_archives')
    if not os.path.isfile('submission/metadata'):
        open('submission/metadata', 'a').close()
    if not os.path.isfile('submission/model.py'):
        print("The model.py file inside the submission folder does not exists path does not exists")
        raise typer.Exit(code=1)

    if os.path.isdir('submission/saved_model'):
        rmtree('submission/saved_model')
    os.mkdir('submission/saved_model')
    
    models = os.listdir('models')
    if len(models) == 0:
        print("There are no models inside the models folder")
        raise typer.Exit(code=1)

    print('The following models are aviable:')
    for i, m in enumerate(models):
        print(i, m)

    model_i = typer.prompt("Which models do you want to use?")
    try:
        model_i = int(model_i)
        model = models[model_i]
    except:
        print("Your election was invalid")
        raise typer.Exit(code=1)

    print('You selected the model ' + model)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        TimeElapsedColumn(),
    ) as progress:
        progress.add_task(description="Copying model to the destination...", total=None)
        copy_tree("models/"+model, "submission/saved_model")

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        TimeElapsedColumn(),
    ) as progress:
        progress.add_task(description="Zipping the submission...", total=None)
        make_archive('submissions_archives/'+model, 'zip', 'submission')

    print('Done!')



if __name__ == "__main__":
    typer.run(main)
