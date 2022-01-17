# Judgments service front end

Use this contents list to navigate the page.

* [Introduction](#introduction)
* [Versioning](#versioning)
* [HTML for judgment text page](#html-for-judgment-text-page)
* [Development approach](#development-approach)
* [Local development setup](#local-development)
* User flow and wireframe iterations
    * [1.8](#iteration-18)
    * [1.7](#iteration-17)
    * [1.6](#iteration-16)
    * [1.5](#iteration-15)
    * [1.4](#iteration-14)
    * [1.3](#iteration-13)
    * [1.2](#iteration-12)
    * [1.1](#iteration-11)
    * [1.0](#iteration-10)
   

## Introduction

This repository:

* Documents iterations of the user flow and wireframes
* Has the code for a Python [Flask](https://flask.palletsprojects.com/en/2.0.x/git) application that includes current versions of HTML and CSS for the user interface. This includes the search application and an example HTML page for a judgment

## Versioning 

Iterations of the flow will are described under headings in this `README.md`. For each there is an explanation of how and why it differs from its predecessor. Each flow iteration is also available as a PDF and as an XML version that can be opened for editing on [app.diagrams.net](https://app.diagrams.net). Where available, wireframes in `.png` are also provided.

All of the relevant information can be found under the corresponding heading. 

The Flask application and front end code will be versioned using Git only.

## HTML for judgment text page

This Flask application in this repository includes a sample HTML page for a judgment with accompanying CSS. This implementation seeks to retain the desired layout while also being inclusive and making the most of what the Web has to offer. Relevant decisions and considerations are described on the [corresponding Wiki page](https://github.com/nationalarchives/ds-judgments-frontend/wiki/Recommendations-for-Judgment-text-HTML-and-CSS)

![Representation of the judgment text page rendered in a browser](/repo_images/judgment_text.png)

## Development approach

The Flask application has been developed following [The National Archives front end development guide](https://github.com/nationalarchives/front-end-development-guide) and process for the [practical application of progressive enhancement](https://github.com/nationalarchives/front-end-development-guide)

## Local development

### What this repository provides

Included in this repository is: 

* Webpack for transpiling JavaScript
* Sass for compiling CSS

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

In a _new terminal_ run these commands:

* `npm install -g sass` will install Sass as a global dependency
* `npm start` will kick off a Sass watch task

_If you are working on JavaScript_, you should also run (in another new terminal):

* `npm run start-scripts` will kick off a Webpack watch task

## Iteration 1.8

This iteration updates [the flow](user_flows/Iterations/1.8) to reflect the need for the supplier / source / provenance of the judgments included in the system.

## Iteration 1.7

This iteration updates [the flow](user_flows/Iterations/1.7) to account for users who have landed on a Judgment text page from an external search engine or web link. It shows that users can access the home page and structured search directly from the judgment text page.

Feedback to this iteration has been captured in [a Wiki page](https://github.com/nationalarchives/ds-judgments-frontend/wiki/Feedback-to-Iteration-1.7-and-design)

## Iteration 1.6 

This iteration updates [the flow](user_flows/Iterations/1.6) to allow users who have ended up on either a disambiguation page or no results page as a results of a neutral citation not having been found to expand their search to the full judgment text. It also removes the option to set sorting within the structured search form and renames the container to 'Structured search form'.

## Iteration 1.5

This iteration updates [the flow](user_flows/Iterations/1.5) to reflect that users entering a search term that matches the pattern for a neutral citation will be presented with a results page, rather than going direct to the matching judgment. The rationale for this decision is that: 

* We anticipate that maintaining consistency between search 'types' will help orientate the user
* Presenting a search result will help assure that the right result has been retrieved
* Where an issue has occurred (for example, the neutral citation has yielded an unexpected result - for example as a result of a typo) the user will have the necessary tools on the page to change direction

## Iteration 1.4

This version: 

* Updates [the flow](user_flows/Iterations/1.4) to
    * merge the two search fields on the home page
    * show the individual judgments can be reached directly from the home page
    * merges the 'courts' and 'collections' fields to be 'courts' (this may need to change at a later date but the numbers are so small that the separation seems redundant)
* Introduces the [version 0.2](wireframes/v0.2) of the wireframes, including: 
    * an updated service homepage (with the two search fields combined)
    * search page
    * a search results page
   
## Iteration 1.3

This version Introduces initial proposals for

1. the [home page design](wireframes/1%20-%20service_homepage%20-%20v0.1.png) 
2. the search page that allows users to provide a more detailed query up front. 

### Using a HTML date input

On the search page we have used the native HTML date input given it has:

* broad support (with the exception of IE) and degrades gracefully to a text field
* will present users with controls appropriate to their browsing context
* it allows us to set minimum and maximum values (which correspond to the available dates)

We recommend that the production implementation of date inputs should use either the `pattern` attribute, server-side validation and/or object detection to support user input (a bit of thought will be necessary to identify the best combination of these). 
    
We also think that the three text box pattern for dates within the GOV.UK design system feels less appropriate in the context of a set of filters than it does in a form. 

### Flow updates

* Brings the browse functionality into the home page
* Updates the advanced search flow to reflect the possibility of no results

### Recent judgments display

* Variable content length suggests a single column layout is more app

Questions: 
* How often are new judgments made 
* How much of a problem is it if people miss a recent judgment?

## Iteration 1.2 

Iteration [1.2](user_flows/Iterations/1.2/1.2.drawio.pdf) is updated to include:

* A disambiguation page where the neutral citation does not have an exact match
* A no results page (that will serve for both search results and neutral citation results)

## Iteration 1.1

Iteration [1.1](user_flows/Iterations/1.1/1.1.drawio.pdf) is updated to reflect advice (from SB) that there will a Terms of Use page _and_ an Open Justice License page. 

## Iteration 1.0 

The team have confirmed that iteration [1.0](user_flows/Iterations/1.0/1.0.drawio.pdf) represents the known scope of the service and is an acceptable starting point for the development of prototypes and wireframes.
