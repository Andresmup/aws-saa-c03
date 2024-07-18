terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.51.1"
    }
  }
}

provider "aws" {
  # Configuration options
}

resource "aws_s3_bucket" "bucket-etag" {
  bucket = "saa-c03-tf-etag-bucket"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }

}

resource "aws_s3_object" "object" {
  bucket = aws_s3_bucket.bucket-etag.id
  key    = "text.txt"
  source = "text.txt"

  # The filemd5() function is available in Terraform 0.11.12 and later
  # For Terraform 0.11.11 and earlier, use the md5() function and the file() function:
  # etag = "${md5(file("path/to/file"))}"
  etag = filemd5("text.txt")
}