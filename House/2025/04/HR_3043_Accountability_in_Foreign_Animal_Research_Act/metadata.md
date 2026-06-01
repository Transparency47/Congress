# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3043?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3043
- Title: Accountability in Foreign Animal Research Act
- Congress: 119
- Bill type: HR
- Bill number: 3043
- Origin chamber: House
- Introduced date: 2025-04-28
- Update date: 2026-03-26T08:06:42Z
- Update date including text: 2026-03-26T08:06:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-28: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-04-28: Introduced in House

## Actions

- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-28",
    "latestAction": {
      "actionDate": "2025-04-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3043",
    "number": "3043",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001136",
        "district": "9",
        "firstName": "Lisa",
        "fullName": "Rep. McClain, Lisa C. [R-MI-9]",
        "lastName": "McClain",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Accountability in Foreign Animal Research Act",
    "type": "HR",
    "updateDate": "2026-03-26T08:06:42Z",
    "updateDateIncludingText": "2026-03-26T08:06:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-28",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-28",
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
          "date": "2025-04-28T16:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "NC"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "DC"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "SC"
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
      "sponsorshipDate": "2025-05-06",
      "state": "VA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "NY"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "IN"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "GA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NH"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3043ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3043\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2025 Mrs. McClain (for herself and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit the use of taxpayer dollars to support animal experimentation in the laboratories of adversarial nations.\n#### 1. Short title\nThis Act may be cited as the Accountability in Foreign Animal Research Act .\n#### 2. Prohibition on funding research on animals in certain foreign countries\n##### (a) In general\nThe Secretary of Health and Human Services may not\u2014\n**(1)**\ndirectly or indirectly conduct biomedical research or experimentation that involves testing on vertebrate animals in any facility, or through any entity, located in, or owned or controlled, directly or indirectly, by\u2014\n**(A)**\nany of the foreign countries specified in subsection (b); or\n**(B)**\nsuch other foreign country that the Secretary of Health and Human Services, in consultation with the Secretary of State and the Secretary of Defense, determines is a foreign country of concern for the purposes of this Act; or\n**(2)**\nsupport, through grants, subgrants, contracts, cooperative agreements, or other funding vehicles, biomedical research or experimentation that involves testing on vertebrate animals conducted by any entity based in a foreign country referred to in paragraph (1).\n##### (b) Foreign countries specified\nThe foreign countries specified in this subsection are the following:\n**(1)**\nThe People\u2019s Republic of China, including the Hong Kong Special Administrative Region.\n**(2)**\nThe Islamic Republic of Iran.\n**(3)**\nThe Democratic People\u2019s Republic of Korea.\n**(4)**\nThe Russian Federation.\n##### (c) Report on addition to list of foreign countries\n**(1) In general**\nThe Secretary of Health and Human Services shall submit to the chairperson and ranking member of each of the appropriate committees of Congress a report with respect to each instance in which the Secretary makes a determination with respect to a country under subsection (a)(1)(B) that contains a detailed accounting of the Secretary\u2019s reasoning for such determination.\n**(2) Timing**\nA report shall be submitted under paragraph (1) not later than 60 days after the date of an instance described in such paragraph.\n**(3) Appropriate committees of Congress**\nIn this section, the term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Appropriations of the Senate;\n**(B)**\nthe Committee on Health, Education, Labor, and Pensions of the Senate;\n**(C)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate;\n**(D)**\nthe Committee on Appropriations of the House of Representatives;\n**(E)**\nthe Committee on Energy and Commerce of the House of Representatives; and\n**(F)**\nthe Committee on Homeland Security of the House of Representatives.",
      "versionDate": "2025-04-28",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-10",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1435",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Accountability in Foreign Animal Research Act",
      "type": "S"
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
        "name": "Health",
        "updateDate": "2025-05-29T12:13:54Z"
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
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3043ih.xml"
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
      "title": "Accountability in Foreign Animal Research Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-09T03:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Accountability in Foreign Animal Research Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T03:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of taxpayer dollars to support animal experimentation in the laboratories of adversarial nations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T03:33:21Z"
    }
  ]
}
```
