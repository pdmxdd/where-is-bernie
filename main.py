from app import app, db
from flask import request, render_template, url_for
import png

@app.before_request
def before_request():
    '''
    print("Request: {}".format(request))
    print("Request endpoint: {}".format(request.endpoint))
    print("Request method: {}".format(request.method))
    print("Request method type: {}".format(type(request.method)))
    print("Request data: {}".format(request.data))
    print("Request values: {}".format(request.values))
    print("Request args: {}".format(request.args))
    print("Request cookies: {}".format(request.cookies))
    '''
    if request.method == 'PUT':
        print("INCOMING PUT REQUEST!")

@app.route('/home', methods=['GET'])
def home_get():
    return render_template('home.html', title="Home")

@app.route('/home', methods=['POST'])
def home_post():
    return render_template('home.html', title="Home")

@app.route('/home', methods=['PUT'])
def home_put():
    print("Request: {}".format(request))
    print("Request endpoint: {}".format(request.endpoint))
    print("Request method: {}".format(request.method))
    print("Request method type: {}".format(type(request.method)))
    print("Request data: {}".format(request.data))
    print("Request values: {}".format(request.values))
    print("Request args: {}".format(request.args))
    print("Request cookies: {}".format(request.cookies))
    return "PUT SUCCESS"

@app.route('/update', methods=['POST'])
def update_post():
    receive_bytes = request.data
    png_reader = png.Reader(bytes=receive_bytes)
    png_info = png_reader.read()
    image_name = request.cookies['image_name']
    write_file = open('static/images/{}'.format(image_name), 'wb')
    png_writer = png.Writer(width=png_info[0], height=png_info[1], palette=png_info[3]['palette'])
    png_writer.write(write_file, png_info[2])
    write_file.close()
    return "UPDATE POST SUCCESS!!!!!!"


if __name__ == '__main__':
    app.run()