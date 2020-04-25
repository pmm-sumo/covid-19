FROM jupyter/scipy-notebook

COPY . /covid
USER root
RUN chmod 1777 /covid
WORKDIR /covid
RUN pip install -r requirements.txt
CMD /covid/update-and-push.sh

