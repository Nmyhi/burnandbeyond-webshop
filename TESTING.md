# Burn and Beyond Webshop - TESTING

This is the manual testing documentation for Burn and Beyond Webshop!

![App Preview](static/images/amiresponsive.png)

![Live link](https://burn-and-beyond-webshop-a7b5a0afa267.herokuapp.com/)

---

## CONTENTS

- [Burn and Beyond Webshop - TESTING](#Burn-and-Beyond-Webshop---testing)
  - [CONTENTS](#contents)
  - [AUTOMATED TESTING](#automated-testing)
    - [PEP8 validation](#pep8-validation)
    - [Lighthouse](#lighthouse)
  - [MANUAL TESTING](#manual-testing)
    - [Testing User Stories](#testing-user-stories)
    - [Full Testing](#full-testing)
  - [BUGS](#bugs)
    - [Known Bugs](#known-bugs)
    - [Solved Bugs](#solved-bugs)

---

## AUTOMATED TESTING

The automated Testing includes all the testing that is carried out by test code like jest, W3C HTML, and CSS validation.

### PEP8 validation

[bag apps.py](static/images/bag_apps_py_validation.png)

[bag contexts.py](static/images/bag_contexts_py_validation.png)

[bag urls.py](static/images/bag_urls_py_validation.png)

[bag views.py](static/images/bag_views_py_validation.png)

[base.css](static/images/base_css_validation.png)

[checkout admin.py ](static/images/checkout_admin_py_validation.png)

[checkout.css](static/images/checkout_css_validation.png)

[checkout forms.py](static/images/checkout_forms_py_validation.png)

[checkout models.py](static/images/checkout_models_py_validation.png)

[checkout urls.py](static/images/checkout_urls_py_validation.png)

[checkout views.py](static/images/checkout_views_py_validation.png)

[checkout webhook_handler.py](static/images/checkout_webhook_handler_py_validation.png)

[checkout webhooks.py](static/images/checkout_webhooks_py_validation.png)

[products admin.py](static/images/products_admin_py_validation.png)

[products forms.py](static/images/products_form_py_validation.png)

[products models.py](static/images/products_models_py_validation.png)

[products urls.py](static/images/products_urls_py_validation.png)

[products views.py](static/images/products_views_py_validation.png)

[profiles forms.py](static/images/profile_forms_py_validation.png)

[profiles models.py](static/images/profiles_models_py_validation.png)

[profiles views.py](static/images/profiles_views_py_validation.png)

[root urls.py](static/images/root_urls_py_validation.png)

[settings.py](static/images/settings_py_validation.png)


### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.
I tested the home page and the products page. I chose to test the products page because it has the most content.

- Home page test
  [Home Page Lighthouse desktop view](static/images/lighthouse_home_desktop.png)
  
  [Home Page Lighthouse mobile view](static/images/lighthouse_home_mobile.png)

- Products page test

  [Products Page Lighthouse desktop view](static/images/lighthouse_products_desktop.png)

  [Products Page Lighthouse mobile view](static/images/lighthouse_products_mobile.png)

## MANUAL TESTING

### Testing User Stories

- Client Goals

* Navigate on the Site.
* Register an account.
* Log-in to the account.
* Log-out of an account.
* Receive an email confirmation after registering.
* Quickly identify product deals.
* View a list of products.
* Have a personalised user profile.
* Sort a list of available products.
* Sort a specific category of products
* Sort multiple categories of products simultaneously.
* Search for products by name and description.
* Easily select the quantity and size (if avaliable).
* Place an order.
* Review and list previous orders.
* Get email confirmation about the order placed.
* Contact the shop via form.

- First Time Visitor Goals

* Navigate on the Site.
* Register an account.
* Log-in to the account.
* Log-out of an account.
* Receive an email confirmation after registering.
* Quickly identify product deals.
* View a list of products.
* Have a personalised user profile.
* Sort a list of available products.
* Sort a specific category of products
* Sort multiple categories of products simultaneously.
* Search for products by name and description.
* Easily select the quantity and size (if avaliable).
* Place an order.
* Review and list previous orders
* Get email confirmation about the order placed.
* Leave comment on Products.
* Leave a rating on products.
* Contact the shop via form.

- Returning Visitor Goals

* Navigate on the Site.
* Register an account.
* Log-in to the account.
* Log-out of an account.
* Receive an email confirmation after registering.
* Quickly identify product deals.
* View a list of products.
* Have a personalised user profile.
* Sort a list of available products.
* Sort a specific category of products
* Sort multiple categories of products simultaneously.
* Search for products by name and description.
* Easily select the quantity and size (if avaliable).
* Place an order.
* Review and list previous orders
* Get email confirmation about the order placed.
* Leave comment on Products.
* Leave a rating on products.
* Contact the shop via form.

- Frequent Visitor Goals

* Navigate on the Site.
* Register an account.
* Log-in to the account.
* Log-out of an account.
* Receive an email confirmation after registering.
* Quickly identify product deals.
* View a list of products.
* Have a personalised user profile.
* Sort a list of available products.
* Sort a specific category of products
* Sort multiple categories of products simultaneously.
* Search for products by name and description.
* Easily select the quantity and size (if avaliable).
* Place an order.
* Review and list previous orders
* Get email confirmation about the order placed.
* Leave comment on Products.
* Leave a rating on products.
* Contact the shop via form.

---

| Goals                                                                   | How are they achieved?                                                                           | Image                                                                              |
| :---------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------- |
| Navigate on the site. | I have achieved this with a main navigation bar. |  [Navbar](static/images/navbar.png) |
| Register an account.  | I have crated a fully functioning registration module with authentication.  | [Register Page](static/images/registerpage.png)  |
| Log-in to the account.  | I have created a login page.  | [Login Page](static/images/loginpage.png) |
| Log-out of an account. | I have created a logout page.  | [Logout Page](static/images/logoutpage.png) |
| Quickly identify product deals. | I have created a deals category | N/A |
| View a list of products.  | I have created a products page  | [Products Page](static/images/productspage.png)  |
| Have a personalised user profile. | I have created a user profile where users can store their default shipping details.| [User Page](static/images/userpage.png)  |
| Sort a list of available products.  | I have displayed the available products on the products page. | N/A  |
| Sort multiple categories of products simultaneously.  | Users can sort products on the products page by various attributes. | N/A  |
| Search for products by name and description.  | I have achieved this goal by implementing a search bar. | N/A |
| Easily select the quantity and size (if avaliable). | I have implemented a bar where users can increment and decrement quantities.  | N/A |
| Place an order. | I have created a checkout system using stripe and stripe webhooks.  | [Checkout Page](static/images/checkoutpage.png)  |
| Review and list previous orders.  | I have implemented previous orders in the user page.  | [Userpage](static/images/userpage.png) |
| Get email confirmation about the order placed.  | I have failed to implement real email.| N/A |
| Contact the shop via email. | I have achieved this by adding an email link to the footer.| [Footer](static/images/footer.png)  |

---

### Full Testing

Full testing was performed on the following devices:

- Laptop:
  - hp pavilion 15" laptop
- Mobile Devices:
  - iPhone 13 pro.
  - Samsung galaxy S10.
  - Samsung galaxy A22.
  - Google pixel 7a

Each device tested the site using the following browsers:

- Google Chrome

Additional testing was taken by friends and family on a variety of devices and screen sizes.

| Feature | Expected Outcome| Testing Performed | Result  | Pass/Fail |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------- |
| `Nav Bar` |
| Navbar Brand logo | Redirects to the home page | Click the brans logo | redirects to the home page | Pass |
| Search Bar | Displays the products with keyword contained in their name or description | type a keyword in and hit enter or click on the button | works as expected | Pass |
| My Account | display a dropdown menu with available options | Click the accounts icon | works as expected | Pass |
| Shopping Bag | Redirects to the shopping bag | Click the shopping bag logo | works as expected | Pass |
| Products filter dropdown menus | each option displays various options | Click the options | works as expected | Pass |
| `Footer` |
| Facebook Logo | Redirects to the site's facebook page | Click the facebook logo | redirects to the facebook page opened in a new tab | Pass |
| Instagram Logo | Redirects to the site's instagram page | Click the instagram logo | redirects to the instagram page in a new tab page | Pass |
| Email Logo | Opens options for the user to send an email | Click the email logo | Starts an email request | Pass |
| `Home Page` |
| Shop Now button | Redirects to the Products page | Click the button | works as expected | Pass |
| `Products Page` |
| Product cards | Display the image of a product with details and if clicked redirects to the product details page | Click the card | works as expected | Pass |
| `Product details Page` |
| Product details | Allow users to view the product details and put it in the shopping bag with the desired quantity | Click add to bag or keep shopping | works as expected | Pass |
| `Shopping bag` |
| Shopping Bag Page | Allow users to view the product details, modify the quantity if needed and check out | Modify the quantities and click checkout | works as expected | Pass |
| `Checkout Page` |
| Checkout Page and payment | Allow users to add shipping details, view the charge and to place an order | fill the form up and after added the card details place an order | works as expected | Pass |
| `Sign Up Page` |
| Registration module | Allow users to register an account via form | fill the form up and register | works as expected | Pass |
| `Login Page` |
| Login module | Allow users to log in with a previously created account | fill the form up and log in | works as expected | Pass |
| `Logout Page` |
| Logout module | Allow users to log out from a previously created account | fill the form up and log out | works as expected | Pass |

I have tested all these main mechanics of the page and I would like to highlight some of the features I have not added in details in the above table.

- If a superuser logs in they have the right to add a product which is called Product Management and it is only visible if a superuser is logged in.

- Throughout the whole system there are toasts provide information for the user's about successfull or failed attempts. In some cases I have coded warning messages as well, all of these work perfectly, I did not find a bug.

- Updating quantities and filtering all works, the system automatically calculates the delivery cost and the grand total as well.

- On the products and product details site edit and delete buttons displayed for superusers only.

## BUGS

### Known Bugs

- I have switched the sending real emails off because I could not make it work.


### Solved Bugs

Most of my bugs was responsiveness related front end bugs which I mostly debugged with additional css styling and media queries.
