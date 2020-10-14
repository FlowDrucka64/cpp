from subprocess import run


def build_container(tag_name, dockerfile, cwd, nocache=False, push=False):
    if nocache:
        no_cache_str = "--no-cache"
    else:
        no_cache_str = ""

    build_cmd = [
        "docker build",
        no_cache_str,
        "-t {}".format(tag_name),
        "-f {}".format(dockerfile),
        ".",
    ]
    build_cmd = " ".join(build_cmd)

    print(build_cmd)
    run(
        build_cmd,
        shell=True,
        check=True,
        env={"DOCKER_BUILDKIT": "1"},
        cwd=cwd,
    )

    if push:
        push_container(tag_name)


def push_container(tag_name):
    cmd = "docker push {}".format(tag_name)

    print(cmd)
    run(
        cmd,
        shell=True,
        check=True,
    )
