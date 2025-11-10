from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        content = toml.loads(content)
        name = content["tool"]["poetry"]["name"]
        license = content["tool"]["poetry"]["license"]
        description = content["tool"]["poetry"]["description"]
        dependencies = list(content["tool"]["poetry"]["dependencies"])
        dev_dependencies = list(content["tool"]["poetry"]["group"]["dev"]["dependencies"])
        authors = list(content["tool"]["poetry"] ["authors"])
        license = content["tool"]["poetry"]["license"]

        project = Project(name,description,license,authors,dependencies, dev_dependencies)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return project
