FROM pypy:latest
WORKDIR /app
copy . /app
CMD python semantic.py