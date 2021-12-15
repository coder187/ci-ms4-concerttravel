![Home Page](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/amiresp.png)

![Events Page](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/ami_resp_2.png)

![Detail Page](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/ami_resp_3.png)

# Concert Travel Django CI MS4 App
[Link to live site](https://ci-ms4-concerttravel.herokuapp.com/)

Project - Full Stack Frameworks With Django - Code Institute

## User Experience (UX)
### Scope
#### User stories

| User Story | As A       | I wan to be able to                                                                | So that I can                                                                   |                                                                                                      
|------------|------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| 1          | Site User  | Easily view prices for travel to concerts and events                               | Make an informed decision on whether to purchase or not                         | 
| 2          | Site User  | [Qucikly retrieve contact information for the buisness operator](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/us/contact.png)        | Verify the business  details   |                                          
| 3          | Site User  | Easily send a message to the buisness via the site                                 | Easily make contact or request more inforation                                  |  
| 4          | Site User  | [Easily view which events are more popular](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/us/pop.png)                                          | Purchase tickets before they are still in stock.                                |  
| 5          | Shopper    | [Easily view the total in my shopping bag at any given time](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/us/bag.png)                        | Avoid over spending                                                            | 
| 6          | Site User  | [Easily create an account](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/us/reg.png)                                                           | Be able to view my purchase history and store my billing details for next visit | 
| 7          | Site User  | [Easily login or out](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/us/signInPasswordReset.png)                                                                | I can view and edit my personal information                                     |  
| 8          | Site User  | Easily reset my password                                                           | I can recover my account                                                        |  
| 9          | Site User  | Receive email cofirmation after registering                                        | Verify successful account registration                                          |  
| 10         | Site User  | [Have a personalised user profile](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/us/orderhist.png)                                                    | View my order history, personal informaton and save  my payment information     | 
| 11         | Shopper    | [Sort list of events by Date, Venue and Artist name](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/us/sort.png)                                 | Easily find the events I am most interested in                                    
| 12         | Shopper    | View multiple Venues for the given City                                            | I can view events in that location                                              |  |
| 13         | Shopper    | [Search for an Event by Artist name or Event description](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/us/search2.png)                            | Find a specific event                                                             |
| 14         | Shopper    | [Easily see what I have searched for and total results](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/us/resultcount.png)                              | Quickly decide whether the Event is available.                                  |  
| 15         | Shopper    | Easily select the number of seats for a given Event when purchasing                | Ensure I don’t select the incorrect Event or quantity                           |  |
| 16         | Shopper    | View contents of my shopping bag                                                   | See the total cost of my order and all items selected                           | |
| 17         | Shopper    | [Adjust the quantity of individual items in my bag](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/us/adjustbag.png)                                  | Easily make changes to my purchase before checkout                              | 
| 18         | Shopper    | [Easily enter my payment informaion](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/us/completeorder.png)                                                 | Easy, quick and hassle free checkout                                            |  
| 19         | Shopper    | Feel my personal information is safe and secure                                    | Confidently provide the needed information to make a checkout                   | |
| 20         | Admin User | [Easily add and edit Events](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/us/addevent.png)                                                         | Update the app with new information                                             | 
| 21         | Admin User | [Easily update an Event so that it is no longer accessiable to shoppers to purchase](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/us/pub3.png) | Prevent over selling available seats.                                           |  
| 22         | Admin User | [Easily edit Pick Up Locations](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/us/addeditpicklocs.png)                                                      | Add new locations as required                                                   |  
| 23         | Admin User | Easily update the price per location                                               | Control fares charged                                                           |  |
## Structure
### Technical Capabilities
HTML5, CCS3, Javascript, Python, Django, SQLITE, Postgres along with Bootstrap framework and are my core strengths in regards to this project.

### Features
  * Responsive on all devices.
  * Individual User Profiles.
  * Admin User can add/delete Events.
  * Admin User can hide individual Events.
  * Admin User can add/delete and Pickup Location (Times, Ticket Price).
  * Users can view the site and purchase tickets anonmously.
  * Users can create a profile and maintain there contact details & view purchase histroy.
  * Users can reset their account password.
  * Users can search the site using the search bar.
  * Users can view events by Artist, Venue & Event Date.
  * Users can also view events by Category (Music, Festivals, Shopping & Family Attractions), Venue & Location (Dublin, Cork).
  * Users can set the order of search results by Artist Name, Date & Venue
  * Events page indicates which events are selling more than the average.
  

### Features Left To Implement In Future
  * Ability create tickets on the fly and attach to confirmation email.
  * Ability for profile users to cancel or amend booked journeys.
  * Admin users should be able to view at a glance completed Orders for a given Event.
  * Api integration to pull Artist, Venue & Event Ticketing details.
  * Mapping tools to help users navigate the various venues.
  * More social share options to allow users share events with family and friends
  * Group Travel option to allow a user organise a private group for travel by allowing non admin users create their own events.
  * Allow users add passenger information to each ticket.
  
  
### Data Model
Initial Data Model Prototype
![Initial Data Model Prototype](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/db_relationships.png)

Final Database Schema.
![Initial Data Model Prototype](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/db_relationships.png)

**Events**  
List of concerts, sporting, shopping trips and day trips.  

| Table           | Events    |                                        |
|-----------------|-----------|----------------------------------------|
| Field           | Type      | Desc                                   |
|     event_type  | int       | Sporting / Concert / Festival          |
|     event_dest  | int       | Venue                                  |
|     name        | char      | Artist or Group name                   |
|     description | char      | Desc of service                        |
|     event_date  | date      | Date of event                          |
|     publish     | bool      | Allow users to view                    |
|     long_desc   | long text | Description of the Artist and or Event |
|     image_url   | char      | path to image                          |
|     image       | image     | uploaded image                         |

**Event Type**
List of Event Types.
| Table           | Event Type |               |
|-----------------|------------|---------------|
| Field           | Type       | Desc          |
| event_type  | char       | Type of Event |
| friendly_name   | char       | Friendly Name | 

**Destination**
List of Venues
| Table           | Destination |               |
|-----------------|------------|---------------|
| Field           | Type       | Desc          |
|     destination  | char       |Venue |
| friendly_name   | char       | Friendly Name |

**PickLoc**
List of Pick up locations and price per location
| Table     | PickLoc |                  |
|-----------|---------|------------------|
| Field     | Type    | Desc             |
| Location  | char    | Pick Up Location |
| pick_time | char    | Time             |
| sort      | int     | Sort Order       |
| fare      | double  | Price            |

**Order**
Processed Orders.
| Table             | Order  |                                 |
|-------------------|--------|---------------------------------|
| Field             | Type   | Desc                            |
| order_number      | char   | autogenerated guid              |
| full_name         | char   | shopper name                    |
| email             | char   | shopper email                   |
| phone_number      | char   |                                 |
| country           | char   |                                 |
| postcode          | char   |                                 |
| town_or_city      | char   |                                 |
| street_address1   | char   |                                 |
|  street_address2  | char   |                                 |
| county            | char   |                                 |
| date              | date   | order date                      |
| order_total       | double |                                 |
| original_bag      | char   | bag contents at time of sale    |
| stripe_pid        | char   | strip unique id for transaction |
| user_profile      | int    | foreign key to Profile          |
| discount          | double |                                 |
| grand total       | double | Order Total                     |

**OrderLineItem**
Order details including ticket no, event and pickup location.
| Table        | OrderLineitem   |                          |
|--------------|-----------------|--------------------------|
| Field        | Type            | Desc                     |
| ticket_no    | int primay key  | ticket no. autogenerated |
| order        | int             | foreign key to Order     |
| event        | int             | foreign key to Event     |
| pickloc      | int             | foreign key to Pickloc   |
| price        | double          | price per ticker         |
| pax_fullname | char            | ticket info              |
| pax_email    | char            | ticket info              |
| pax_tel      | char            | ticket info              |

**Profile**
Extended User information store for created user accounts.
| Table                                       | OrderLineitem                |                           |
|---------------------------------------------|------------------------------|---------------------------|
| Field                                       | Type                         | Desc                      |
| user                                        | one to one with account User |                           |
| default_phone_number                        |                              | Profile Data For App User |
| default_street_address1                     |                              |                           |
| efault_street_address2                      |                              |                           |
| default_town_or_city                        |                              |                           |
| default_count                               |                              |                           |
| default_postcode                            |                              |                           |
| default_countr                              |                              |                           |


## Skeleton

### Wireframes
  * Desktop
    * [Home](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/wireframes/desktop/home.png)
    * [Event List](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/wireframes/desktop/event_list.png)
    * [Event Detail](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/wireframes/desktop/eventDetail.png)
    * [Adjust Bag](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/wireframes/desktop/adjust_cart.png)
    * [Checkout](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/wireframes/desktop/checkout.png)
    * [Checkout Success](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/wireframes/desktop/checkout_success.png)

  * Tablet
    * [Home](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/wireframes/tablet/home_tablet.png)
    * [Event List](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/wireframes/tablet/events_tablet.png)
    * [Adjust Bag](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/wireframes/tablet/shopping_bag_tablet.png)
    * [Checkout](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/wireframes/tablet/checkout_tablet.png)

* Mobile
    * [Home](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/wireframes/mobile/home.png)
    * [Event List](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/wireframes/mobile/events_list.png)
    * [Adjust Bag](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/wireframes/mobile/bag_page.png)
    * [Checkout](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/wireframes/mobile/checkout_summary.png)
    * [Checkout](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/wireframes/mobile/checkout_form.png)
    * [Checkout Success](https://raw.githubusercontent.com/coder187/ci-ms4-concerttravel/main/support/wireframes/mobile/checkout_success.png)

## Surface

### Design
  * Colour Scheme	
    I chose black/green/yellow combinations as this matches well with the exisitng concert-travel business logo.
  * Typography
    Lato and Sora google fonts. Sora stood out as a good poster type font which suits the sites style of concert posters.
   * Imagery
    Hero images taken from google images of various scenes of crowds of people at concerts with translucent hints of blue, purle and yellow.
    Imaged fot event cards are comprised of Event/Artist promotional media combined with the site concer-travel main "peace" logo with yellow green concert scene.
  
## Technologies
#### Languages Used
  * HTML5
  * CSS3
  * Javascript
  * Python 
  * Django
  * SQLITE
  * Postgres 
  * Heroku
  * Stripe  
  * Amazon Web Services 
  

#### Frameworks, Libraries & Programs Used
1. [HTML5](https://www.w3.org/)
1. [CSS3](https://www.w3.org/Style/CSS/Overview.en.html)
1. [Javascript](https://www.javascript.com/) 
1. [Bootstrap:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Django:](https://www.djangoproject.com/)
    - Python web framework.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Prompt' font into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery is a fast, small, and feature-rich JavaScript library.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [GIMP:](https://www.gimp.org/)
    - GIMP 2 was used to resizing & edit images for the website.
1. [GITPOD:](https://gitpod.io/)
    - GitPod was used to create & debug the html,css, javascript & Python
1. [Google Chrome Dev tools](https://developers.google.com/web/tools/chrome-devtools) 
    - for debugging.
1. [Microsoft Edge](https://www.microsoft.com/en-us/edge) 
    - Dev Tools for testing and debugging.
1. [JShint](https://jshint.com/) 
    - to analyse Javascript code.
1. [SEO CHECKUP](https://seositecheckup.com/)  
    - verify alt tags.
1. [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) 
    - for debugging.
1. [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) 
    - for performance audit.
1. [W3C Markup Validation Service](https://validator.w3.org/)
1. [W3C Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/)
1. [Code Institute Course Material](https://codeinstitute.net/)
1. [w3schools](https://www.w3schools.com/) 
    - help with HTML, CSS & Javascript
1. [Stackoverflow](https://stackoverflow.com/) 
    - help with HTML, CSS & Javascript
1. [Slack](https://slack.com/intl/en-ie/) 
    - communication hub with mentor, tutors and fellow students.
1. [Markdown Guide](https://www.markdownguide.org/basic-syntax/) 
    - Markdown Guide for this readme file.
1. [Am I Responsive](http://ami.responsivedesign.is/) 
    - Screen Grab of site on various devices.
1. [Temp Mail](https://temp-mail.org/en/) 
    - Generate temporary emails accouts for testing


## Testing
[Link to Testing.md file](https://github.com/coder187/ci-ms4-concerttravel/blob/main/testing.md)


                          
## Deployment
### Deploy Locally via GIT
1. On GitHub, navigate to the main page of the repository [https://github.com/coder187/ci-ms4-concerttravel/](https://github.com/coder187/ci-ms4-concerttravel/)
2. Above the list of files, click Code.
![](https://docs.github.com/assets/images/help/repository/code-button.png)
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link text or click the icon to right. 
To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, 
click **Use SSH**, then copy the link or click the icon.
To clone a repository using GitHub CLI, click **Use GitHub CLI**, then copy the link text.
![](https://docs.github.com/assets/images/help/repository/https-url-clone.png)
![](https://docs.github.com/assets/images/help/repository/https-url-clone-cli.png)
4. Open Git Bash (or command prompt on Windows. Note you will need [GIT](https://git-scm.com/download/win) for Windows
5. Change the current working directory to the location where you want the cloned directory.
6. Type ```git clone``` and then paste the URL you copied earlier.\
```$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY```
7. Press **Enter** to create your local clone.

### Heroku
1. Add requrirements.txt file to project with "pip3 freeze > requiremnets.txt"
1. Add Procfile to project.
1. Push changes to github
1. On HEROKU.com, navigate to the site's repository @ [https://github.com/coder187/ci-ms4-concerttravel/](https://github.com/coder187/ci-ms4-concerttravel/)
1. New App
1. Name must be unique.
1. Select Region
1. Heroku / Resource / Add Resource
1. Provision New Postgres database
1. Add connection string to environment variables
1. Deploy - GitHub Connect
1. Select  [https://github.com/coder187/ci-ms4-concerttravel/](https://github.com/coder187/ci-ms4-concerttravel/)
1. Connect App
1. Build App.
1. Settings / Reveal Config Vars
1. Select Open App button from Heroku dashboard.


### Deploy Locally via zip file download
1. On GitHub, navigate to the main page of the repository @ [https://github.com/coder187/ci-ms4-concerttravel/](https://github.com/coder187/ci-ms4-concerttravel/)
2. Above the list of files, click Code.
![](https://docs.github.com/assets/images/help/repository/code-button.png)
3. Click **Download Zip**
4. Extract the downloaded file to the location where you want the cloned directory.


## Credits
1. Date picker on Edit Event has date format mm/dd/yy
1. Save retrieve User Name to/from user accounts


## Credits
### Code
  * Jonathan Kelly for Code Institute Milestone Project Four.
  * Code Institute Courseware
  * [Stackoverflow](https://stackoverflow.com/) for help with debugging css, javascript python and django. 
  * [Django Docs](https://docs.djangoproject.com/en/4.0/) to learn jinja templating and routing.
  * This project takes inspiration from the Boutique Ado walkthrough project.

### Media
  * Hero image is from [Pexels](https://www.pexels.com/) for home app hero images.
  * Event images were taken from the 3Arena website [3Arena](https://3arena.ie/).
  * No-Image image from [iStockPhoto.com](https://www.istockphoto.com/).

  
## Data Licensing\Terms of Use
-   This is a fictional application and does not represent a real world business

## User Accounts
* Admin User 
    * user:superuser
    * password:bigpassword

* Normal User 
    * I used [Temp Mail](https://temp-mail.org/en/) to generate temporary emails accouts for testing

## Acknowledgements	
-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.

-   Special Thank you to Sarah and my girls for your suppprt and encouragement in allowing me to broaden my skillset.

**Please note : this project is for educational use only and was created for the Code Institute Module of Full Stack Frameworks With Django - Milestone Project**

**Created by Jonathan Kelly**