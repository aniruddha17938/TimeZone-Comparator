from flask import Flask, render_template, request
import pytz
from datetime import datetime

app = Flask(__name__)
timezones = pytz.all_timezones

@app.route("/", methods=["GET", "POST"])
def index():
    source_time = None
    target_time = None
    source_zone = None
    target_zone = None

    if request.method == "POST":
        source_zone = request.form.get("source_timezone")
        target_zone = request.form.get("target_timezone")

        if source_zone in timezones and target_zone in timezones:
            utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)

            # Convert to source timezone
            source_dt = utc_now.astimezone(pytz.timezone(source_zone))
            source_time = source_dt.strftime("%Y-%m-%dT%H:%M:%S")

            # Convert to target timezone
            target_dt = utc_now.astimezone(pytz.timezone(target_zone))
            target_time = target_dt.strftime("%Y-%m-%dT%H:%M:%S")

    return render_template(
        "index.html",
        timezones=timezones,
        source_timezone=source_zone,
        target_timezone=target_zone,
        source_time=source_time,
        target_time=target_time,
    )

if __name__ == "__main__":
    app.run(debug=True)
