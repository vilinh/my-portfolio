# Production Engineering - Portfolio Site

A portfolio website that has sections to display basic information, experiences, education, hobbies, and contact info.

View the website here: http://vifolio.duckdns.org:5000/

## Visuals
<img width="500" alt="Screen Shot 2022-06-17 at 9 49 08 AM" src="https://user-images.githubusercontent.com/81380688/174342044-d68c9d20-bc5b-4f02-8d34-d9c0841e23a9.png">
<img width="500" alt="Screen Shot 2022-06-17 at 9 50 03 AM" src="https://user-images.githubusercontent.com/81380688/174342160-7a73dbc7-f7ad-4e49-9dfd-cc8e259e6e1d.png">

## Technologies Used
- HTML & CSS for the frontend
- Python, Flask, & Jinja to make use of reusable templates and route to different URLs

## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
