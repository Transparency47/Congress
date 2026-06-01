# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7749?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7749
- Title: Quantum in Practice Act
- Congress: 119
- Bill type: HR
- Bill number: 7749
- Origin chamber: House
- Introduced date: 2026-03-02
- Update date: 2026-03-19T15:27:10Z
- Update date including text: 2026-03-19T15:27:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-02: Introduced in House
- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2026-03-02: Introduced in House

## Actions

- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-02",
    "latestAction": {
      "actionDate": "2026-03-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7749",
    "number": "7749",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "F000446",
        "district": "4",
        "firstName": "Randy",
        "fullName": "Rep. Feenstra, Randy [R-IA-4]",
        "lastName": "Feenstra",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Quantum in Practice Act",
    "type": "HR",
    "updateDate": "2026-03-19T15:27:10Z",
    "updateDateIncludingText": "2026-03-19T15:27:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-02",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-02",
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
          "date": "2026-03-02T14:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "MI"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "CA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "IA"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "NJ"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "VA"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "IN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "NY"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "DE"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CO"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "TN"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7749ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7749\nIN THE HOUSE OF REPRESENTATIVES\nMarch 2, 2026 Mr. Feenstra (for himself, Ms. Stevens , Mr. Valadao , Mrs. Miller-Meeks , Mr. Kean , Mr. Wittman , Mr. Yakym , Mr. Lawler , Ms. McBride , and Ms. Lofgren ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo amend the National Quantum Initiative Act to make certain additions relating to quantum modeling and simulation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Quantum in Practice Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nQuantum computing has the potential to spur advancements in molecular modeling and simulation that will benefit Americans.\n**(2)**\nQuantum molecular simulations and modeling will enable scientists to study chemical elements and reactions with accuracy and speed that is far beyond the abilities of existing supercomputers.\n**(3)**\nAdvances in molecular simulations and modeling would give researchers tools that could lead to breakthroughs across industries and sectors, including\u2014\n**(A)**\nmodeling the nitrogen fixation process utilized by bacteria, which could be used to develop synthetic fertilizers without the high energy and material costs of current methods, creating the next generation of fertilizers;\n**(B)**\ncreating more effective medications and reducing harmful interactions or side effects;\n**(C)**\ndeveloping new materials to increase energy storage capacity and create more powerful battery technologies;\n**(D)**\ndeveloping lighter, stronger metals;\n**(E)**\ncreating materials for more durable protective gear for law enforcement and military; and\n**(F)**\ndeveloping new types of superconductors.\n#### 3. Quantum modeling and simulation\n##### (a) Definition of quantum information science\nSection 2(6) of the National Quantum Initiative Act ( 15 U.S.C. 8801(6) ) is amended by inserting modeling, simulation, after computing .\n##### (b) Quantum information science research program\nSection 401(b)(3) of the National Quantum Initiative Act ( 15 U.S.C. 8851(b)(3) ) is amended\u2014\n**(1)**\nin subparagraph (F), by striking and at the end;\n**(2)**\nin subparagraph (G), by adding and after the semicolon; and\n**(3)**\nby adding at the end the following new subparagraph:\n(H) quantum molecular modeling or simulation; .",
      "versionDate": "2026-03-02",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-03-19T15:27:10Z"
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
      "date": "2026-03-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7749ih.xml"
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
      "title": "Quantum in Practice Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T04:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Quantum in Practice Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-18T04:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Quantum Initiative Act to make certain additions relating to quantum modeling and simulation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-18T04:48:31Z"
    }
  ]
}
```
