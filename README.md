# omp
Install Required Libraries:
- Flask: To build the API.
- Pillow: For image processing.
- Transformers & TorchVision: For AI-based image/content classification.
- Pandas: For managing blacklist data.

## Project Structure:
omp-block-app/
│
├── app.py               # Flask API
├── blacklist.csv        # Blacklist file for URLs
├── models.py            # AI classification logic
└── utils.py             # Utility functions (e.g., reading blacklist)