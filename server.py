from flask_app import app

#on/off switch: remener to put your controllers here
# Server imporst entire file 
from flask_app.controllers import user_controller  
from flask_app.controllers import recipe_controller

@app.route('/<path:path>')
def catch_all(path):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(debug=True,port=5001)