FROM python:3
RUN mkdir /root/macio/
COPY . /root/macio/
RUN ls -la /root/macio/venv
RUN ls -la /root/macio/venv/bin
RUN ls -la /root/macio/
RUN pip install requests
RUN /bin/bash -c "source /root/macio/venv/bin/activate"
CMD [ "python", "/root/macio/main.py" ]