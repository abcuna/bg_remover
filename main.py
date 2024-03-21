from flask import Flask, render_template, request, send_file
from remove_bg import export_img

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/download", methods=['GET', 'POST'])
def upload():
     if request.method == 'POST':
        if 'file' not in request.files:
                return 'No file part'

        file = request.files['file']
        if file.filename == '':
                return 'No selected file'
        
        file_path = 'uploads/' + file.filename
        file.save(file_path)
        try:
            my_data = export_img(f"./{file_path}")
        except:
            my_data = "ERROR"
        return send_file(my_data, as_attachment=True)

if __name__== "__main__":
    app.run(debug=True,port=5001)