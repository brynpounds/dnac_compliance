from flask import Flask, render_template, send_from_directory, request, url_for, flash, redirect
import json
import requests
import time
import subprocess
import shutil
from subprocess import PIPE
from dotenv import load_dotenv
from configuration_template import DNAC_URL, DNAC_PASS, DNAC_USER
from compliance_mon import *
from difference_engine import *
from system_setup import *
load_dotenv()

try:
    from API import (app,
                     api,
                     HealthController,docs,
                     DNACenterCompliance,
                     WeatherController,
                     DNACTokenController,
                     get_all_device_infoController,
                     get_device_infoController,
                     delete_deviceController,
                     get_project_idController,
                     get_project_infoController,
                     create_commit_templateController,
                     commit_templateController,
                     update_commit_templateController,
                     upload_templateController,
                     delete_templateController,
                     get_all_template_infoController,
                     get_template_name_infoController,
                     get_template_idController,
                     get_template_id_versionController,
                     get_template_id_versionController,
                     deploy_templateController,
                     check_template_deployment_statusController,
                     get_client_infoController,
                     locate_client_ipController,
                     get_device_id_nameController,
                     get_device_statusController,
                     get_device_management_ipController,
                     get_device_id_snController,
                     get_device_locationController,
                     create_siteController,
                     get_site_idController,
                     create_buildingController,
                     get_building_idController,
                     create_floorController,
                     get_floor_idController,
                     assign_device_sn_buildingController,
                     assign_device_name_buildingController,
                     get_geo_infoController,
                     sync_deviceController,
                     check_task_id_statusController,
                     check_task_id_outputController,
                     create_path_traceController,
                     get_path_trace_infoController,
                     check_ipv4_network_interfaceController,
                     get_device_info_ipController,
                     get_legit_cli_command_runnerController,
                     get_content_file_idController,
                     get_output_command_runnerController,
                     get_all_configsController,
                     get_device_configController,
                     check_ipv4_addressController,
                     check_ipv4_address_configsController,
                     check_ipv4_duplicateController,
                     get_device_healthController,
                     pnp_get_device_countController,
                     pnp_get_device_listController,
                     pnp_claim_ap_siteController,
                     pnp_delete_provisioned_deviceController,
                     pnp_get_device_infoController,
                     get_physical_topologyController
                     )
except Exception as e:
    print("Modules are Missing : {} ".format(e))
    
messages=["howdy"]
    
@app.route("/")
def home():
    my_var = "Welcome to DNA Center Compliance Lite"
    result = subprocess.run(["ls", "-l", "/app/DNAC-CompMon-Data/Reports", "/dev/null"], stdout=PIPE, stderr=PIPE)
    contents = result.stdout.decode('utf8')
    return render_template("home.html", message = contents.split("total")[1])

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/configure_system", methods=('GET', 'POST'))
#modified to use existing code
def configure_system():
    global DNAC_IP
    global DNAC_USER
    global DNAC_PASS
    global DNAC_URL
    if request.method == 'POST':
        DNAC_IP = request.form['ip_address']
        DNAC_USER = request.form['username']
        DNAC_PASS = request.form['password']
        # Define the path to the Python file to update
        PATH = "./configuration_template.py"
        if not DNAC_IP:
            flash('IP Address is required!')
        elif not DNAC_USER:
            flash('Username is required!')        
        elif not DNAC_PASS:
            flash('Password is required!')
        else:
            DNAC_setup_app(PATH,DNAC_IP,DNAC_USER,DNAC_PASS)
            return redirect(url_for('status'))    
    return render_template("configure_system.html",ip_address=DNAC_IP,username=DNAC_USER,password=DNAC_PASS )

