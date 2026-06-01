# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3635?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3635
- Title: Fort Peck Water System Reauthorization Act
- Congress: 119
- Bill type: S
- Bill number: 3635
- Origin chamber: Senate
- Introduced date: 2026-01-14
- Update date: 2026-05-29T13:11:54Z
- Update date including text: 2026-05-29T13:11:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-14: Introduced in Senate
- 2026-01-14 - IntroReferral: Introduced in Senate
- 2026-01-14 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.
- Latest action: 2026-01-14: Introduced in Senate

## Actions

- 2026-01-14 - IntroReferral: Introduced in Senate
- 2026-01-14 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3635",
    "number": "3635",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "D000618",
        "district": "",
        "firstName": "Steve",
        "fullName": "Sen. Daines, Steve [R-MT]",
        "lastName": "Daines",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Fort Peck Water System Reauthorization Act",
    "type": "S",
    "updateDate": "2026-05-29T13:11:54Z",
    "updateDateIncludingText": "2026-05-29T13:11:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-14",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-14",
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
          "date": "2026-01-14T17:45:08Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-17T14:00:14Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3635is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3635\nIN THE SENATE OF THE UNITED STATES\nJanuary 14, 2026 Mr. Daines (for himself and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo reauthorize the Fort Peck Reservation Rural Water System Act of 2000.\n#### 1. Short title\nThis Act may be cited as the Fort Peck Water System Reauthorization Act .\n#### 2. Reauthorization\nSection 9 of the Fort Peck Reservation Rural Water System Act of 2000 ( Public Law 106\u2013382 ; 114 Stat. 1457; 123 Stat. 2856; 128 Stat. 164; 132 Stat. 2906) is amended, in each of subsections (a)(1) and (b), by striking 2026 and inserting 2028 .",
      "versionDate": "2026-01-14",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-05-22",
        "text": "Placed on the Union Calendar, Calendar No. 581."
      },
      "number": "9022",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Energy and Water Development and Related Agencies Appropriations Act, 2027",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-05-14",
        "text": "Ordered to be Reported by Unanimous Consent."
      },
      "number": "7250",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To reauthorize the Fort Peck Reservation Rural Water System Act of 2000.",
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
            "name": "Montana",
            "updateDate": "2026-03-30T18:10:46Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2026-03-30T18:11:01Z"
          },
          {
            "name": "Water resources funding",
            "updateDate": "2026-03-30T18:10:51Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2026-03-30T18:10:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2026-02-10T21:40:54Z"
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
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3635is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Fort Peck Water System Reauthorization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fort Peck Water System Reauthorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-05T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reauthorize the Fort Peck Reservation Rural Water System Act of 2000.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-05T05:48:35Z"
    }
  ]
}
```
