from invoke import task


@task
def test(ctx):
    cmd = 'py.test -v --cov=carnet --cov-report term-missing tests'
    ctx.run(cmd, pty=True)


@task
def lint(ctx):
    cmd = 'flake8 --ignore=F401 carnet'
    ctx.run(cmd)


@task
def docs_generate(ctx):
    cmd = 'pipenv run sphinx-apidoc -F -e -o docs carnet'
    ctx.run(cmd)


@task
def docs(ctx):
    cmd = 'make -C docs html'
    ctx.run(cmd)


@task
def safety(ctx):
    cmd = 'safety check'
    ctx.run(cmd)


@task
def qa(ctx):
    cmd = 'tox'
    ctx.run(cmd, pty=True)


@task
def dist(ctx):
    cmd = 'python setup.py sdist bdist_wheel'
    ctx.run(cmd)


@task
def readme_rst(ctx):
    cmd = 'pandoc --from=markdown --to=rst README.md -o README.rst'
    ctx.run(cmd)


@task
def pypi_register(ctx):
    cmd = 'python setup.py register -r pypi'
    ctx.run(cmd)


@task
def pypi_upload(ctx):
    cmd = 'python setup.py sdist upload -r pypi'
    ctx.run(cmd)


@task
def pypi_test_register(ctx):
    cmd = 'python setup.py register -r pypitest'
    ctx.run(cmd)


@task
def pypi_test_upload(ctx):
    cmd = 'python setup.py sdist upload -r pypitest'
    ctx.run(cmd)
