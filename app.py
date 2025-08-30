from flask import Flask, request, jsonify, send_file
import os, subprocess, uuid

app = Flask(__name__)

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route('/compile', methods=['POST'])
def compile_extension():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    filename = str(uuid.uuid4()) + ".zip"
    filepath = os.path.join(UPLOAD_DIR, filename)
    file.save(filepath)

    # Dummy compiler - In real case, integrate AI2 extension compiler
    aix_file = os.path.join(OUTPUT_DIR, filename.replace(".zip", ".aix"))
    with open(aix_file, "w") as f:
        f.write("Dummy AIX content for testing")

    return send_file(aix_file, as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
