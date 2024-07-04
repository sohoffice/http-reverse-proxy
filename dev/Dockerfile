
FROM python:3.11.7

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
ADD ./src /app/
COPY ./dev/init.sh /app/

RUN pip install -r requirements.txt \
    && chmod 755 /app/init.sh

EXPOSE 8080
 
ENTRYPOINT ["/app/init.sh"]
