from flask import Flask
app = Flask(__name__)
@app.route('/')

def index():
	return 'CI/CD DEPLOYMENT USING PIPELINE'
app.run(debug=True , host='0.0.0.0', port=5000)
