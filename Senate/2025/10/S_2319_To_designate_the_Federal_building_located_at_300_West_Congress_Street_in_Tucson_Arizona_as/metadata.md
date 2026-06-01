# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2319?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2319
- Title: A bill to designate the Federal building located at 300 West Congress Street in Tucson, Arizona, as the "Raul M. Grijalva Federal Building".
- Congress: 119
- Bill type: S
- Bill number: 2319
- Origin chamber: Senate
- Introduced date: 2025-07-17
- Update date: 2026-03-31T16:19:31Z
- Update date including text: 2026-03-31T16:19:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in Senate
- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- 2025-10-29 - Committee: Committee on Environment and Public Works. Ordered to be reported without amendment favorably.
- 2025-10-29 - Committee: Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.
- 2025-10-29 - Committee: Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.
- 2025-10-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 227.
- Latest action: 2025-07-17: Introduced in Senate

## Actions

- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- 2025-10-29 - Committee: Committee on Environment and Public Works. Ordered to be reported without amendment favorably.
- 2025-10-29 - Committee: Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.
- 2025-10-29 - Committee: Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.
- 2025-10-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 227.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2319",
    "number": "2319",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "K000377",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Kelly, Mark [D-AZ]",
        "lastName": "Kelly",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "A bill to designate the Federal building located at 300 West Congress Street in Tucson, Arizona, as the \"Raul M. Grijalva Federal Building\".",
    "type": "S",
    "updateDate": "2026-03-31T16:19:31Z",
    "updateDateIncludingText": "2026-03-31T16:19:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-29",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 227.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-29",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-10-29",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-29",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Environment and Public Works. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-17",
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
        "item": [
          {
            "date": "2025-10-29T21:33:41Z",
            "name": "Reported By"
          },
          {
            "date": "2025-10-29T14:00:08Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-17T15:54:49Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2319is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2319\nIN THE SENATE OF THE UNITED STATES\nJuly 17, 2025 Mr. Kelly (for himself and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo designate the Federal building located at 300 West Congress Street in Tucson, Arizona, as the Ra\u00fal M. Grijalva Federal Building .\n#### 1. Designation\nThe Federal building located at 300 West Congress Street in Tucson, Arizona, shall be known and designated as the Ra\u00fal M. Grijalva Federal Building .\n#### 2. References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the Federal building referred to in section 1 shall be deemed to be a reference to the Ra\u00fal M. Grijalva Federal Building .",
      "versionDate": "2025-07-17",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2319rs.xml",
      "text": "II\nCalendar No. 227\n119th CONGRESS\n1st Session\nS. 2319\nIN THE SENATE OF THE UNITED STATES\nJuly 17, 2025 Mr. Kelly (for himself and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nOctober 29, 2025 Reported by Mrs. Capito , without amendment\nA BILL\nTo designate the Federal building located at 300 West Congress Street in Tucson, Arizona, as the Ra\u00fal M. Grijalva Federal Building .\n#### 1. Designation\nThe Federal building located at 300 West Congress Street in Tucson, Arizona, shall be known and designated as the Ra\u00fal M. Grijalva Federal Building .\n#### 2. References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the Federal building referred to in section 1 shall be deemed to be a reference to the Ra\u00fal M. Grijalva Federal Building .",
      "versionDate": "2025-10-29",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-06-03",
        "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management."
      },
      "number": "3671",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To designate the Federal building located at 300 West Congress Street in Tucson, Arizona, as the \"Ra\u00fal M. Grijalva Federal Building\".",
      "type": "HR"
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
            "name": "Arizona",
            "updateDate": "2025-11-17T18:32:31Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2025-11-17T18:32:27Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-11-17T18:32:21Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-11-17T18:32:35Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-08T16:12:14Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2319is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2319rs.xml"
        }
      ],
      "type": "Reported in Senate"
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
      "title": "A bill to designate the Federal building located at 300 West Congress Street in Tucson, Arizona, as the \"Raul M. Grijalva Federal Building\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T04:18:29Z"
    },
    {
      "title": "A bill to designate the Federal building located at 300 West Congress Street in Tucson, Arizona, as the \"Raul M. Grijalva Federal Building\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-18T10:56:19Z"
    }
  ]
}
```
