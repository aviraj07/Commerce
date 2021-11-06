from django.contrib.auth import authenticate, login, logout
from django.core.checks import messages
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib import messages
from django import forms

from .models import *

class NewBidForm(forms.Form):
    bid = forms.CharField(label="Place Bid:  ")



def index(request):
    listings = Listings.objects.filter(Active=True)
    
    return render(request, "auctions/index.html",{
        "listings": listings
    })
    


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create_listing(request):
    if request.method == "POST":
        title = request.POST["title"]
        category = request.POST["category"]
        url = request.POST["url"]
        description = request.POST["description"]
        starting_bid = request.POST["bid"]
        Listings.objects.create(user=request.user,listing=title, description=description, ini_bid=starting_bid,category=category, url=url)
        
        
        return HttpResponseRedirect(reverse('index'))

    else:
        return render(request, "auctions/create_listing.html")

def content(request,id):

    if Listings.objects.get(pk=id).Active == True:
        user_name = Listings.objects.get(pk=id).user
        comments = {}
        all = Comments.objects.filter(item=Listings.objects.get(pk=id))
        owner = False
        if Listings.objects.get(pk=id).user == request.user.username:
            owner = True

        for each in all:
            user= each.user
            comments[user] = each.comment
        if user_name == request.user:
            return render(request,"auctions/content.html",{
                "user":user_name
            })
        info = Listings.objects.filter(pk=id)
        if request.method == "POST":
            form = NewBidForm(request.POST)
            if form.is_valid():
                bid = form.cleaned_data["bid"]
                bid = int(bid)
                price = Listings.objects.get(pk=id).ini_bid
                if price < bid:
                    updated_bid = Listings.objects.get(pk=id)
                    updated_bid.ini_bid = bid
                    updated_bid.save()
                    if Bids.objects.filter(item = Listings.objects.get(pk=id)).exists():
                        new_bid = Bids.objects.get(item = Listings.objects.get(pk=id))
                        new_bid.bid = bid
                        new_bid.user = request.user
                        new_bid.save()
                    else:
                        Bids.objects.create(user=request.user, item = Listings.objects.get(pk=id), bid = bid)
                else:
                    return render(request, "auctions/content.html",{
                        "info":info, "form":form, "message":"Place bid higher than current price.","owner":owner
                    })   
                return HttpResponseRedirect(reverse("content",args=[id]))     
            else:
                return render(request, "auctions/content.html",{
                        "info":info, "form":form, "message":"Invalid bid.","owner":owner
                }) 
        
        else:
            return render(request, "auctions/content.html",{
                "comments":comments, "info":info,"form":NewBidForm,"owner":owner
            })

    else:
        return render(request,"auctions/content.html",{
            "done":True
            })

def watchlist_add(request, id):
    if request.method == "POST":
        item_del = Watchlist.objects.get(user=request.user).item.get(pk=id)
        Watchlist.objects.get(user=request.user).item.remove(item_del)
        return HttpResponseRedirect(reverse("watchlist"))

    item_add = get_object_or_404(Listings, pk=id)
    if Watchlist.objects.filter(user=request.user, item=id).exists():
        messages.add_message(request, messages.ERROR, "Already there in wishlist")
        return HttpResponseRedirect(reverse("watchlist"))

    user_list, created = Watchlist.objects.get_or_create(user=request.user)
    user_list.item.add(item_add)
    messages.add_message(request, messages.SUCCESS, "Successfully added")
    return HttpResponseRedirect(reverse("watchlist"))

def watchlist(request):
    if not Watchlist.objects.filter(user=request.user).exists():
        return HttpResponse("No item in Watchlist")

    user_list = Watchlist.objects.get(user=request.user)
    return render(request, "auctions/watchlist.html",{
        "listings" : user_list.item.all()
    })  

def close_listing(request,id):
    if Bids.objects.get(item = Listings.objects.get(pk=id)):
        user_obj = Bids.objects.get(item = Listings.objects.get(pk=id))
    closed = Listings.objects.get(pk=id)
    closed.Active = False
    closed.save()
    

    
    return HttpResponseRedirect(reverse("index"))

def add_comment(request,id):
    info = Listings.objects.filter(pk=id)
    comment = request.GET["comment"]
    Comments.objects.create(user=request.user, item= Listings.objects.get(pk=id),comment=comment)
    
    
    return HttpResponseRedirect(reverse("content",args=[id]))

def categories(request,category):
    if Listings.objects.filter(category=category,Active=True):
        obj = Listings.objects.filter(category=category,Active=True)
        
        return render(request,"auctions/categories.html",{
            "all_objs":obj
        })
    else:
        return HttpResponse("No entry related to this.")    

def Categories(request):
    all = Listings.objects.filter(Active=True)
    obj = []
    for each in all:
        obj.append(each.category)

    
    return render(request,"auctions/category.html",{
        "all_objs":obj
    })