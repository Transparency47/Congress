# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1952?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1952
- Title: Protecting Law Enforcement from Doxxing Act
- Congress: 119
- Bill type: S
- Bill number: 1952
- Origin chamber: Senate
- Introduced date: 2025-06-04
- Update date: 2026-05-12T11:03:31Z
- Update date including text: 2026-05-12T11:03:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-04: Introduced in Senate
- 2025-06-04 - IntroReferral: Introduced in Senate
- 2025-06-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-06-04: Introduced in Senate

## Actions

- 2025-06-04 - IntroReferral: Introduced in Senate
- 2025-06-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1952",
    "number": "1952",
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
    "title": "Protecting Law Enforcement from Doxxing Act",
    "type": "S",
    "updateDate": "2026-05-12T11:03:31Z",
    "updateDateIncludingText": "2026-05-12T11:03:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-04",
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
      "actionDate": "2025-06-04",
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
            "date": "2025-06-04T21:15:12Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-04T21:15:12Z",
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
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "SC"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "FL"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1952is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1952\nIN THE SENATE OF THE UNITED STATES\nJune 4, 2025 Mrs. Blackburn introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to establish a criminal prohibition on the public release of the name of a Federal law enforcement officer with the intent to obstruct a criminal investigation or immigration enforcement operation.\n#### 1. Short title\nThis Act may be cited as the Protecting Law Enforcement from Doxxing Act .\n#### 2. Prohibition on public release of name of Federal law enforcement officer\n##### (a) In general\nSection 1510 of title 18, United States Code, is amended\u2014\n**(1)**\nin the heading, by inserting and immigration enforcement operations after criminal investigations ; and\n**(2)**\nby adding at the end the following:\n(f) Releasing name of Federal law enforcement officer (1) Definition In this section, the term Federal law enforcement officer means any officer, agent, or employee of the United States authorized by law or by a Government agency to engage in or supervise the prevention, detection, investigation, or prosecution of any violation of Federal criminal law or immigration law. (2) Offense It shall be unlawful to make the name of a Federal law enforcement officer publicly available with the intent to obstruct a criminal investigation or immigration enforcement operation. (3) Penalty Any person who violates paragraph (2) shall be fined under this title, imprisoned for not more than 5 years, or both. .\n##### (b) Technical and conforming amendments\n**(1) Table of sections**\nThe table of sections for chapter 73 of title 18, United States Code, is amended by striking the item relating to section 1510 and inserting the following:\n1510. Obstruction of criminal investigations and immigration enforcement operations. .\n**(2) Other amendments**\n**(A)**\nSection 1961(1) of title 18, United States Code, is amended by inserting after section 1510 (relating to obstruction of criminal investigations the following: and immigration enforcement operations .\n**(B)**\nSection 2516(1)(c) of title 18, United States Code, is amended by inserting after section 1510 (obstruction of criminal investigations the following: and immigration enforcement operations .\n**(C)**\nSection 3142(h)(2)(C) of title 18, United States Code, is amended by inserting after 1510 (relating to obstruction of criminal investigations the following: and immigration enforcement operations .",
      "versionDate": "2025-06-04",
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
        "actionDate": "2025-09-03",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "5118",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Protecting Law Enforcement from Doxxing Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-06-23T14:11:31Z"
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
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1952is.xml"
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
      "title": "Protecting Law Enforcement from Doxxing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T11:03:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Law Enforcement from Doxxing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-10T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to establish a criminal prohibition on the public release of the name of a Federal law enforcement officer with the intent to obstruct a criminal investigation or immigration enforcement operation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-10T02:48:16Z"
    }
  ]
}
```
