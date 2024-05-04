# claude-test
Testing Anthropic Claude Model

steps: https://docs.aws.amazon.com/bedrock/latest/userguide/api-setup.html

* cerate a user in IAM
* give access to bedrock
* login with aws cli

user services:
* Bedrock : https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock.html
    * list_foundation_models()

* Bedrock Runtime : https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime.html
    * invoke_model()

# usage
```cmd
(venv) VectorMind\claude-test>python bedrock_test.py
anthropic.claude-instant-v1
anthropic.claude-v2:1:18k
anthropic.claude-v2:1:200k
anthropic.claude-v2:1
anthropic.claude-v2
```
