from flask import Flask, render_template, request
import numpy as np
from skimage import color, io
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs("static", exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        files = request.files.getlist("image")       
        k_value = int(request.form["k"])

        results_data = [] 
        for file in files:
            if file.filename == '':
                continue

            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            original_file_size = os.path.getsize(filepath)  
            
            img = io.imread(filepath) 
            
            if img.ndim == 3:
                if img.shape[2] == 4:  
                    img = img[:, :, :3]
                gray = color.rgb2gray(img)
            else:
                gray = img / 255.0

            M, N = gray.shape

            k = min(k_value, min(M, N))

            # SVD
            U, S, Vt = np.linalg.svd(gray, full_matrices=False)
            compressed = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
            
            out_filename = f"out_{filename}.png"
            output_path = os.path.join("static", out_filename)
            plt.imsave(output_path, compressed, cmap="gray")

            bytes_per_float = 8  
            original_matrix_size = M * N * bytes_per_float
            compressed_matrix_size = (
                U[:, :k].size +
                S[:k].size +
                Vt[:k, :].size
            ) * bytes_per_float

            compression_ratio = original_matrix_size / compressed_matrix_size
            gain_percent = (1 - compressed_matrix_size / original_matrix_size) * 100

            results_data.append({
                "filename": filename,
                "out_filename": out_filename,
                "M": M,
                "N": N,
                "k": k,
                "original_file_size": original_file_size,
                "original_matrix_size": original_matrix_size,
                "compressed_matrix_size": compressed_matrix_size,
                "compression_ratio": compression_ratio,
                "gain_percent": gain_percent
            })

        return render_template("index.html", results=results_data)

    return render_template("index.html", results=None)

if __name__ == "__main__":
    app.run(debug=True)