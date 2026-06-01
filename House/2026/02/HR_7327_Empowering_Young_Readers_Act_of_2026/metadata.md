# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7327?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7327
- Title: Empowering Young Readers Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7327
- Origin chamber: House
- Introduced date: 2026-02-03
- Update date: 2026-03-13T08:05:36Z
- Update date including text: 2026-03-13T08:05:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-03: Introduced in House
- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-02-03: Introduced in House

## Actions

- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-03",
    "latestAction": {
      "actionDate": "2026-02-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7327",
    "number": "7327",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "F000477",
        "district": "4",
        "firstName": "Valerie",
        "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
        "lastName": "Foushee",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Empowering Young Readers Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-13T08:05:36Z",
    "updateDateIncludingText": "2026-03-13T08:05:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-03",
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
      "actionDate": "2026-02-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-03",
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
          "date": "2026-02-03T15:02:10Z",
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
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "NC"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "TX"
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
      "sponsorshipDate": "2026-03-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7327ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7327\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 3, 2026 Mrs. Foushee (for herself and Ms. Adams ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo require the Secretary of Education to establish a pilot program to award grants to eligible organizations to carry out activities related to book access, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Empowering Young Readers Act of 2026 .\n#### 2. Pilot program for book access\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Secretary of Education shall establish a pilot program to award grants, on a competitive basis, to eligible organizations to carry out the activities described in subsection (c).\n##### (b) Application\nAn eligible organization desiring a grant under this section shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may reasonably require, including\u2014\n**(1)**\ninformation about past work the eligible organization has performed related to book access;\n**(2)**\na comprehensive strategic plan for how the eligible organization would use a grant under this section to carry out one or more of the activities described in subsection (c), including a description of how such activities would address the needs of the community served by the eligible organization; and\n**(3)**\na letter from a leader in the community served by the eligible organization in support of the eligible organization and the comprehensive strategic plan.\n##### (c) Activities\nGrant funds awarded under this section shall be used by an eligible entity to carry out one or more of the following activities:\n**(1)**\nPurchasing or otherwise acquiring new or used books for distribution to children.\n**(2)**\nDistributing new or used books to children, including through delivery or in-person events.\n**(3)**\nDonating new or used books to public libraries.\n**(4)**\nHosting or organizing literacy-related programming for children and their families, including book fairs, reading hours, book drives, and story times.\n**(5)**\nAny other activity the Secretary determines appropriate related to book access.\n##### (d) Grant amounts and duration\nA grant under this section\u2014\n**(1)**\nshall be in an amount that is not more than $200,000; and\n**(2)**\nshall be for a period of 2 years.\n##### (e) Viewpoint-Neutral\nIn awarding grants under this section, the Secretary shall ensure that applications submitted pursuant to subsection (b) are reviewed based on viewpoint-neutral criteria.\n##### (f) Report\nNot later than 6 months after the grant period of the final grant awarded pursuant to this section expires, the Secretary shall submit to Congress a report on the pilot program, which shall include\u2014\n**(1)**\nqualitative data with respect to the activities carried out by grant recipients, including the number of books provided to children and their families; and\n**(2)**\nto the extent data is available, information about how child literacy rates in communities served by eligible organizations changed during and after such activities were carried out.\n##### (g) Rule of construction\nNothing in this section may be construed as restricting, infringing upon, or otherwise interfering with the ability of a public library or other entity to reject all or part of a donation of books.\n##### (h) Definitions\nIn this section:\n**(1) Child**\nThe term child means an individual under 19 years of age.\n**(2) Eligible organization**\nThe term eligible organization means\u2014\n**(A)**\na nongovernmental organization; or\n**(B)**\na nonprofit organization.\n##### (i) Authorization of appropriations\nThere is authorized to be appropriated to carry out this subsection $10,000,000 for fiscal year 2026, to remain available through fiscal year 2027.",
      "versionDate": "2026-02-03",
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
        "name": "Education",
        "updateDate": "2026-02-25T16:48:01Z"
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
      "date": "2026-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7327ih.xml"
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
      "title": "Empowering Young Readers Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T08:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Empowering Young Readers Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T08:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Education to establish a pilot program to award grants to eligible organizations to carry out activities related to book access, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T08:34:00Z"
    }
  ]
}
```
