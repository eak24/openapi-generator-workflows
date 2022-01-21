const core = require('@actions/core');
const fetch = require("node-fetch");

try {
  const repo = core.getInput('repo');
  const branch = core.getInput('branch');
  fetch(`https://api.github.com/repos/${repo}/git/ref/heads/${branch}`).then(r => {
    console.log(r.text());
    console.log(r.json());
    core.setOutput("sha", r.text())
  });
} catch (error) {
  core.setFailed(error.message);
}