import pytest
import time
from selenium import webdriver
from data.full_data import MAIN_PAGE,LOGIN, PASSWORD
from pages.login_page import LoginPage
from data.conftest import driver,driver_and_auth,chrome_options

def test_auth(driver_and_auth):
    login_page = driver_and_auth


  
    
