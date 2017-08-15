# [Submitting Primitives to D3M](https://datadrivendiscovery.org/wiki/display/gov/Primitive+Submission+Process)

1. Fork the official [`primitives_repo`](https://gitlab.datadrivendiscovery.org/jpl/primitives_repo)
 * This repo will only contain the `primitive.json` annotations file and `Dockerfile` in the case of Docker primitives.

2. Write your code
 * Make it public.

3. Write annotations file.
 * If you want an exaple the annotations files are included in this repo;
   search for `*.json` files.
 * Look over the [annotation schema](https://datadrivendiscovery.org/wiki/display/gov/Primitives+Annotation+Schema)
 * One of the fields in the annotations filed is `uuid`, the convention we are
    using to generate these ids is:
```
import uuid

uuid.uuid3(uuid.NAMESPACE_DNS, "datadrivendiscovery.org/"+"punk.feature_extraction.pca.pca_feature_exatraction"+"0.1.0")
```

4. Validate your annotations file.
 * For example,
```
curl -u <username> -i -H "Content-Type: application/json" -X POST -d "@primitive.json" https://marvin.datadrivendiscovery.org/primitives/validate
```
5. Last step, go back to the [`primitives_repo`](https://gitlab.datadrivendiscovery.org/jpl/primitives_repo) and create a merge request against the master branch.



# PyPi: Registering this as a Python package
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
