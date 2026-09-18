output "ec2_public_ip" {

  description = "Public IP address of the Mini AI Support EC2 instance"

  value = aws_instance.mini_ai_support.public_ip
}


output "ec2_public_dns" {

  description = "Public DNS name of the Mini AI Support EC2 instance"

  value = aws_instance.mini_ai_support.public_dns
}