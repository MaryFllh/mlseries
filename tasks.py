from invoke import task

file_paths = "ml/ server/ deploy/ shared_utils/ tasks.py"


@task
def tests(cmd):
    cmd.run("pytest")


@task
def mltests(cmd):
    """
    Used by ml_unittest.yml to seperate the actions and make debugging easier
    """
    cmd.run("pytest ml/")


@task
def servertests(cmd):
    """
    Used by server_unittest.yml to seperate the actions and make debugging easier
    """
    cmd.run("pytest server/")


@task
def lint(cmd):
    cmd.run(f"flake8 --ignore E501 --count --statistics {file_paths}")


@task
def lintfix(cmd):
    cmd.run(f"black {file_paths}")
    cmd.run(f"isort -rc {file_paths}")
