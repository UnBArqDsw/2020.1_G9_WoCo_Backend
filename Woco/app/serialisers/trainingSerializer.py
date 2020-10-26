class TrainingSerializer:
  @staticmethod
  def serialise(resource) -> dict:
    return {
      'id': resource.id,
      'name': resource.name,
      'instructions': resource.instructions,
      'created': resource.created.strftime("%Y-%m-%dT%H:%M:%S"),
      'responsibleCoach': resource.coachName
    }

  @staticmethod
  def serialiseArray(resources) -> dict:
    return { 'data' : [TrainingSerializer.serialise(resource) for resource in resources ]}