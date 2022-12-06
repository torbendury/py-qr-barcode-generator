# START BUILD OF BASE IMAGE
FROM python:3.11-slim as build

# least privilege user
RUN groupadd -g 999 python && \
    useradd -r -u 999 -g python python

ENV APP_HOME /app
ENV PYTHONUNBUFFERED TRUE

# update base image and install dependencies
RUN apt update && apt upgrade -y
RUN apt install -y --no-install-recommends \
    ghostscript

# add virtual environment for better isolation
WORKDIR ${APP_HOME}
RUN python -m venv ${APP_HOME}/venv
ENV PATH="${APP_HOME}/venv/bin:$PATH"

# add pip dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt


# END BUILD, START PACKAGING

FROM python:3.11-slim
ENV APP_HOME /app
WORKDIR ${APP_HOME}
# copy everything from build layer
COPY --from=build ${APP_HOME}/venv ./venv
# add code
COPY . .

USER 999

ENV PATH="${APP_HOME}/venv/bin:$PATH"
CMD exec functions-framework --target=entrypoint