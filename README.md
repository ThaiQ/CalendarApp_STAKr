# STAKr
By: Alex Montgomery (AMontgomery123), Thai Quach (ThaiQ), Sean Milner(shengda419), Nguyen Cuu Khanh (khanhsjsu)

**Problem Statement**  
Many people in the professional world need a way to manage appointments. The problem, though, is that many calendar applications do not present a streamlined way to manage them.

**Product Objectives**  
Build an application using Python-3 and the Flask Framework to create an appointment system. This system will allow the customer and owner to communicate with one another by creating meetings through a Calendar-like interface.

---
# SETUP!
## Required Libraries

    Python3  
    pip3

## Installing Dependencies

    python3 setup.py

## Run Project with <nobr>run.py</nobr>
    python3 run.py

---
# Product  
**Functional Requirements:**  

-    Database should hold owner login information
    
-   User should not be able to login to an account without providing matching information
    
-   System sends confirmation emails for both registration and appointment confirmation
    
-   Owner can configure what times they are available using Calendar
    
-   Customer can follow email to select desired appointment time with Owner
    
-   Owner can successfully log out of the system

**Non-Functional Requirements:**

-   System must display messages in English
    
-   System will respond to owner and customer commands within 3 seconds
    
-   The site shall be able to run on Windows, Mac, and Linux machines
    
-   System must use Gregorian calendar

# Project Planner
### **Grantt Chart**
![grantt chart](https://user-images.githubusercontent.com/60629468/79679202-a9259700-81b8-11ea-879c-99a78675ef62.JPG)

# Use Case Description
### **UML Diagram**  
![UML](https://user-images.githubusercontent.com/18486562/79171733-b3562880-7da7-11ea-8cf3-6e66574cb90f.png)

## Owners’ Use Case Description  
### **Register** 
**Summary:** Allows a user to register for an account  
**Actor(s):** Unregistered user

**Pre-conditions:**  
 *  User must not have an existing account  
 *  User must have a valid email address  

**Primary sequence:**  
  1.  Click on "Register"  
  2.  Input desired login info (email) and password  
  3.  Click on “Create Account”  
  4.  Confirm email address  

**Alternative sequence:**  
1.  Email does not exist  
    * System displays error message “Invalid email address” to the customer

**Post-condition:**
1.  Customer email is successfully confirmed  
    * Customer receives a confirmation email and has accepted it  
    * Customer can now login with their credentials  
1.  Email has not been confirmed
    *  Customer can not login because they have not confirmed the email verification
3.  Customer has not successfully created an account  
    *  No account was created presumably due to invalid login info  
---
### **Login**  
**Summary:** Allows a user to log in to their account  
**Actor(s):** Registered-Owner

**Pre-conditions:**  
  *   Registered an account
  *   Confirmed email address of account

**Primary sequence:**  
  1.  Enter a username and a password  
  2.  (Optional) Select ”Remember Me”  
  3.  Click “Login”  

**Alternative sequence:**
1.  If user does not have an account
    *  User inputs an email and password that has not been made  
    *  System displays message to customer saying the account does not exist  
2.  Invalid email
    *  User inputs an email that has not been registered  
    *  System displays message to customer saying the account does not exist  
3.  Invalid password  
    *  User inputs an email matching one in our database, but has an invalid password    
    *  System displays message to customer saying the password was typed incorrectly
4.  User wants to register an account
    *  User selects the “Register” button
    *  System redirects user to the register screen
    
**Post-condition:**
1.  User has successfully logged in
    *  User is redirected to his/her home page by the system.
2.  User has not successfully logged in
    *  User remains on the login page until they provide proper credentials
---
### **Configure active schedule**  
**Summary:** Allows the owner to configure their desired time for customers to make an appointment with   
**Actor(s):** Owner 

**Pre-conditions:**  
 *   The owner must be logged into their account

**Primary sequence:**
  1.  Click on "Set Working Schedule"
  2.  Choose desired "Working Time" through a drop-down list 
  3.  Click on “Save”
    
**Alternative sequence:**
1.  Click on “Cancel”
    *  System redirects User to home page
    
**Post-condition:**
1.  Working Schedule has been set
    *  System displays a message “Working Schedule set” to the Owner
    *  System redirects the owner to home page
2.  Working Schedule was cancelled
    *  System redirects the owner to home page
    *  Working schedule is the same as it was previously or not set if the owner has not set it previously
 ---   
### **Send appointment invitation**
**Summary:** Allows the owner to get their unique URL which allows their customer to create an appointment from their selected time  
**Actor(s):** Owner

**Pre-conditions:**
*   The owner must have an account
*   The owner must be logged in
    
**Primary sequence:**   
1.  The owner  will log into their account
2.  The owner click the “My appointment link” button
3.  The owner must click and copy a unique URL-link
    
**Alternative sequence:**
1.  The owner will add customers' emails into a text box
2.  The owner must click “Send my invitation”
3.  An email will be sent to customers' emails
    
**Post-condition:**   
1. The owner chooses to copy their URL
   * A URL is available for copy/paste
2. The owner chooses to send an email
   * An email with the owner's URL will be sent to their customers

---
## **Customers’ Use Case Description**
### **Make an appointment**  
**Summary:** Allow a customer to make an appointment through the owner's invitation-URL  
**Actor(s):** Customers

**Pre-conditions:** 
* Must have the invitation-URL from the owner
  * The customer receives URL through email
  * The customer recieved URL directly from the owner
    
**Primary sequence:**  
1.  The customer selects the link URL in the email
2.  The calendar shows the available date/time and customers pick their date.
3.  Confirm Reservation
    *  If data were valid: confirmed reservation
    *  If data were invalid: showed problem in reservation
    
**Alternative sequence:**
1.  Customer cancels making the appointment
    *  Customer clicks “Cancel”    
    *  System displays message “Appointment was cancelled”
    
2.  Owner is busy at selected time
    *  System displays the message “The person is busy at that time. Please select a new time”
    
3.  Error when connecting to database information
    *  System displays the message “System error communicating to database. Please refresh the page and try again shortly and make sure you have proper internet connection”
    
**Post-condition:**
1.  Customer has successfully made appointment
    *  Notify the owner and customer about the appointment.
    
2.  Customer cancels making appointment
    *  Notifications not sent to customer and owner

3.  Owner is busy at selected time
    *  Notifications not sent to customer and owner

4.  Error when connecting to database information
    *  Notifications not sent to customer and owner
    
## Glossary:  
**The owner** should be able to: log into their account, configure their working schedule, get/send a URL invitation link to make an appointment with them.  
**The customer** should be able to: make an appointment with the owner through their invitation URL without the need to log in.  
