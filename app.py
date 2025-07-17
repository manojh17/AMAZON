from flask import Flask, render_template
import os
app = Flask(__name__)

# Sample product data
products = [
    {
        "title": "boAt Rockerz 255 Pro+ Wireless",
        "image": "https://m.media-amazon.com/images/I/51HBom8xz7L._SL1500_.jpg",
        "link": "https://www.amazon.in/dp/B08X1Z1Q2B?tag=your-affiliate-id"
    },
    {
        "title": "Mi Smart Band 6",
        "image": "https://m.media-amazon.com/images/I/71X8NdnCsvL._SL1500_.jpg",
        "link": "https://www.amazon.in/dp/B09B1F4WBS?tag=your-affiliate-id"
    },
    {
        "title": "Noise ColorFit Pulse Grand",
        "image": "https://m.media-amazon.com/images/I/619f09kK7tL._SL1500_.jpg",
        "link": "https://www.amazon.in/dp/B09R3L9DPF?tag=your-affiliate-id"
    }
]

@app.route('/')
def home():
    return render_template('index.html', products=products)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
