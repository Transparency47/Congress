# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5118?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5118
- Title: Protecting Law Enforcement from Doxxing Act
- Congress: 119
- Bill type: HR
- Bill number: 5118
- Origin chamber: House
- Introduced date: 2025-09-03
- Update date: 2025-12-11T09:07:39Z
- Update date including text: 2025-12-11T09:07:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-03: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-03: Introduced in House

## Actions

- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-03",
    "latestAction": {
      "actionDate": "2025-09-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5118",
    "number": "5118",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "O000175",
        "district": "5",
        "firstName": "Andrew",
        "fullName": "Rep. Ogles, Andrew [R-TN-5]",
        "lastName": "Ogles",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Protecting Law Enforcement from Doxxing Act",
    "type": "HR",
    "updateDate": "2025-12-11T09:07:39Z",
    "updateDateIncludingText": "2025-12-11T09:07:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-03",
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
      "actionDate": "2025-09-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-03",
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
          "date": "2025-09-03T14:02:30Z",
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
      "bioguideId": "C001051",
      "district": "31",
      "firstName": "John",
      "fullName": "Rep. Carter, John R. [R-TX-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5118ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5118\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 3, 2025 Mr. Ogles introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to establish a criminal prohibition on the public release of the name of a Federal law enforcement officer with the intent to obstruct a criminal investigation or immigration enforcement operation.\n#### 1. Short title\nThis Act may be cited as the Protecting Law Enforcement from Doxxing Act .\n#### 2. Prohibition on public release of name of Federal law enforcement officer\n##### (a) In general\nSection 1510 of title 18, United States Code, is amended\u2014\n**(1)**\nin the heading, by inserting and immigration enforcement operations after criminal investigations ; and\n**(2)**\nby adding at the end the following:\n(f) Releasing name of Federal law enforcement officer (1) Definition In this section, the term Federal law enforcement officer means any officer, agent, or employee of the United States authorized by law or by a Government agency to engage in or supervise the prevention, detection, investigation, or prosecution of any violation of Federal criminal law or immigration law. (2) Offense It shall be unlawful to make the name of a Federal law enforcement officer publicly available with the intent to obstruct a criminal investigation or immigration enforcement operation. (3) Penalty Any person who violates paragraph (2) shall be fined under this title, imprisoned for not more than 5 years, or both. .\n##### (b) Technical and conforming amendments\n**(1) Table of sections**\nThe table of sections for chapter 73 of title 18, United States Code, is amended by striking the item relating to section 1510 and inserting the following:\n1510. Obstruction of criminal investigations and immigration enforcement operations. .\n**(2) Other amendments**\n**(A)**\nSection 1961(1) of title 18, United States Code, is amended by inserting after section 1510 (relating to obstruction of criminal investigations the following: and immigration enforcement operations .\n**(B)**\nSection 2516(1)(c) of title 18, United States Code, is amended by inserting after section 1510 (obstruction of criminal investigations the following: and immigration enforcement operations .\n**(C)**\nSection 3142(h)(2)(C) of title 18, United States Code, is amended by inserting after 1510 (relating to obstruction of criminal investigations the following: and immigration enforcement operations .",
      "versionDate": "2025-09-03",
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
        "actionDate": "2025-06-04",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "1952",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Protecting Law Enforcement from Doxxing Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-22T15:41:12Z"
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
      "date": "2025-09-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5118ih.xml"
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
      "title": "Protecting Law Enforcement from Doxxing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-06T07:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Law Enforcement from Doxxing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-06T07:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to establish a criminal prohibition on the public release of the name of a Federal law enforcement officer with the intent to obstruct a criminal investigation or immigration enforcement operation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-06T07:33:24Z"
    }
  ]
}
```
