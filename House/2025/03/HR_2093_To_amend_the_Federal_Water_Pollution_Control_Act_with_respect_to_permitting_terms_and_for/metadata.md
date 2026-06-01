# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2093?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2093
- Title: To amend the Federal Water Pollution Control Act with respect to permitting terms, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 2093
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2025-03-31T13:50:10Z
- Update date including text: 2025-03-31T13:50:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-14 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-14 - Committee: Referred to the Subcommittee on Water Resources and Environment.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2093",
    "number": "2093",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "C000059",
        "district": "41",
        "firstName": "Ken",
        "fullName": "Rep. Calvert, Ken [R-CA-41]",
        "lastName": "Calvert",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "To amend the Federal Water Pollution Control Act with respect to permitting terms, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-03-31T13:50:10Z",
    "updateDateIncludingText": "2025-03-31T13:50:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water Resources and Environment.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-03-14T13:05:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-14T22:08:06Z",
              "name": "Referred to"
            }
          },
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "CA"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2093ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2093\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Calvert (for himself, Mr. Garamendi , and Mr. Rouzer ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Federal Water Pollution Control Act with respect to permitting terms, and for other purposes.\n#### 1. National pollutant discharge elimination system (NPDES) terms\n##### (a) In general\nSection 402(b)(1)(B) of the Federal Water Pollution Control Act ( 33 U.S.C. 1342(b)(1)(B) ) is amended to read as follows:\n(B) are for fixed terms\u2014 (i) not exceeding 10 years, for a permit issued to a State or municipality; and (ii) not exceeding 5 years, for a permit issued to any person not described in clause (i); and .\n##### (b) Technical corrections\nSection 402( l )(3) of the Federal Water Pollution Control Act (33 U.S.C. 1342( l )(3)) is amended\u2014\n**(1)**\nin subparagraph (B)\u2014\n**(A)**\nby striking section 402 and inserting this section ; and\n**(B)**\nby striking federal and inserting Federal ; and\n**(2)**\nin subparagraph (C)\u2014\n**(A)**\nby striking Section and inserting section ;\n**(B)**\nby striking 402(p)(6) and inserting subsection (p)(6) ;\n**(C)**\nby striking 402(l)(3)(A), and inserting subparagraph (A), ; and\n**(D)**\nby striking 402(l)(3)(A). and inserting such subparagraph. .",
      "versionDate": "2025-03-14",
      "versionType": "Introduced in House"
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
        "name": "Environmental Protection",
        "updateDate": "2025-03-31T13:50:10Z"
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
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2093ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Water Pollution Control Act with respect to permitting terms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-28T11:18:25Z"
    },
    {
      "title": "To amend the Federal Water Pollution Control Act with respect to permitting terms, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-15T08:05:54Z"
    }
  ]
}
```
