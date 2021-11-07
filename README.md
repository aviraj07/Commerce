# Commerce
It is a web based app that makes it easy for you to list your products so that you can buy and sell them.

<br>
[See it in action](https://youtu.be/8Qp1ko2MJrY)

## Installation
- You need to have **Django** installed on your local machine.
- Download this zip code.
- Go into this project's directory and run `python(or python3) manage.py runserver`.
- You'll be able to run the application.
- To install django on your machine, [click here](https://docs.djangoproject.com/en/3.2/topics/install/).
- To link database to your webapp run `python(or python3) manage.py makemigrations auctions` and then `python(or python3) manage.py migrate`.

## Usage
- After running the application, you need to register (if you're new a user) to use the webapp.
- After login, you'll have options to create a listing, see the active listings, add an item to your watchlist, bid on an item, or see the items based on their categories.
- To create a listing click on **Create Listings**. After typing in all the required information, click on **Submit** button to create a listing.
- You'll be directly rendered to the default page that shows all the active listings.
- To **bid** on an item, click on the item and place your bid(higher than the current price) in the **Place Bid:** box.
- When the user who listed the item on the webapp closes that listing, whoever bids the highest will win that bid.
- You can add an item to your **Wattchlist** by clicking on **Add to Watchlist** on the specific listing page.
- You can add **comments** on any item's page by typing in the comment in the commnet box.
- To see the items based on their categories, click on **Categories**. It will list all the categories of the item that are currently active, clicking on any category will show you the list of all item(s) of that categories.

## Structure/Design of program
This is a commerce project under which there's an app called auctions. It is mainly written in Django. HTML and CSS are used for layout and styling.
<br>
Main files:
<br>
* *manage.py* - It contains all the required files to run your webapp.
* *acutions/static* - It include the required styling css page to help user to have a good experience of the webapp.
* *auctions/templates* - These include all the html pages of the webapp from a basic layout file to each and every html page of the webapp.
* *auctions/models.py* - It contains all the database tables that django will handle to store information in it.
* *auctions/views.py* - It contains all the logic behind rendering the required pages upon request and acting as a mediator between databse and user.
* *auctions/urls.py* - It has all the urls that a user can request to visit the pages of the webapp.

There are other supporting files as well.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
