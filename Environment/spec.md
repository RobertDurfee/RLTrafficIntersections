# API Specification

## Creating an Intersection Environment

### Request
```json
{
  "paths": [
    {
      "type": "automated",
      "spawnPeriodMean": null,
      "spawnPeriodStdDev": null,
      "speedLimit": null,
      "xs": [],
      "ys": []
    },
    {
      "type": "controlled",
      "speedLimit": null,
      "xs": [],
      "ys": []
    }
  ],
  "cars": [
    {
      "acceleration": null,
      "followingDistanceMean": null,
      "followingDistanceStdDev": null,
      "speedingMean": null,
      "speedingStdDev": null,
      "width": null,
      "height": null
    }
  ]
}
```

### Response

```json
{
  "paths": [
    {
      "$id": "c7cba0de18db4667836626404ddd6ccf",
      "type": "automated",
      "spawnPeriodMean": null,
      "spawnPeriodStdDev": null,
      "speedLimit": null,
      "xs": [],
      "ys": [],
      "cars": [
        {
          "$id": "1ec43cc4f6cd455a99b65550931a5829",
          "type": { "$ref": "a01d619d8ad049a08a17c977ec55f06e" },
          "x": null,
          "y": null,
          "dx": null,
          "dy": null
        }
      ]
    },
    {
      "$id": "af396791395747a18b13a5cb5a0ea035",
      "type": "controlled",
      "speedLimit": null,
      "xs": [],
      "ys": [],
      "cars": [
        {
          "$id": "612cfc8822ff442dac240323a7b0edff",
          "type": { "$ref": "f476644803a541928264fdf630598459" },
          "x": null,
          "y": null,
          "dx": null,
          "dy": null
        }
      ]
    }
  ],
  "carTypes": [
    {
      "$id": "a01d619d8ad049a08a17c977ec55f06e"
    },
    {
      "$id": "f476644803a541928264fdf630598459"
    }
  ]
}
```