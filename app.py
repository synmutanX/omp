from flask import Flask, request, jsonify
from utils import load_blacklist, is_blacklisted
from models import classify_text, classify_image

app = Flask(__name__)
blacklist = load_blacklist()

@app.route("/classify-url", methods=["POST"])
def classify_url():
    data = request.json
    url = data.get("url")
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    # Check against blacklist
    if is_blacklisted(url, blacklist):
        return jsonify({"status": "blocked", "reason": "Blacklisted"})
    
    # Classify URL content (placeholder for AI logic)
    # You could scrape or fetch content here for text classification
    if classify_text(url):  # Simple example
        return jsonify({"status": "blocked", "reason": "NSFW content detected"})
    
    return jsonify({"status": "allowed"})

@app.route("/classify-image", methods=["POST"])
def classify_image_endpoint():
    if 'file' not in request.files:
        return jsonify({"error": "Image file is required"}), 400
    
    file = request.files['file']
    file_path = f"temp/{file.filename}"
    file.save(file_path)
    
    # Classify the image
    if classify_image(file_path):
        return jsonify({"status": "blocked", "reason": "NSFW image detected"})
    
    return jsonify({"status": "allowed"})

@app.route("/update-blacklist", methods=["POST"])
def update_blacklist():
    data = request.json
    url = data.get("url")
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    # Append to blacklist file
    with open("blacklist.csv", "a") as f:
        f.write(f"{url}\n")
    
    global blacklist
    blacklist = load_blacklist()  # Reload the blacklist
    return jsonify({"status": "success", "message": "Blacklist updated"})

if __name__ == "__main__":
    app.run(debug=True)
