# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8169?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8169
- Title: Export Control Enforcement and Enhancement Act
- Congress: 119
- Bill type: HR
- Bill number: 8169
- Origin chamber: House
- Introduced date: 2026-03-30
- Update date: 2026-05-06T13:35:29Z
- Update date including text: 2026-05-06T13:35:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-30: Introduced in House
- 2026-03-30 - IntroReferral: Introduced in House
- 2026-03-30 - IntroReferral: Introduced in House
- 2026-03-30 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 44 - 0.
- Latest action: 2026-03-30: Introduced in House

## Actions

- 2026-03-30 - IntroReferral: Introduced in House
- 2026-03-30 - IntroReferral: Introduced in House
- 2026-03-30 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 44 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-30",
    "latestAction": {
      "actionDate": "2026-03-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8169",
    "number": "8169",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "W000812",
        "district": "2",
        "firstName": "Ann",
        "fullName": "Rep. Wagner, Ann [R-MO-2]",
        "lastName": "Wagner",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Export Control Enforcement and Enhancement Act",
    "type": "HR",
    "updateDate": "2026-05-06T13:35:29Z",
    "updateDateIncludingText": "2026-05-06T13:35:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 44 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-30",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-30",
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
        "item": [
          {
            "date": "2026-04-22T20:04:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-03-30T16:00:15Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8169ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8169\nIN THE HOUSE OF REPRESENTATIVES\nMarch 30, 2026 Mrs. Wagner introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo amend the Export Control Reform Act of 2018 to provide for expedited consideration of proposals for additions to, removals from, or other modifications with respect to entities on the Entity List, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Export Control Enforcement and Enhancement Act .\n#### 2. Expedited consideration of proposals for additions to, removals from, or other modifications with respect to entities on the Entity List\nSection 1754 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4813 ) is amended by adding at the end the following:\n(g) Expedited consideration of proposals for additions to, removals from, or other modifications with respect to entities on the Entity List (1) In general Any member of the End-User Review Committee may submit a proposal directly to the Committee requesting a vote of all members of the Committee for additions to, removals from, or other modifications with respect to the Entity List. A proposal to add an entity to the Entity List shall be made in accordance with the provisions of paragraph (3). (2) Consideration Subject to paragraph (4)(B), the End-User Review Committee shall vote to approve or disapprove a proposal submitted under paragraph (1) not later than 30 days after the date on which the proposal is submitted to the Committee. (3) Additional information The Chair of the End-User Review Committee, with the concurrence of the member of the Committee that submitted a proposal under paragraph (1), may suspend for an additional 15 days the time period specified in paragraph (2) with respect to consideration of the proposal if the Chair and the member determine that additional information is required in order to make a determination with respect to the proposal, including the impact and effect of the proposal. (4) Additions to the Entity List (A) In general An entity may be added to the Entity List if the End-User Review Committee by majority vote of its members has determined that the entity has engaged, is engaged, or is at risk of engaging in activities contrary to the national security or foreign policy interests of the United States. (B) Licensing policy (i) In general Subject to clause (ii), there shall be in effect a policy of presumption of denial for all applications for a license to export, reexport, or in-country transfer any item subject to the Export Administration Regulations if an entity added to the Entity List under this subsection is or would be a party to a transaction with respect to which the application applies. (ii) Exception The licensing policy required by clause (i) shall not apply with respect an entity described in such clause if the members of the End-User Review Committee that voted to add the entity to the Entity List under this subsection agree by majority vote of such members to apply a different policy with respect to the entity for all or specific types of items subject to the Export Administration Regulations that would be in the national security and foreign policy interests of the United States. (C) Rule of construction Nothing in this paragraph may be construed to limit or otherwise affect the escalation procedures described in part 750 of the Export Administration Regulations. (5) Administrative provisions (A) In general Each member of the End-User Review Committee shall have 1 vote with respect to matters described in this subsection. The chairperson of the Committee shall not have the authority to make determinations or override any voting decision with respect to such matters. (B) Suspension of voting period The chairperson of the End-User Review Committee may suspend the 30-day voting period described in paragraph (2) if the members of the Committee unanimously agree to postpone the vote. (C) Notice; implementing authority The chairperson of the End-User Review Committee shall notify the Assistant Secretary of Commerce for Export Administration of all final decisions of the Committee with respect to additions to, removals from, or other modifications with respect to the Entity List under this subsection so that the Assistant Secretary of Commerce for Export Administration may implement all such modifications. (6) Definitions In this subsection\u2014 (A) the terms End-User Review Committee and Committee mean\u2014 (i) the End-User Review Committee established under section 744.16(d) of title 15, Code of Federal Regulations; and (ii) any successor committee; and (B) the term Entity List means the list maintained by the Bureau of Industry and Security of the Department of Commerce and set forth in Supplement No. 4 to part 744 of the Export Administration Regulations, or successor regulations. .",
      "versionDate": "2026-03-30",
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
            "name": "Licensing and registrations",
            "updateDate": "2026-05-01T18:38:49Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2026-05-01T18:38:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-04-13T21:12:55Z"
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
      "date": "2026-03-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8169ih.xml"
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
      "title": "Export Control Enforcement and Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-08T12:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Export Control Enforcement and Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Export Control Reform Act of 2018 to provide for expedited consideration of proposals for additions to, removals from, or other modifications with respect to entities on the Entity List, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:24Z"
    }
  ]
}
```
