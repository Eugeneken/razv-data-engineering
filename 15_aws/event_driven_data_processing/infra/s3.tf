resource "aws_s3_bucket" "buckets" {
    count           = length(var.bucket_names)
    bucket          = "${var.prefix}-${var.bucket_names[count.index]}-${var.account_id}"

    force_destroy   = true
    tags            = local.common_tags
}

resource "aws_s3_bucket_server_side_encryption_configuration" "bucket_see" {
    count           = length(var.bucket_names)
    bucket          = "${var.prefix}-${var.bucket_names[count.index]}-${var.account_id}"

    rule {
        apply_server_side_encryption_by_default {
          sse_algorithm = "AES256"
        }
    }
}

resource "aws_s3_bucket_acl" "bucket_acl" {
    count           = length(var.bucket_names)
    bucket          = "${var.prefix}-${var.bucket_names[count.index]}-${var.account_id}"
    acl = "private"
}

resource "aws_s3_bucket_public_access_block" "public_access_block" {
  count  = length(var.bucket_names)
  bucket = "${var.prefix}-${var.bucket_names[count.index]}-${var.account_id}"

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}