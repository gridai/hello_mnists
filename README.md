# Hello MNIST in 3 Frameworks

Simple MNIST classifier written in PyTorch, PyTorch Lightning, and Keras.

# Install Dependencies

```bash
conda create --yes --name mnist python=3.8
conda activate mnist
pip install -r requirements.txt
pip install lightning-grid
grid login
```

# PyTorch

```bash
# Local Run
python pytorch.py

# Grid.ai Run
grid run pytorch.py | tee /tmp/grid.run.log
```

# PyTorch Lightning

```bash
# Local Run
python pl_mnist.py

# Grid.ai Run
grid run pl_mnist.py | tee /tmp/grid.run.log
```

# Keras

```bash
# Local Run
python keras.py

# Grid.ai Run
grid run keras.py | tee /tmp/grid.run.log
```

# CIFAR-10 Bonus

```bash
# Local Run
python pl_cifar10.py

# Grid.ai Run
grid run pl_cifar10.py | tee /tmp/grid.run.log
```

# Default Command Line Argument Values per Script

| Argument Name  | keras.py | pl_cifar10.py | pl_mnist.py | pytorch.py| 
|  --:| :--: | :--: | :--: | :--: | 
| --max_epochs | 5 | 10 | 10 | 14| 
| --lr | 1.00E-03 | 1.00E-03 | 1.00E-03 | 1 | 
| --batch_size | 32 | 32 | 32 | 64 | 
| --data_dir | ./data/ | os.getcwd | os.getcwd |  | 
| --num_workers |   | 8 | 8 |  | 
| --gpus |   | 0 | 0 |  | 
| --test_batch_size |   |   |   | 1000| 
| --seed |   |   |   | 1| 
| --save_model |   |   |   | FALSE| 
| --log_interval |   |   |   | 10| 
| --gamma |   |   |   | 0.7| 
| --dry_run |   |   |   | FALSE| 
| --cuda |   |   |   | FALSE | 

# Grid.ai Run Monitor

```bash
RUN_NAME=$(grep grid_name /tmp/grid.run.log | cut -d':' -f 2 | sed -e 's/^[[:space:]]*//')
watch grid status --details $RUN_NAME
grid history | grep $RUN_NAME
grid logs ${RUN_NAME}-exp0 | tee /tmp/grid.exp0.log
```
