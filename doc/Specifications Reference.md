# Monolithe Specifications Reference

Monolithe is using well defined specifications to generate sdks and documentations. This document describes how Specifications work and how to create your own.


## Specifications Folder

Specifications are files that must have the extension `.spec`. One and only one object must be described in a Specification file and all Specification files must be in the same subdirectory.


## Specification API Version

The specification folder **must** contains a special file named `api.info`. This file contains the backend basic information about the api.

For instance:

```json
    {
        "version": "3.2",
        "prefix": "api",
        "root": "root"
    }
```


## Specification File

A Specification File describes a particular object of the API. It will tell what are the parent and children APIs, information about itself, and informations about its attributes.

It **must** contains valid json data. And the structure is following (the order of the key does not make any difference).

```json
    {
        "attributes": [
            // ...
        ],
        "children": [
            // ...
        ],
        "model": {
            // ...
        }
    }
```

### The Model Section

The `model` describes the object itself: it **must** contains the following keys:

#### rest_name
The singlar name of the object. This will be used as a unique key to identify and object from the sdks. It will be used each time something must reference a kind of object.

For example:

```json
    "rest_name": "unicorn"
```

#### resource_name
Usually, the plural version of the `rest_name`. This will be used to generate the API calls like `/unicorns/{id}`

For example:

```json
    "resource_name": "unicorns"
```

#### entity_name
Will be used for the class name of the SDK. As it is impossible for Monolithe to guess your capitalization system, you must give this attribute. If not set, a capitalized version `rest_name` will be used, but you should always provide it yourself.

For example:

```json
    "entity_name": "Unicorn"
```

#### package
Used to group the objects in the generated API documentation.

For example:

```json
    "package": "magic"
```

#### description
Will be used to populate the api documentation. You should put extensive description of the object, what it represents, what it does etc.

For example:

```json
    "description": "Unicorn is a pretty cool mystic creature."
```

#### extends
The list of other Specification Files the current Specification inherits from. More information on that later.

For example:

```json
    "extends": [
        "@base",
        "@namedobject"
    ]
```

#### operations

The operations consists of the additional tokens `get`, `update`, `delete`, that can be true or false, according to what kind of operations you want to allow on the model.

For example:

```json
    "model": {
        "get": true,
        "create": false,
        "delete": false
    }
```

### The Attributes Section
The list of Attributes the model has. It is a dictionary where the key is the name of the attribute, and the content, all its characteristics.

For example:

```json
    "attributes" : [
        { 
            "allowed_chars":    <string>,
            "allowed_choices":  <list>,
            "autogenerated":    <bool>,
            "creation_only":    <bool>,
            "default_order":    <bool>,
            "default_value":    <string>,
            "description":      <string>,
            "filterable":       <bool>,
            "format":           <string>,
            "min_length":       <integer>,
            "max_length":       <integer>,
            "min_value":        <integer>,
            "max_value":        <integer>,
            "name":             <string>,
            "orderable":        <bool>,
            "read_only":        <bool>,
            "required":         <bool>,
            "type":             <string>
            "subtype":          <string>,
            "unique":           <bool>
        },
    ]
```

The attribute must contains its charateristics. Each characteristic define one behavior of the attribute, and multiple things can happen during the sdk/documentation generation process according to these characteristics.

#### allowed_chars

Python-style regular expression that will be used to validates the content of the attribute.

> Only working for attributes of type `string`.

Example:

```json
    "allowed_chars": "[A-Za-z]"
```

#### allowed_choices

Array containing the list of allowed values the attribute can take.

> Only working for attributes of type `enum`.

Example:

```json
    "allowed_choices": [
        "MALE",
        "FEMALE",
        "OTHER"
    ]
```

#### autogenerated

Boolean that tells if the value of the attribute will be autogenerated by the server.

> `autogenated` attributes are always `read_only`

Example:

```json
    "autogenerated": false
```

#### availability

Reserved for future usage.

#### channel

Reserved for future usage.

#### creation_only

Boolean that tells if the value can???t be modified once the object has been created.

Example:

```json
    "creation_only": false
```

#### default_order

Boolean that tells if that property is used as the default ordering key when fetching a list of objects.

> Only one attribute can be marked as `default_order` per Specification.

Example:

```json
    "default_order": true
```

#### default_value

string containing what will be the default value of the attribute if the attributes is not set when sending the object to the server.

Example:

```json
    "default_value": "hello world"
```

#### description

string containing the description of the attribute. This will be used when Monolithe generates the API documentation.

Example:

```json
    "description": "This attribute is very cool!"
```

#### exposed

Reserved for future usage.

#### filterable

Boolean that tells if the object can be filtered using that attribute.

Example:

```json
    "filterable": true
```

#### format

format for the attribute. It can be anything, and the interpretation will be up to the server. This can be seen as a macro for the `allowed_chars` property:

Example:

```json
    "format": "email"
```

#### min_length / max_length

Integer indicating the min / max length of an attribute.

> Only available for attribute of type `string`.

Example:

```json
    "min_length": 1,
    "max_length": 1024
```

#### min_value / max_value

Integer indicating the min / max value of an attribute.

