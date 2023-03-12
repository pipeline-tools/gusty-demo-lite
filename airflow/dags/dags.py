import os
import airflow
from gusty import create_dags

#####################
## DAG Directories ##
#####################

# point to your dags directory
dag_parent_dir = os.path.join(os.environ["AIRFLOW_HOME"], "dags")

# create_dags (plural) is great for when you have multiple dags to create
# create_dag (singular) is also available for when you want to just create one dag
create_dags(
    dag_parent_dir,
    globals(),
    tags=["default", "tags"],
    task_group_defaults={"tooltip": "this is a default tooltip"},
    wait_for_defaults={"retries": 10, "check_existence": True},
    latest_only=False,
)