@app.route("/report", methods=('GET', 'POST'))
#modified to use existing code
def serve_report():
    if request.method == 'POST':
        #message = "Reports..."
        #result = subprocess.run(["ls", "-l", "/app/DNAC-CompMon-Data/Reports/", "/dev/null"], stdout=PIPE, stderr=PIPE)
        #contents = result.stdout.decode('utf8')    
        comp_main()
        return redirect('report.html') 
        #return render_template('report.html', message=message, reports=contents.split("total")[1])
    message = "Reports..."
    result = subprocess.run(["ls", "-l", "/app/DNAC-CompMon-Data/Reports/", "/dev/null"], stdout=PIPE, stderr=PIPE)
    contents = result.stdout.decode('utf8')
    return render_template('report.html', message=message, reports=contents.split("total")[1])

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/status")
def status():
    file1 = open('/app/configuration_template.py', 'r')
    contents = file1.read()
    file1.close()
    url = 'http://localhost:8080/health_check'
    response = requests.get(url)
    our_response_content = response.content.decode('utf8')
    proper_json_response = json.loads(our_response_content)
    return render_template("status.html", testing=proper_json_response, DNAC_URL=DNAC_URL, DNAC_USER=DNAC_USER, messages=messages, contents=contents)

@app.route("/weather")
def weather():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    
    json_data = {
        'city': 'Overland Park',
        'zip': '66085',
    }
    
    response = requests.post('http://localhost:8080/check_weather', headers=headers, json=json_data)    
    #url = 'http://192.241.187.136/data/2.5/weather?zip=66085,us&appid=11a1aac6bc7d01ea13f0d2a8e78c227e'
    #my_response = requests.get(url)
    our_response_content = response.content.decode('utf8')
    proper_json_response = json.loads(our_response_content)
    return render_template("weather.html", message="HOWDY", testing=proper_json_response)

api.add_resource(HealthController, '/health_check')
docs.register(HealthController)

api.add_resource(DNACenterCompliance, '/DNA_Center_Compliance_Lite')
docs.register(DNACenterCompliance)

api.add_resource(WeatherController, '/check_weather')
docs.register(WeatherController)

api.add_resource(DNACTokenController, '/get_dnac_token')
docs.register(DNACTokenController)

api.add_resource(get_all_device_infoController, '/get_all_device_info')
docs.register(get_all_device_infoController)

api.add_resource(get_device_infoController, '/get_device_info')
docs.register(get_device_infoController)

api.add_resource(delete_deviceController, '/delete_device')
docs.register(delete_deviceController)

api.add_resource(get_project_idController, '/get_project_id')
docs.register(get_project_idController)

api.add_resource(get_project_infoController, '/get_project_info')
docs.register(get_project_infoController)

api.add_resource(create_commit_templateController, '/create_commit_template')
docs.register(create_commit_templateController)

api.add_resource(commit_templateController, '/commit_template')
docs.register(commit_templateController)

api.add_resource(update_commit_templateController, '/update_commit_template')
docs.register(update_commit_templateController)

api.add_resource(upload_templateController, '/upload_template')
docs.register(upload_templateController)

api.add_resource(delete_templateController, '/delete_template')
docs.register(delete_templateController)

api.add_resource(get_all_template_infoController, '/get_all_template_info')
docs.register(get_all_template_infoController)

api.add_resource(get_template_name_infoController, '/get_template_name_info')
docs.register(get_template_name_infoController)

api.add_resource(get_template_idController, '/get_template_id')
docs.register(get_template_idController)

api.add_resource(get_template_id_versionController, '/get_template_id_version')
docs.register(get_template_id_versionController)

api.add_resource(deploy_templateController, '/deploy_template')
docs.register(deploy_templateController)

api.add_resource(check_template_deployment_statusController, '/check_template_deployment_status')
docs.register(check_template_deployment_statusController)

api.add_resource(get_client_infoController, '/get_client_info')
docs.register(get_client_infoController)

api.add_resource(locate_client_ipController, '/locate_client_ip')
docs.register(locate_client_ipController)

api.add_resource(get_device_id_nameController, '/get_device_id_name')
docs.register(get_device_id_nameController)

