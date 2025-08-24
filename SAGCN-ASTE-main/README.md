# SAGCN


## Requirements

- python==3.7.6

- torch==1.4.0
- transformers==3.4.0
- argparse==1.1

## Training

To train the SAGCN model, run:

```
cd SAGCN/code
sh run.sh
```
or
```
python main.py --mode train --dataset res14 --batch_size 16 --epochs 100 --model_dir savemodel/ --seed 1000 --pooling avg --prefix ../data/D2/
```

## Inference

To test the performance of SAGCN, you only need to modify the --mode parameter.
```
python main.py --mode test --dataset res14 --batch_size 16 --epochs 100 --model_dir savemodel/ --seed 1000 --pooling avg --prefix ../data/D2/
```

