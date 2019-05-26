# Project Title

Rotten Tomatoes Ratings

### Prerequisites

This program requires EITHER <p>
python 3 or<p>
Docker installed<p>


### Installing

1. If using python. Then the program can be invoked by<p>
python movierate.py <Movie Name><p>
  This will return an error message if the movie rating is not available and returns the following result 
  if the data is available:<p>
  'Rotten Tomatoes rating for the movie <Movie name> is <Movie rating>'<p>
<p>
2. If using docker,<p>
  2.1  A docker build file is provided with the python script. A docker image can be built and run from a command line as below.
  <p>sudo docker build -t movieratedockerimage .
  <p>sudo docker run -ti movieratedockerimage python3 /movierate.py <Movie Name>
    
  2.2 Alternatively a docker image is available on dockerhub, which can be downloaded and run using
  <p>sudo docker pull renu083/dockermovie:latest
  <p>sudo docker run renu083/dockermovie python movierate.py <Movie name>


## Authors
Renuka Nayak
