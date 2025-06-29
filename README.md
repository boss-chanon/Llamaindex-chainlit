# Llamaindex-chainlit
This repository have objective for as an example llama-index and chainlit to inference LLM with Google GeminiAPI

## Setup
1. Create and activate conda environment
```bash
conda create -p ./env python=3.10 -y
conda activate ./env
```
2. Install requirement
```bash
pip install -r ./requirement.txt
```
3. Download example document
```bash
medir ./data
curl https://www.ipcc.ch/report/ar6/wg2/downloads/report/IPCC_AR6_WGII_Chapter03.pdf --output ./data/IPCC_AR6_WGII_Chapter03.pdf
```

## Run
1. Create index
```bash
python create_index.py
```

2. Run app
```bash
chainlit run app.py
```