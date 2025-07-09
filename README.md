 Football_analysis

 ## 🚀 How to Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/JamesMensah740/Football_analysis.git
cd Football_analysis

python -m venv .venv
source .venv/bin/activate     # On Windows: .venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py

file structure 
Football_analysis/
│
├── app.py                      # Main Streamlit app
├── requirements.txt            # Python dependencies
├── .gitignore
├── utils/                      # Modular data loaders
│   ├── fbref_loader.py
│   ├── whoscored_loader.py
│   ├── ...
└── README.md                   # You are here
