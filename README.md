# Render Blender 3D scenes in the cloud (using Docker)

A simple web service that renders a [Blender](http://www.blender.org/) 3D scene with custom text.

Run with `docker run -p 8080:8080 steren/blender-as-a-service`

## API

### URL parameters:

* `text`: The text to render, defaults to `HELLO`.
* `scene`: the name of the `.blend` file to render (without the extension), defaults to `basic`, other supported values are `outrun` and `outrun-filter`.

Example: `/?text=OUTRUN&scene=outrun`

### Bring your own 3D scene:

1. Create a Blender scene, if your scene contains a text object with the name `Text`, the text will be replaced with the value of the `text` parameter.
2. The service looks for `.blend` files  `/app/models/` folder. You can add your own `.blend` files at build time or mount a volume at runtime.

## Running the server locally

* Build with `docker build . -t steren/blender-as-a-service`
* Start with `docker run -p 8080:8080 steren/blender-as-a-service`
* Open in your browser at `http://localhost:8080/?text=Hey`

