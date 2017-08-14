# UUID
```
import uuid

uuid.uuid3(uuid.NAMESPACE_URL, "datadrivendiscovery.org/"+"punk.feature_extraction.pca.pca_feature_exatraction"+"0.1.0")
```

# Validate
```
curl -u jochoa -i -H "Content-Type: application/json" -X POST -d "@primitive.json" https://marvin.datadrivendiscovery.org/primitives/validate
```

# PyPi
`vi  ~/.pypirc`
```
[pypi]
username = <username>
password = <password>

```

then do,
```
python setup.py sdist

python setup.py bdist_wheel

twine upload dist/*

```

# References

* Primitive Submission Process https://datadrivendiscovery.org/wiki/display/gov/Primitive+Submission+Process

* Primitives Annotation Schema
  https://datadrivendiscovery.org/wiki/display/gov/Primitives+Annotation+Schema

* Repo https://gitlab.datadrivendiscovery.org/jpl/primitives_repo



# Dev Notes
## Feature selection
## General
* Make object to chose between GridSearch and Bayesian Optimization.

## Datasets
* For Bayesian optimization based on data distribution -> get a good schema for
  dataset organization
 * https://archive.ics.uci.edu/ml/datasets/
 * https://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes

