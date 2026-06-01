# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1572?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1572
- Title: Federal Carjacking Enforcement Act
- Congress: 119
- Bill type: S
- Bill number: 1572
- Origin chamber: Senate
- Introduced date: 2025-05-01
- Update date: 2026-05-27T20:35:27Z
- Update date including text: 2026-05-27T20:35:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in Senate
- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-04-30 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-05-11 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-05-11 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-05-11 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 404.
- Latest action: 2025-05-01: Introduced in Senate

## Actions

- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-04-30 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-05-11 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-05-11 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-05-11 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 404.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1572",
    "number": "1572",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Federal Carjacking Enforcement Act",
    "type": "S",
    "updateDate": "2026-05-27T20:35:27Z",
    "updateDateIncludingText": "2026-05-27T20:35:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-11",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 404.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-05-11",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-05-11",
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
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
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
      "text": "Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-01",
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
      "actionDate": "2025-05-01",
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
            "date": "2026-05-11T20:27:03Z",
            "name": "Reported By"
          },
          {
            "date": "2026-04-30T14:15:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-01T17:11:12Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-01T17:11:12Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "NM"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NV"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "TX"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "NC"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "MN"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "TN"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "NH"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "AL"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "NC"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "UT"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "MO"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "VA"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "MO"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "FL"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1572is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1572\nIN THE SENATE OF THE UNITED STATES\nMay 1, 2025 Mrs. Blackburn introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to improve the Federal carjacking statute.\n#### 1. Short title\nThis Act may be cited as the Federal Carjacking Enforcement Act .\n#### 2. Motor vehicles\nSection 2119 of title 18, United States Code, is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking , with the intent to cause death or serious bodily harm and inserting knowingly ; and\n**(2)**\nin paragraph (3), by striking if death results, and inserting if the motor vehicle is taken with the intent to cause death or serious bodily harm, and death results, .",
      "versionDate": "2025-05-01",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1572rs.xml",
      "text": "II\nCalendar No. 404\n119th CONGRESS\n2d Session\nS. 1572\nIN THE SENATE OF THE UNITED STATES\nMay 1, 2025 Mrs. Blackburn (for herself, Mr. Luj\u00e1n , Ms. Cortez Masto , Mr. Cornyn , Mr. Tillis , Ms. Klobuchar , Mr. Hagerty , Mrs. Shaheen , Mrs. Britt , Mr. Budd , Mr. Cruz , Mr. Lee , Mr. Hawley , Mr. Warner , Mr. Schmitt , Mrs. Moody , and Mr. Graham ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nMay 11, 2026 Reported by Mr. Grassley , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo amend title 18, United States Code, to improve the Federal carjacking statute.\n#### 1. Short title\nThis Act may be cited as the Federal Carjacking Enforcement Act .\n#### 2. Motor vehicles\nSection 2119 of title 18, United States Code, is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking , with the intent to cause death or serious bodily harm and inserting knowingly ; and\n**(2)**\nin paragraph (3), by striking if death results, and inserting if the motor vehicle is taken with the intent to cause death or serious bodily harm, and death results, .",
      "versionDate": "2026-05-11",
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
        "actionDate": "2025-11-19",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "6155",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Federal Carjacking Enforcement Act",
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
            "name": "Crimes against property",
            "updateDate": "2026-05-22T19:17:34Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2026-05-22T19:17:57Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2026-05-22T19:17:52Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2026-05-22T19:17:47Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2026-05-22T19:17:43Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-05-15T19:11:21Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1572is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-05-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1572rs.xml"
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
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Federal Carjacking Enforcement Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-05-13T04:53:27Z"
    },
    {
      "title": "Federal Carjacking Enforcement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T11:03:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Federal Carjacking Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to improve the Federal carjacking statute.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:24Z"
    }
  ]
}
```
