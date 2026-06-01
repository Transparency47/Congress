# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6328?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6328
- Title: Main Street Home Builders Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6328
- Origin chamber: House
- Introduced date: 2025-11-28
- Update date: 2026-01-07T09:05:34Z
- Update date including text: 2026-01-07T09:05:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-28: Introduced in House
- 2025-11-28 - IntroReferral: Introduced in House
- 2025-11-28 - IntroReferral: Introduced in House
- 2025-11-28 - IntroReferral: Referred to the House Committee on Small Business.
- Latest action: 2025-11-28: Introduced in House

## Actions

- 2025-11-28 - IntroReferral: Introduced in House
- 2025-11-28 - IntroReferral: Introduced in House
- 2025-11-28 - IntroReferral: Referred to the House Committee on Small Business.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-28",
    "latestAction": {
      "actionDate": "2025-11-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6328",
    "number": "6328",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "V000138",
        "district": "7",
        "firstName": "Eugene",
        "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
        "lastName": "Vindman",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Main Street Home Builders Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-07T09:05:34Z",
    "updateDateIncludingText": "2026-01-07T09:05:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-28",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Small Business.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-28",
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
          "date": "2025-11-28T15:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
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
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-11-28",
      "state": "PA"
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
      "sponsorshipDate": "2026-01-06",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6328ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6328\nIN THE HOUSE OF REPRESENTATIVES\nNovember 28, 2025 Mr. Vindman (for himself and Mr. Bresnahan ) introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo require the Administrator of the Small Business Administration to carry out a pilot program for construction or management of build-to-rent multifamily housing, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Main Street Home Builders Act of 2025 .\n#### 2. Pilot program for construction or management of build-to-rent multifamily housing\n##### (a) In general\nThe Administrator shall carry out a pilot program to be known as the 505 Pilot Program to make loans to State development companies in accordance with title V of the Small Business Investment Act of 1958 ( 15 U.S.C. 695 et seq. ) to provide assistance to covered persons for projects to\u2014\n**(1)**\nconstruct, refurbish, expand, or make improvements to build-to-rent multifamily housing; and\n**(2)**\nmanage such build-to-rent multifamily housing.\n##### (b) Consideration\nA covered person that participates in the 505 Pilot Program shall not be considered to be a speculative business or a passive business (as such terms are defined, respectively, in section 120.110 of title 13, Code of Federal Regulations).\n##### (c) Requirements\nA loan made under the 505 Pilot Program shall be made in the same manner and for the same purposes as a loan made under title V of the Small Business Investment Act of 1958 ( 15 U.S.C. 695 et seq. ), except that a project to be funded under the 505 Pilot Program shall not be subject to\u2014\n**(1)**\nthe requirements of section 501(d)(1) of the Small Business Investment Act of 1958 ( 15 U.S.C. 695(d)(1) ) or any other job creation requirements; or\n**(2)**\nthe requirements of paragraph (4) or (5) of section 502 of such Act ( 15 U.S.C. 696 ) or any other limitation on leasing a project assisted under the 505 Pilot Program.\n##### (d) Lender due diligence\nA lender shall conduct appropriate due diligence to ensure that a covered person receiving assistance under the 505 Pilot Program\u2014\n**(1)**\nwill be the end user of the project for which the covered person seeks such assistance;\n**(2)**\nhas a proven track record of successfully constructing or managing build-to-rent multifamily housing; and\n**(3)**\nhas adequate assets to construct or manage the project for which the covered person seeks such assistance.\n##### (e) Use of assistance\nA covered person receiving assistance under the 505 Pilot Program shall ensure that\u2014\n**(1)**\nwith respect to a project to construct a new facility, the project creates at least one additional dwelling unit than existed before the commencement of such project; and\n**(2)**\nwith respect to a project to acquire, renovate, or reconstruct an existing facility, the project creates at least one additional dwelling unit than the existing facility.\n##### (f) Funding\n**(1) In general**\nSubject to paragraph (2), amounts appropriated to the Administrator of the Small Business Administration for loans under title V of the Small Business Investment Act of 1958 ( 15 U.S.C. 695 et seq. ) shall be used to carry out the pilot program established by this section.\n**(2) Limitation**\nThe Administrator may use not more than the following amounts to carry out the pilot program:\n**(A)**\nFor fiscal year 2026, $1,000,000,000.\n**(B)**\nFor fiscal year 2027, $2,000,000,000.\n**(C)**\nFor each of fiscal years 2028 through 2030, $3,000,000,000.\n##### (g) Termination\nThe authority to carry out the pilot program established by this section shall terminate on the date that is five years after the date of the enactment of this Act.\n##### (h) Definitions\nIn this Act:\n**(1) Build-to-rent multifamily housing**\nThe term build-to-rent multifamily housing means multifamily housing constructed with the intention of renting or leasing such housing.\n**(2) Covered person**\nThe term covered person means a small business concern (as defined under section 3 of the Small Business Act ( 15 U.S.C. 632 )) that\u2014\n**(A)**\nconstructs, refurbishes, expands, or makes improvements to build-to-rent multifamily housing; and\n**(B)**\nmanages such build-to-rent multifamily housing.\n**(3) Dwelling unit**\nThe term dwelling unit means a single unit of residence for a household of one or more persons.\n**(4) Multifamily housing**\nThe term multifamily housing means a facility that contains more than one dwelling unit.",
      "versionDate": "2025-11-28",
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
        "name": "Commerce",
        "updateDate": "2025-12-10T18:35:02Z"
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
      "date": "2025-11-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6328ih.xml"
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
      "title": "Main Street Home Builders Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T10:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Main Street Home Builders Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Administrator of the Small Business Administration to carry out a pilot program for construction or management of build-to-rent multifamily housing, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-09T10:18:26Z"
    }
  ]
}
```
