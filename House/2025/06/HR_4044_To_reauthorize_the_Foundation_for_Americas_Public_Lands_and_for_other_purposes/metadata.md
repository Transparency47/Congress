# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4044?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4044
- Title: Foundation for America’s Public Lands Reauthorization Act
- Congress: 119
- Bill type: HR
- Bill number: 4044
- Origin chamber: House
- Introduced date: 2025-06-17
- Update date: 2026-03-10T08:05:25Z
- Update date including text: 2026-03-10T08:05:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-17: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-06-17: Introduced in House

## Actions

- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4044",
    "number": "4044",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "M001213",
        "district": "1",
        "firstName": "Blake",
        "fullName": "Rep. Moore, Blake D. [R-UT-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Foundation for America\u2019s Public Lands Reauthorization Act",
    "type": "HR",
    "updateDate": "2026-03-10T08:05:25Z",
    "updateDateIncludingText": "2026-03-10T08:05:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-17",
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
          "date": "2025-06-17T15:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "CO"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "NV"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "VA"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "CO"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "NM"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "CO"
    },
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4044ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4044\nIN THE HOUSE OF REPRESENTATIVES\nJune 17, 2025 Mr. Moore of Utah (for himself and Mr. Neguse ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo reauthorize the Foundation for America\u2019s Public Lands, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Foundation for America\u2019s Public Lands Reauthorization Act .\n#### 2. Bureau of Land Management Foundation\nSection 122 of division G of Public Law 115\u201331 ( 43 U.S.C. 1748c ) is amended as follows:\n**(1)**\nIn subsection (a)(3), by striking Bureau of Land Management Foundation and inserting Foundation for America\u2019s Public Lands .\n**(2)**\nIn subsection (b)\u2014\n**(A)**\nin paragraph (1)(A), by striking Bureau of Land Management Foundation and inserting Foundation for America\u2019s Public Lands ; and\n**(B)**\nin paragraph (2)(D)\u2014\n**(i)**\nin clause (ii), by striking ; and and inserting a semicolon;\n**(ii)**\nin clause (iii), by striking the period and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(iv) the fulfillment of the Bureau of Land Management\u2019s multiple use mandate. .\n**(3)**\nBy amending subsection (c)(1)(B)(i) to read as follows:\n(i) Number of board members The number of members on the Board shall be as follows: (I) Not later than 180 days after the date of the enactment of the Foundation for America\u2019s Public Lands Reauthorization Act, not more than 12 members. (II) Two years after the date of the enactment of the Foundation for America\u2019s Public Lands Reauthorization Act, not more than 15 members. (III) Four years after the date of the enactment of the Foundation for America\u2019s Public Lands Reauthorization Act and thereafter, not more than 18 members. .\n**(4)**\nBy amending subsection (c)(1)(C)(ii) to read as follows:\n(ii) Expertise; representation (I) Expertise Not less than one-third of the members of the Board shall have education or experience relating to natural, cultural, conservation, or other resource management, law, or research. (II) Representation Not later than 4 years after the date of the enactment of the Foundation for America\u2019s Public Lands Reauthorization Act, the 18 members of the Board shall include not fewer than\u2014 (aa) two members with experience in energy production; including one with experience with fossil fuels and one with experience in non-fossil fueled energy production; (bb) one member with experience ranching or grazing on Federal land under the administrative jurisdiction of the Bureau of Land Management; (cc) one member from the non-motorized outdoor recreation community; (dd) one member from the motorized outdoor recreation community; (ee) one member from the hunting/fishing community or one member from the recreational shooting industry; and (ff) one member from the mining industry. .\n**(5)**\nBy inserting after subsection (i) the following:\n(j) Prohibition on use of amounts for litigation and lobbying expenses Amounts made available under this Act shall not be used for\u2014 (1) any expense related to litigation; or (2) any activity the purpose of which is to influence legislation pending before Congress. (k) Use of gifts, devises, or bequests of money or other property Any gifts, devises, or bequests of amounts or other property, or any other amounts or other property, transferred to, deposited with, or otherwise in the possession of the Foundation pursuant to this Act, may be made available by the Foundation to Federal departments, agencies, or instrumentalities and may be accepted and expended (or the disposition of the amounts or property directed), without further appropriation, by those Federal departments, agencies, or instrumentalities, subject to the condition that the amounts or property be used for purposes that further the multiple use mission of the Bureau of Land Mangement. .\n**(6)**\nBy redesignating subsection (j) as subsection (l).\n**(7)**\nIn subsection (l) (as so redesignated by paragraph (7) of this subsection), by striking such sums as are necessary to carry out this section and inserting to the Secretary of the Interior to carry out this Act, $10,000,000 for each of the five fiscal years after the date of the enactment of this Act .",
      "versionDate": "2025-06-17",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-14T18:04:47Z"
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
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4044ih.xml"
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
      "title": "Foundation for America\u2019s Public Lands Reauthorization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-27T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Foundation for America\u2019s Public Lands Reauthorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-27T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reauthorize the Foundation for America's Public Lands, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-27T11:18:24Z"
    }
  ]
}
```
