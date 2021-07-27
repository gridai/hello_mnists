# Hello MNIST in 3 Frameworks

Simple MNIST classifier written in PyTorch, PyTorch Lightning, and Keras.

## Install Dependencies

```bash
conda create --yes --name mnist python=3.8
conda activate mnist
pip install -r requirements.txt
pip install lightning-grid --upgrade
```

## PyTorch

```bash
# Local Run
python pytorch.py

# Grid.ai Run
grid run pytorch.py
```

# PyTorch Lightning

```bash
# Local Run
python pl_mnist.py

# Grid.ai Run
grid run pl_mnist.py
```

## Keras

```bash
# Local Run
python keras.py

# Grid.ai Run
grid run keras.py
```
