# Diffusion Models with PyTorch
This work is derived from DeepFindr https://www.youtube.com/watch?v=a4Yfz2FxXiY

## Neural Network Background

Three types of network:

### Generative Adversarial Networks *(GAN)*:

- **Pro:** High-quality samples and fast sampling.
- **Con:** Lack of mode coverage/diversity.

### Denoting Diffusion Models:

- **Pro:** High-quality samples and mode coverage/diversity.
- **Con:** Lack of fast sampling.

### Variational Autoencoders, Normalizing Flows

- **Pro:** Fast sampling and mode coverage/diversity.
- **Con:** Lack of high-quality samples.

## What is Diffusion Model

1. The **diffusion model** works by *destroying* the input until noise is left over. It then recovers the image from the
   noise using the neural network.
2. The diffusion model does not have very fast sampling speed because of the sequential reverse process.
3. It is much slower than GAN and VAEs

## Build a simple diffusion model

#### Important Papers

1. ***Demonising Diffusion Probabilistic Models***
2. ***Diffusion Models Beat GANs on Image Synthesis***