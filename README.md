[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/3e23_jye)

# Introduction
## What is the Grocery Deal Finder?

Students often struggle to find the best place to buy their groceries. The Grocery Deal Finder (GDF) solves that by comparing prices across websites of different stores while also looking for special deals. It uses Selenium and Flask in combination with React to create a website that aggregates special deals from Aldi and County Market.

# Technical Architecture

![image](https://github.com/CS222-UIUC-SP24/group-project-team-27/assets/60373662/886346f7-f399-41ac-b7bd-8d5607f940ae)

## Frontend

The frontend uses React to connect to the backend scrapers and display it on the website.

## Backend

The backend API is hosted using Flask on a local server. The scraping is done using Selenium and Python, allowing the data to be jsonifyed into an endpoint for the frontend to use.

# Installation
Create a repository on your local machine and pull from main.

Make sure the npm package is installed. If it's not installed, install it using a package manager like [Homebrew](https://brew.sh/) or [Pip](https://pypi.org/project/pip/)

In this repository, run
```npm init```,

then

```npm install```,

and finally

```npm start```.

This should start and run the website.


# Developers

* Sunny Lee - Worked on frontend creation and integration with the backend.
* Ryan Kowalski - Worked on frontend creation and integration with the backend.
* Alex Yang - Worked on the creation of the API and the backend server. Also worked on the County Market scraper.
* Aditya Kshirsagar - Worked on the Aldi Selenium scraper and endpoints.


