# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2425?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2425
- Title: Kairo Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2425
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2425",
    "number": "2425",
    "originChamber": "House",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "F000246",
        "district": "4",
        "firstName": "Pat",
        "fullName": "Rep. Fallon, Pat [R-TX-4]",
        "lastName": "Fallon",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Kairo Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:08:30Z",
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
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CT"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "TX"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "TX"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2425ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2425\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Mr. Fallon (for himself, Mrs. Hayes , Ms. Van Duyne , Mr. Gooden , and Mr. Nehls ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo protect babies and young children in childcare settings by strengthening transparency and safety requirements.\n#### 1. Short title\nThis Act may be cited as the Kairo Act of 2025 .\n#### 2. Definitions\nFor purposes of this Act:\n**(1)**\nThe term certain child care provider means a center-based child care provider, a family child care provider, a sectarian child care provider, or other provider of child care services for compensation that receives any amount of Federal funding towards providing child care or early learning programs, including but not limited to Child Care Development Block Grants and Head Start funding.\n**(2)**\nThe term Center-based child care provider means a provider licensed or otherwise authorized to provide child care services for fewer than 24 hours per day per child in a non-residential setting, unless care in excess of 24 hours is due to the nature of the parent(s)' work.\n**(3)**\nThe term family child care provider means one or more individual(s) who provide child care services for fewer than 24 hours per day per child, in a private residence other than the child's residence, unless care in excess of 24 hours is due to the nature of the parent(s)' work.\n**(4)**\nThe term sectarian organization and sectarian child care provider means a religious organization or religious provider generally. The terms embrace any organization or provider that engages in religious conduct or activity or that seeks to maintain a religious identity in some or all of its functions. There is no requirement that a sectarian organization or provider be managed by clergy or have any particular degree of religious management, control, or content.\n#### 3. Parental rights as a condition of funding\n##### (a)\nAny provider receiving Federal funds towards providing child care or early learning programs, including but not limited to Child Care Development Block Grants or Head Start funding must develop a parent\u2019s bill of rights for child care that includes\u2014\n**(1)**\ncontact information for the state child abuse hotline and agency responsible for investigating suspected abuse, neglect, or exploitation in a child care operation;\n**(2)**\ninformation on how to access the State\u2019s electronic database, if applicable, of child care monitoring and inspection reports as described in section 658E(c)(2)D) of the Child Care and Development Block Grant Act;\n**(3)**\nfor Head Start and Early Head Start programs information on how to access monitoring reports conducted by the Office of Head Start;\n**(4)**\naccess to review such child care facility\u2019s written records concerning the such child;\n**(5)**\nreceive from the child care facility, upon request, the responsible state agency\u2019s inspection reports for the child care facility and information about how to access the child care facility\u2019s compliance history online;\n**(6)**\ncompliance by the facility with a court order preventing another parent or guardian of such child from visiting or removing such child from such facility;\n**(7)**\nthe contact information for the division responsible for regulating the child care facility, including the division\u2019s name, address, and phone number;\n**(8)**\naccess, within 2 business days from time of written request, to any video recording of an alleged incident of abuse or neglect involving such child if\u2014\n**(A)**\nsuch a video recording of the alleged incident is available;\n**(B)**\nsuch parent or guardian is prohibited from retaining any part of the video recording depicting a child who is not the child of such parent or guardian;\n**(C)**\nthe parent or guardian of any other child captured in such video recording receives written notice from such provider of a request for access to such video recording;\n**(D)**\na copy of the child care facility\u2019s policies and procedures; access to review such provider\u2019s\u2014\n**(i)**\nstaff training records; and\n**(ii)**\nany in-house staff training curriculum used by such provider; and\n**(E)**\nfreedom from any retaliatory action by such a provider for exercising any of the parent\u2019s or guardian\u2019s rights under this Act.\n##### (b)\nA child care provider shall provide the parent or guardian of a child for whom it provides child care services a written copy of the rights listed in subsection (a) no later than 45 days after the effective date of this Act; or not later than the child\u2019s 1st day on which such services begin after such effective date.\n##### (c)\nThis section does not affect the ability of a law enforcement agency or a local- or state-run child protective services agency to access a video recording as part of an investigation of an incident depicted in such video recording.\n#### 4. Notice of requirement to comply\nNot later than 30 days after the effective date of this Act, the Director of the Department of Health and Human Services will direct the Office of Child Care (OCC) and the Office of Head Start (OHS) to make all current and future potential recipients of Child Care Development Block Grants and Head Start funding aware of the new requirements.\n#### 5. Effective date\nThis Act shall take effect 30 days after the date of the enactment of this Act, the date of the enactment of this Act.",
      "versionDate": "2025-03-27",
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
        "name": "Families",
        "updateDate": "2025-05-05T12:50:26Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2425ih.xml"
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
      "title": "Kairo Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-30T03:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Kairo Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-30T03:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To protect babies and young children in childcare settings by strengthening transparency and safety requirements.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-30T03:48:16Z"
    }
  ]
}
```
