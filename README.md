# Judgments service front end

Use this contents list to navigate the page.

* [Introduction](#introduction)
* [Versioning](#versioning)
* [Development approach](#development-approach)
* [Local development setup](#local-development)
* User flow iterations
    * [1.0](#iteration-10)

## Introduction

This repository:

* Documents iterations of the user flow
* Has the code for a Python [Flask](https://flask.palletsprojects.com/en/2.0.x/git) application that includes current versions of HTML and CSS for the user interface

## Versioning 

Iterations of the flow will be described in this `README.md` file with an explanation of how and why it differs from its predecessor. Each flow iteration will also be available as a PDF and as an XML version that can be opened for editing on [app.diagrams.net](https://app.diagrams.net). 

All of the relevant information can be found under the corresponding heading. 

The Flask application and front end code will be versioned using Git only.

## Development approach

The Flask application has been developed following [The National Archives front end development guide](https://github.com/nationalarchives/front-end-development-guide) and process for the [practical application of progressive enhancement](https://github.com/nationalarchives/front-end-development-guide)

## Local development

### What this repository provides

Included in this repository is: 

* GulpJS for compiling SASS and transpiling JavaScript

### Development machine configuration

Use these steps to get up and running

1. Ensure you have _at least_ Python 3.7 and pip installed
2. Clone this repository
3. Create a virtual environment with `python3 -m venv venv`
4. From the root directory run `source venv/bin/activate` 
5. Install dependencies with `pip install -r requirements.txt`
6. Start the application with `flask run`
7. See the command line for the URL to visit
8. When finished run `deactivate` from the virtual environment

For front end assets:

In a _new terminal_ run these commands

9. Install Gulp CLI globally with `npm install --global gulp-cli` (Note: you only need to do this once)
10. Install Node dependencies with `npm install`
11. Start Gulp (a run-through of tasks followed by a watch) with `npm start`

## Iteration 1.0 

The team have confirmed that iteration [1.0](user_flows/Iterations/1.0/1.0.drawio.pdf) represents the known scope of the service and is an acceptable starting point for the development of prototypes and wireframes.