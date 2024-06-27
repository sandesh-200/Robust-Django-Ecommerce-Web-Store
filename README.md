Django Web Application
======================

Welcome to the Django Web Application repository. This application is a fully functional e-commerce platform built using Django. It includes user authentication, product management, search functionality, and more.

Features
--------

*   User registration and authentication
    
*   Product listing and detailed view
    
*   Category-based product filtering
    
*   Contact form
    
*   User profile management
    
*   Product search
    
*   Cart and purchase functionality with order processing
    

Installation
------------

To get a local copy up and running, follow these simple steps.

1.  git clone https://github.com/your-username/your-repo-name.git
    
2.  pip install -r requirements.txt
    
3.  python manage.py migrate
    
4.  python manage.py createsuperuser
    
5.  python manage.py runserver
    

Usage
-----

1.  Open your browser and navigate to http://127.0.0.1:8000/ to access the application.
    
2.  Use the admin interface at http://127.0.0.1:8000/admin/ to manage products, categories, and users.
    

Views
-----

### Home

*   **URL**: /
    
*   **Description**: Displays all products and category images.
    
*   **Template**: pasal/home.html
    

### Category Items

*   **URL**: /category//
    
*   **Description**: Displays items of a specific category.
    
*   **Template**: pasal/categories.html
    

### About

*   **URL**: /about/
    
*   **Description**: About page.
    
*   **Template**: pasal/about.html
    

### Contact

*   **URL**: /contact/
    
*   **Description**: Contact form.
    
*   **Template**: pasal/contact.html
    

### Firm

*   **URL**: /firm/
    
*   **Description**: Firm page.
    
*   **Template**: pasal/firm.html
    

### Product

*   **URL**: /product//
    
*   **Description**: Detailed view of a product.
    
*   **Template**: pasal/product.html
    

### Collection

*   **URL**: /collection/
    
*   **Description**: Displays all products in the collection.
    
*   **Template**: pasal/more\_items.html
    

### User Registration

*   **URL**: /register/
    
*   **Description**: User registration form.
    
*   **Template**: pasal/register.html
    

### User Login

*   **URL**: /login/
    
*   **Description**: User login form.
    
*   **Template**: pasal/login.html
    

### User Account

*   **URL**: /account/
    
*   **Description**: Displays and edits user profile.
    
*   **Template**: pasal/profile.html
    

### User Logout

*   **URL**: /logout/
    
*   **Description**: Logs out the user.
    
*   **Template**: None (redirects to home)
    

### Remove Picture

*   **URL**: /remove-pic/
    
*   **Description**: Removes user's profile picture.
    
*   **Template**: None (redirects to user account)
    

### Search

*   **URL**: /search/
    
*   **Description**: Searches for products.
    
*   **Template**: pasal/search.html
    

### Purchase

*   **URL**: /purchase/
    
*   **Description**: Processes the cart and creates orders.
    
*   **Template**: pasal/purchase.html
