# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/583?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/583
- Title: A resolution recognizing 2026 as "The Year of The Power of Nurses" in Celebration of the 130th Anniversary of the American Nurses Association.
- Congress: 119
- Bill type: SRES
- Bill number: 583
- Origin chamber: Senate
- Introduced date: 2026-01-15
- Update date: 2026-01-22T15:25:47Z
- Update date including text: 2026-01-22T15:25:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in Senate
- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S260)
- Latest action: 2026-01-15: Introduced in Senate

## Actions

- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S260)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/583",
    "number": "583",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "A resolution recognizing 2026 as \"The Year of The Power of Nurses\" in Celebration of the 130th Anniversary of the American Nurses Association.",
    "type": "SRES",
    "updateDate": "2026-01-22T15:25:47Z",
    "updateDateIncludingText": "2026-01-22T15:25:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S260)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T19:31:44Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres583is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 583\nIN THE SENATE OF THE UNITED STATES\nJanuary 15, 2026 Mr. Merkley submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nRecognizing 2026 as The Year of The Power of Nurses in Celebration of the 130th Anniversary of the American Nurses Association.\nThat the Senate\u2014\n**(1)**\nrecognizes 2026 as The Year of The Power of Nurses in recognition of the 130th Anniversary of the American Nurses Association; and\n**(2)**\nhonors the extraordinary contributions of nurses to the health, safety, and prosperity of the United States of America.",
      "versionDate": "2026-01-15",
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
        "actionDate": "2026-01-20",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1010",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Recognizing 2026 as \"The Year of The Power of Nurses\" in Celebration of the 130th Anniversary of the American Nurses Association.",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-01-20T15:20:19Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres583is.xml"
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
      "title": "A resolution recognizing 2026 as \"The Year of The Power of Nurses\" in Celebration of the 130th Anniversary of the American Nurses Association.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T08:03:46Z"
    },
    {
      "title": "A resolution recognizing 2026 as \"The Year of The Power of Nurses\" in Celebration of the 130th Anniversary of the American Nurses Association.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T11:56:24Z"
    }
  ]
}
```
