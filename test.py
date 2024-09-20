rom fabric import Connection, task

CONNECTION_PROPERTIES = {
"host": "192.16.10.1",
"user": "ec2aws",
"password": "user_login_pass"
"connect_kwargs": {
"key_filename": "RSA file path"
},
}

@task
def run_pwd(ctx):
with Connection(**CONNECTION_PROPERTIES) as c:
c.run("pwd")
