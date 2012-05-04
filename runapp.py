import os

from paste.deploy import loadapp
from waitress import serve

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app = loadapp('config:settings.ini', relative_to='.')
    
    durl = os.environ.get("DATABASE_URL")

    serve(app, host='0.0.0.0', port=port)
