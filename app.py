from flask import Flask
from API.views import api_blueprint
from GET.views import get_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(get_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def error_404(error_code):
    return f"Такая страница не найдена {error_code}"


@app.errorhandler(500)
def error_500(error_code):
    return f"Ошибка сервера {error_code}"


app.run(debug=True)