> Only available for attribute of type `int` or `float`.

Example:

```json
    "min_value": -100,
    "max_value": 100
```

#### name

String indicating the name of the attribute.

Example:

```json
    "name": "firstName"
```

#### orderable

Boolean that tells if the attribute can be used to order a query.

Example:

```json
    "orderable": true
```

#### read_only

Boolean that tells if the attribute is read only

Example:

```json
    "read_only": false
```

#### required

Boolean that tells if the attribute is required or can be sent as `null`

> Note that `null` is different than 0.

Example:

```json
    "required": true
```

#### transient

Reserved for later usage.

#### type

The type of the attribute. It can be one of the following:

- `string`
- `boolean`
- `integer`
- `float`
- `enum`
- `list`
- `object`

#### subtype

The subtype of the attribute. It can be set to a remote entity `rest_name`. This is useful for the type `list` and `object`:

Example:

```json
    "type": "list",
    "subtype": "dog" // if we have a dog.spec
```


#### unique

Boolean that tells if the attribute value is unique.

> Depending on the server business logic implementation, it could mean unique in the context of its parent, or unique in the global context

Example:

```json
    "unique": true
```

### The Children Section

The Children section describes all the APIs that can be used to fetch its children.

The structure of an children api definition looks like:

```json
    {
        "rest_name": "legs",
        "relationship": "child"
        "get": true,
        "create": true,
        "put": false,
    }
```

The `rest_name` *must* be the remote specification `rest_name` attribute (which translates to the filename `<rest_name>.spec`).

This means it is possible to call:

    GET /unicorns/3/legs # get the list a legs of unicorn3
    POST /unicorns/3/legs # create a new leg for unicorn3

#### rest_name

The `rest_name` of the remote specification describing the children object.

#### relationship

Describes what kind of relation the parent has with the child. It can be:

- `child`: the standard relationship: all children are created under the parent
- `member`: this is used for the assignation api. Parent will have a list of members, but thoses member are not directly related to the parent
- `root`: special relationship that means the child has no parent (i.e. it's a root object.)

#### Operations

A children API describes has three additional tokens ??? `get`, `create`, `put` ??? that will discribe the operations that can be done on the children.

For instance:

```json
    "legs" : {
        ...
        "get": true,
        "create": true,
    }
```

> Note that if the relationship is `child` or `root`, only `get` and `create` are valid. In case of `member`, only `get` and `update` are valid


## Inheritance

As briefly discussed in a previous section, a Specification File can inherit information from other ones. The list of Specification Files a Specification File inherits from is given using the `extends` section of the `model` section.

### Model Inheritance
It is possible to inherits models values. The parent Specification can be a real declared object, or just a file that only contains the section you need.

For instance, we can have the following:

> The specifications are simplified for readablity

A file named `horse.spec`:

```json
    {
        "model": {
            "rest_name": "horse",
            "resource_name": "horses",
        },

        "attributes": [
            {
                "name": "name",
                "type": "string",
            },
            {
                "name": "age",
                "type": "integer",
            },
            {
                "name": "size",
                "type": "string",
            }
        ]
    }
```

A file named `unicorn.spec`:

```json
    {
        "model": {
            "extends": [
                "horse"
            ],
            "rest_name": "unicorn",
            "resource_name": "unicorns"
        },

        "attributes": [
            {
                "name": "hornSize",
                "type": "integer",
                //...
            }
        ]
    }
```

This will generate two objects, one `Horse` with `name`, `age` and `size` as attributes and one `Unicorn` with `name`, `age` and `size` and `hornSize`.

It is also possible to inherit APIs. For instance if you want all the objects in your model to have a common children api, say `metadata`, you can do the following:

file `@metadata-capable.spec`:

```json
    {
        "children": [
            {
                "rest_name": "metadata",
                "get": true,
                "create": true
            }
        ]
    }
```

file `horse.spec`:

```json
    {
        "model": {
            "extends": [
                "@metadata-capable"
            ],
            "rest_name": "unicorn",
            "resource_name": "unicorns"
        },

        "attributes": [
            {
                "hornSize": 22,
                "type": "integer",
            }
        ]
    }
```

Then both `Horse` and `Unicorn` object will have `metadata` as child API. 



#### Abstract Specification Files

In the previous example, you can notice the `@` prefixing the `@metadatas-capable.spec` Specification File name. This will make Monolithe to skip the generation of an actual object from that specification. It???s very useful to set some files that groups common attributes and apis, but doesn???t necessarily need to be generated as a solid api object.

#### Multiple inheritance

The `extends` property is an array, so it is possible to inherit apis and attributes from multiple files.

For instance:

``` json
    "extends": [
        "@metadatas-capable",
        "@named-object",
        "horse"
    ]
```

The ordering of the `extends` array will decide the precedence in case of conflicts. the information described in the specification at index 0 will be applied, then overwritten by index 1, etc. Finally, whatever is described in the current specification will overwrite values coming from an extension.

For instance, in the previous example, if both `@metadatas-capable` and `horse` contains a `package` attribute in the `model`, section, the one in `horse` will be the one used in the end.

