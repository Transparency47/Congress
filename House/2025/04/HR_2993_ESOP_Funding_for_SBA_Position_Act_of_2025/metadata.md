# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2993?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2993
- Title: ESOP Funding for SBA Position Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2993
- Origin chamber: House
- Introduced date: 2025-04-24
- Update date: 2025-10-01T08:06:15Z
- Update date including text: 2025-10-01T08:06:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-24: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Small Business.
- 2025-04-24 - IntroReferral: Sponsor introductory remarks on measure. (CR E337)
- Latest action: 2025-04-24: Introduced in House

## Actions

- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Small Business.
- 2025-04-24 - IntroReferral: Sponsor introductory remarks on measure. (CR E337)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-24",
    "latestAction": {
      "actionDate": "2025-04-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2993",
    "number": "2993",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001055",
        "district": "1",
        "firstName": "Ed",
        "fullName": "Rep. Case, Ed [D-HI-1]",
        "lastName": "Case",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "ESOP Funding for SBA Position Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-01T08:06:15Z",
    "updateDateIncludingText": "2025-10-01T08:06:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-24",
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
      "actionDate": "2025-04-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-04-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E337)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-24",
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
          "date": "2025-04-24T15:03:30Z",
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
      "fullName": "Rep. Bresnahan, Robert [R-PA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "PA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "MI"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "CO"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "MN"
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
      "sponsorshipDate": "2025-05-29",
      "state": "PA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NY"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "IN"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2993ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2993\nIN THE HOUSE OF REPRESENTATIVES\nApril 24, 2025 Mr. Case (for himself, Mr. Bresnahan , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo establish a position in the Small Business Administration to provide to small businesses assistance with establishing employee stock ownership plans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the ESOP Funding for SBA Position Act of 2025 .\n#### 2. Establishment of ESOP support position\n##### (a) In general\nThere is established in the Administration a position in the competitive service (as such term is defined in section 2102 of title 5, United States Code) which shall be appointed by the Administrator and responsible for providing small business concerns assistance with establishing employee stock ownership plans.\n##### (b) Responsibilities\nThe responsibilities of the position established under subsection (a) include\u2014\n**(1)**\nproviding guidance to small business concerns on establishing employee stock ownership plans, including tax treatment of such plans, regulatory compliance, stock valuation, and opportunities to acquire funding to establish such a plan;\n**(2)**\ncoordinating with relevant public and private entities to provide assistance and resources for establishing employee stock ownership plans that are tailored for small business concerns;\n**(3)**\ncoordinating with the relevant personnel at the Department of Labor to assist small business concerns establishing employee stock ownership plans with compliance with all relevant regulatory requirements;\n**(4)**\nadvocating for appropriate guidance from relevant Federal agencies, including the Department of Labor, regarding regulations relating to establishing and maintaining employee stock ownership plans, including regulations regarding stock valuation and employee ownership; and\n**(5)**\nsuch other responsibilities as determined appropriate by the Administrator.\n#### 3. Reporting\nNot later than one year after the date of the enactment of this Act, and annually thereafter, the Administrator shall submit to Congress a report on the activities of the position established under section 2(a), including the number of small business concerns that have received assistance from such position, the types of assistance and resources provided to small business concerns by such position, and any policy recommendations for improving the process for small business concerns to establish and maintain employee stock ownership plans.\n#### 4. Definitions\nIn this Act:\n**(1) Administration**\nThe term Administration means the Small Business Administration.\n**(2) Administrator**\nThe term Administrator means the Administrator of the Administration.\n**(3) Employee stock ownership plan**\nThe term employee stock ownership plan has the meaning given such term in section 4975(e)(7) of the Internal Revenue Code of 1986 ( 26 U.S.C. 4975(e)(7) ).\n**(4) Small business concern**\nThe term small business concern has the meaning given such term under section 3 of the Small Business Act ( 15 U.S.C. 632 ).\n#### 5. Authorization of appropriations\nThere is authorized to be appropriated such sums as are necessary to carry out this Act, except that, for the fiscal year in which this Act is enacted, there is authorized $500,000 to carry out this Act.",
      "versionDate": "2025-04-24",
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
        "updateDate": "2025-05-21T12:59:11Z"
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
      "date": "2025-04-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2993ih.xml"
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
      "title": "ESOP Funding for SBA Position Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-09T03:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ESOP Funding for SBA Position Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T03:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a position in the Small Business Administration to provide to small businesses assistance with establishing employee stock ownership plans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T03:33:20Z"
    }
  ]
}
```
