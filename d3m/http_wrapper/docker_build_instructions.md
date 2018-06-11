#Building a new Docker image

1. Build image: `docker build -t http_features .` 
1. Run to test: `docker run -p 5000:5000 http_features`
1. Login to registry: `docker login primitives.azurecr.io -u primitives -p <password>`
1. Tag docker image: `docker tag http_features primitives.azurecr.io/http_features:<version-number>`
1. Push docker image to registry: `docker push primitives.azurecr.io/http_features:<version-number>`