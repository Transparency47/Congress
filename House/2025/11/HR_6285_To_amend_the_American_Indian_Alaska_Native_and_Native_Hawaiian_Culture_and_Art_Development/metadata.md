# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6285?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6285
- Title: Native Arts and Culture Promotion Act
- Congress: 119
- Bill type: HR
- Bill number: 6285
- Origin chamber: House
- Introduced date: 2025-11-21
- Update date: 2025-12-18T15:54:38Z
- Update date including text: 2025-12-18T15:54:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-21: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-11-21: Introduced in House

## Actions

- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-21",
    "latestAction": {
      "actionDate": "2025-11-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6285",
    "number": "6285",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "T000487",
        "district": "2",
        "firstName": "Jill",
        "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
        "lastName": "Tokuda",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Native Arts and Culture Promotion Act",
    "type": "HR",
    "updateDate": "2025-12-18T15:54:38Z",
    "updateDateIncludingText": "2025-12-18T15:54:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-21",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-21",
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
          "date": "2025-11-21T14:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "HI"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "AK"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6285ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6285\nIN THE HOUSE OF REPRESENTATIVES\nNovember 21, 2025 Ms. Tokuda (for herself and Mr. Case ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the American Indian, Alaska Native, and Native Hawaiian Culture and Art Development Act.\n#### 1. Short title\nThis Act may be cited as the Native Arts and Culture Promotion Act .\n#### 2. Amendments to American Indian, Alaska Native, and Native Hawaiian Culture and Art Development Act\nSection 1521 of the American Indian, Alaska Native, and Native Hawaiian Culture and Art Development Act ( 20 U.S.C. 4441 ) is amended\u2014\n**(1)**\nin subsection (a), by striking private, ; and\n**(2)**\nin subsection (c)\u2014\n**(A)**\nby amending paragraph (2) to read as follows:\n(2) For any grants made with respect to Native Hawaiian art and culture, the members of the governing board which is required to be established under paragraph (1) shall\u2014 (A) include Native Hawaiians and individuals widely recognized in the field of Native Hawaiian art and culture, and (B) serve for a fixed term. ; and\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (A), striking the comma at the end and inserting , and ;\n**(ii)**\nby striking subparagraph (B); and\n**(iii)**\nby redesignating subparagraph (C) as subparagraph (B).",
      "versionDate": "2025-11-21",
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
        "name": "Native Americans",
        "updateDate": "2025-12-18T15:54:38Z"
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
      "date": "2025-11-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6285ih.xml"
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
      "title": "Native Arts and Culture Promotion Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T05:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Native Arts and Culture Promotion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T05:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the American Indian, Alaska Native, and Native Hawaiian Culture and Art Development Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-18T05:18:14Z"
    }
  ]
}
```
