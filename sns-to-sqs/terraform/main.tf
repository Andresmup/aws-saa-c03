terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.52.0"
    }
  }
}

provider "aws" {
  # Configuration options
}


resource "aws_sns_topic" "terraform_topic_fifo" {
  name                        = "terraform-topic.fifo"
  fifo_topic                  = true
  content_based_deduplication = true
}

resource "aws_sqs_queue" "terraform_queue_fifo" {
  name                        = "terraform-sqs.fifo"
  fifo_queue                  = true
  content_based_deduplication = true
}

resource "aws_sqs_queue_policy" "terraform_queue_policy" {
  queue_url = aws_sqs_queue.terraform_queue_fifo.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "sns.amazonaws.com"
        }
        Action   = "sqs:SendMessage"
        Resource = aws_sqs_queue.terraform_queue_fifo.arn
        Condition = {
          ArnEquals = {
            "aws:SourceArn" = aws_sns_topic.terraform_topic_fifo.arn
          }
        }
      }
    ]
  })
}

resource "aws_sns_topic_subscription" "sqs_target" {
  topic_arn = aws_sns_topic.terraform_topic_fifo.arn
  protocol  = "sqs"
  endpoint  = aws_sqs_queue.terraform_queue_fifo.arn
}

