include {
  path = find_in_parent_folders()
}

terraform {
   source = "../../terraform-modules/local_resource"
}

locals {
  config = yamldecode(file("${get_env("TG_CONFIG_FILE_PATH")}"))
}

inputs = {
  name = local.config.name

}