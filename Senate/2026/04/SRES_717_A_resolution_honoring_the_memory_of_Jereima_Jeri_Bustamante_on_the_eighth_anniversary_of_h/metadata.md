# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/717?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/717
- Title: A resolution honoring the memory of Jereima "Jeri" Bustamante on the eighth anniversary of her passing.
- Congress: 119
- Bill type: SRES
- Bill number: 717
- Origin chamber: Senate
- Introduced date: 2026-04-30
- Update date: 2026-05-18T18:44:28Z
- Update date including text: 2026-05-18T18:44:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in Senate
- 2026-04-30 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S2179)
- 2026-04-30 - IntroReferral: Submitted in Senate
- Latest action: 2026-04-30: Submitted in Senate

## Actions

- 2026-04-30 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S2179)
- 2026-04-30 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/717",
    "number": "717",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "A resolution honoring the memory of Jereima \"Jeri\" Bustamante on the eighth anniversary of her passing.",
    "type": "SRES",
    "updateDate": "2026-05-18T18:44:28Z",
    "updateDateIncludingText": "2026-05-18T18:44:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S2179)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T19:25:53Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres717is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 717\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2026 Mr. Scott of Florida submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nHonoring the memory of Jereima Jeri Bustamante on the eighth anniversary of her passing.\nThat the Senate\u2014\n**(1)**\nhonors the life and memory of Jereima Jeri Bustamante (referred to in this resolution as Jeri Bustamante );\n**(2)**\noffers heartfelt condolences to the family, loved ones, and friends of Jeri Bustamante;\n**(3)**\nrecognizes that living the American Dream remains possible for any individual who, following the example of Jeri Bustamante, works hard to pursue and achieve a goal; and\n**(4)**\nencourages the recipients of the Jereima Bustamante Memorial Scholarship to carry on the legacy of Jeri Bustamante.",
      "versionDate": "2026-04-30",
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
        "actionDate": "2025-04-08",
        "text": "Referred to the Committee on the Judiciary. (text: CR S2478)"
      },
      "number": "162",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution honoring the memory of Jereima \"Jeri\" Bustamante on the seventh anniversary of her passing.",
      "type": "SRES"
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
        "name": "Congress",
        "updateDate": "2026-05-18T18:44:28Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres717is.xml"
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
      "title": "A resolution honoring the memory of Jereima \"Jeri\" Bustamante on the eighth anniversary of her passing.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-06T04:18:29Z"
    },
    {
      "title": "A resolution honoring the memory of Jereima \"Jeri\" Bustamante on the eighth anniversary of her passing.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-01T10:56:30Z"
    }
  ]
}
```
