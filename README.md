# Render Blender 3D scenes in the cloud (using Docker)

A simple web app that renders a [Blender](http://www.blender.org/) 3D scene with custom text.

Run with `docker run -p 8080:8080 gcr.io/as-a-service-dev/render`

[![Run on Google Cloud](https://storage.googleapis.com/cloudrun/button.svg)](https://deploy.cloud.run)

## API

### URL parameters:

* `text`: The text to render, defaults to `HELLO`.
* `scene`: the name of the `.blend` file to render (without the extension), defaults to `basic`, other supported values are `outrun` and `outrun-filter`.

Example: `/?text=OUTRUN&scene=outrun`

### Bring your own 3D scene:

1. Create a Blender scene, your scene must contain a text object with the name `Text`,
2. Add your `.blend` file in the `models/` folder,

## Running the server locally

* Build with `docker build . -t render`
* Start with `docker run -p 8080:8080 render`
* Open in your browser at `http://localhost:8080/?text=Hey`

![Cloud Build](https://badger-l7zawt5jsq-uw.a.run.app/build/status?project=as-a-service-dev&id=c19e0b78-b8f0-4ff2-bccb-9b694837d0fc)
