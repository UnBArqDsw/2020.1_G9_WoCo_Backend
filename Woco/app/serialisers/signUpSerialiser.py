class SignUpSerializer:
  @staticmethod
  def serialise(resource) -> dict:
    return {
      'id': resource.id,
      'username': resource.username,
      'email': resource.email,
      'password': resource.password,
      'created': resource.created.strftime("%Y-%m-%dT%H:%M:%S")
    }

  @staticmethod
  def serialiseArray(resources) -> dict:
    return { 'data' : [SignUpSerializer.serialise(resource) for resource in resources ]}