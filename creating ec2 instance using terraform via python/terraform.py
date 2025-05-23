import subprocess
import sys
import time

dir = r"/root/python-with-terraform/pyo/terraform" #enter your link here for tarraform folder 

def terraform_init(dir):

    try:
        subprocess.run(f"terraform -chdir={dir} init", shell=True, check=True)
        print("Terraform init command successfully executed.")
    except subprocess.CalledProcessError as e:
        print(f"Error checking initialization phase: {e}")
        sys.exit(1)

def terraform_plan(dir):

     try:
        subprocess.run(f"terraform -chdir={dir} plan", shell=True, check=True)
        print("Terraform plan command successfully.")
     except subprocess.CalledProcessError as e:
        print(f"Error checking while planning: {e}")
        sys.exit(1)

def terraform_apply(apply_c):

     try:
        subprocess.run(f"terraform -chdir={dir} apply", shell=True, check=True)
        print("Terraform apply command successfully.")
     except subprocess.CalledProcessError as e:
        print(f"Error checking while applying: {e}")
        sys.exit(1)

def terraform_validate(validate_c):
     try:
        subprocess.run(f"terraform -chdir={dir} validate", shell=True, check=True)
        print("Terraform validation checking....")
     except subprocess.CalledProcessError as e:
        print(f"Error checking while validation: {e}")
        sys.exit(1)

Query = ""
while  Query != "stop":
   Query = input("What you want to do? please enter following commands \n \n - 'init' for terraform init \n \n - 'plan' for terraform plan \n \n - 'apply' for terraform apply \n \n - 'validate' for terraform validate \n \n - 'stop' for quite \n \n - please enter command: ")
   if Query == "init":
      time.sleep(2)
      print("-------- your code is being initialized -----------")
      terraform_init(dir)
   if Query == "plan":
      time.sleep(2)
      print("-------- plan phase has been started -----------")      
      terraform_plan(dir)
   if Query == "apply":
      time.sleep(2)
      print("-------- apply phase started -----------")
      terraform_apply(dir)
   if Query == "validate":
      time.sleep(2)
      print("-------- scanning for validation -----------")
      terraform_validate(dir)
   else:
      print("you're logging out.. ")
      time.sleep(2)
