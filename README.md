# color-caddie
Helps you read the field and select your tools, but in a coloring context.

## Dependencies

Most dependencies should be resolved using the virtualenv guide below. Some
requirements need to be installed manually.

 * python, only Py 3.6+ tested.
 * virtualenv and pip
 * The dependencies for tesserocr, see https://pypi.org/project/tesserocr/

Depending on the download location for your tessdata, you may need to specify
it when testing. I.e. `TESSDATA_PREFIX="$HOME/work/" nose2`

## Quick virtualenv guide

#### Initial creation
`$ virtualenv venv_caddie`


#### Install requirements listed in requirements.txt
`$ pip install -r requirements.txt`


#### Activate the venv
`$ source venv_caddie/bin/activate`

#### Save changed requirements to requirements.txt
`$ pip freeze > requirements.txt`
