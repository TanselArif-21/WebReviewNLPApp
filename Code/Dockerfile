FROM python:3.6

WORKDIR /Code

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8080

COPY . /Code

ENTRYPOINT ["streamlit","run"]

CMD streamlit run --server.port 8080 --server.enableCORS false app.py