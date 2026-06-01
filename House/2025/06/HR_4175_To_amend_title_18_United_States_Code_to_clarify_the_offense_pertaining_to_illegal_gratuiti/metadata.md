# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4175?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4175
- Title: No Gratuities for Governing Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4175
- Origin chamber: House
- Introduced date: 2025-06-26
- Update date: 2026-04-03T08:05:35Z
- Update date including text: 2026-04-03T08:05:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-26: Introduced in House

## Actions

- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4175",
    "number": "4175",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000599",
        "district": "10",
        "firstName": "Daniel",
        "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
        "lastName": "Goldman",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "No Gratuities for Governing Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-03T08:05:35Z",
    "updateDateIncludingText": "2026-04-03T08:05:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T14:05:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "AZ"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "NC"
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "PA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4175ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4175\nIN THE HOUSE OF REPRESENTATIVES\nJune 26, 2025 Mr. Goldman of New York (for himself and Mr. Ciscomani ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to clarify the offense pertaining to illegal gratuities concerning programs receiving Federal funds.\n#### 1. Short title\nThis Act may be cited as the No Gratuities for Governing Act of 2025 .\n#### 2. Illegal gratuities concerning programs receiving Federal funds\nSection 666 of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating subsections (b) through (d) as subsection (c) through (e), respectively;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nby striking if the circumstance described in subsection (b) of this section exists and inserting if the circumstance described in subsection (c) of this section exists ; and\n**(B)**\nby striking imprisoned not more than 10 years, and inserting imprisoned not more than 15 years, ;\n**(3)**\nby inserting after subsection (a) the following:\n(b) Whoever, if the circumstance described in subsection (c) of this section exists\u2014 (1) directly or indirectly, knowingly and purposefully gives, offers, or promises anything of value of $1,000 or more to any agent of an organization, or of a State, local, or Indian Tribal government, or any agency thereof, for or because of any official act performed by such agent in connection with any business, transaction, or series of transactions of such organization, government, or agency involving anything of value of $5,000 or more; or (2) being an agent of an organization, or of a State, local, or Indian Tribal government, or any agency thereof, directly or indirectly, knowingly and purposefully demands, seeks, receives, accepts, or agrees to receive or accept anything of value of $1,000 or more personally for or because of any official act performed by such agent in connection with any business, transaction, or series of transactions of such organization, government, or agency involving anything of value of $5,000 or more; shall be fined under this title, imprisoned not more than 2 years, or both. ; and\n**(4)**\nin subsection (c), as redesignated, by striking circumstance referred to in subsection (a) and inserting circumstances referred to in subsections (a) and (b) .",
      "versionDate": "2025-06-26",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-07-22T12:46:02Z"
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
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4175ih.xml"
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
      "title": "No Gratuities for Governing Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-09T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Gratuities for Governing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-09T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to clarify the offense pertaining to illegal gratuities concerning programs receiving Federal funds.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-09T04:18:24Z"
    }
  ]
}
```
