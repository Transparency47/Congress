# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/731?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/731
- Title: A resolution recognizing the 175th anniversary of the founding of Alpha Delta Pi Sorority.
- Congress: 119
- Bill type: SRES
- Bill number: 731
- Origin chamber: Senate
- Introduced date: 2026-05-14
- Update date: 2026-05-29T14:59:36Z
- Update date including text: 2026-05-29T14:59:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-05-14: Introduced in Senate
- 2026-05-14 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S2308-2309)
- 2026-05-14 - IntroReferral: Submitted in Senate
- Latest action: 2026-05-14: Submitted in Senate

## Actions

- 2026-05-14 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S2308-2309)
- 2026-05-14 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-14",
    "latestAction": {
      "actionDate": "2026-05-14",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/731",
    "number": "731",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M001244",
        "district": "",
        "firstName": "Ashley",
        "fullName": "Sen. Moody, Ashley [R-FL]",
        "lastName": "Moody",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "A resolution recognizing the 175th anniversary of the founding of Alpha Delta Pi Sorority.",
    "type": "SRES",
    "updateDate": "2026-05-29T14:59:36Z",
    "updateDateIncludingText": "2026-05-29T14:59:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S2308-2309)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in Senate",
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
          "date": "2026-05-14T18:05:34Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres731is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 731\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2026 Mrs. Moody submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nRecognizing the 175th anniversary of the founding of Alpha Delta Pi Sorority.\nThat the Senate\u2014\n**(1)**\ncongratulates Alpha Delta Pi Sorority on the occasion of its 175th anniversary;\n**(2)**\nacknowledges the contributions of Alpha Delta Pi members to education, science and technology, the arts, athletics, government, the military, business, and community service; and\n**(3)**\nrecognizes the members of Alpha Delta Pi Sorority for their lifelong commitment to personal growth, friendship, and community enrichment.",
      "versionDate": "2026-05-14",
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
        "actionDate": "2026-05-13",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "1281",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Recognizing the 175th anniversary of the founding of Alpha Delta Pi sorority.",
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
        "name": "Education",
        "updateDate": "2026-05-29T14:59:36Z"
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
      "date": "2026-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres731is.xml"
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
      "title": "A resolution recognizing the 175th anniversary of the founding of Alpha Delta Pi Sorority.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-19T00:48:50Z"
    },
    {
      "title": "A resolution recognizing the 175th anniversary of the founding of Alpha Delta Pi Sorority.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T10:56:22Z"
    }
  ]
}
```
