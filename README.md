[![Build Status](https://travis-ci.org/aledgriffiths79/cambrian_whiskey.svg?branch=master)](https://travis-ci.org/aledgriffiths79/cambrian_whiskey)


# Cambrian Whiskey
-----------------

### Milestone Project 4: Django Ecommerce

In this project, I will build a full-stack site where the consumer can buy an item/items. In this case, it will be selling high-end whiskey from my base in the Cambrian Mountains of Mid Wales. It's purpose is to provide a website where you can buy top brand whiskey of all brands from one website rather than going to each brand website. It's making the consumers life easier by staying on one website rather than scanning multiple websites.

I will focus on building this application to be visually appealing and user friendly. It will be simple to navigate and understand with features for users to locate specific items, to navigate through to paying for the item/items and the paying process will be secure and efficient using the stripe software.

This project can be viewed [here](https://cambrian-whiskey.herokuapp.com/)

## User Experience Design
--------------------------

### Scope Plane:

  - What they say they need?

    I want to share with consumers, the top-end whiskey that is available out there in one place so that they the consumer can have a place to come too and find what they may'be looking for or find something that they were'nt initially looking for. The website is to feature images of the whiskey and a description of it's origin, and its distinct flavours

  - What they actually need?

    A intuitive website thats easy to navigate around and to minimise the required steps to complete tasks. It will provide you with all the whiskey that's on offer, and you can look to see if there is a specific whiskey you want by using the search function. Also there will be a cart for if you want to buy an item, a shopping basket to provide list of what you have in the cart and a checkout to complete the process.

    There will be a page describing the origins of the company in the About page and a Contact page for any questions the consumer may have.

  - What they don't know they need?

    For it not to be complex in design. A good website is a simple functional website thats intuitive. A mixture of appealing images and short but descriptive content. I will also need to consider for the future to what constraints does the app have to perform within (scalability) i.e as your user base grows can your app handle the growth in traffic.

### Structure Plane:

The website will present you the user with a intuitive and structured format starting with the navigation. It will be clear and simple, displayed in a horizontal fashion on desktop, thus, it being a predictable structure. I will also display a hamburger navigation for mobile use. Color theme on all pages will be the same to make it consistent. 

I will structure the home page so that images will use up half the real estate, as i find an appealing image more satisfying to the eye than a lot of content, however i will leave some space to describe the origins and flavours of the item as well as the price. Underneath the price will be a container with the quantity option to how much of the specified item you want.

Once specified what items you want i will provide a cart page displaying the item in question and a summary of the overall cost of the itm/items.

From there you will be taken to the checkout page where you will provide your home address and card details. 

There will also be a About page and a Contact Us page. 

My intention is to allow users to:

  - Have a clear description of the item in question
  - A self explantory map of the website to all the features that you have in your disposal

Allow me as the developer to:

  - Accomodate growth and change in the application

### Skeleton Plane

This particular plane focuses on:

  - Navigation design
  - Interface design

In this projects directory is a folder **wireframe**. In that folder i have designed a mockup of my inital plan for the project. I have designed it so that i have the flexibility if needed to alter something, whether it be the functionality, the color scheme, fonts etc as i progress through the project. Its not good practice to set anything in stone from the start but important to have an idea of the structure of the application.

Here is my wireframe with ideas to building this project
  + [Wireframe](wireframe.pdf)
  

## Features

The project has multiple pages that provide different features and options.
  + **homepage** is the base of the project and provides the following features: navigation bar, a image/description/price, and option to buy feature. At the bottom is the footers section.

  + **About** Gives you a description of the history of the company

  + **Contact Us** For customers to get in touch for any enquiries

  + **Search bar** for customers to search for a particular item

  + **Login/Registration** If a customer has not registered, in order to buy an item they must, therefore i provide a registration page to fill. If you have a registered you are also provided woth a login page

  + **cart** A cart for when you add an item to be purchased. It provides you with the description of the item and a summary

  + **Checkout** For a customer to finalise the order through providing your delivery address and payment

### Features Left to Implement

  + In the future i may add a feature where you can buy an item without having to register.

## Technologies Used

  + Python
    + Python is used for the back-end functionality of this project
  + Javascript
    + Javascript was used for the functionality of the hamburger (navigation) bar
  + HTML5
    + Used to construct the structure of the front-end of the project
  + CSS/Bootstrap
    + Provides styling for the pages and all content
    + Bootstrap is a modern responsive CSS framework
  + Django
    + Django was used for the backend of the project, for the functionality of the contact/registration forms, models/views files, login details and for the front end templates architectural pattern.
  + Heroku
    + Heroku is a container-based cloud Platform. I used Heroku to deploy, manage, and scale this application/project. The platform is a simple path to getting the application to production.
  + AWS S3
    + I used Amazons Web Services (AWS) S3. It's use is to store data in a cloud. In developing the project i used db.sqlite to store data but for production i used AWS S3. AWS S3 is effectively a NoSQL database but it can store very large Key-Value pairs and has low costs and simple setup

## Testing

I have tested the application manually on the basis of going over my UX section and ensure they all work as intended with the project providing an easy and straightforward way for the users to achieve their goals.

All the pages have been tested by going from one page to the other and seeing if it loads correctly. The search box was a feature i made sure worked properly. I typed a small part from a title for a whiskey in the application and see if it loads the whiskeys that match those specific words, i also tried some incorrect words. It worked as intended.

I tested the forms on both the Registration and Contact Us pages, and that the data is passed to my administration panel and that it was saved. From that, i would test that i could Login in the login.html page. I tried logging in with correct username but incorrect password and vice versa. Also i intentionally filled the user input details in the registration form, for example, an email address without @ and a different password to the password confirmation. 

I added an item i wanted to purchase and went through the process of buying it, in multiple scenarios, like adding an item on 4 different whiskeys and going from the cart page to the checkout and testing the Stripe software. I also tried buying an item without logging in which you can't which is what i wanted. 

I concentrated on producing a intuitative project where logic and functionality is at its core. I kept my design to be usable and simple to navigate with readable font faces and breathable spacing (i.e. negative space).

As the site is built with a responsive design it works for mobiles, ipad and desktop. I used the development tools on google to make sure the different size devices scalability worked.



## Deployment

My application was coded in the IDE: **Virtual Studio Code**, a local GIT directory was used for version control and then uploaded to GITHUB.
This site is hosted using Heroku and is deployed directly from the master branch. The deployed site will update automatically upon new commits to the master branch.

In order for the success of the deployment version, i would create an environment variable file in my applications repository named env.py. In this file i will store the AWS S3 and Stripe configuration key and values in order to keep the production database connection string private. AWS S3 database was used as the place to store data for this application. I also need to store these configuration variables in my **config vars** in my heroku settings which acts like a security confirmation in accordance with the values i have set in my env.py file. As these variables and its values are confidential they must not be seen by the public, therefore, i have created a file called .gitignore. In this file will be a list of files that i have within the applications repository that i dont want to share to github/public. And one of those files and its data is the environment variable file, **env.py**. 

In the development phase of my application it was important to keep the security of my configuration variables private, because even though my application wasnt in deployment at that stage, in order to work on the development stage i still had to upload my code to github for the changes in my application to take place. 

Hosting the development version was used using the url local host **127.0.0.1:5000/**. This is issued in your local command terminal after inputting **python3 manage.py** in the command terminal. When you make new features/functions in your IDE you refresh your development version browser and the changes will be seen live. However to make a permanent change to an updated file you then will have to use git in your command terminal to make those changes which then will be stored in your GITHUB repository.

With Heroku an updated application will be uploaded automatically once you update your github repository as Heroku uses your chosen **deployment method** i.e. Github and **master branch** as every push to master will deploy a new version of the app. 

## Credits

### Content

  + I used code from the django documentation for a lot of the methods and the general syntax in development of the application. I also used stackoverflow, w3 school, Bootstrap, Mdn Web Docs, youtube for pagination, search queries, navigation and other app functionalties. As well as the assistance of the sites mentioned i also had advice by some of the tutors for how to look up for solutions to problems.

### Media

  + I added images from various sites through google engine. I'd input in the search box, **valuable whiskey**, **expensive whiskey** etc and copy the image of the various whiskey images displayed

### Acknowledgements

  + I received some structure ideas from the [The Whiskey Exchange](https://www.thewhiskyexchange.com/) and [Glenfiddich](https://www.glenfiddich.com/uk/)

  + My **Mentor** for his guidance at the beginning, middle and end of the project

  + And to the **Tutors** at [Code Institute](https://codeinstitute.net/) 



  

