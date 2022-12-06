# QR and CODE128 generator

This Python 3.11. function is intended to create QR codes as well as CODE128 barcodes as PNG files.

It runs as a serverless function and is built upon Googles' `function-framework`.

To create barcodes, I use `treepoem` which is a wrapper around BWIPP and Ghostscript.

**Disclaimer: This code is intended for learning on how to create file buffers and returning them within web servers. I am not responsible if you break something using this.**

## Running locally

To run and debug your function locally, install the `functions-framework`:

```bash
  pip install functions-framework
```

And then start up a local development server:

```bash
  functions-framework --target entrypoint --debug
```

### Containerized

You can package the function into a slim container and run it from there. I pre-built a container version from the [Dockerfile](Dockerfile) inside this repository.

```bash
  docker run -ti --rm --port 8080:8080 torbendury/qr-barcode-generator:0.0.2
```

If you would like to build the container yourself, enter the following command into your terminal:

```bash
  docker build -t torbendury/qr-barcode-generator:0.0.2-snapshot
```

## Security

For security scans, I use `bandit`. This is a tool that used to be maintained by the OpenStack, but was moved to PyCQA and resides [here](https://bandit.readthedocs.io/en/latest/start.html).

Here is the latest output:

```bash
Run started:2022-12-06 20:01:06.542299

Test results:
        No issues identified.

Code scanned:
        Total lines of code: 47
        Total lines skipped (#nosec): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0
                Low: 0
                Medium: 0
                High: 0
        Total issues (by confidence):
                Undefined: 0
                Low: 0
                Medium: 0
                High: 0
Files skipped (0):
```

## Contributing

Contributions are always welcome! If you'd like to contribute, fork the repository and create a pull request. If you have any other considerations, open up a GitHub issue.

## Links

- [functions-framework](https://github.com/GoogleCloudPlatform/functions-framework-python)
