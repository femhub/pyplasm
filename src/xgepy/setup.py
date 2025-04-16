import os, sys, shutil

PROJECT_VERSION = "3.0.21"

this_dir = os.path.dirname(os.path.abspath(__file__))


# ///////////////////////////////////////////////////////////////
def DoSetup():
    shutil.rmtree("./build", ignore_errors=True)
    shutil.rmtree("./dist", ignore_errors=True)
    shutil.rmtree("./pyplasm.egg-info", ignore_errors=True)
    shutil.rmtree("./__pycache__", ignore_errors=True)
    shutil.rmtree("./examples/__pycache__", ignore_errors=True)

    # findFilesInCurrentDirectory
    def findFilesInCurrentDirectory():
        ret = []
        for dirpath, __dirnames__, filenames in os.walk("."):
            for filename in filenames:
                file = os.path.abspath(os.path.join(dirpath, filename))
                ret.append(file)
        return ret

    from setuptools import setup

    setup(
        name="pyplasm",
        description="Plasm is a design language for geometric and solid parametric design, developed by the CAD Group at the Universities La Sapienza and Roma Tre in Italy",
        version=PROJECT_VERSION,
        url="https://github.com/plasm-language/pyplasm",
        author="Giorgio Scorzelli",
        author_email="scorzell@dia.uniroma3.it",
        packages=["pyplasm"],
        package_dir={"pyplasm": "."},
        package_data={"pyplasm": findFilesInCurrentDirectory()},
        platforms=["Linux"],
        license="GPL",
    )


# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    DoSetup()
    sys.exit(0)
