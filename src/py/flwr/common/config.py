# Copyright 2024 Flower Labs GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Provide functions for managing global Flower config."""

from logging import WARNING
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import tomli

from flwr.cli.config_utils import validate_fields
from flwr.common import log
from flwr.common.constant import APP_DIR, FAB_CONFIG_FILE, FLWR_HOME
from flwr.common.typing import Run


def get_flwr_dir(provided_path: Optional[str] = None) -> Path:
    """Return the Flower home directory based on env variables."""
    if provided_path is None or not Path(provided_path).is_dir():
        return Path(
            os.getenv(
                FLWR_HOME,
                f"{os.getenv('XDG_DATA_HOME', os.getenv('HOME'))}/.flwr",
            )
        )
    return Path(provided_path).absolute()


def get_project_dir(
    fab_id: str, fab_version: str, flwr_dir: Optional[Union[str, Path]] = None
) -> Path:
    """Return the project directory based on the given fab_id and fab_version."""
    # Check the fab_id
    if fab_id.count("/") != 1:
        raise ValueError(
            f"Invalid FAB ID: {fab_id}",
        )
    publisher, project_name = fab_id.split("/")
    if flwr_dir is None:
        flwr_dir = get_flwr_dir()
    return Path(flwr_dir) / APP_DIR / publisher / project_name / fab_version


def get_project_config(project_dir: Union[str, Path]) -> Dict[str, Any]:
    """Return pyproject.toml in the given project directory."""
    # Load pyproject.toml file
    toml_path = Path(project_dir) / FAB_CONFIG_FILE
    if not toml_path.is_file():
        raise FileNotFoundError(
            f"Cannot find {FAB_CONFIG_FILE} in {project_dir}",
        )
    with toml_path.open(encoding="utf-8") as toml_file:
        config = tomli.loads(toml_file.read())

    # Validate pyproject.toml fields
    is_valid, errors, _ = validate_fields(config)
    if not is_valid:
        error_msg = "\n".join([f"  - {error}" for error in errors])
        raise ValueError(
            f"Invalid {FAB_CONFIG_FILE}:\n{error_msg}",
        )

    return config


def _flatten_dict(
    raw_dict: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, str]:
    items: List[Tuple[str, str]] = []
    for k, v in raw_dict.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(_flatten_dict(v, parent_key=new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def get_fused_config(run: Run, flwr_dir: Optional[Path]) -> Dict[str, str]:
    """Get the config using the fab_id and the fab_version, remove the nesting by adding
    the nested keys as prefixes separated by dots, and fuse it with the override
    dict."""
    if not run.fab_id or not run.fab_version:
        return {}

    default_config = _flatten_dict(
        get_project_config(get_project_dir(run.fab_id, run.fab_version, flwr_dir))[
            "flower"
        ]["config"]
    )
    final_config = default_config.copy()

    for key, value in run.override_config.items():
        if key in default_config:
            final_config[key] = value
        else:
            if key[0] == "+":
                final_config[key[1:]] = value
            else:
                log(
                    WARNING,
                    "The following override key: '%s' doesn't exist in the "
                    "original config and thus it will be ignored, if this wasn't "
                    "and mistake and you want to add a new key to the config, "
                    "you must prepend the key with '+'. For example: "
                    "`flwr run --config +newkey=1` will add a new key "
                    "named 'newkey' to the config.",
                    key,
                )

    return final_config
