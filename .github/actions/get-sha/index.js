const core = require('@actions/core');
import fetch from "node-fetch";

try {
  const repo = core.getInput('repo');
  const branch = core.getInput('branch');
  fetch(`https://api.github.com/repos/${repo}/git/ref/heads/${branch}`).then(r => core.setOutput("sha", r.json().object.sha));
} catch (error) {
  core.setFailed(error.message);
}