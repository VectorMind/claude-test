import boto3
bedrock = boto3.client(service_name='bedrock')


response = bedrock.list_foundation_models(byProvider='Anthropic')
for model in response["modelSummaries"]:
    print(model["modelId"])
