import requests

def send_image(image):
    with open(image, 'rb') as f:
        requests.post('http://127.0.0.1:5000/update', data=f, cookies={'image_name': 'an_image.png'})

if __name__ == '__main__':
    send_image('test_image.png')