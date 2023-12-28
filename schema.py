flare:{
  "classes": {
    "_User": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "username": {"type": "string", "required": True},
        "password": {"type": "string", "required": True},
        "email": {"type": "string", "required": True},
        "emailVerified": {"type": "boolean", "required": True},
        "authData": {"type": "object", "required": True}
      },
      "indexes": ["username", "email"]
    },
    "_Role": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "name": {"type": "string", "required": True}
      },
      "relations": {
        "users": "_User",
        "roles": "_Role"
      },
      "indexes": ["name"]
    },
    "Concepts": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "Magic": {"type": "string", "required": True},
        "Time": {"type": "string", "required": True},
        "Balance": {"type": "string", "required": True},
        "Knowledge": {"type": "string", "required": True},
        "ParallelRealities": {"type": "string", "required": True},
        "RepeatingProphecies": {"type": "string", "required": True},
        "CyclicCatastrophes": {"type": "string", "required": True},
        "description": {"type": "string"}
      }
    },
    "Signal": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "name": {"type": "string", "required": True},
        "notebookID": {"type": "string", "required": True},
        "state": {"type": "number", "required": True},
        "valueA": {"type": "string", "required": True},
        "valueB": {"type": "string", "required": True},
        "valueC": {"type": "string", "required": True},
        "type": {"type": "number", "required": True},
        "ID_A": {"type": "string", "required": True},
        "ID_B": {"type": "string", "required": True},
        "ID_C": {"type": "string", "required": True},
        "cellIDs": {"type": "array", "targetClass": "Object"},
        "description": {"type": "string"}
      }
    },
    "Actions": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "name": {"type": "string", "required": True},
        "parameters": {"type": "array", "targetClass": "Object"},
        "domain": {"type": "string", "required": True},
        "expectedResponseType": {"type": "string", "required": True},
        "operationType": {"type": "string", "required": True},
        "map": {"type": "pointer", "targetClass": "Map"},
        "form": {"type": "pointer", "

game:{
  "classes": {
    "_User": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "username": {"type": "string", "required": True},
        "password": {"type": "string", "required": True},
        "email": {"type": "string", "required": True},
        "emailVerified": {"type": "boolean", "required": True},
        "authData": {"type": "object", "required": True}
      },
      "indexes": ["username", "email"]
    },
    "_Role": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "name": {"type": "string", "required": True}
      },
      "relations": {
        "users": "_User",
        "roles": "_Role"
      },
      "indexes": ["name"]
    },
    "Pass": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "load": {"type": "object", "required": True}
      }
    },
    "Baton": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "name": {"type": "string", "required": True},
        "type": {"type": "string", "required": True},
        "team": {"type": "string", "required": True},
        "room": {"type": "string", "required": True},
        "load": {"type": "object", "required": True}
      }
    },
    "Team": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "a": {"type": "string", "required": True},
        "b": {"type": "string", "required": True},
        "c": {"type": "string", "required": True},
        "synergency": {"type": "number", "required": True},
        "role": {"type": "string", "required": True},
        "rate": {"type": "number", "required": True},
        "preprompt": {"type": "object", "required": True},
        "p1": {"type": "object", "required": True},
        "p2": {"type": "object", "required": True},
        "p3": {"type": "object", "required": True}
      }
    },
    "Character": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "attributes": {"type": "pointer", "targetClass": "Attributes"},
        "_id": {"type": "string", "index": True}
      }
    },
    "Signal": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
