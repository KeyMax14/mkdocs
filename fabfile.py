from fabric.api import env, cd, local, run

# nombre de la máquina de producción
env.hosts = ["cloud"]
# env.user
# env.password


def deploy():
    local("git push")
    with cd("~/github-repositories/mkdocs"):
        run("git pull")
        run("source /home/alu5905/.virtualenvs/mkdocs/bin/activate")
	run("mkdocs build")
