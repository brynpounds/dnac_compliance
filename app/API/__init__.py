try:
    from flask import Flask, render_template
    from flask_restful import Resource, Api
    from apispec import APISpec
    from marshmallow import Schema, fields
    from apispec.ext.marshmallow import MarshmallowPlugin
    from flask_apispec.extension import FlaskApiSpec
    from flask_apispec.views import MethodResource
    from flask_apispec import marshal_with, doc, use_kwargs

    from API.ClusterHealth.views import HeathController
    from API.KeithCode.views import KeithController
    from API.KeithCode.views import WeatherController
    from API.KeithCode.views import DNACTokenController
    from API.KeithCode.views import get_all_device_infoController
    from API.KeithCode.views import get_device_infoController
    from API.KeithCode.views import delete_deviceController
    from API.KeithCode.views import get_project_idController
    from API.KeithCode.views import get_project_infoController
    from API.KeithCode.views import create_commit_templateController
    from API.KeithCode.views import commit_templateController
    from API.KeithCode.views import update_commit_templateController
    from API.KeithCode.views import upload_templateController
    from API.KeithCode.views import delete_templateController
    from API.KeithCode.views import get_all_template_infoController
    from API.KeithCode.views import get_template_name_infoController
    from API.KeithCode.views import get_template_idController
    from API.KeithCode.views import get_template_id_versionController
    from API.KeithCode.views import deploy_templateController
    from API.KeithCode.views import check_template_deployment_statusController
    from API.KeithCode.views import get_client_infoController
    from API.KeithCode.views import locate_client_ipController
    from API.KeithCode.views import get_device_id_nameController
    from API.KeithCode.views import get_device_statusController
    from API.KeithCode.views import get_device_management_ipController
    from API.KeithCode.views import get_device_id_snController
    from API.KeithCode.views import get_device_locationController 
    from API.KeithCode.views import create_siteController
    from API.KeithCode.views import get_site_idController
    from API.KeithCode.views import create_buildingController
    from API.KeithCode.views import get_building_idController
    from API.KeithCode.views import create_floorController
    from API.KeithCode.views import get_floor_idController
    from API.KeithCode.views import assign_device_sn_buildingController
    from API.KeithCode.views import assign_device_name_buildingController
    from API.KeithCode.views import get_geo_infoController
    from API.KeithCode.views import sync_deviceController
    from API.KeithCode.views import check_task_id_statusController
    from API.KeithCode.views import check_task_id_outputController
    from API.KeithCode.views import create_path_traceController
    from API.KeithCode.views import get_path_trace_infoController
    from API.KeithCode.views import check_ipv4_network_interfaceController
    from API.KeithCode.views import get_device_info_ipController
    from API.KeithCode.views import get_legit_cli_command_runnerController
    from API.KeithCode.views import get_content_file_idController
    from API.KeithCode.views import get_output_command_runnerController
    from API.KeithCode.views import get_all_configsController
    from API.KeithCode.views import get_device_configController
    from API.KeithCode.views import check_ipv4_addressController
    from API.KeithCode.views import check_ipv4_address_configsController
    from API.KeithCode.views import check_ipv4_duplicateController
    from API.KeithCode.views import get_device_healthController
    from API.KeithCode.views import pnp_get_device_countController
    from API.KeithCode.views import pnp_get_device_listController
    from API.KeithCode.views import pnp_claim_ap_siteController
    from API.KeithCode.views import pnp_delete_provisioned_deviceController
    from API.KeithCode.views import pnp_get_device_infoController
    from API.KeithCode.views import get_physical_topologyController
    
    import requests
    import json
    import subprocess
    
except Exception as e:
    print("__init Modules are Missing {}".format(e))

app = Flask(__name__)  # Flask app instance initiated
app.config['SECRET_KEY'] = 'C1sc012345'
api = Api(app)  # Flask restful wraps Flask app around it.
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='DNAC Complaince',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)
