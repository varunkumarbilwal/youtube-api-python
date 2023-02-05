
import pytube
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def wel():
    return 'Hello World'

@app.route('/api', methods=['GET'])
def index():
	args = request.args
	vurl = args.get("url")
	youtube = pytube.YouTube(vurl)
	video = youtube.streams.filter(progressive=True)
	returnJSON = {
		'144p': video.get_by_itag(17).url,
		'320p': video.get_by_itag(18).url,
		'720p': video.get_by_itag(22).url
	}
	return jsonify(returnJSON)

