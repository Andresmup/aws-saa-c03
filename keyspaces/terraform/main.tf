terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.54.1"
    }
  }
}

provider "aws" {
  # Configuration options
}


resource "aws_keyspaces_keyspace" "keyspaces" {
  name = "keyspaces_${var.app_name}_${var.app_environment}_db"
}

resource "aws_keyspaces_table" "users_table" {
  keyspace_name = aws_keyspaces_keyspace.keyspaces.name
  table_name    = "users_${var.app_name}_${var.app_environment}_table"

  capacity_specification {
    throughput_mode = "PAY_PER_REQUEST"
  }

  schema_definition {
    column {
      name = "id"
      type = "ascii"
    }

    column {
      name = "first_name"
      type = "text"
    }

    column {
      name = "last_name"
      type = "text"
    }

    column {
      name = "age"
      type = "int"
    }

    column {
      name = "active_member"
      type = "boolean"
    }

    partition_key {
      name = "id"
    }
  }

  comment {
    message = "Cassandra table for the ${var.app_name} app in the ${var.app_environment} environment"
  }
}