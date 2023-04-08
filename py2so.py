import os
import click
from distutils.core import setup
from Cython.Build import cythonize


def find_modules(build_dir="./", build_file=None):

    if build_dir == "__pycache__":
        return []
    
    if os.path.isfile(build_dir):
        if not build_dir.endswith(".py"):
            return []
        if os.path.basename(build_dir).startswith("__"):
            return []
        return [build_dir]

    targets = []
    for f in os.listdir(build_dir):
        if isinstance(build_file, str) and os.path.isfile(os.path.join(build_dir, build_file)):
            targets.append(build_file)
        elif isinstance(build_file, list):
            for _f in build_file:
                full_path = os.path.abspath(os.path.join(build_dir, _f))
                if os.path.isfile(full_path):
                    targets.append(_f)
        else:
            # print(os.path.abspath(os.path.join(build_dir, f)))
            full_path = os.path.abspath(os.path.join(build_dir, f))
            targets.extend(find_modules(full_path))
    return targets



def build(modules):
    build_dir = "build"
    build_tmp_dir = f"{build_dir}/tmp"
    setup(
        author="fanbin.meng",
        version="0.0.1",
        description="build so",
        ext_modules=cythonize(modules, compiler_directives={'language_level' : "3"}),
        script_args=[
            "build_ext",
            "-b", build_dir,
            "-t", build_tmp_dir
        ]
    )


@click.command()
@click.option("--build_dir", default="./example/projects/src")
@click.option("--build_files", default=None)
def main(build_dir, build_files):
    modules = find_modules(build_dir)
    # print(modules)
    build(modules)


if __name__ == "__main__":
    main()