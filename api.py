from concurrent.futures import process
from tabnanny import process_tokens
from venv import create
from saagieapi import SaagieApi

saagie = SaagieApi(
                    url_saagie="https://demo-workspace.a4.saagie.io/",
                    id_platform="2",
                    user="ESTIAM_G10_johnny.hu",
                    password="Goyave2020",
                    realm="demo")

def get_projects():
    projectlist = saagie.projects.list()
    return projectlist

def get_project_data(project_id):
    project_data = saagie.projects.get_info(project_id)['project']
    project_data['jobs'] = saagie.jobs.list_for_project(project_id,2)['jobs']
    project_data['apps'] = saagie.apps.list_for_project(project_id)['labWebApps']
    project_data['rights'] = saagie.projects.get_rights(project_id)['rights']

    return project_data

def copy_projects(projectid):
    project_data = get_project_data(projectid)
    projects = saagie.projects.list()

    count = 0
    for project in projects['projects']:
        if '[ESTIAM] G10 Hackathon' in project['name']:
            count += 1

    newname = project_data['name'] + " - Copy (" + str(count) +")"
    groupname = project_data['rights'][0]['name']
    grouperole = "Manager" #project_data['Rights'][0]['role']
    description = project_data['description']
    jobs = {"saagie":["python"]}
    apps = {"saagie":["[Lab] Jupyter Notebook with Spark"]}

    joblist = project_data['jobs']
    applist = project_data['apps']

    saagie.projects.create(newname, groupname, grouperole, description, jobs, apps)

    # for job in joblist:
    #     techid = job['technology']['id']
    #     jobtech = (saagie.jobs.get_job_technology(techid)['technology']['label'])
    #     jobname = job['name'] + "Copy ("+str(count)+")"
    #     jobcategory = (job['category'])
    #     jobruntime = (job['versions'][0]['runtimeVersion'])
    #     jobcommand = (job['versions'][0]['commandLine'])
    #     jobreleasenote = (job['versions'][0]['releaseNote'])
    #     jobresources = (job['resources'])
    #     jobpath = "C:\\Users\\Mathieu RANIERI\\OneDrive - ESTIAM\\Documents\\SaagiAPI\\api.py"

    # saagie.jobs.create(jobname, projectid, jobpath, "", jobcategory, jobtech, "Saagie", jobruntime, jobcommand, jobreleasenote, "", "", None, "UTC", jobresources, None, None)

    return "Copy successfull !"