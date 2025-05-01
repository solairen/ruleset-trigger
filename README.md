# GitHub Ruleset Manager

A Python utility for managing GitHub repository rulesets through the GitHub API.

## Overview

This utility simplifies the process of managing GitHub repository ruleset configurations programmatically. It allows you to enable and disable ruleset through simple API calls.

## Features

- Enable/disable enforcement of rules

## Usage

Add the following step to your GitHub workflow:

```yml
- name: Enable ruleset in repository
  uses: solairen/ruleset-trigger@main
  with:
    token: ${{ secrets.GITHUB_TOKEN }}
    ruleset_id: '12345'
    # Optional parameters
    repository: 'owner/repo'
    enforcement: 'active'
```

### Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `token` | GitHub token for repository access | Yes | N/A |
| `ruleset_id` | The ruleset id | Yes | N/A |
| `repository` | The repository name | No | `owner/repo` |
| `enforcement` | Disable or enable ruleset | No | `active` |

## Development

### Prerequisites

- Python 3.6+
- `requests` library

### Local Development

```bash
# Clone the repository
git clone https://github.com/solairen/ruleset-trigger.git
cd ruleset-trigger

# Install dependencies
pip install requests

# Set environment variables
export INPUT_TOKEN="your-github-token"
export INPUT_REPOSITORY="username/repository"
export INPUT_RULESET_ID="your-ruleset-id"
export INPUT_ENFORCEMENT="active/disabled"

# Run the script
python update_ruleset.py
```

## Contributing

Contributions are welcome! See CONTRIBUTING.md for details on how to contribute to this project.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Code of Conduct

Please review our Code of Conduct before contributing to this project.

## Acknowledgments

Thank you to all contributors who have helped with this project.

## Support

If you find this project helpful, consider [buying me a coffee](https://www.buymeacoffee.com/solairen).
