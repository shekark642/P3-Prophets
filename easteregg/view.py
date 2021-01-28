from flask import Flask, render_template, redirect, url_for, request, app
from easteregg import easteregg_bp

app.register_blueprint(easteregg_bp, url_prefix='/easteregg')

@easteregg_bp.route('/easteregg')
def easteregg():
    return render_template("easteregg.html")

if __name__ == "__main__":
    app.run(debug=True)