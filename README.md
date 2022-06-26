# Production Engineering - Portfolio Site

A portfolio website that that displays everything from my projects to interests! Utilizes PE concepts including (bash) scripting, databases, and services.

View the website here: http://vifolio.duckdns.org:5000/

## Technologies Used & Concepts Implemented
#### Frontend #### 
-  HTML & CSS
#### Backend ####
- Python Flask, Jinja
- MySQL Database 
- API routes for "Timeline Posts"

#### Production ####
- Auto-Deployed on VPS with Bash Script
- Configured a Systemd Service to run the application


## Running Locally

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
