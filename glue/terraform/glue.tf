#GLUE DATABASE RESOURCE
#################################################################################################################

resource "aws_glue_catalog_database" "catalog_database" {
  name = "vehicles-${var.app_name}-${var.app_environment}-database"
}

#GLUE TABLE RESOURCE
#################################################################################################################
resource "aws_glue_catalog_table" "vehicles_table" {
  name          = "vehicles-${var.app_name}-${var.app_environment}-table"
  database_name = aws_glue_catalog_database.catalog_database.name

  storage_descriptor {
    location      = "s3://${var.bucket_name}/data/"
    input_format  = "org.apache.hadoop.mapred.TextInputFormat"
    output_format = "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat"
    ser_de_info {
      serialization_library = "org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe"
    }
  }
}

#GLUE CRAWLER RESOURCE
#################################################################################################################

resource "aws_glue_crawler" "crawler_vehicles" {
  database_name = aws_glue_catalog_database.catalog_database.name
  name          = "catalog-${var.app_name}-${var.app_environment}-crawler"
  role          = aws_iam_role.glue_execution_role.arn

  catalog_target {
    database_name = aws_glue_catalog_database.catalog_database.name
    tables        = [aws_glue_catalog_table.vehicles_table.name]
  }

  schema_change_policy {
    delete_behavior = "LOG"
  }

  configuration = <<EOF
{
  "Version":1.0,
  "Grouping": {
    "TableGroupingPolicy": "CombineCompatibleSchemas"
  }
}
EOF
}