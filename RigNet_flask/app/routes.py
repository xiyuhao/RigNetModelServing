
import os
from flask import Flask, request, jsonify
import json

from app import app
from config import Config


# files
from flask import send_file, send_from_directory, safe_join, abort
from werkzeug.utils import secure_filename

# Load in our meta_data
meda_data_path = os.path.join( app.root_path, app.config['MODEL_FOLDER'], 'meta_data.txt')
meta_data_f = open(meda_data_path, "r")
load_meta_data = json.loads(meta_data_f.read())

# basedir = os.path.abspath(os.path.dirname(__file__))
# uploads = os.path.join( app.root_path, app.config['UPLOAD_FOLDER'])
uploads = app.config['UPLOAD_FOLDER']

# Meta data endpoint
@app.route('/', methods=['GET'])
def meta_data():

	return jsonify(load_meta_data)

#str(sami) #jsonify(load_meta_data)

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
	# ID requested
	# req = request.get_json()
	remesh_file = request.files['remesh_file']
	filename = secure_filename('1_remesh.obj')
	remesh_file.save(os.path.join(uploads, filename))
    # # print(str(uploaded_file.filename))
	# for key in req:
	# 	print(key)
        # filename = images.save(fileI)

	# Log the request
	# print({'request': req['ID']})

	# from quick_start_cpu_v2 import *
	# runRigNet()
	import quick_start_cpu_v2
	quick_start_cpu_v2


	# f_output = open("quick_start/" + str(req['ID'][0])+ "_ori_rig.txt", "r")
	f_output = open("quick_start/1_ori_rig.txt", "r")
	output = f_output.read()

	return output

# app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000, ssl_context="adhoc")
	app.run(host='0.0.0.0', port=5000, ssl_context=('/etc/letsencrypt/live/api.logeo.co/cert.pem', '/etc/letsencrypt/live/api.logeo.co/key.pem') )
