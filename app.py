# -*- coding: utf-8 -*-
"""
Created on Wednesday, November 25, 2020
@author: Sandra Milena Lopez Zamora
slopezza@outlook.com
"""
import os
from flask import Flask, request, jsonify
# from config import Config
import json

# files
from flask import send_file, send_from_directory, safe_join, abort
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Install requirement

basedir = os.path.abspath(os.path.dirname(__file__))

# class Config(object):
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'PersonalWebsite'
#     # MODEL_FOLDER = 'model/code'
#     UPLOAD_FOLDER = os.path.join(basedir, 'quick_start')

# Load in our meta_data
meda_data_path = os.path.join( app.root_path, 'model/code/meta_data.txt')
meta_data_f = open(meda_data_path, "r")
load_meta_data = json.loads(meta_data_f.read())


# basedir = os.path.abspath(os.path.dirname(__file__))
# uploads = os.path.join( app.root_path, app.config['UPLOAD_FOLDER'])
uploads = os.path.join(basedir, 'quick_start')

# Meta data endpoint
@app.route('/', methods=['GET'])
def meta_data():

	return jsonify(load_meta_data)

#str(sami) #jsonify(load_meta_data)

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
	print("Deleting previous files")
	sandra = os.path.join(uploads, '1_normalized.binvox')
	print(str(sandra))
	try:
		os.remove(os.path.join(uploads, '1_normalized.binvox') )
	except:
		print("No file: 1_normalized.binvox")

	try:
		os.remove(os.path.join(uploads, '1_normalized.mtl') )
	except:
		print("No file: 1_normalized.mtl")

	try:
		os.remove(os.path.join(uploads, '1_normalized.obj') )
	except:
		print("No file: 1_normalized.obj")

	try:
		os.remove(os.path.join(uploads, '1_normalized_simplified.mtl') )
	except:
		print("No file: 1_normalized_simplified.mtl")

	try:
		os.remove(os.path.join(uploads, '1_ori_rig.txt') )
	except:
		print("No file: 1_ori_rig.txt")

	try:
		os.remove(os.path.join(uploads, '1_remesh.obj') )
	except:
		print("No file: 1_remesh.obj")

	remesh_file = request.files['remesh_file']
	filename = secure_filename('1_remesh.obj')
	remesh_file.save(os.path.join(uploads, filename))

	try:
		import open3d as o3d
	except:
		os.system("echo Installing needed package")
		os.system("sudo apt update")
		os.system("sudo apt install libgl1-mesa-glx")


	import quick_start_cpu_fun
	quick_start_cpu_fun.runApp("1", 0.045, 0.75e-5)

	f_output = open("quick_start/1_ori_rig.txt", "r")
	output = f_output.read()




	return output

# app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)#, ssl_context="adhoc")
	# app.run(host='0.0.0.0', port=5000, ssl_context=('/etc/letsencrypt/live/api.logeo.co/cert.pem', '/etc/letsencrypt/live/api.logeo.co/key.pem') )
