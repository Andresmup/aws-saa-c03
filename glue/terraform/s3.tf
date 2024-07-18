#S3 BUCKET RESOURCE
#################################################################################################################

resource "aws_s3_bucket" "bucket_data_storage" {
  bucket        = var.bucket_name
  force_destroy = true
  lifecycle {
    prevent_destroy = false
  }
}


#S3 BUCKET VEHICLE DATA
#################################################################################################################

resource "aws_s3_object" "sample_data_object" {
  bucket = var.bucket_name
  key    = "data/vehicles.csv"
  source = "../data/vehicles.csv"

  depends_on = [
    aws_s3_bucket.bucket_data_storage
  ]


}