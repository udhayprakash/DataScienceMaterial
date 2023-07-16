FROM continuumio/miniconda3:4.10.3p1

RUN conda install pandas

CMD jupyter notebook