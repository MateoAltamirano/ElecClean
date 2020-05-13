#!/bin/bash

OPTIONS=ibdwr
LONGOPTS=install,build,deploy,website,remove

! PARSED=$(getopt --options=$OPTIONS --longoptions=$LONGOPTS --name "$0" -- "$@")

if [[ ${PIPESTATUS[0]} -ne 0 ]]; then
  exit 2
fi

i=0 p=0 b=0 d=0 w=0

CF_FILE="/tmp/cf_file.txt"
DEPLOYMENTS_BUCKET="website-deployments-elecclean-test-weimar"
WEBSIDE_BUCKET="webpage-elecclean-test-weimar"

case "$1" in
  -i|--install)
    i=1
    shift
    ;;
  -r|--remove)
    r=1
    shift
    ;;
  -b|--build)
    b=1
    shift
    ;;
  -d|--deploy)
    d=1
    shift
    ;;
  -w|--website)
    w=1
    shift
    ;;
  --)
    shift
    break
    ;;
  *)
    ;;
esac

if [[ $i -eq 1 ]]; then
  echo No es necesario instalar
fi

if [[ $b -eq 1 ]]; then

  aws cloudformation package \
    --template-file template.yaml \
    --s3-bucket $DEPLOYMENTS_BUCKET \
    --output-template-file $CF_FILE

fi

if [[ $d -eq 1 ]]; then

  aws cloudformation deploy \
    --no-fail-on-empty-changeset \
    --template-file $CF_FILE \
    --parameter-overrides bucketName=$WEBSIDE_BUCKET \
    --stack-name "ProjectWebsiteStack" \
    --capabilities CAPABILITY_NAMED_IAM

fi

if [[ $w -eq 1 ]]; then

  aws s3 rm s3://$WEBSIDE_BUCKET --recursive
  aws s3 cp website s3://$WEBSIDE_BUCKET/ --acl public-read --recursive

fi

if [[ $r -eq 1 ]]; then

  aws s3 rm s3://$WEBSIDE_BUCKET --recursive

  aws cloudformation delete-stack \
    --stack-name "ProjectWebsiteStack"

fi
