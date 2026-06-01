# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8259?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8259
- Title: Federal Water Projects Consultation Improvement Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8259
- Origin chamber: House
- Introduced date: 2026-04-14
- Update date: 2026-05-05T19:49:12Z
- Update date including text: 2026-05-05T19:49:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-14: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-04-22 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-04-29 - Committee: Subcommittee Hearings Held
- Latest action: 2026-04-14: Introduced in House

## Actions

- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-04-22 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-04-29 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-14",
    "latestAction": {
      "actionDate": "2026-04-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8259",
    "number": "8259",
    "originChamber": "House",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "B000668",
        "district": "2",
        "firstName": "Cliff",
        "fullName": "Rep. Bentz, Cliff [R-OR-2]",
        "lastName": "Bentz",
        "party": "R",
        "state": "OR"
      }
    ],
    "title": "Federal Water Projects Consultation Improvement Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-05T19:49:12Z",
    "updateDateIncludingText": "2026-05-05T19:49:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water, Wildlife and Fisheries.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-14",
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
      "actionDate": "2026-04-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-14",
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
          "date": "2026-04-14T16:03:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-04-29T18:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-04-22T19:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
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
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8259ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8259\nIN THE HOUSE OF REPRESENTATIVES\nApril 14, 2026 Mr. Bentz (for himself and Mr. Fulcher ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo ensure meaningful consultation and cooperation between Federal and local entities in the operation of Federal water projects in the Reclamation States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Water Projects Consultation Improvement Act of 2026 .\n#### 2. Consultation with affected contractors of Federal water projects\n##### (a) Resolution of water resource issues\nIn furtherance of the policy established by section 2(c)(2) of the Endangered Species Act of 1973 ( 16 U.S.C. 1531(c)(2) ), in a consultation or reconsultation under section 7 of that Act ( 16 U.S.C. 1536 ) with respect to the operation of a Federal water project, the head of each action agency, the Secretary, or the head of an action agency and the Secretary working in coordination, as applicable, shall ensure that each covered entity that so requests shall\u2014\n**(1)**\nhave routine and continuing opportunities\u2014\n**(A)**\nto discuss and submit information to the action agency for consideration during the development of any biological assessment; and\n**(B)**\nengage with the action agency with respect to the preparation of the biological assessment;\n**(2)**\nif the head of an action agency suggests or considers an agency action that would not result in full delivery of water pursuant to a contract for contractors of the Federal water project, be informed and engaged as to\u2014\n**(A)**\nthe legal authority invoked by the action agency to support that such agency action would be within the scope of the authority of the action agency;\n**(B)**\nhow each component of the agency action would contribute to avoiding jeopardizing the continued existence of any threatened species or endangered species and destroying or adversely modifying critical habitat and the scientific data or information that supports each component of the agency action under consideration; and\n**(C)**\nwhy any other agency actions that would have fewer adverse water supply and economic impacts are inadequate to avoid jeopardizing the continued existence of any threatened species or endangered species and destroying or adversely modifying critical habitat;\n**(3)**\nbe informed by the head of the action agency of the schedule for preparation of a biological assessment;\n**(4)**\nbe informed by the Secretary of the schedule for preparation of the biological opinion at such time as the biological assessment is submitted to the Services by the action agency;\n**(5)**\nreceive a copy of draft biological opinion and have the opportunity to review each such draft biological opinion and provide comment to the Secretary through engagement with the action agency, which comments shall be afforded due consideration during the consultation;\n**(6)**\nhave the opportunity to confer and engage with the head of the action agency and applicant, if any, with respect to reasonable and prudent alternatives prior to the identification of any reasonable and prudent alternative for consideration;\n**(7)**\nif the Secretary suggests a reasonable and prudent alternative, be informed and engaged with respect to\u2014\n**(A)**\nhow each component of the reasonable and prudent alternative will contribute to avoiding jeopardizing the continued existence of any threatened species or endangered species and destroying or adversely modifying critical habitat and the scientific data or information that supports each component of the reasonable and prudent alternative; and\n**(B)**\nwhy any other proposed reasonable and prudent alternatives that would have fewer adverse water supply and economic impacts are inadequate to avoid jeopardizing the continued existence of any threatened species or endangered species and destroying or adversely modifying critical habitat; and\n**(8)**\nif the Secretary proposes a reasonable and prudent measure to avoid or minimize take of threatened species or endangered species, or terms and conditions to implement such reasonable and prudent measure, be informed and engaged with respect to\u2014\n**(A)**\nhow the reasonable and prudent measure or terms and conditions relate to avoiding or minimizing such take; and\n**(B)**\nwhether the reasonable and prudent measure or terms and conditions conform to any applicable limitations.\n#### 3. Definitions\nIn this Act:\n**(1) Action agency**\nThe term action agency means the Federal agency responsible for authorizing, funding, or carrying out an action subject to consultation under section 7 of the Endangered Species Act of 1973 ( 16 U.S.C. 1536 ).\n**(2) Agency action**\nThe term agency action has the meaning given the term in section 7(a)(2) of the Endangered Species Act of 1973 ( 16 U.S.C. 1536(a)(2) ).\n**(3) Biological assessment**\nThe term biological assessment means a biological assessment conducted under section 7(c) of the Endangered Species Act of 1973 ( 16 U.S.C. 1536(c) ).\n**(4) Biological opinion**\nThe term biological opinion means a written statement provided by the Secretary under section 7(b)(3) of the Endangered Species Act of 1973 ( 16 U.S.C. 1536(b)(3) ).\n**(5) Contractor**\nThe term contractor means any public agency, quasi-municipal corporation, irrigation district, water users association, or similar entity that has entered into a water service, repayment, or other contract with the United States related to storage, diversion, or delivery of water from a Federal water project.\n**(6) Covered entity**\nThe term covered entity means a public or quasi-municipal agency or water users association that has a contract with the Bureau of Reclamation for municipal or agricultural water supply from a Federal water project.\n**(7) Critical habitat**\nThe term critical habitat has the meaning given the term in section 3 of the Endangered Species Act of 1973 ( 16 U.S.C. 1532 ).\n**(8) Endangered species**\nThe term endangered species has the meaning given the term in section 3 of the Endangered Species Act of 1973 ( 16 U.S.C. 1532 ).\n**(9) Engage**\nThe term engage means to conduct direct written and in-person communications recognizing the unique interest of the contractor and promoting maximum candor and cooperation.\n**(10) Federal water project**\nThe term Federal water project means any project or facility\u2014\n**(A)**\nin a Reclamation State described in subparagraphs (B) through (R) of section 128(a)(7) of the EXPLORE Act ( 16 U.S.C. 8426(a)(7) ); and\n**(B)**\noperated or managed by a Federal agency for the authorized purpose of municipal or agricultural water supply.\n**(11) Reasonable and prudent alternative**\nThe term reasonable and prudent alternative means a reasonable and prudent alternative suggested by the Secretary under section 7(b)(3) of the Endangered Species Act of 1973 ( 16 U.S.C. 1536(b)(3) ).\n**(12) Reasonable and prudent measure**\nThe term reasonable and prudent measure means a reasonable and prudent measure specified by the Secretary under section 7(b)(4) of the Endangered Species Act of 1973 ( 16 U.S.C. 1536(b)(4) ).\n**(13) Secretary**\nThe term Secretary has the meaning given the term in section 3 of the Endangered Species Act of 1973 ( 16 U.S.C. 1532 ).\n**(14) Take**\nThe term take has the meaning given the term in section 3 of the Endangered Species Act of 1973 ( 16 U.S.C. 1532 ).\n**(15) Threatened species**\nThe term threatened species has the meaning given the term in section 3 of the Endangered Species Act of 1973 ( 16 U.S.C. 1532 ).",
      "versionDate": "2026-04-14",
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
            "name": "Biological and life sciences",
            "updateDate": "2026-05-05T19:49:02Z"
          },
          {
            "name": "Endangered and threatened species",
            "updateDate": "2026-05-05T19:49:06Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2026-05-05T19:48:56Z"
          },
          {
            "name": "Water resources funding",
            "updateDate": "2026-05-05T19:48:48Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2026-05-05T19:49:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2026-04-21T22:20:09Z"
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
      "date": "2026-04-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8259ih.xml"
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
      "title": "Federal Water Projects Consultation Improvement Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T08:23:37Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Water Projects Consultation Improvement Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-17T08:23:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure meaningful consultation and cooperation between Federal and local entities in the operation of Federal water projects in the Reclamation States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-17T08:18:43Z"
    }
  ]
}
```