api.add_resource(get_device_statusController, '/get_device_status')
docs.register(get_device_statusController)

api.add_resource(get_device_management_ipController, '/get_device_management_ip')
docs.register(get_device_management_ipController)

api.add_resource(get_device_id_snController, '/get_device_id_sn')
docs.register(get_device_id_snController)

api.add_resource(get_device_locationController, '/get_device_location')
docs.register(get_device_locationController)

api.add_resource(create_siteController, '/create_site')
docs.register(create_siteController)

api.add_resource(get_site_idController, '/get_site_id')
docs.register(get_site_idController)

api.add_resource(create_buildingController, '/create_building')
docs.register(create_buildingController)

api.add_resource(get_building_idController, '/get_building_id')
docs.register(get_building_idController)

api.add_resource(create_floorController, '/create_floor')
docs.register(create_floorController)

api.add_resource(get_floor_idController, '/get_floor_id')
docs.register(get_floor_idController)

api.add_resource(assign_device_sn_buildingController, '/assign_device_sn_building')
docs.register(assign_device_sn_buildingController)

api.add_resource(assign_device_name_buildingController, '/assign_device_name_building')
docs.register(assign_device_name_buildingController)

api.add_resource(get_geo_infoController, '/get_geo_info')
docs.register(get_geo_infoController)

api.add_resource(sync_deviceController, '/sync_device')
docs.register(sync_deviceController)

api.add_resource(check_task_id_statusController, '/check_task_id_status')
docs.register(check_task_id_statusController)

api.add_resource(check_task_id_outputController, '/check_task_id_output')
docs.register(check_task_id_outputController)

api.add_resource(create_path_traceController, '/create_path_trace')
docs.register(create_path_traceController)

api.add_resource(get_path_trace_infoController, '/get_path_trace_info')
docs.register(get_path_trace_infoController)

api.add_resource(check_ipv4_network_interfaceController, '/check_ipv4_network_interface')
docs.register(check_ipv4_network_interfaceController)

api.add_resource(get_device_info_ipController, '/get_device_info_ip')
docs.register(get_device_info_ipController)

api.add_resource(get_legit_cli_command_runnerController, '/get_legit_cli_command_runner')
docs.register(get_legit_cli_command_runnerController)

api.add_resource(get_content_file_idController, '/get_content_file_id')
docs.register(get_content_file_idController)

api.add_resource(get_output_command_runnerController, '/get_output_command_runner')
docs.register(get_output_command_runnerController)

api.add_resource(get_all_configsController, '/get_all_configs')
docs.register(get_all_configsController)

api.add_resource(get_device_configController, '/get_device_config')
docs.register(get_device_configController)

api.add_resource(check_ipv4_addressController, '/check_ipv4_address')
docs.register(check_ipv4_addressController)

api.add_resource(check_ipv4_address_configsController, '/check_ipv4_address_configs')
docs.register(check_ipv4_address_configsController)

api.add_resource(check_ipv4_duplicateController, '/check_ipv4_duplicate')
docs.register(check_ipv4_duplicateController)

api.add_resource(get_device_healthController, '/get_device_health')
docs.register(get_device_healthController)

api.add_resource(pnp_get_device_countController, '/pnp_get_device_count')
docs.register(pnp_get_device_countController)

api.add_resource(pnp_get_device_listController, '/pnp_get_device_list')
docs.register(pnp_get_device_listController)

api.add_resource(pnp_claim_ap_siteController, '/pnp_claim_ap_site')
docs.register(pnp_claim_ap_siteController)

api.add_resource(pnp_delete_provisioned_deviceController, '/pnp_delete_provisioned_device')
docs.register(pnp_delete_provisioned_deviceController)

api.add_resource(pnp_get_device_infoController, '/pnp_get_device_info')
docs.register(pnp_get_device_infoController)

api.add_resource(get_physical_topologyController, '/get_physical_topology')
docs.register(get_physical_topologyController)

if __name__ == '__main__':
    app.run(threaded=True)