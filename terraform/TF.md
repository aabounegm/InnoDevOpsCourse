# Terraform best practices

- Use built-in formatter (`terraform fmt`) and validator (`terraform validate`)
- Use `terraform plan` to see what changes will be made
- Prefer remotely managed state. Use `terraform remote config` to configure remote state.
- Use variables for any sensitive information, and make use of `*.tfvars` files and `-var-file` option.
- Pin the Terraform provider to a specific version. Use `terraform providers` to list available providers.
- Give meaningful names to the resources you create.
- Do not add the state file to VCS if it contains any sensitive information (prefer a remote in that case).
- Separate the configuration over multiple files based on the natural grouping of these resources.
- For large infrastructures, use [Terraform modules](https://www.terraform.io/docs/language/modules/syntax.html).
- A possible folder structure for small projects would use `main.tf` (to configure the infrastructure resources), `variables.tf` (to define the variables), and `outputs.tf` (to configure the outputs).
