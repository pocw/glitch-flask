from flask import Flask, Response
import time

app = Flask(__name__)

@app.route('/')
def stream():
    def generate():
        while True:
            # Generate a string with 10,000 characters
            large_text = 'A' * 10000
            # Send the data to the client
            yield f"data: {large_text}\n\n"
            # Wait for 1 second
            time.sleep(1)
    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    # Only used for local testing
    app.run(host='0.0.0.0', port=3000)  # Glitch default port is 3000
