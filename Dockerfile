FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    git

# install chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN sudo apt install ./google-chrome-stable_current_amd64.deb -y

# install chromedriver
ARG CHROME_MAJOR_VERSION=$(google-chrome-stable --version | ruby -e 'puts $stdin.read[/\d+/]')
ARG CHROMEDRIVER_VERSION=$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_MAJOR_VERSION})
RUN wget https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN sudo mv chromedriver /usr/local/bin/

#RUN pip3 install pyyaml

COPY download_league.py /usr/bin/download_league.py

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]