# ML - API
Machine learning API para clasificar vinos utilizando el algoritmo de K-Medias.
El API es implementando en FastAPI y puede ser mantenido en Docker.

Requisitos:
- Docker

### Para iniciar el API con Docker 

```
docker build . -t ml-api
```

```
docker run -p 8080:8080 ml-api
```

### Para probar el API con curl
```
curl --location 'http://127.0.0.1:8080/predict' \
--header 'Content-Type: application/json' \
--data '{
    "fix_acid": -0.52836,
    "vol_acid": 0.961877,
    "cit_acid": -1.391472,
    "res_sugar": -0.453218,
    "chlor": -0.243707,
    "free_sulf": -0.466193,
    "tot_sulf": -0.379133,
    "dens": 0.558274,
    "pH": 1.288643,
    "sulph": -0.579207,
    "alc": -0.960246,
    "qual": -0.787823

}'
```