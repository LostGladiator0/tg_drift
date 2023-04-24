import os
import subprocess
import re
import logging
import json_log_formatter

# Create a logger
logger = logging.getLogger()

# Set a default log level for the logger
logging.basicConfig(level=logging.INFO)

# Create a JSON formatter
formatter = json_log_formatter.JSONFormatter()

# Create a stream handler and set its formatter
handler = logging.StreamHandler()
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)




os.chdir("/home/thomas/dev/tg_drift/test-terragrunt/")
os.environ["TG_CONFIG_FILE_PATH"] = "/home/thomas/dev/tg_drift/test-terragrunt/values.yaml"



def run_all_plan():
    logging.info("Running terragrunt run-all plan...")
    run_all_plan = subprocess.check_output(["terragrunt", "run-all", "plan", "-no-color"])

    output_str = run_all_plan.decode('utf-8')
    matches = re.findall(r'Plan: (\d+) to add, (\d+) to change, (\d+) to destroy', output_str)

    # Extract the numbers from the match and store them in a list of dictionaries
    plans = []
    for match in matches:
        plan = {
            'add': int(match[0]),
            'change': int(match[1]),
            'destroy': int(match[2]),
            'resources': {}
        }
        plans.append(plan)

# Loop through each line and add the resources to the correct plan
    current_plan = 0
    for line in output_str.split("\n"):
        match = re.search(r'^\s*\#\s+(\w+)\.(\w+)\s+will be (\w+)', line)
        if match:
            resource_type = match.group(1)
            resource_name = match.group(2)
            resource_action = match.group(3)
            resource_key = f"{resource_type}.{resource_name}"
            plans[current_plan]['resources'][resource_key] = resource_action
        else:
            #  Check if the line contains a new plan
            match = re.search(r'^Plan: (\d+) to add, (\d+) to change, (\d+) to destroy', line)
            if match:
                current_plan += 1

    print(plans)

run_all_plan()



b'\nTerraform used the selected providers to generate the following execution\nplan. Resource actions are indicated with the following symbols:\n  + create\n\nTerraform will perform the following actions:\n\n  # local_file.afd will be created\n  + resource "local_file" "afd" {\n      + content              = "gusto-env"\n      + content_base64sha256 = (known after apply)\n      + content_base64sha512 = (known after apply)\n      + content_md5          = (known after apply)\n      + content_sha1         = (known after apply)\n      + content_sha256       = (known after apply)\n      + content_sha512       = (known after apply)\n      + directory_permission = "0777"\n      + file_permission      = "0777"\n      + filename             = "~/temp/foo.bar"\n      + id                   = (known after apply)\n    }\n\n  # local_file.aged will be created\n  + resource "local_file" "aged" {\n      + content              = "gusto-env"\n      + content_base64sha256 = (known after apply)\n      + content_base64sha512 = (known after apply)\n      + content_md5          = (known after apply)\n      + content_sha1         = (known after apply)\n      + content_sha256       = (known after apply)\n      + content_sha512       = (known after apply)\n      + directory_permission = "0777"\n      + file_permission      = "0777"\n      + filename             = "~/temp/foo.bar"\n      + id                   = (known after apply)\n    }\n\n  # local_file.fds will be created\n  + resource "local_file" "fds" {\n      + content              = "gusto-env"\n      + content_base64sha256 = (known after apply)\n      + content_base64sha512 = (known after apply)\n      + content_md5          = (known after apply)\n      + content_sha1         = (known after apply)\n      + content_sha256       = (known after apply)\n      + content_sha512       = (known after apply)\n      + directory_permission = "0777"\n      + file_permission      = "0777"\n      + filename             = "~/temp/foo.bar"\n      + id                   = (known after apply)\n    }\n\n  # local_file.foo will be created\n  + resource "local_file" "foo" {\n      + content              = "gusto-env"\n      + content_base64sha256 = (known after apply)\n      + content_base64sha512 = (known after apply)\n      + content_md5          = (known after apply)\n      + content_sha1         = (known after apply)\n      + content_sha256       = (known after apply)\n      + content_sha512       = (known after apply)\n      + directory_permission = "0777"\n      + file_permission      = "0777"\n      + filename             = "~/temp/foo.bar"\n      + id                   = (known after apply)\n    }\n\nPlan: 4 to add, 0 to change, 0 to destroy.\n\n\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\nNote: You didn\'t use the -out option to save this plan, so Terraform can\'t\nguarantee to take exactly these actions if you run "terraform apply" now.\n\nTerraform used the selected providers to generate the following execution\nplan. Resource actions are indicated with the following symbols:\n  + create\n\nTerraform will perform the following actions:\n\n  # local_file.afd will be created\n  + resource "local_file" "afd" {\n      + content              = "test-env"\n      + content_base64sha256 = (known after apply)\n      + content_base64sha512 = (known after apply)\n      + content_md5          = (known after apply)\n      + content_sha1         = (known after apply)\n      + content_sha256       = (known after apply)\n      + content_sha512       = (known after apply)\n      + directory_permission = "0777"\n      + file_permission      = "0777"\n      + filename             = "~/temp/foo.bar"\n      + id                   = (known after apply)\n    }\n\n  # local_file.aged will be created\n  + resource "local_file" "aged" {\n      + content              = "test-env"\n      + content_base64sha256 = (known after apply)\n      + content_base64sha512 = (known after apply)\n      + content_md5          = (known after apply)\n      + content_sha1         = (known after apply)\n      + content_sha256       = (known after apply)\n      + content_sha512       = (known after apply)\n      + directory_permission = "0777"\n      + file_permission      = "0777"\n      + filename             = "~/temp/foo.bar"\n      + id                   = (known after apply)\n    }\n\n  # local_file.fds will be created\n  + resource "local_file" "fds" {\n      + content              = "test-env"\n      + content_base64sha256 = (known after apply)\n      + content_base64sha512 = (known after apply)\n      + content_md5          = (known after apply)\n      + content_sha1         = (known after apply)\n      + content_sha256       = (known after apply)\n      + content_sha512       = (known after apply)\n      + directory_permission = "0777"\n      + file_permission      = "0777"\n      + filename             = "~/temp/foo.bar"\n      + id                   = (known after apply)\n    }\n\n  # local_file.foo will be created\n  + resource "local_file" "foo" {\n      + content              = "test-env"\n      + content_base64sha256 = (known after apply)\n      + content_base64sha512 = (known after apply)\n      + content_md5          = (known after apply)\n      + content_sha1         = (known after apply)\n      + content_sha256       = (known after apply)\n      + content_sha512       = (known after apply)\n      + directory_permission = "0777"\n      + file_permission      = "0777"\n      + filename             = "~/temp/foo.bar"\n      + id                   = (known after apply)\n    }\n\nPlan: 4 to add, 0 to change, 0 to destroy.\n\n\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\nNote: You didn\'t use the -out option to save this plan, so Terraform can\'t\nguarantee to take exactly these actions if you run "terraform apply" now.\n'
