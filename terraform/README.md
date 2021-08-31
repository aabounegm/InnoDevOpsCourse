# Terraform

[Terraform](https://www.terraform.io/) is an open-source tool by [hashicorp](https://www.hashicorp.com/) for building, deploying, and managing infrastructure.
It is a declarative language for describing the structure of your infrastructure (a paradigm known as Infrastructure as Code), and has a lot of plugins to support different types of infrastructure and (cloud) providers.

## Usage

After installing Terraform and writing the `.tf` file describing the infrastructure, run `terraform init` to download the required plugins and modules.
Then run `terraform plan` to see the changes Terraform will make to your infrastructure.
If everything looks good, run `terraform apply` to actually create the infrastructure.
