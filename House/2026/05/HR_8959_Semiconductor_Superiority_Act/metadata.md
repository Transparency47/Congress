# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8959?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8959
- Title: Semiconductor Superiority Act
- Congress: 119
- Bill type: HR
- Bill number: 8959
- Origin chamber: House
- Introduced date: 2026-05-21
- Update date: 2026-05-28T20:38:22Z
- Update date including text: 2026-05-28T20:38:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-21: Introduced in House
- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-05-21: Introduced in House

## Actions

- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-21",
    "latestAction": {
      "actionDate": "2026-05-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8959",
    "number": "8959",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001260",
        "district": "16",
        "firstName": "Vern",
        "fullName": "Rep. Buchanan, Vern [R-FL-16]",
        "lastName": "Buchanan",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Semiconductor Superiority Act",
    "type": "HR",
    "updateDate": "2026-05-28T20:38:22Z",
    "updateDateIncludingText": "2026-05-28T20:38:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-21",
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
          "date": "2026-05-21T14:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "AL"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8959ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8959\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2026 Mr. Buchanan (for himself, Ms. Sewell , and Ms. DelBene ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to clarify the application of the advanced manufacturing investment credit with respect to semiconductor manufacturing facilities located in outer space.\n#### 1. Short title\nThis Act may be cited as the Semiconductor Superiority Act .\n#### 2. Clarifying application of advanced manufacturing investment credit for semiconductor manufacturing facilities located in outer space\n##### (a) In general\nSection 48D(b) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(6) Application to facilities located in outer space (A) In general In the case of an advanced manufacturing facility which is located in outer space\u2014 (i) for purposes of paragraph (1), qualified property shall not fail to be treated as part of such facility solely because such qualified property is\u2014 (I) used to transport crew, goods, equipment, material, or supplies in outer space to and from such facility, or (II) not located in outer space, and (ii) for purposes of paragraph (2)\u2014 (I) property shall not fail to be treated as qualified property solely because such property is located in outer space, (II) with respect to subparagraph (A)(iv), property shall not fail to be treated as integral to the operation of such facility solely because such property is\u2014 (aa) used in the manner described in clause (i)(I), or (bb) not located in outer space, and (III) with respect to subparagraph (B)(ii), functions related to manufacturing shall include\u2014 (aa) flight control operations, (bb) crew habitation in outer space, (cc) repair of the facility, and (dd) transportation of crew, goods, equipment, material, or supplies to and from the facility. (B) Outer space For purposes of this paragraph, the term outer space shall include low-Earth orbit. (C) Exclusion For purposes of this subsection, the term qualified property shall not include a rocket or similar launch vehicle constructed for the purpose of propelling a payload from Earth into outer space. .\n##### (b) Other special rules\nSection 50(b) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin paragraph (1)(B), by inserting or any qualified property which is part of an advanced manufacturing facility located in outer space (as such terms are defined under section 48D(b)) and held by a United States person if such property was launched from within the United States after section 168(g)(4) , and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (C), by striking and at the end,\n**(B)**\nin subparagraph (D), by striking the period at the end and inserting ; and , and\n**(C)**\nby adding at the end the following new subparagraph:\n(E) any qualified property which is part of an advanced manufacturing facility located in outer space (as such terms are defined under section 48D(b)). .\n##### (c) Effective date\nThe amendments made by this section shall apply to property placed in service after the date of enactment of this Act.\n##### (d) Rule of construction\nNothing in this Act, or the amendments made by this Act, shall be construed to create any inference with respect to the allowance or determination of the advanced manufacturing investment credit under section 48D of the Internal Revenue Code of 1986 with respect to an advanced manufacturing facility located in outer space on or before the date of the enactment of this Act.",
      "versionDate": "2026-05-21",
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
        "name": "Taxation",
        "updateDate": "2026-05-28T20:38:22Z"
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
      "date": "2026-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8959ih.xml"
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
      "title": "Semiconductor Superiority Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T10:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Semiconductor Superiority Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-22T10:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to clarify the application of the advanced manufacturing investment credit with respect to semiconductor manufacturing facilities located in outer space.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:18:29Z"
    }
  ]
}
```
