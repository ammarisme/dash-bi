FROM python:3.9



# setting working directory
RUN mkdir /app
WORKDIR /app



# updating kernal database
RUN apt-get update \
&& apt-get install unixodbc -y \
&& apt-get install unixodbc-dev -y \
&& apt-get install freetds-dev -y \
&& apt-get install freetds-bin -y \
&& apt-get install tdsodbc -y \
&& apt-get install --reinstall build-essential -y



# populate "ocbcinst.ini" as this is where ODBC driver config sits
RUN echo "[FreeTDS]\n\
Description = FreeTDS Driver\n\
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\n\
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbcinst.ini



# copying the requirements.txt to working directory
COPY requirements.txt ./requirements.txt



# installing pip packages
RUN pip install -r requirements.txt



# copying the files
COPY * /app/



# running the app
CMD python index.py
# CMD gunicorn -b 0.0.0.0:8000 index:server