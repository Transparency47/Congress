# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3463?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3463
- Title: Protect Greenbury Point Conservation Area Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3463
- Origin chamber: Senate
- Introduced date: 2025-12-11
- Update date: 2026-01-12T18:48:46Z
- Update date including text: 2026-01-12T18:48:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in Senate
- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-12-11: Introduced in Senate

## Actions

- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3463",
    "number": "3463",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Protect Greenbury Point Conservation Area Act of 2025",
    "type": "S",
    "updateDate": "2026-01-12T18:48:46Z",
    "updateDateIncludingText": "2026-01-12T18:48:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T20:19:52Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3463is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3463\nIN THE SENATE OF THE UNITED STATES\nDecember 11, 2025 Mr. Van Hollen (for himself and Ms. Alsobrooks ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo prohibit the development of a golf course at Greenbury Point Conservation Area at Naval Support Activity Annapolis, Maryland.\n#### 1. Short title\nThis Act may be cited as the Protect Greenbury Point Conservation Area Act of 2025 .\n#### 2. Prohibition on development of a golf course at Greenbury Point Conservation Area at Naval Support Activity Annapolis, Maryland\nSection 2855 of the Military Construction Authorization Act for Fiscal Year 2024 (division B of Public Law 118\u201331 ; 137 Stat. 766) is amended\u2014\n**(1)**\nin the section heading, by striking Limitation on authority to modify or restrict public access to and inserting Prohibition on development of a golf course at ;\n**(2)**\nin subsection (a), by inserting construct a golf course on, or otherwise before modify or restrict ; and\n**(3)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by striking ; or and inserting a semicolon;\n**(B)**\nin paragraph (2), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following new paragraph:\n(3) restrictions related to environmental restoration of the Greenbury Point Conservation Area in a manner consistent with existing law and regulation. .",
      "versionDate": "2025-12-11",
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
        "actionDate": "2025-12-11",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "6628",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protect Greenbury Point Conservation Area Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-18",
        "text": "Became Public Law No: 119-60."
      },
      "number": "1071",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-06T19:45:11Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3463is.xml"
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
      "title": "Protect Greenbury Point Conservation Area Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-31T03:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protect Greenbury Point Conservation Area Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the development of a golf course at Greenbury Point Conservation Area at Naval Support Activity Annapolis, Maryland.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-31T03:33:15Z"
    }
  ]
}
```
