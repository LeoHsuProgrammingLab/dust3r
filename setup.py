from setuptools import setup, find_packages

print('Found packages:', find_packages())
setup(
    description='DUSt3R as a package',
    name='dust3r',
    version='1.0',    
    packages=find_packages(),
    install_requires=[
        'torch==2.5.1',
        'torchvision>=0.16.0',
        'roma',
        'gradio==4.44.1',
        'matplotlib',
        'tqdm',
        'opencv-python',
        'scipy',
        'einops',
        'trimesh',
        'tensorboard',
        'pyglet<2',
        'huggingface-hub[torch]>=0.22',
    ],
    extras_require={
        'all': [
            'croco @ git+https://github.com/hongsukchoi/croco.git'
        ],
    },
)
