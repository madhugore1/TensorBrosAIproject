import os
from final_model import get_result
from flask import Flask, request, abort, jsonify, send_from_directory

app = Flask(__name__)

UPLOAD_DIRECTORY = '/home/madhura/Madhu/TensorBros/temp'
app.config['UPLOAD_FOLDER'] = UPLOAD_DIRECTORY

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


# @api.route('/')
# def index():
#     return "Homepage"

#@api.route('uploader', methods=['GET', 'POST'])

# def upload(path):

# @api.route('/files1')
# def list_files():
#     """Endpoint to list files on the server."""
#     files = []
#     for filename in os.listdir(UPLOAD_DIRECTORY):
#         path = os.path.join(UPLOAD_DIRECTORY, filename)
#         if os.path.isfile(path):
#             files.append(filename)
#     return jsonify(files)


@app.route('/files/<path:path>/')
def get_file(path):
    """Download a file."""
    result = get_result(path)
    print 'success'
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


# @api.route('/files', methods=['POST'])
# def post_file():
#     """Upload a file."""
#
#     # if '/' in filename:
#     #     # Return 400 BAD REQUEST
#     #     abort(400, 'no subdirectories directories allowed')
#
#     file = request.files['video']
#     filename = file.filename
#     file.save(filename)
#     print(filename)
#
#     # with open(os.path.join(UPLOAD_DIRECTORY, filename), 'wb') as fp:
#     #     fp.write(request.data)
#
#     # Return 201 CREATED
#     return "hello world"

@app.route('/files', methods=['GET', 'POST'])
def upload_file():
    message = "success"
    if request.method == 'POST':
        f = request.files['video']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        print(message)
    return message


if __name__ == '__main__':
    app.run(debug=True, port=5000)
