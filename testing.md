# Concert Travel
[Link to live site on Heroku](https://ci-ms4-concerttravel.herokuapp.com/)

[Link to main README.md file](https://github.com/coder187/ci-ms4-concerttravel/blob/main/README.md)
                              


Project - Data Centric Development - Code Institute

## Testing

### Testing planning.
With this project I have use Test [Driven Development](https://en.wikipedia.org/wiki/Test-driven_development) model (TDD).

The TDD method consists of a cycle of :
* write new test
* implement new feature
* run all tests & repeat all steps until all tests pass.


| Action                                                                                 | Expected Outcome                                                                                                                                                            | Result |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Install Django and Create Base.html template                                           | Django starts and serves pages                                                                                                                                              | Pass   |
| Add Home App Index.html                                                                | Carousel Control with footer containing contact form and contact details                                                                                                    | pass   |
| Submit Contact Form                                                                    | Email sent to site admin and sender of message.                                                                                                                             | Pass   |
| Add menu option Events By Artist\Date\Venue                                            | Events are returned by the order selected                                                                                                                                   | Pass   |
| Add menu option Event Type                                                             | Only events of that type are displayed. Types may have multiple sub-types. These are displated at the top of the page and be selected to narrrow the search results further | Pass   |
| Add menu option Location                                                               | Only events taking place in that location are displayed. Each Venue in the sellected location is displayed and be selected to all events for that venue only.               | Pass   |
| Add menu option Venue                                                                  | Only events taking place in that venue are displayed.                                                                                                                       | Pass   |
| Future Dates Only                                                                      | Only events with an Event Date >= to today are listed.                                                                                                                      | Pass   |
| Publish = True                                                                         | Only events where the Publish field is true are displayed                                                                                                                   | Pass   |
| Free text search                                                                       | Search is executed on the Artist Name and Event Description Fields                                                                                                          | Pass   |
| Number of results are displayed                                                        | The number of search results are displayed                                                                                                                                  | Pass   |
| Re Order Search Result By Date Asc/Desc                                                | Results are ordered by event date                                                                                                                                           | Pass   |
| Re Order Search Result By NameAsc/Desc                                                 | Results are ordered by event name                                                                                                                                           | Pass   |
| Re Order Search Result By Name Venue                                                   | Results are ordered by Venue                                                                                                                                                | Pass   |
| Icon Appears dependent on numbe of sales.                                              | For events having sales > average a an icon is dsplayed on card footer.                                                                                                     | Pass   |
|                                                                                        | Event Name, Date and Venue  & type is disaplayed on Event footer                                                                                                            | Pass   |
|                                                                                        | Select an event type to view all events of that type                                                                                                                        | Pass   |
| Select an Event                                                                        | Event Details (Artist, Event Date, Desc) along with options to select a collection point witjh corresponding price is displayed                                             | Pass   |
| Select an Quantity                                                                     | Quantity Updates                                                                                                                                                            | Pass   |
| Select Add To Bag                                                                      | Selected quantity is added to bag. Bag total is updated and displayed in top right of screen                                                                                | Pass   |
| Select Add To Bag                                                                      | Toast Message confirms add to bag action completed successfully                                                                                                             | Pass   |
| Bag Page View                                                                          | Displays bag contents, total price, discounts and total price. Discount delta is displayed                                                                                  | Pass   |
| Select Secure Checkout                                                                 | Check out form is displayed showing order summart and payee details.                                                                                                        | Pass   |
|                                                                                        | Payee details are loaded from Profile if logged in                                                                                                                          | Pass   |
|                                                                                        | Shopper is prompted to create an account if not authenticated or may proceed with anonymous checkout                                                                        | Pass   |
| Complete Order                                                                         | Transaction is processed by Stripe. If unsuccessful an error message is displayed.                                                                                          | Pass   |
| Successful transaction                                                                 | Checkout success page loads and displays order summary                                                                                                                      | Pass   |
|                                                                                        | Email confirmation is sent to email address supplied                                                                                                                        | Pass   |
|                                                                                        | Order is written to database                                                                                                                                                | Pass   |
| Successful Stripe transaction followed by application failure or user error/disconnect | Stripe Webhook enures the order is written to the database and email confirmation is sent                                                                                   | Pass   |
| Enter 3Dsecure Card #                                                                  | User must complete 3DSecure check                                                                                                                                           | Pass   |
| Enter Card Lost/Stolen                                                                 | Transaction is stopped and error message displayed                                                                                                                          | Pass   |
| Enter Invalid CVV Number                                                               | Transaction is stopped and error message displayed                                                                                                                          | Pass   |
| Click My Account Menu Option                                                           | User may login or register if not logged in. Otherwise the My Profile menu link is displayed                                                                                | Pass   |
| Create an account                                                                      |                                                                                                                                                                             |        |
| Supply Email Address, Username and Password                                            | A profile is created in the database and the user is sent an email to confirm their address                                                                                 | Pass   |
| Click Confirm                                                                          | The user can log in via the login page                                                                                                                                      | Pass   |
| Reset Password                                                                         | An email is sent wit a reset link to recover the account                                                                                                                    | Pass   |
| Click recover                                                                          | The user must reset their password and can now login                                                                                                                        | Pass   |
| Login                                                                                  | enter user name and password to login.                                                                                                                                      | Pass   |
| View Profile                                                                           | The users Order history is listed along with their personal info                                                                                                            | Pass   |
| Update Personanl Data                                                                  | The record is updated on the database                                                                                                                                       | Pass   |
| Click Order                                                                            | The order summart is displayed                                                                                                                                              | Pass   |
| Logout                                                                                 | The user is prompted to logout                                                                                                                                              | Pass   |
| Admin User                                                                             |                                                                                                                                                                             |        |
|                                                                                        | The events list dusplays and additional Edit/Delete link for Admin users.                                                                                                   | Pass   |
| Click Delete                                                                           | The Event is deleted if it has no existing Orders. A toast message confirms the action.                                                                                     | Pass   |
| Edit                                                                                   | The Edit Event Page is displayed. Edits are saved on clicking update. A toast message confirms the save.                                                                    | Pass   |
|                                                                                        | The events list displays and additional Is Published Icon for admin users                                                                                                   | Pass   |
|                                                                                        |                                                                                                                                                                             |        |
| Admin - My Account                                                                     |                                                                                                                                                                             |        |
| Add Event                                                                              | The Add Event Page is rendered.                                                                                                                                             | Pass   |
| Click Add Event                                                                        | All fields are required excpet for Long Desc and Image. The form will not submit until fields are validated.                                                                | Pass   |
| Pick Location Add Edit                                                                 | The Pick Up Location Add Edit form is displated                                                                                                                             | Pass   |
| Complete the form                                                                      | Form valifation checks the input before submitting the form and adding the record to the datanase                                                                           | Pass   |
| Delete Pick Location                                                                   | Select the Delete option to Delete the Pick Location                                                                                                                        | Pass   |
| Edit Pick Location                                                                     | Select Edit to load the Pick Location to edit form.                                                                                                                         | Pass   |
|                                                                                        |                                                                                                                                                                             |        |
| Discounts                                                                              |                                                                                                                                                                             |        |
| Discount Delta & Discount percentage is set in settings.py                             | As the Order is updated the applicatio recalculates and applies the set discount if the delta is exceeded.                                                                  | Pass   |

### Responsive Design
I tested the site layout using the built in  Chrome Dev Tools with following device emulation:
| Device | Resolution | Throttling | Orientation |
|---------|------------|------------|-------------|
| Moto G4 | 360x640 | None | Portrait|
| Pixel 2 | 411x731 | None | Portrait|
| iPhone 5 | 320x568 | None | Portrait|
| iPad | 768x1024 | None | Portrait|
| iPad | 1024x768 | None | Portrait|
| iPad Pro | 1024x1366 | None | Portrait|
| iPad Pro | 1024x1366 | Mid Tier | Portrait|
| iPad Pro | 1024x1366 | Low End | Portrait|
| Galaxy Fold| 280x653 | None | Portrait|
| Galaxy Fold| 653x280 | None | Landscape|
| Galaxy Fold| 512x717 | None | Portrait|
| Galaxy Fold| 717x512 | None | Landscape|

I tested the site layout using physical devices as follows:
| Device | Browser |Resolution | Throttling | Orientation |
|---------|------------|------------|-------------|--------|
| Samsung A50 on Android 10 | Android Chrome | 412x892 | Cellular / Broadband | Portrait|
| Samsung A50 on Android 10 | Android Chrome | 892x412 | Cellular / Broadband | Landscape|
| Samsung S10 on Android 9 | Android Chrome | 412x869 | Broadband | Portrait |
| Samsung S10 on Android 9 | Android Chrome | 869x412 | Broadband | Portrait |
| HP Laptop on Win 10 Pro 10.0.19041.867 | Chrome 89.0.4389.90| 1366x768 | None |
| HP Laptop on Win 10 Pro 10.0.19041.867 | Chrome 89.0.4389.90| 800x600 | None |
| HP Laptop on Win 10 Pro 10.0.19041.867 | Edge 89.0.774.57 | 1366x768 | None |
| HP zBook on Win 10 Pro 10.0.19041.685 | Chrome 88.0.4324.190 | 1920x1080 | None |




### Further Testing
  * I want to further enhance the error trapping and implement a logging system such that admin users may view a log of activity.