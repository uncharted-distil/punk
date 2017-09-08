# Deployment
## Integration with Apache Kafka
For D3M related purposes we provide a template, [kafka wrapper](https://github.com/NewKnowledge/punk/tree/master/d3m/kafka_wrapper), for using primitives with Kafka.

The main file in this template is [kafka_wrapper.py](https://github.com/NewKnowledge/punk/blob/master/d3m/kafka_wrapper/kafka_wrapper.py#L6).
This file provides the function `process_msg` which will process an incoing
message from a Kafka topic and will output a message to be produced back to
kafka.
Thus any processing needed needs to be done within this function alone.

In order to control the consumer and producer topics you will only need to
specify these as environmental variables in [environment.env](https://github.com/NewKnowledge/punk/blob/master/d3m/kafka_wrapper/environment.env).

Finally, any python dependencies go in the `requirements.txt`.


**For a complete dev envirnoment (Dockerized + primitive + Kafka) you can check  out [sample integration with kafka](https://github.com/NewKnowledge/punk/tree/master/d3m/sample_primitive_delivering_to_kafka)** In this example, you will have an end-to-end environment for development. There are three componenets to it:
* `Kafka`: Dockerized Kafka cluster
* `Primitive`: Sample on how to use a primitive in this context. See [kafka wrapper](https://github.com/NewKnowledge/punk/tree/master/d3m/kafka_wrapper).
* `sample client`: A small python app which will send a dataset to be consumed
  by a primitive and consequently wait for a response to be sent back.  


# [Submitting Primitives to D3M](https://datadrivendiscovery.org/wiki/display/gov/Primitive+Submission+Process)

1. Fork the official [`primitives_repo`](https://gitlab.datadrivendiscovery.org/jpl/primitives_repo)
 * This repo will only contain the `primitive.json` annotations file and `Dockerfile` in the case of Docker primitives.

2. Write your code
 * Make it public.

3. Write annotations file.
 * If you want an exaple the annotations files are included in this repo;
   search for `*.json` files.
 * Look over the [annotation schema](https://datadrivendiscovery.org/wiki/display/gov/Primitives+Annotation+Schema)
 * Be sure to specify not only the language but the version you are using.
 * One of the fields in the annotations filed is `uuid`, the convention we are
    using to generate these ids is:
```
import uuid

base_uuid = uuid.uuid3(uuid.NAMESPACE_DNS, "datadrivendiscovery.org")
uuid.uuid3(base_uuid, "punk.feature_extraction.pca.pca_feature_exatraction"+"0.1.0")
```

4. Validate your annotations file.
 * For example,
```
curl -u <username> -i -H "Content-Type: application/json" -X POST -d "@primitive.json" https://marvin.datadrivendiscovery.org/primitives/validate
```
5. Last step, go back to the [`primitives_repo`](https://gitlab.datadrivendiscovery.org/jpl/primitives_repo) and create a merge request against the master branch.



# OpenStack
* For instructions on how to use [Openstack](https://datadrivendiscovery.org/wiki/display/gov/OpenStack+Guide)
 * [VPN](https://datadrivendiscovery.org/wiki/display/gov/Connect+to+VPN)

Run `vpnc`,
```
ssh -l ubuntu -i {name of keypair}.pem {associated IP address for instance}
```



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
