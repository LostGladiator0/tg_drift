resource "local_file" "foo" {
  content  = var.name
  filename = "~/temp/foo.bar"
}

resource "local_file" "aged" {
  content  = var.name
  filename = "~/temp/foo.bar"
}

resource "local_file" "fds" {
  content  = var.name
  filename = "~/temp/foo.bar"
}

resource "local_file" "afd" {
  content  = var.name
  filename = "~/temp/foo.bar"
}