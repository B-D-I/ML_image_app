from classification import *
from mitigations import sanity_check, integrity_check
from flask import Flask, render_template, request, render_template_string

app = Flask(__name__, template_folder='templates')


@app.errorhandler(500)
def page_error(e):
    print(e)
    return render_template('500.html'), 500


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def predict():
    try:
        if sanity_check() and integrity_check(model_path):
            image_file = request.files['image_file']
            predict_image_path = "static/images/" + image_file.filename
            image_file.save(predict_image_path)

            img = set_image(predict_image_path)
            scene = prediction(img)
            landing = safe_landing(scene)

            return render_template('index.html', prediction=scene, safe_landing=landing, image=predict_image_path)
        else:
            page_error()
    except Exception as ex:
        page_error(ex)


@app.route('/contact')
def index():
    name = request.args.get('name') or "undefined"
    template = f'''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Contact</title>
</head>
<body>

<h1>Hello User: {name}</h1><br />
<h4>For queries please contact us at: vulnerable@email.com</h4>

</body>
</html>
    '''
    return render_template_string(template)


if __name__ == '__main__':
    app.run(port=3000)
