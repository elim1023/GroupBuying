# Helper functions

# import requests 
# import json
import os
# import base64
# import uuid

# from config import TEXT_PATH
# from openai import OpenAI
from flask import request, session, url_for
from application.models import db, User, GroupBuy, Order


def is_active(current_path:str, nav_path:str) -> str:
    """Returns a string that shows which page is active in the navigation menu."""

    if current_path == nav_path:
        return "is-active"
    
    return ""

def add_groupbuy(
        title,
        image_url,
        description,
        product_url,
        deadline,
        delivery_method,
        organizer_id):

    groupbuy = GroupBuy(
        title=title,
        image_url=image_url,
        description=description,
        product_url=product_url,
        deadline=deadline,
        delivery_method=delivery_method,
        organizer_id=organizer_id
    )

    db.session.add(groupbuy)
    db.session.commit()