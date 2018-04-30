# Pangram Validation

Check a string to determine if all the alpha characters are a pangram.

**URL** : `/check-string/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Headers** : `Content-Type: application/json`

**Data constraints** : JSON

Provide the string to be analyzed.

```json
{
    "data": "[unicode]"
}
```

**Data example** All fields must be sent.

```json
{
    "data": "the quick brown fox jumps over the lazy dog"
}
```

## Success Response

**Condition** : The string sent contains at least one instance of every letter in the alphabet.

**Code** : `200 OK`

**Headers** : `Content-Type: application/json`

**Content example**

```json
{
    "success": True
}
```

## Error Responses

**Condition** : 'data' key not in JSON payload.

**Code** : `400 BAD REQUEST`

**Headers** : `Content-Type: application/json`

**Content**

```json
{
    "error": "'data' key missing from JSON payload."
}
```

***

**Condition** : Data type sent is not a string.

**Code** : `400 BAD REQUEST`

**Headers** : `Content-Type: application/json`

**Content example**

```json
{
    "error": "Value of 'data' key is not of type 'string'."
}
```

**Condition** : Sting passed is not a pangram

**Code** : `400 BAD REQUEST`

**Headers** : `Content-Type: application/json`

**Content example**

```json
{
    "error": False
}
```