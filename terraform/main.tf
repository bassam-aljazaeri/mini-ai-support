terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}


# --------------------------------------------------
# VPC
# --------------------------------------------------

resource "aws_vpc" "mini_ai_support" {

  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "mini-ai-support-vpc"
  }
}


# --------------------------------------------------
# Internet Gateway
# --------------------------------------------------

resource "aws_internet_gateway" "mini_ai_support" {

  vpc_id = aws_vpc.mini_ai_support.id

  tags = {
    Name = "mini-ai-support-internet-gateway"
  }
}


# --------------------------------------------------
# Subnet
# --------------------------------------------------

resource "aws_subnet" "mini_ai_support" {

  vpc_id = aws_vpc.mini_ai_support.id

  cidr_block = "10.0.1.0/24"

  map_public_ip_on_launch = true

  availability_zone = "us-east-1a"

  tags = {
    Name = "mini-ai-support-subnet"
  }
}


# --------------------------------------------------
# Route Table
# --------------------------------------------------

resource "aws_route_table" "mini_ai_support" {

  vpc_id = aws_vpc.mini_ai_support.id

  route {

    cidr_block = "0.0.0.0/0"

    gateway_id = aws_internet_gateway.mini_ai_support.id
  }

  tags = {
    Name = "mini-ai-support-route-table"
  }
}


# --------------------------------------------------
# Route Table Association
# --------------------------------------------------

resource "aws_route_table_association" "mini_ai_support" {

  subnet_id = aws_subnet.mini_ai_support.id

  route_table_id = aws_route_table.mini_ai_support.id
}


# --------------------------------------------------
# Security Group
# --------------------------------------------------

resource "aws_security_group" "mini_ai_support" {

  name = "mini-ai-support-security-group"

  description = "Security group for Mini AI Support Assistant"

  vpc_id = aws_vpc.mini_ai_support.id

  ingress {

    description = "SSH"

    from_port = 22

    to_port = 22

    protocol = "tcp"

    cidr_blocks = [
      "0.0.0.0/0"
    ]
  }

  ingress {

    description = "FastAPI"

    from_port = 8000

    to_port = 8000

    protocol = "tcp"

    cidr_blocks = [
      "0.0.0.0/0"
    ]
  }

  egress {

    from_port = 0

    to_port = 0

    protocol = "-1"

    cidr_blocks = [
      "0.0.0.0/0"
    ]
  }

  tags = {
    Name = "mini-ai-support-security-group"
  }
}


# --------------------------------------------------
# SSH Key Pair
# --------------------------------------------------

resource "aws_key_pair" "mini_ai_support" {

  key_name = "mini-ai-support-key"

  public_key = file(
    pathexpand("~/.ssh/mini-ai-support-key.pub")
  )
}


# --------------------------------------------------
# EC2 Instance
# --------------------------------------------------

resource "aws_instance" "mini_ai_support" {

  ami = "ami-0c101f26f147fa7fd"

  instance_type = "t3.micro"

  subnet_id = aws_subnet.mini_ai_support.id

  key_name = aws_key_pair.mini_ai_support.key_name

  vpc_security_group_ids = [
    aws_security_group.mini_ai_support.id
  ]

  tags = {

    Name = "mini-ai-support"

  }
}