# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7845?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7845
- Title: DROUGHT Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7845
- Origin chamber: House
- Introduced date: 2026-03-05
- Update date: 2026-05-15T08:07:45Z
- Update date including text: 2026-05-15T08:07:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-05 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-05: Introduced in House

## Actions

- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-05 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7845",
    "number": "7845",
    "originChamber": "House",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "P000608",
        "district": "50",
        "firstName": "Scott",
        "fullName": "Rep. Peters, Scott H. [D-CA-50]",
        "lastName": "Peters",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "DROUGHT Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-15T08:07:45Z",
    "updateDateIncludingText": "2026-05-15T08:07:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-05",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-05",
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
          "date": "2026-03-05T15:06:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-05T15:05:50Z",
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
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "CA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7845ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7845\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2026 Mr. Peters (for himself, Ms. Barrag\u00e1n , Mr. Garamendi , Mr. Vargas , Ms. Jacobs , Mr. Costa , Mr. Ruiz , and Mr. Levin ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Water Infrastructure Finance and Innovation Act of 2014 with respect to the total amount of Federal assistance for projects in States experiencing severe drought, regionally and nationally significant projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Drought Relief Obtained Using Government Help Today Act of 2026 or the DROUGHT Act of 2026 .\n#### 2. Federal assistance for certain water infrastructure projects\nSection 5029(b)(9) of the Water Infrastructure Finance and Innovation Act of 2014 ( 33 U.S.C. 3908(b)(9) ) is amended by adding at the end the following:\n(D) Exceptions for certain projects (i) In general Notwithstanding subparagraph (A), the total amount of Federal assistance for a covered project for which assistance is provided under this subtitle shall not exceed 90 percent of the total project cost. (ii) Priority In carrying out this section, the Secretary or the Administrator, as applicable shall prioritize financing for covered projects. (iii) Definitions In this subparagraph, the term covered project means a project described in paragraph (6) or (7) of section 5026\u2014 (I) that is located in\u2014 (aa) a State that has been designated as D2 (severe drought) or greater according to the United States Drought Monitor for a minimum of 4 weeks during the 5-year period preceding the date on which assistance is provided for the project under this subtitle; or (bb) a county for which a drought emergency has been declared by the applicable Governor at any time during such period; (II) that serves\u2014 (aa) an area in which, on the date on which assistance is provided for the project under this subtitle, the average household income is at or below 200 percent of the poverty threshold established by the Bureau of the Census; or (bb) an area that meets the affordability criteria established by a State pursuant to section 1452(d)(3) of the Safe Drinking Water Act ( 42 U.S.C. 300j12(d)(3) ) or section 603(i)(2) of the Federal Water Pollution Control Act ( 33 U.S.C. 1383(i)(2) ); or (III) that the Secretary or the Administrator, as applicable, has designated to be a project of regional or national significance because the project demonstrably\u2014 (aa) increases drinking water supply capacity or reliability; (bb) enhances water reuse or recycling; (cc) reduces regional water usage; (dd) lowers costs to ratepayers; or (ee) provides substantial public health or environmental benefits. .",
      "versionDate": "2026-03-05",
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
        "name": "Water Resources Development",
        "updateDate": "2026-04-01T20:21:57Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7845ih.xml"
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
      "title": "DROUGHT Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-27T02:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DROUGHT Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-27T02:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Drought Relief Obtained Using Government Help Today Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-27T02:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Water Infrastructure Finance and Innovation Act of 2014 with respect to the total amount of Federal assistance for projects in States experiencing severe drought, regionally and nationally significant projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-27T02:48:23Z"
    }
  ]
}
```
