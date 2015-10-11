from flask.ext.restplus import fields
from . import api


# Roles fields

roles_fields = api.model(
    'Roles', {
        'name': fields.String(required=True),
        'description': fields.String(required=True),
    }
)


# User fields
user_fields = api.model(
    'User', {
        'email': fields.String(
            description='The email',
            required=True,
            default='admin@example.com'
        ),
        'first_name': fields.String,
        'last_name': fields.String,
        'password': fields.String(
            description='Password',
            required=True,
            default='Sekrit'
        ),
    }
)

get_user_fields = api.extend(
    'Get Users', user_fields, {
        'id': fields.String,
        'roles': fields.Nested(roles_fields),
    }
)


# Auth fields
auth_fields = api.model(
    'Auth', {
        'email': fields.String(
            description='The email',
            required=True,
            default='admin@example.com'
        ),
        'password': fields.String(
            description='The password',
            required=True,
            default='Sekrit'
        ),
    }
)

token_response = api.model(
    'Token', {
        'token': fields.String,
    }
)

# Application fields
application_fields = api.model(
    'Application', {
        'application_name': fields.String(required=True),
        'galaxy_role': fields.String(required=True),
        'name': fields.String(required=True),
    }
)

# Provider fields
provider_fields = api.model(
    'Provider', {
        'name': fields.String(required=True),
        'type': fields.String(required=True),
    }
)


# Cluster fields
cluster_owner_fields = api.model(
    'Owner', {
        'id': fields.String,
        'email': fields.String(),
        'first_name': fields.String,
        'last_name': fields.String,
        'roles': fields.Nested(roles_fields),
    }
)

cluster_fields = api.model(
    'Cluster', {
        'name': fields.String(required=True),
    }
)

get_cluster_fields = api.extend('Get Clusters', cluster_fields, {
    'providers': fields.Nested(provider_fields),
    'id': fields.String,
    'owner': fields.Nested(cluster_owner_fields),
    'applications': fields.Nested(application_fields),
}
)

# Task fields
task_fields = api.model(
    'Task', {
        'id': fields.String,
        'celery_id': fields.String,
    }
)
