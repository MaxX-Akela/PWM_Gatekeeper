[Unit]
Description=Clover demo application

[Service]
ExecStart=/bin/bash -c ". @(InstallationPrefix)/setup.bash; \
                      ROS_HOSTNAME=`hostname`.local exec stdbuf -o L roslaunch @(Name) main.launch --wait --screen --skip-log-check"
Restart=on-failure
RestartSec=3

[Install]
WantedBy=multi-user.target
