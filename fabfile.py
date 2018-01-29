from fabric.api import env, cd, local, run, prefix

# nombre de la máquina de producción
env.hosts = ["cloud"]
# env.user
# env.password


def deploy():
    local("git push")
    with cd("~/github-repositories/mkdocs"):
        run("git pull")
    with prefix("source /home/alu5905/.virtualenvs/mkdocs/bin/activate"):
        with cd("~/github-repositories/mkdocs/project"):
            run("mkdocs build")
