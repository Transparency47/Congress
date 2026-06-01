# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8633?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8633
- Title: Competitive Prices Act.
- Congress: 119
- Bill type: HR
- Bill number: 8633
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-20T20:24:33Z
- Update date including text: 2026-05-20T20:24:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-30: Introduced in House

## Actions

- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8633",
    "number": "8633",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "S001205",
        "district": "5",
        "firstName": "Mary Gay",
        "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
        "lastName": "Scanlon",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Competitive Prices Act.",
    "type": "HR",
    "updateDate": "2026-05-20T20:24:33Z",
    "updateDateIncludingText": "2026-05-20T20:24:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T13:04:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8633ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8633\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Ms. Scanlon (for herself and Mr. Nadler ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo specify the standards governing claims of consciously parallel pricing coordination in civil actions under the Sherman Act, and to clarify the meaning of contract, combination in the form of trust or otherwise, or conspiracy under the Sherman Act.\n#### 1. Short title\nThis Act may be cited as the Competitive Prices Act.\n#### 2. Pleading an antitrust violation through parallel conduct and plus factors\n##### (a) Definitions\n**(1)**\nThe term antitrust laws means the Sherman Act ( 15 U.S.C. 1 , et seq.), the Clayton Act ( 15 U.S.C. 12 , et seq.), and the Federal Trade Commission Act ( 15 U.S.C. 41 , et seq.).\n**(2)**\nThe term parallel conduct means two or more persons acting similarly to raise, lower, maintain, stabilize, or manipulate price, output, capacity, supply, or other terms of competition for reasonably interchangeable commodities or services. Parallel conduct need not be uniform and can be varied in timing, method, and amount.\n**(3)**\nThe term person has the meaning given the term in subsection (a) of the 1st section of the Clayton Act ( 5 U.S.C. 12(a) ).\n**(4)**\nThe term plus factors means allegations other than parallel conduct supporting the inference of a conspiracy, including\u2014\n**(A)**\na motive to coordinate efforts to raise, lower, maintain, stabilize, or manipulate price, output, capacity, supply, or other terms of competition for the purchase or sale of reasonably interchangeable commodities or services;\n**(B)**\nactions that would be contrary to a person\u2019s unilateral economic self-interest absent a conspiracy;\n**(C)**\ndeparture from prior pricing methodology and practices;\n**(D)**\nexchanges of competitively sensitive information;\n**(E)**\nprice or output levels unexplained by cost, supply, or demand;\n**(F)**\nan opportunity to conspire at industry events, conferences, trade association activities, or through any other meetings or venues;\n**(G)**\npast collusive practices;\n**(H)**\nan invitation to participate in a common scheme, including by public signaling of pricing, output, capacity, supply, or other competitive strategies, or offering of a method to engage in parallel conduct; and\n**(I)**\nmarket conditions conducive to coordination, including high market concentration, high barriers to entry, high exit barriers, inelastic demand, or fungible products.\n**(5)**\nThe terms State attorney general and State have the meaning given in section 4G of the Clayton Act ( 15 U.S.C. 15g ).\n##### (b) Standards of pleading and proof\nIn a civil action, including an action brought by the United States, the Federal Trade Commission, a State attorney general, or any person seeking damages or injunctive relief for violations of the antitrust laws\u2014\n**(1)**\nwhen opposing any motion to dismiss a complaint, motion for judgment on the pleadings, or any other motion challenging the sufficiency of the allegations, a claimant\u2014\n**(A)**\nplausibly states a claim by alleging parallel conduct and the presence of two or more plus factors;\n**(B)**\nneed not allege direct evidence of a conspiracy;\n**(C)**\nneed not allege facts tending to exclude the possibility of independent action; and\n**(D)**\nneed not allege a theory that is more plausible than one offered by defendants, as the court at the pleading stage must only consider whether the allegations are plausible, not whether an alternative explanation is equally or more plausible; and\n**(2)**\nwhen opposing any motion for summary judgment, motion for directed verdict, motion for judgment as a matter of law, or any other motion challenging the sufficiency of the evidence and permitting a ruling as matter of law, a claimant\u2014\n**(A)**\ndemonstrates a genuine issue of material fact by offering evidence, which may be direct evidence, circumstantial evidence, or some combination of the two, that is sufficient to allow a trier of fact to find that the defending party engaged in an unlawful conspiracy;\n**(B)**\nneed not offer evidence tending to exclude the possibility that the defending party acted independently; and\n**(C)**\nneed not demonstrate that the weight of the evidence favors the claimant, as all evidence must be construed in the light most favorable to the party opposing summary judgment and the weighing of the evidence is an issue for the finder of fact.\n##### (c) Rule of construction\nNothing in this Act shall be construed to abridge or narrow the remedies available under the antitrust laws.",
      "versionDate": "2026-04-30",
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
        "updateDate": "2026-05-20T20:24:33Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8633ih.xml"
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
      "title": "Competitive Prices Act.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T10:08:45Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Competitive Prices Act.",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T10:08:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To specify the standards governing claims of consciously parallel pricing coordination in civil actions under the Sherman Act, and to clarify the meaning of contract, combination in the form of trust or otherwise, or conspiracy under the Sherman Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T10:03:32Z"
    }
  ]
}
```
