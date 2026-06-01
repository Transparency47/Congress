# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8640?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8640
- Title: Non-Domiciled CDL Reporting Act
- Congress: 119
- Bill type: HR
- Bill number: 8640
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-19T20:00:37Z
- Update date including text: 2026-05-19T20:00:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-04-30: Introduced in House

## Actions

- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8640",
    "number": "8640",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "T000490",
        "district": "2",
        "firstName": "David",
        "fullName": "Rep. Taylor, David J. [R-OH-2]",
        "lastName": "Taylor",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Non-Domiciled CDL Reporting Act",
    "type": "HR",
    "updateDate": "2026-05-19T20:00:37Z",
    "updateDateIncludingText": "2026-05-19T20:00:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
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
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T13:07:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
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
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8640ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8640\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Mr. Taylor (for himself and Mr. Shreve ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Administrator of the Federal Motor Carrier Safety Administration to establish and maintain a database for commercial driver\u2019s license data, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Non-Domiciled CDL Reporting Act .\n#### 2. Commercial driver\u2019s license database\n##### (a) In general\nSubchapter IV of chapter 311 of title 49, United States Code, is amended by adding at the end the following:\n31162. Commercial driver\u2019s license database (a) In general Not later than 90 days after the date of enactment of this section, the Director of the U.S. Citizenship and Immigration Services shall make the Systematic Alien Verification for Entitlements service available for the Federal Motor Carrier Safety Administration. (b) Synchronization with States State driver license agencies shall submit to the Administrator of the Federal Motor Carrier Safety Administration\u2014 (1) the expiration date of any non-domiciled license issued by such State; and (2) a copy of the existing driver\u2019s license for each individual issued a non-domiciled commercial driver\u2019s license in such State. (c) Waiver of submission States may request a waiver of the provisions of this section under section 31315. (d) Processing of non-Domiciled CDLs (1) In general After the Administrator receives a submission from a State under subsection (b), the Administrator shall process such information through the Systematic Alien Verification for Entitlements service described in subsection (a). (2) Submission to USCIS If the Administrator determines any non-domiciled commercial driver\u2019s license holder has an unlawful presence in the United States, using the Systematic Alien Verification for Entitlements service, the Administrator shall submit information on such holder to the Director of the U.S. Citizenship and Immigration Services. (3) Removal After receiving any submission under paragraph (2), the Director shall investigate the holder for which the submission occurred to determine whether such holder is eligible for removal from the United States. (e) Report to Congress Not later than 1 year after the date of enactment of this section, and each year thereafter, the Administrator shall submit to the Committee on Transportation and Infrastructure of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a report containing information on how many non-domiciled commercial driver\u2019s licenses were flagged using the system described in subsection (a) and the State in which such licenses were obtained. .\n##### (b) Clerical amendment\nThe analysis for chapter 311 of title 49, United States Code, is amended by adding at the end the following:\n31162. Commercial driver\u2019s license database. .\n##### (c) Withholding amounts for State noncompliance\nSection 31314 of title 49, United States Code, is amended by inserting or section 31162 after section 31311(a) each place it appears.\n##### (d) Waivers, exemptions, and pilot programs\nSubsections (a), (b), and (c) of section 31315 of title 49, United States Code, are amended\u2014\n**(1)**\nby inserting or a State after a person each place it appears;\n**(2)**\nby inserting or State after the person each place it appears; and\n**(3)**\nby inserting or, with respect to States, the requirements of section 31162 after 31136 each place it appears.",
      "versionDate": "2026-04-30",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-05-19T20:00:37Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8640ih.xml"
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
      "title": "Non-Domiciled CDL Reporting Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T09:38:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Non-Domiciled CDL Reporting Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:38:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the Federal Motor Carrier Safety Administration to establish and maintain a database for commercial driver's license data, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T09:33:35Z"
    }
  ]
}
```