lore:{{
  "classes": {
    "_User": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "username": {"type": "string", "required": True},
        "password": {"type": "string", "required": True},
        "email": {"type": "string", "required": True},
        "emailVerified": {"type": "boolean", "required": True},
        "authData": {"type": "object", "required": True}
      },
      "indexes": ["username", "email"]
    },
    "_Role": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "name": {"type": "string", "required": True}
      },
      "relations": {
        "users": "_User",
        "roles": "_Role"
      },
      "indexes": ["name"]
    },
    "Monsters": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "Fauna": {"type": "string", "required": True},
        "Order": {"type": "string", "required": True},
        "Rarity": {"type": "string", "required": True},
        "Monster": {"type": "string", "required": True}
      }
    },
    "Magic": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "Path": {"type": "string", "required": True},
        "type": {"type": "string", "required": True},
        "Order": {"type": "string", "required": True},
        "School": {"type": "string", "required": True}
      }
    },
    "Attributes": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "Name": {"type": "string", "required": True},
        "Pair": {"type": "string", "required": True},
        "Path": {"type": "string", "required": True},
        "Point": {"type": "string", "required": True},
        "Effect": {"type": "string", "required": True},
        "Rarity": {"type": "string", "required": True},
        "Values": {"type": "array", "targetClass": "Object"},
        "Description": {"type": "string", "required": True},
        "CharacterAppearance": {"type": "pointer", "targetClass": "CharacterAppearance"}
      }
    },
    "Structure": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "Arch": {"type": "string", "required": True},
        "City": {"type": "string", "required": True},
        "Gate": {"type": "string", "required": True},
        "Path": {"type": "string", "required": True},
        "Wall": {"type": "string", "required": True},
        "camp":
}
autoprompter:{
{
  "classes": {
    "_User": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "username": {"type": "string", "required": True},
        "password": {"type": "string", "required": True},
        "email": {"type": "string", "required": True},
        "emailVerified": {"type": "boolean", "required": True},
        "authData": {"type": "object", "required": True}
      },
      "indexes": ["username", "email"]
    },
    "_Role": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "name": {"type": "string", "required": True}
      },
      "relations": {
        "users": "_User",
        "roles": "_Role"
      },
      "indexes": ["name"]
    },
    "Task": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "stageName": {"type": "string", "required": True},
        "stepToStage": {"type": "string", "required": True},
        "dependencies": {"type": "array", "targetClass": "Task"},
        "subTasks": {"type": "array", "targetClass": "Task"},
        "estimatedTime": {"type": "number", "required": True},
        "progressTracking": {"type": "string", "required": True},
        "assignedTo": {"type": "string", "required": True},
        "priorityLevel": {"type": "number", "required": True},
        "feedbackLoop": {"type": "string", "required": True},
        "completionCriteria": {"type": "string", "required": True},
        "resourceLinks": {"type": "array", "targetClass": "Object"},
        "tokensUsed": {"type": "array", "targetClass": "Object"},
        "priority": {"type": "number", "required": True},
        "status": {"type": "string", "required": True},
        "description": {"type": "string", "required": True},
        "prompt": {"type": "string", "required": True},
        "title": {"type": "string", "required": True},
        "operation": {"type": "pointer", "targetClass": "Operation"}
      }
    },
    "Rules": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "rule": {"type": "string", "required": True},
        "description": {"type": "string", "required": True},
        "enforcement": {"type": "string", "required": True},
        "violation": {"type": "string", "required": True}
      }
    },
    "Completed": {
        "fields": {
            "objectId": {"type": "string", "required": True},
            "createdAt": {"type": "string", "required": True},
            "updatedAt": {"type": "string", "required": True},
            "ACL": {"type": "object", "required": True},
            "originalTaskId": {"type": "string", "required": True},
            "result": {"type": "string", "required": True},
            "completedAt": {"type": "string", "required": True}
        }
    },
    "Plan": {
      "fields":
   
}
iQueue:{{
  "classes": {
    "_User": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "username": {"type": "string", "required": True},
        "password": {"type": "string", "required": True},
        "email": {"type": "string", "required": True},
        "emailVerified": {"type": "boolean", "required": True},
        "authData": {"type": "object", "required": True}
      },
      "indexes": ["username", "email"]
    },
    "_Role": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "name": {"type": "string", "required": True}
      },
      "relations": {
        "users": "_User",
        "roles": "_Role"
      },
      "indexes": ["name"]
    },
    "Game": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "type": {"type": "string", "required": True},
        "target": {"type": "string", "required": True},
        "content": {"type": "string", "required": True},
        "data": {"type": "object", "required": True}
      },
      "indexes": ["type", "target"]
    },
    "Lore": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "type": {"type": "string", "required": True},
        "target": {"type": "string", "required": True},
        "content": {"type": "string", "required": True},
        "data": {"type": "object", "required": True}
      },
      "indexes": ["type", "target"]
    },
    "Flare": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "type": {"type": "string", "required": True},
        "target": {"type": "string", "required": True},
        "content": {"type": "string", "required": True},
        "data": {"type": "object", "required": True}
      },
      "indexes": ["type", "target"]
    },
    "Cook": {
      "fields": {
        "objectId": {"type": "string", "required": True},
        "createdAt": {"type": "string", "required": True},
        "updatedAt": {"type": "string", "required": True},
        "ACL": {"type": "object", "required": True},
        "Stage": {"type": "string", "required": True},
        "Order": {"type": "number", "required": True},
        "Method": {"type": "string", "required": True},
        "About": {"type": "string", "required": True}
      },
      "indexes

    
}