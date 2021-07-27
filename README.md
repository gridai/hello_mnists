# Hello MNIST in 3 Frameworks

Simple MNIST classifier written in PyTorch, PyTorch Lightning, and Keras.

# Install Dependencies

```bash
conda create --yes --name mnist python=3.8
conda activate mnist
pip install -r requirements.txt
pip install lightning-grid
```

# PyTorch

```bash
# Local Run
python pytorch.py

# Grid.ai Run
grid run pytorch.py | tee /tmp/grid.run.log

# Grid.ai Run Monitor
RUN_NAME=$(grep /tmp/grid_name grid.run.log | cut -d':' -f 2 | sed -e 's/^[[:space:]]*//')
watch grid status --details $RUN_NAME
grid history | grep $RUN_NAME
grid logs ${RUN_NAME}-exp0 | tee /tmp/grid.exp0.log
```

# PyTorch Lightning

```bash
# Local Run
python pl_mnist.py

# Grid.ai Run
grid run pl_mnist.py | tee /tmp/grid.run.log

# Grid.ai Run Monitor
RUN_NAME=$(grep /tmp/grid_name grid.run.log | cut -d':' -f 2 | sed -e 's/^[[:space:]]*//')
watch grid status --details $RUN_NAME
grid history | grep $RUN_NAME
grid logs ${RUN_NAME}-exp0 | tee /tmp/grid.exp0.log
```

# Keras

```bash
# Local Run
python keras.py

# Grid.ai Run
grid run keras.py | tee /tmp/grid.run.log

# Grid.ai Run Monitor
RUN_NAME=$(grep /tmp/grid_name grid.run.log | cut -d':' -f 2 | sed -e 's/^[[:space:]]*//')
watch grid status --details $RUN_NAME
grid history | grep $RUN_NAME
grid logs ${RUN_NAME}-exp0 | tee /tmp/grid.exp0.log
```
