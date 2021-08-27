# Docker best practices

The following is a list of best practices for Docker that are being followed in this project:

- Follow the [Dockerfile best practices guide](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- Use `.dockerignore` to exclude files from the build process.
- Minimise the number of layers in your image.
- Use a `Dockerfile` that is easy to read and maintain.
- Add comments to your `Dockerfile` to help other people understand what it does.
- Use a `Dockerfile` that is as small as possible.
- Use `COPY` instructions instead of `ADD` whenever possible.
- Order the instructions in a way to minimize cache invalidation.
  - Put `COPY` instructions for files that are not changed often (ex: files listing deps) at the top of the `Dockerfile`.
- Use multi-stage builds whenever it makes sense.
- Decouple applications such that each container has only one concern, making it easier to scale horizontally and reuse containers.
- Minimize the build context of the image.
- Use small base image as much as possible.
