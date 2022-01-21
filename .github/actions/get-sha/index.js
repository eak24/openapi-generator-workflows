const core = require('@actions/core');

try {
  const repo = core.getInput('repo');
  const branch = core.getInput('branch');
  const response = await fetch(`https://api.github.com/repos/${repo}/git/ref/heads/${branch}`)
  core.setOutput("sha", response.json().object.sha);
} catch (error) {
  core.setFailed(error.message);
}