# thoughtworks_demo

* Python Flask used, as i have no idea about java web
* jenkins multibranch pipeline used


# environment variables

just 2 env vars used for parameters build in jenkins
* string defaultValue: 'latest', description: 'the repo version we want to', name: 'tag', trim: false
* string defaultValue: '3333', description: 'the publish port for proxy container', name: 'HTTP_PUBLISH_PORT', trim: false


# environ

accord to the git repo branch name, there are 3 env
* master (production)
* dev
* testing 

in the app, there are 3 config class, too.


# the output

* accord to environ, there are 2 image for each, one is app, the other is proxy used for static content, like this

    ![cicd-image](https://liwb-csdn.oss-cn-hangzhou.aliyuncs.com/cicd-image.png)

