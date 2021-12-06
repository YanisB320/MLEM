# MLEM

## HOW TO USE

You can run the following command at the root to launch the project:
```shell
./launch.sh
```

This script does the following stuff:
- create virtual env and install ```requirements.txt```
- install kafka
- launch zookeeper and kafka
- create topic
- sends training and predict messages to our consumers with python scripts
- uninstall kafka

You can ^C to stop it.
