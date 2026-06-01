# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4079?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4079
- Title: Safer Response Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4079
- Origin chamber: House
- Introduced date: 2025-06-23
- Update date: 2026-04-03T19:55:49Z
- Update date including text: 2026-04-03T19:55:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-23: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-06-23: Introduced in House

## Actions

- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-23",
    "latestAction": {
      "actionDate": "2025-06-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4079",
    "number": "4079",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001090",
        "district": "9",
        "firstName": "Josh",
        "fullName": "Rep. Harder, Josh [D-CA-9]",
        "lastName": "Harder",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Safer Response Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-03T19:55:49Z",
    "updateDateIncludingText": "2026-04-03T19:55:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-23",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-23",
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
          "date": "2025-06-23T16:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "NY"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "IA"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4079ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4079\nIN THE HOUSE OF REPRESENTATIVES\nJune 23, 2025 Mr. Harder of California (for himself and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to reauthorize grants for first responder training.\n#### 1. Short title\nThis Act may be cited as the Safer Response Act of 2025 .\n#### 2. First responder training program\nSection 546 of the Public Health Service Act ( 42 U.S.C. 290ee\u20131 ) is amended\u2014\n**(1)**\nin subsection (a), by striking tribes and tribal and inserting Tribes and Tribal ;\n**(2)**\nin subsections (a), (c), and (d)\u2014\n**(A)**\nby striking approved or cleared each place it appears and inserting approved, cleared, or otherwise legally marketed ; and\n**(B)**\nby striking opioid each place it appears;\n**(3)**\nin subsection (f)\u2014\n**(A)**\nby striking approved or cleared each place it appears and inserting approved, cleared, or otherwise legally marketed ;\n**(B)**\nin paragraph (1), by striking opioid ;\n**(C)**\nin paragraph (2)\u2014\n**(i)**\nby striking opioid and heroin and inserting opioid, heroin, and other drug ; and\n**(ii)**\nby striking opioid overdose and inserting overdose ; and\n**(D)**\nin paragraph (3), by striking opioid and heroin ; and\n**(4)**\nin subsection (h), by striking $36,000,000 for each of fiscal years 2019 through 2023 and inserting $57,000,000 for each of fiscal years 2026 through 2030 .",
      "versionDate": "2025-06-23",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-12-01",
        "text": "Became Public Law No: 119-44."
      },
      "number": "2483",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SUPPORT for Patients and Communities Reauthorization Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-18",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2121",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SUPPORT for Patients and Communities Reauthorization Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-30",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2532",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Safe Response Act",
      "type": "S"
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
        "updateDate": "2025-07-31T11:48:46Z"
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
      "date": "2025-06-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4079ih.xml"
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
      "title": "Safer Response Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-09T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safer Response Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-09T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to reauthorize grants for first responder training.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-09T04:19:02Z"
    }
  ]
}
```
