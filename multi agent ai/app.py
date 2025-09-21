from flask import Flask, render_template, request, jsonify
from pipeline import run_pipeline

app = Flask(__name__)

# Serve the frontend page
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Handle pipeline requests (AJAX/Fetch)
@app.route("/process", methods=["POST"])
def process():
    try:
        data = request.get_json()
        user_input = data.get("requirement", "")
        if not user_input:
            return jsonify({"error": "No requirement provided"}), 400

        # run_pipeline returns final structured output
        final_output = run_pipeline(user_input)
        return jsonify({"FinalOutput": final_output})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
