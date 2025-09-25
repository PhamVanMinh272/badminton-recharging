Features:
Equal Split – Divide the bill evenly.
Custom Split – Allow different amounts per person.
Weighted Split – Split based on weights (e.g., percentage or item cost).
Tip and Tax Handling – Include tip or tax in the total.
Output Summary – Show who owes how much.

Problem:
1. Create python layer:
pip install <libs> -t python
Note: libs must be compatible with linux os
pip install --platform manylinux2014_x86_64 --target=. --implementation cp --python-version 3.11 --only-binary=:all: --upgrade fastapi pydantic

2. CORS error for aws lambda application

Enable CORS in API Gateway, using AWS Console or AWS cloudformation template:
Example:
  ApiBadmintonRechargingDeployment:
    Type: AWS::Serverless::Api
    Properties:
      StageName: dev
      Cors:
        AllowMethods: "'OPTIONS,POST,GET,PUT,DELETE'"
        AllowHeaders: "'Content-Type,X-Amz-Date,Authorization,X-Api-Key'"
        AllowOrigin: "'*'"
