# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8200?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8200
- Title: Interstate Ferry Fairness Act
- Congress: 119
- Bill type: HR
- Bill number: 8200
- Origin chamber: House
- Introduced date: 2026-04-06
- Update date: 2026-04-09T19:59:58Z
- Update date including text: 2026-04-09T19:59:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-06: Introduced in House
- 2026-04-06 - IntroReferral: Introduced in House
- 2026-04-06 - IntroReferral: Introduced in House
- 2026-04-06 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-04-06: Introduced in House

## Actions

- 2026-04-06 - IntroReferral: Introduced in House
- 2026-04-06 - IntroReferral: Introduced in House
- 2026-04-06 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-06",
    "latestAction": {
      "actionDate": "2026-04-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8200",
    "number": "8200",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "L000598",
        "district": "1",
        "firstName": "Nick",
        "fullName": "Rep. LaLota, Nick [R-NY-1]",
        "lastName": "LaLota",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Interstate Ferry Fairness Act",
    "type": "HR",
    "updateDate": "2026-04-09T19:59:58Z",
    "updateDateIncludingText": "2026-04-09T19:59:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-06",
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
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-06",
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
          "date": "2026-04-06T14:02:00Z",
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
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8200ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8200\nIN THE HOUSE OF REPRESENTATIVES\nApril 6, 2026 Mr. LaLota (for himself and Mr. Courtney ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 23, United States Code, so that a privately or majority-privately owned ferry or ferry terminal facility is an eligible entity for purposes of participation in the Ferry Boat Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Interstate Ferry Fairness Act .\n#### 2. Amendment to allow privately owned ferries and ferry terminal facilities to be eligible for Ferry Boat Program\n##### (a) Permissibility of Federal participation in construction of privately owned ferries or ferry terminal facilities\nSection 129(c) of title 23, United States Code, is amended\u2014\n**(1)**\nin paragraph (2)\u2014\n**(A)**\nby inserting (A) before The operation ; and\n**(B)**\nby striking on a route and all that follows through the period at the end and inserting\non a route\u2014 (i) classified as a public road within the State and which has not been designated as a route on the Interstate System or on a public transit ferry eligible under chapter 53 of title 49; or (ii) between 2 adjoining States and that connects one or more public roads. (B) Projects under this subsection may be eligible for both ferry boats carrying cars and passengers and ferry boats carrying passengers only. ;\n**(2)**\nin paragraph (3)\u2014\n**(A)**\nin subparagraph (A), by striking shall be and all that follows through the period at the end and inserting\nshall be\u2014 (i) publicly owned or operated; (ii) majority publicly owned, if the Secretary determines with respect to such majority publicly owned ferry or ferry terminal facility that the ferry boat or ferry terminal facility provides substantial public benefits; or (iii) with respect to a ferry that operates between 2 adjoining States or a ferry terminal facility that supports such a ferry, privately owned or majority privately owned, if the Secretary determines with respect to such ferry or ferry terminal facility that the ferry boat or ferry terminal facility provides substantial public benefits or otherwise meets the foremost needs of the surface transportation system described in section 101(b)(3)(D). ; and\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nby striking Any Federal participation and inserting (i) Except as provided in clause (ii), any Federal participation ; and\n**(ii)**\nby adding at the end the following new clause:\n(ii) Federal participation may involve the construction or purchase, for private ownership, of\u2014 (I) a ferry boat that operates between 2 adjoining States; or (II) a ferry terminal facility or any other eligible project under this section that supports such ferry boat. ; and\n**(3)**\nin paragraph (4)\u2014\n**(A)**\nby inserting (A) before The operating authority ;\n**(B)**\nby striking such ferry and inserting a publicly owned or a majority publicly owned ferry ;\n**(C)**\nby striking a privately operated toll ferry and inserting a privately operated toll ferry not subject to subparagraph (B) ; and\n**(D)**\nby adding at the end the following new subparagraph:\n(B) A privately owned or majority privately owned ferry operating between 2 adjoining States may charge a fare for passage on such ferry in an amount not more than the sum of an amount necessary to produce revenues sufficient to cover actual and necessary costs of operation, maintenance, repair, debt service, negotiated management fees, plus an amount that the Secretary determines is a reasonable rate of return for the ferry. All revenues derived therefrom shall be applied to such actual and necessary costs, except the ferry may retain the amount that the Secretary determines is a reasonable rate of return. .\n##### (b) Conforming amendments\n**(1) Surface transportation block grant program**\nSection 133(b)(1)(B) of title 23, United States Code, is amended to read as follows:\n(B) ferry boats and terminal facilities that are eligible for funding under section 129(c); .\n**(2) Construction of ferry boats and ferry terminal facilities**\nSection 147(c) of title 23, United States Code, is amended by striking public entities and inserting entities .\n##### (c) Effective date\nThe amendments made by this section shall take affect with respect to a privately owned, or majority privately owned, ferry or ferry terminal facility for purposes of eligibility of the program under section 147 of title 23, United States Code, on the date that is 1 year after the date of enactment of this Act.",
      "versionDate": "2026-04-06",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-04-09T19:59:58Z"
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
      "date": "2026-04-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8200ih.xml"
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
      "title": "Interstate Ferry Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-07T08:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Interstate Ferry Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-07T08:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 23, United States Code, so that a privately or majority-privately owned ferry or ferry terminal facility is an eligible entity for purposes of participation in the Ferry Boat Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-07T08:18:27Z"
    }
  ]
}
```
