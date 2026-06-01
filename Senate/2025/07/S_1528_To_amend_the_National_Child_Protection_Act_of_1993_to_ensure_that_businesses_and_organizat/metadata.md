# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1528?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1528
- Title: CHILD Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1528
- Origin chamber: Senate
- Introduced date: 2025-04-30
- Update date: 2026-04-24T17:12:55Z
- Update date including text: 2026-04-24T17:12:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in Senate
- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S2716)
- 2025-07-24 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2025-07-28 - Committee: Committee on the Judiciary. Reported without amendment. Without written report.
- 2025-07-28 - Committee: Committee on the Judiciary. Reported without amendment. Without written report.
- 2025-07-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 128.
- 2026-04-21 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S1854; text: CR S1854)
- 2026-04-21 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2026-04-22 - Floor: Message on Senate action sent to the House.
- 2026-04-22 13:35:35 - Floor: Received in the House.
- 2026-04-22 13:41:12 - Floor: Held at the desk.
- Latest action: 2025-04-30: Introduced in Senate

## Actions

- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S2716)
- 2025-07-24 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2025-07-28 - Committee: Committee on the Judiciary. Reported without amendment. Without written report.
- 2025-07-28 - Committee: Committee on the Judiciary. Reported without amendment. Without written report.
- 2025-07-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 128.
- 2026-04-21 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S1854; text: CR S1854)
- 2026-04-21 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2026-04-22 - Floor: Message on Senate action sent to the House.
- 2026-04-22 13:35:35 - Floor: Received in the House.
- 2026-04-22 13:41:12 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1528",
    "number": "1528",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "CHILD Act of 2025",
    "type": "S",
    "updateDate": "2026-04-24T17:12:55Z",
    "updateDateIncludingText": "2026-04-24T17:12:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2026-04-22",
      "actionTime": "13:41:12",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2026-04-22",
      "actionTime": "13:35:35",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-04-22",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-04-21",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S1854; text: CR S1854)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-04-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-07-28",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 128.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-07-28",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-07-28",
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
      "text": "Committee on the Judiciary. Reported without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-24",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S2716)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-30",
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
            "date": "2025-07-28T20:01:50Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-24T14:07:12Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-30T16:33:43Z",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "IA"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "GA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1528is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1528\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2025 Mr. Durbin (for himself and Mr. Grassley ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the National Child Protection Act of 1993 to ensure that businesses and organizations that work with vulnerable populations are able to request background checks for their contractors who work with those populations, as well as for individuals that the businesses or organizations license or certify to provide care for those populations.\n#### 1. Short title\nThis Act may be cited as the Comprehensive Health and Integrity in Licensing and Documentation Act of 2025 or the CHILD Act of 2025 .\n#### 2. Defining covered individual for purposes of background checks under the National Child Protection Act of 1993\nSection 5(9)(B) of the National Child Protection Act of 1993 ( 34 U.S.C. 40104(9)(B) ) is amended\u2014\n**(1)**\nin clause (i)\u2014\n**(A)**\nby inserting , contracts with, after is employed by ;\n**(B)**\nby inserting , contract with, after be employed by ; and\n**(C)**\nby striking or at the end;\n**(2)**\nby redesignating clause (ii) as clause (iii);\n**(3)**\nby inserting after clause (i) the following:\n(ii) is employed by or volunteers with, or seeks to be employed by or volunteer with, an entity that is under contract with a qualified entity; ;\n**(4)**\nin clause (iii), as so redesignated, by adding or at the end; and\n**(5)**\nby adding at the end the following:\n(iv) is licensed or certified, or seeks to be licensed or certified, by a qualified entity; .",
      "versionDate": "2025-04-30",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1528rs.xml",
      "text": "II\nCalendar No. 128\n119th CONGRESS\n1st Session\nS. 1528\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2025 Mr. Durbin (for himself, Mr. Grassley , and Mr. Ossoff ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nJuly 28, 2025 Reported by Mr. Grassley , without amendment\nA BILL\nTo amend the National Child Protection Act of 1993 to ensure that businesses and organizations that work with vulnerable populations are able to request background checks for their contractors who work with those populations, as well as for individuals that the businesses or organizations license or certify to provide care for those populations.\n#### 1. Short title\nThis Act may be cited as the Comprehensive Health and Integrity in Licensing and Documentation Act of 2025 or the CHILD Act of 2025 .\n#### 2. Defining covered individual for purposes of background checks under the National Child Protection Act of 1993\nSection 5(9)(B) of the National Child Protection Act of 1993 ( 34 U.S.C. 40104(9)(B) ) is amended\u2014\n**(1)**\nin clause (i)\u2014\n**(A)**\nby inserting , contracts with, after is employed by ;\n**(B)**\nby inserting , contract with, after be employed by ; and\n**(C)**\nby striking or at the end;\n**(2)**\nby redesignating clause (ii) as clause (iii);\n**(3)**\nby inserting after clause (i) the following:\n(ii) is employed by or volunteers with, or seeks to be employed by or volunteer with, an entity that is under contract with a qualified entity; ;\n**(4)**\nin clause (iii), as so redesignated, by adding or at the end; and\n**(5)**\nby adding at the end the following:\n(iv) is licensed or certified, or seeks to be licensed or certified, by a qualified entity; .",
      "versionDate": "2025-07-28",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1528es.xml",
      "text": "119th CONGRESS\n2d Session\nS. 1528\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo amend the National Child Protection Act of 1993 to ensure that businesses and organizations that work with vulnerable populations are able to request background checks for their contractors who work with those populations, as well as for individuals that the businesses or organizations license or certify to provide care for those populations.\n#### 1. Short title\nThis Act may be cited as the Comprehensive Health and Integrity in Licensing and Documentation Act of 2025 or the CHILD Act of 2025 .\n#### 2. Defining covered individual for purposes of background checks under the National Child Protection Act of 1993\nSection 5(9)(B) of the National Child Protection Act of 1993 ( 34 U.S.C. 40104(9)(B) ) is amended\u2014\n**(1)**\nin clause (i)\u2014\n**(A)**\nby inserting , contracts with, after is employed by ;\n**(B)**\nby inserting , contract with, after be employed by ; and\n**(C)**\nby striking or at the end;\n**(2)**\nby redesignating clause (ii) as clause (iii);\n**(3)**\nby inserting after clause (i) the following:\n(ii) is employed by or volunteers with, or seeks to be employed by or volunteer with, an entity that is under contract with a qualified entity; ;\n**(4)**\nin clause (iii), as so redesignated, by adding or at the end; and\n**(5)**\nby adding at the end the following:\n(iv) is licensed or certified, or seeks to be licensed or certified, by a qualified entity; .",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-04-30",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "3100",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend the National Child Protection Act of 1993 to ensure that businesses and organizations that work with vulnerable populations are able to request background checks for their contractors who work with those populations, as well as for individuals that the businesses or organizations license or certify to provide care for those populations.",
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
            "name": "Child safety and welfare",
            "updateDate": "2025-08-08T15:14:13Z"
          },
          {
            "name": "Contracts and agency",
            "updateDate": "2025-08-08T15:14:18Z"
          },
          {
            "name": "Criminal justice information and records",
            "updateDate": "2025-08-08T15:14:06Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2025-08-08T15:14:27Z"
          },
          {
            "name": "Social work, volunteer service, charitable organizations",
            "updateDate": "2025-08-08T15:14:33Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-24T17:12:54Z"
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
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1528is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-07-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1528rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1528es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "CHILD Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T11:03:25Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "CHILD Act of 2025",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-04-22T03:38:22Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Comprehensive Health and Integrity in Licensing and Documentation Act of 2025",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-04-22T03:38:22Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Comprehensive Health and Integrity in Licensing and Documentation Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-07-30T06:38:22Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "CHILD Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-07-30T06:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CHILD Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Comprehensive Health and Integrity in Licensing and Documentation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the National Child Protection Act of 1993 to ensure that businesses and organizations that work with vulnerable populations are able to request background checks for their contractors who work with those populations, as well as for individuals that the businesses or organizations license or certify to provide care for those populations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:48:31Z"
    }
  ]
}
```
