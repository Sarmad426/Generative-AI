# Diffusion Models

Diffusion models are the generative ai models that are studied under [Computer Vision](/0-AI-ML-Basics/Readme.md#computer-vision). These models have the ability of converting a text prompt into a realistic image. Diffusion is a physics concept which means going from larger intensity to lower intensity.

## How Diffusion Model Works?

Diffusion models add noise to image, and then a trained algorithm removes that noise from the image and gives back the original image. These models are very expensive as they require lot of computational power and extra-ordinary resources.

**Forward Diffusion:**
Compressing the image in latent representation.

**Reverse Diffusion:**
Reversing the image to its previous state.

## Latency

After removing noise from the image, diffusion models convert this image into a vector, whereas vector is just a number or numerical array, this vector is called **Latent Representation**. Whereas Latent is just a word for secret representation.
