class ExerciseSerializer:
  @staticmethod
  def serialise(resource) -> dict:
    return {
      'id': resource.id,
      'name': resouce.name,
      'instructions': resource.instructions,
      'created': resource.created.strftime("%Y-%m-%dT%H:%M:%S")
    }