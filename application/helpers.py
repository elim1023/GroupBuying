# Helper functions

import requests
import json
import os
import base64
import uuid

from config import TEXT_PATH
from openai import OpenAI
from flask import url_for

def is_active(current_path:str, nav_path:str) -> str:
    """Returns a string that shows which page is active in the navigation menu."""

    if current_path == nav_path:
        return "is-active"
    
    return ""
