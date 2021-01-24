from flask import Flask, url_for, render_template, redirect
from .forms import ListingForm


app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')


@app.route("/listing", methods=["GET", "POST"])
def listing():
    """Standard `listing` form."""
    form = ListingForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "contact.jinja2",
        form=form,
        template="form-template"
    )
