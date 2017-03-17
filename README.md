## Overview

Growth Street is building a platform to allow growing businesses to borrow money at affordable rates. Our ability to make the entire process efficient on our web platform will be critical in offering the lowest rates to our customers. 

#### Usage

The web page can be accessed at either the main index or at /borrowing/.  The form will take the following information:

* The borrower's name, email, and telephone number.
* The borrower's business' name, address, registered company number (8 digit number), and business sector (pick from Retail, Professional Services, Food & Drink, or Entertainment).
* The amount the borrower wishes to borrow in GBP (between £10000 and £100000), for how long (number of days), and a reason for the loan (text description).

On success, a summary page is shown - only accessible by the user who submitted the loan request.

An account is automatically created using the email address as the username and the supplied password - recorded using djangos user auth models

#### Admin

The admin page is accessible at the usual /admin/

* username: admin
* password: admin

#### Database

An empty simple sqlite database has been set up and is shipped with this for testing.