#!/bin/sh
# -*- coding: utf-8 -*-

"""Example Case of the Script"""
from instapy import InstaPy

#if you don't provide arguments, the script will look for INSTA_USER and INSTA_PW in the environment
session = InstaPy()

"""Logging in"""
#logs you in with the specified username and password
session.login()

"""Comment util"""
#default enabled=False, ~ every 4th image will be commented on
session.set_do_comment(enabled=True, percentage=25)
session.set_comments(['Demais!', 'Top!', 'Animal!', 'Massa!'])

"""Follow util"""
#default enabled=False, follows ~ every 10th user from the images
session.set_do_follow(enabled=True, percentage=10)

#checks the image for keywords food and lunch, if found, sets the comments possible comments
#to the given comments
# session.check_image_for(['food', 'lunch'], comment=True, comments=['Tasty!', 'Yum!'])
# session.check_image_for(['dog', 'cat', 'cute'], comment=True, comments=['Sweet!', 'Cutie!!!'])

"""Unfollow util"""
#will prevent commenting and unfollowing your good friends
# session.set_dont_include(['friend1', 'friend2', 'friend3'])

"""Different tasks"""
# you can put in as much tags as you want, likes 100 of each tag
session.like_by_tags(['#instarung', '#GreenValleyBR', '#sotrackboa'], amount=50)

#get's the tags from the description and likes 100 images of each tag
# session.like_from_image(url='www.instagram.com/image', amount=100)

# session.unfollow_users(amount=10) #unfollows 10 of the accounts your following -> instagram will only unfollow 10 before you'll be 'blocked
#  for 10 minutes' (if you enter a higher number than 10 it will unfollow 10, then wait 10 minutes and will continue then)

"""Ending the script"""
#clears all the cookies, deleting you password and all information from this session
session.end()
