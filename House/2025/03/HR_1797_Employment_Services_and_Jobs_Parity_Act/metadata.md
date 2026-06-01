# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1797?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1797
- Title: Employment Services and Jobs Parity Act
- Congress: 119
- Bill type: HR
- Bill number: 1797
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2026-02-11T15:11:31Z
- Update date including text: 2026-02-11T15:11:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-03-03 - IntroReferral: Sponsor introductory remarks on measure. (CR E179)
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-03-03 - IntroReferral: Sponsor introductory remarks on measure. (CR E179)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1797",
    "number": "1797",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "K000404",
        "district": "",
        "firstName": "Kimberlyn",
        "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
        "lastName": "King-Hinds",
        "party": "R",
        "state": "MP"
      }
    ],
    "title": "Employment Services and Jobs Parity Act",
    "type": "HR",
    "updateDate": "2026-02-11T15:11:31Z",
    "updateDateIncludingText": "2026-02-11T15:11:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
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
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E179)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:03:20Z",
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
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "AS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1797ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1797\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Ms. King-Hinds (for herself and Mrs. Radewagen ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Wagner-Peyser Act to include the Commonwealth of the Northern Mariana Islands and American Samoa, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Employment Services and Jobs Parity Act .\n#### 2. Amendments to the Wagner-Peyser Act\n##### (a) Definitions\nSection 2(5) of the Wagner-Peyser Act ( 29 U.S.C. 49a(5) ) is amended by inserting the Commonwealth of the Northern Mariana Islands, American Samoa, after Guam, .\n##### (b) Unemployment compensation law requirement\nSection 5(b)(1) of such Act is amended by inserting the Commonwealth of the Northern Mariana Islands, American Samoa, after Guam, .\n##### (c) Allotments\nSection 6 of such Act ( 29 U.S.C. 49e ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking except for Guam and inserting except for Guam, the Commonwealth of the Northern Mariana Islands, and American Samoa ;\n**(B)**\nby striking first allot to Guam and the Virgin Islands and inserting the following:\nfirst allot\u2014 (1) to Guam and the Virgin Islands ;\n**(C)**\nby striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following:\n(2) beginning with the first fiscal year for which the total amount available for allotments under this section is greater than the total amount available for allotments under this section for fiscal year 2025, and for each succeeding fiscal year, to each of the Commonwealth of the Northern Mariana Islands and American Samoa, an amount which is equal to one-half of the amount allotted to Guam under paragraph (1) for the corresponding fiscal year. ; and\n**(2)**\nin subsection (b)(1), in the matter following subparagraph (B), by inserting , the Commonwealth of the Northern Mariana Islands, American Samoa, after Guam .",
      "versionDate": "2025-03-03",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "American Samoa",
            "updateDate": "2026-02-11T15:11:25Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2026-02-11T15:11:31Z"
          },
          {
            "name": "Northern Mariana Islands",
            "updateDate": "2026-02-11T15:11:21Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-05-14T16:11:04Z"
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
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1797ih.xml"
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
      "title": "Employment Services and Jobs Parity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T03:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Employment Services and Jobs Parity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T03:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Wagner-Peyser Act to include the Commonwealth of the Northern Mariana Islands and American Samoa, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T03:03:26Z"
    }
  ]
}
```
