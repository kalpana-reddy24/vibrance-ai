# -*- coding: utf-8 -*-
"""
Created on Mon May 20 10:11:21 2024

@author: shiva
"""
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["AIzaSyDoj5c3b3Vlp8MOXlQjmj8MP7yPK8Lu_Ns"])
model = genai.GenerativeModel('gemini-1.0-pro-latest')
response = model.generate_content("The opposite of hot is")
print(response.text)