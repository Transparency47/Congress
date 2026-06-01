# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2532?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2532
- Title: Safe Response Act
- Congress: 119
- Bill type: S
- Bill number: 2532
- Origin chamber: Senate
- Introduced date: 2025-07-30
- Update date: 2026-04-03T19:55:26Z
- Update date including text: 2026-04-03T19:55:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-30: Introduced in Senate
- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-07-30: Introduced in Senate

## Actions

- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-30",
    "latestAction": {
      "actionDate": "2025-07-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2532",
    "number": "2532",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001230",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Baldwin, Tammy [D-WI]",
        "lastName": "Baldwin",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "Safe Response Act",
    "type": "S",
    "updateDate": "2026-04-03T19:55:26Z",
    "updateDateIncludingText": "2026-04-03T19:55:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-30",
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
          "date": "2025-07-30T15:24:04Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NH"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-07-30",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2532is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2532\nIN THE SENATE OF THE UNITED STATES\nJuly 30, 2025 Ms. Baldwin (for herself, Ms. Hassan , and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo reauthorize the program of first responder training.\n#### 1. Short title\nThis Act may be cited as the Safe Response Act .\n#### 2. First responder training program\nSection 546 of the Public Health Service Act ( 42 U.S.C. 290ee\u20131 ) is amended\u2014\n**(1)**\nin subsection (a), by striking tribes and tribal and inserting Tribes and Tribal ;\n**(2)**\nin subsections (a), (c), and (d)\u2014\n**(A)**\nby striking approved or cleared each place it appears and inserting approved, cleared, or otherwise legally marketed ; and\n**(B)**\nby striking opioid each place it appears;\n**(3)**\nin subsection (f)\u2014\n**(A)**\nby striking approved or cleared each place it appears and inserting approved, cleared, or otherwise legally marketed ;\n**(B)**\nin paragraph (1), by striking opioid ;\n**(C)**\nin paragraph (2)\u2014\n**(i)**\nby striking opioid and heroin and inserting opioid, heroin, and other drug ; and\n**(ii)**\nby striking opioid overdose and inserting overdose ; and\n**(D)**\nin paragraph (3), by striking opioid and heroin ; and\n**(4)**\nin subsection (h), by striking $36,000,000 for each of fiscal years 2019 through 2023 and inserting $57,000,000 for each of fiscal years 2026 through 2030 .",
      "versionDate": "2025-07-30",
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
        "actionDate": "2025-06-23",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "4079",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Safer Response Act of 2025",
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
        "updateDate": "2025-09-17T16:15:33Z"
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
      "date": "2025-07-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2532is.xml"
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
      "title": "Safe Response Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-07T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safe Response Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reauthorize the program of first responder training.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-07T04:48:17Z"
    }
  ]
}
```
