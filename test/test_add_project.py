from model.project import Project


import random

def test_add_project(app):
    app.session.login("administrator", "root")
    old_projects = app.soap.get_project_list("administrator", "root")
    new_name = "new "+str(random.randrange(1, 1000))
    project = Project(name=new_name)
    app.project.add_project(project)
    new_projects = app.soap.get_project_list("administrator", "root")
    assert len(old_projects)+1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)



