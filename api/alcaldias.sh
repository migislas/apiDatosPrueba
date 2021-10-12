#!/bin/sh

url="https://datos.cdmx.gob.mx/dataset/239c78c0-e456-4bc3-806f-e33e71371bad/resource/0e6a8032-efb2-4ef8-8fce-2cb75e48976b/download/limite_de_las_alcaldias.zip"
mkdir ./alcaldiasm                         && \
cd ./alcaldiasm                            && \
curl -sS $url > unidadesMetrobus.zip && \
unzip unidadesMetrobus.zip                                  && \
rm unidadesMetrobus.zip