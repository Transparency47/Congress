# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/484?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/484
- Title: PLCAA Federal Jurisdiction Act
- Congress: 119
- Bill type: S
- Bill number: 484
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2026-02-04T04:11:36Z
- Update date including text: 2026-02-04T04:11:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/484",
    "number": "484",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "PLCAA Federal Jurisdiction Act",
    "type": "S",
    "updateDate": "2026-02-04T04:11:36Z",
    "updateDateIncludingText": "2026-02-04T04:11:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T22:23:52Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MO"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "LA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "FL"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "TN"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s484is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 484\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Lee (for himself, Mr. Hawley , Mr. Cassidy , Mr. Scott of Florida , Mrs. Blackburn , and Mr. Budd ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Protection of Lawful Commerce in Arms Act to provide for the removal and dismissal of qualified civil liability actions.\n#### 1. Short title\nThis Act may be cited as the Protection of Lawful Commerce in Arms Act Federal Jurisdiction Act or the PLCAA Federal Jurisdiction Act .\n#### 2. Removal and dismissal of qualified civil liability actions\nSection 3 of the Protection of Lawful Commerce in Arms Act ( 15 U.S.C. 7902 ) is amended by adding at the end the following:\n(c) Removal and dismissal (1) Removal In any civil action in a State court in which a defendant that is a manufacturer, seller, or trade association asserts that the civil action is a qualified civil liability action, that defendant may remove the civil action to the district court of the United States for the district and division embracing the place where the civil action is pending. (2) Dismissal The district court of the United States to which a civil action is removed under paragraph (1) may\u2014 (A) determine whether the civil action is a qualified civil liability action; and (B) dismiss the civil action accordingly. .",
      "versionDate": "2025-02-06",
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
        "actionDate": "2025-02-06",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1068",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "PLCAA Federal Jurisdiction Act",
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
            "name": "Civil actions and liability",
            "updateDate": "2025-07-03T12:55:11Z"
          },
          {
            "name": "Federal district courts",
            "updateDate": "2025-07-03T12:55:11Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-07-03T12:55:11Z"
          },
          {
            "name": "Jurisdiction and venue",
            "updateDate": "2025-07-03T12:55:11Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-07-03T12:55:11Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2025-07-03T12:55:11Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-09T11:42:34Z"
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
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s484is.xml"
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
      "title": "PLCAA Federal Jurisdiction Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:23:35Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PLCAA Federal Jurisdiction Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protection of Lawful Commerce in Arms Act Federal Jurisdiction Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Protection of Lawful Commerce in Arms Act to provide for the removal and dismissal of qualified civil liability actions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:19:00Z"
    }
  ]
}
```
