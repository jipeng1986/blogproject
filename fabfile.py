"""
作者    ：Jimingpeng
创建时间：2018/9/4  17:33 
"""

from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "https://github.com/jipeng1986/blogproject.git"

env.user = '312911698@qq.com'
env.password = 'qwer1234'

# 填写你自己的主机对应的域名
env.hosts = ['60.205.190.158']

# 一般情况下为 22 端口，如果非 22 端口请查看你的主机服务提供商提供的信息
env.port = '22'


def deploy():
    source_folder = '/home/jmp/sites/jmp86.top/blogproject'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('restart gunicorn-jmp86.top')
    sudo('service nginx reload')
