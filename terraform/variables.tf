variable "project_id" {
  description = "The ID of the project in which to provision resources."
  type        = string
}

variable "zone" {
  description = "The zone for the solution to be deployed."
  type        = string
}

// Marketplace requires this variable name to be declared
variable "goog_cm_deployment_name" {
  description = "The name of the deployment and VM instance."
  type        = string
  default     = "jenkins-vm-deployment"
}

variable "ssh_public_key" {
  type        = string
  description = "Public SSH key for the jenkins user"
}

variable "source_image" {
  description = "The image name for the disk for the VM instance."
  type        = string
  default     = "projects/mpi-click-to-deploy-images/global/images/jenkins-v20241201"
}

variable "machine_type" {
  description = "The machine type to create, e.g. e2-small"
  type        = string
  default     = "e2-standard-2"
}

variable "boot_disk_type" {
  description = "The boot disk type for the VM instance."
  type        = string
  default     = "pd-standard"
}

variable "boot_disk_size" {
  description = "The boot disk size for the VM instance in GBs"
  type        = number
  default     = 20
}

variable "networks" {
  description = "The network name to attach the VM instance."
  type        = list(string)
  default     = ["default"]
}

variable "sub_networks" {
  description = "The sub network name to attach the VM instance."
  type        = list(string)
  default     = []
}

variable "external_ips" {
  description = "The external IPs assigned to the VM for public access."
  type        = list(string)
  default     = ["EPHEMERAL"]
}

variable "enable_tcp_80" {
  description = "Allow HTTP traffic from the Internet"
  type        = bool
  default     = true
}

variable "tcp_80_source_ranges" {
  description = "Source IP ranges for HTTP traffic"
  type        = string
  default     = ""
}

variable "enable_tcp_443" {
  description = "Allow HTTPS traffic from the Internet"
  type        = bool
  default     = true
}

variable "tcp_443_source_ranges" {
  description = "Source IP ranges for HTTPS traffic"
  type        = string
  default     = ""
}

variable "enable_cloud_logging" {
  description = "Enables Cloud Logging."
  type        = bool
  default     = false
}

variable "enable_cloud_monitoring" {
  description = "Enables Cloud Monitoring."
  type        = bool
  default     = false
}

variable "enable_compute_api" {
  description = "Allow read write access to Google Compute Engine APIs on the VM"
  type        = bool
  default     = true
}
