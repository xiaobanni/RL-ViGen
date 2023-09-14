# Installation

Clone the RL-ViGen repo:
```
git clone https://github.com/gemcollector/RL-ViGen.git
cd RL-ViGen/
```

Create a conda environment:
```
conda create -n rl-vigen python=3.8
```
Run the installation script:
```
bash setup/install_rlvigen.sh
```

We apply CARLA 0.9.10 which is a stable version in RL-ViGen. The CARLA 0.9.10 should be downloaded first, and place it to the `./third_party` folder, :
```
wget https://carla-releases.s3.eu-west-3.amazonaws.com/Linux/CARLA_0.9.10.tar.gz
mkdir CARLA_0.9.10
tar -zxvf CARLA_0.9.10.tar.gz -C CARLA_0.9.10
```

Install `xvfb` for rendering.

```
sudo apt install xvfb 
```

The algorithms(pieg, sgqn, srm, svea) will use the [Places](http://places2.csail.mit.edu/download.html) dataset for data augmentation, which can be downloaded in by running
```
wget http://data.csail.mit.edu/places/places365/places365standard_easyformat.tar # in third_party folder
tar -xvf places365standard_easyformat.tar
```
After downloading and extracting the data, add your dataset directory to the datasets list in `cfgs/aug_config.cfg`.

See `envs/carlaVGB/carla_README.md` for training and testing.