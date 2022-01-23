# OpenApi Generator Workflows

The OpenApi Generator Workflows repo contains a number of workflows that are ready-to-incorporate for those hoping to automate the update, test and deploy steps of their OpenApi Generator process.

## Quick Start

### Setup 'Deploy Repos'

The first step is to setup the multi-repo structure of the generated, deployable clients/servers. To do this, for each client you wish to deploy, generate a GitHub repo. This will be the 'deployment' repo that holds all the deployable code, as well as the tests and templates if you are using [template customization](https://openapi-generator.tech/docs/templating/). The expected file structure in each client/server repo is:
```bash
.github/workflows/<Generate-Install-Test-Deploy workflow>
templates/
tests/
openapi-config.yaml
<The rest of the generated code>
```

### Setup 'Dispatch Repo'

The next step is to create the single dispatching repo that holds the OpenApi specs themselves and the workflow responsible for dispatching update requests to each of the `Deploy Repos`.
