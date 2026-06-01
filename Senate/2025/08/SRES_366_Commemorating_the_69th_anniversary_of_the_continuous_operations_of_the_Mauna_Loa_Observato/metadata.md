# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/366?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/366
- Title: A resolution commemorating the 69th anniversary of the continuous operations of the Mauna Loa Observatory.
- Congress: 119
- Bill type: SRES
- Bill number: 366
- Origin chamber: Senate
- Introduced date: 2025-08-01
- Update date: 2026-04-09T13:31:00Z
- Update date including text: 2026-04-09T13:31:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in Senate
- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Referred to the Committee on Commerce, Science, and Transportation. (text: CR S5212)
- Latest action: 2025-08-01: Introduced in Senate

## Actions

- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Referred to the Committee on Commerce, Science, and Transportation. (text: CR S5212)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/366",
    "number": "366",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "H001042",
        "district": "",
        "firstName": "Mazie",
        "fullName": "Sen. Hirono, Mazie K. [D-HI]",
        "lastName": "Hirono",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "A resolution commemorating the 69th anniversary of the continuous operations of the Mauna Loa Observatory.",
    "type": "SRES",
    "updateDate": "2026-04-09T13:31:00Z",
    "updateDateIncludingText": "2026-04-09T13:31:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-01",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Commerce, Science, and Transportation. (text: CR S5212)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-08-01T21:38:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
      "type": "Standing"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres366is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 366\nIN THE SENATE OF THE UNITED STATES\nAugust 1, 2025 Ms. Hirono submitted the following resolution; which was referred to the Committee on Commerce, Science, and Transportation\nRESOLUTION\nCommemorating the 69th anniversary of the continuous operations of the Mauna Loa Observatory.\nThat the Senate\u2014\n**(1)**\ncommemorates the 69th anniversary of the continuous operations of the Mauna Loa Observatory (referred to in this resolution as the MLO );\n**(2)**\nrecognizes the monumental contributions that the research conducted at and data produced by the MLO has provided to the global leadership in atmospheric research of the United States;\n**(3)**\nreaffirms the Senate\u2019s strong support for the critical ongoing operations of the MLO, including its 4 sites on Hawaii Island; and\n**(4)**\nhonors the cultural significance of Mauna Loa to the Native Hawaiian community.",
      "versionDate": "2025-08-01",
      "versionType": "IS"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-08-05",
        "text": "Referred to the House Committee on Science, Space, and Technology."
      },
      "number": "637",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Commemorating the 69th anniversary of the continuous operations of the Mauna Loa Observatory.",
      "type": "HRES"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Atmospheric science and weather",
            "updateDate": "2025-09-12T16:37:32Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2026-04-09T13:31:00Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2025-09-12T16:38:07Z"
          },
          {
            "name": "Hawaii",
            "updateDate": "2025-09-12T16:34:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-09-12T14:52:41Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres366is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution commemorating the 69th anniversary of the continuous operations of the Mauna Loa Observatory.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T05:03:52Z"
    },
    {
      "title": "A resolution commemorating the 69th anniversary of the continuous operations of the Mauna Loa Observatory.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T10:56:21Z"
    }
  ]
}
```
