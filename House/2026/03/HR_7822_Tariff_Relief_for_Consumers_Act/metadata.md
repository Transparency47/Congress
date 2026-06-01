# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7822?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7822
- Title: Tariff Relief for Consumers Act
- Congress: 119
- Bill type: HR
- Bill number: 7822
- Origin chamber: House
- Introduced date: 2026-03-05
- Update date: 2026-04-28T08:05:57Z
- Update date including text: 2026-04-28T08:05:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-03-05: Introduced in House

## Actions

- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the House Committee on Ways and Means.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7822",
    "number": "7822",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "D000216",
        "district": "3",
        "firstName": "Rosa",
        "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
        "lastName": "DeLauro",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Tariff Relief for Consumers Act",
    "type": "HR",
    "updateDate": "2026-04-28T08:05:57Z",
    "updateDateIncludingText": "2026-04-28T08:05:57Z"
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
          "date": "2026-03-05T15:05:25Z",
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
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "IN"
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
      "sponsorshipDate": "2026-03-18",
      "state": "DC"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7822ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7822\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2026 Ms. DeLauro (for herself and Mr. Mrvan ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo direct the Secretary of the Treasury to promulgate regulations for the payment of refunds for tariffs invalidly assessed using authorities provided by the International Emergency Economic Powers Act to entities that demonstrably lower consumer prices, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tariff Relief for Consumers Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nPresident Trump\u2019s tariffs imposed under the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) (IEEPA) in many sectors raised prices for consumers and imposed additional costs on businesses.\n**(2)**\nResearch has shown that consumers have shouldered up to 96 percent of the burden of the IEEPA tariffs, meaning companies have passed the increased costs in their supply chains due to tariffs on to consumers in the form of higher prices.\n**(3)**\nGiven the Supreme Court\u2019s holding in Learning Resources, Inc. v. Trump that the tariffs imposed by President Trump under IEEPA are unlawful, the Administration must ensure that consumers, not just large corporations, are the ones who receive relief from the costs of these tariffs.\n**(4)**\nAs consideration of refunding tariffs paid due to the President\u2019s policies is undertaken by the Administration and the courts, priority should be given to ensuring that final consumers of products subject to tariffs obtain relief. It is unlikely that large corporations will pass on to consumers the benefit of any tariff refunds they receive without specific stipulations to that effect.\n**(5)**\nTherefore, the Secretary of the Treasury, the Commissioner of U.S. Customs and Border Protection, and the head of any other relevant Federal agency should rapidly draft and implement rules to ensure tariff refunds are returned directly to consumers in the form of price reductions or rebates.\n#### 3. Tariff refund program\n##### (a) Establishment\nNot later than 30 days after the date of the enactment of this Act, the Secretary of the Treasury, in consultation with the Commissioner of U.S. Customs and Border Protection, shall promulgate such regulations as may be necessary to carry out a program by which covered importers may receive refunds in the amount the Secretary determines such covered importers paid the United States in tariffs or other duties imposed through the assertion of authorities provided by the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) and invalidated by the Supreme Court in Learning Resources, Inc. v. Trump on February 20, 2026.\n##### (b) Application requirements\nIn applying for a refund under the regulations promulgated pursuant to this section, a covered importer shall\u2014\n**(1)**\nset forth in the application the steps such covered importer intends to take to lower the prices paid by their customers for goods formerly subject to such tariffs, in full proportion to the refund applied to be received with respect to such goods; and\n**(2)**\ndemonstrate, to the extent practicable\u2014\n**(A)**\nthat such reductions in prices are targeted towards essential consumer goods;\n**(B)**\nto the extent that the covered importer does not trade in essential consumer goods, that the covered importer has implemented other means by which prior customers of the importer can receive rebates or refunds on prospective purchases commensurate with the amount refunded; or\n**(C)**\nthat the covered importer did not increase customer prices due to the imposition of the tariffs described in subsection (a) and instead absorbed that cost directly.\n##### (c) Prioritization\nThe Secretary shall prioritize the payment of refunds described in subsection (a) to\u2014\n**(1)**\ncovered importers that credibly demonstrate, as described in subsection (b)(2)(A), that in anticipation of receiving such refunds the covered importer has reduced prices for essential consumer goods; and\n**(2)**\ncovered importers that credibly demonstrate, as described in subsection (b)(2)(B), that in anticipation of receiving such refunds the covered importer has created a mechanism for prior consumers to receive rebates on prospective purchases.\n##### (d) Prohibition\nNo covered importer may conduct stock buybacks or distribute dividends unless the covered importer certifies to the Secretary of the Treasury that the covered importer has completed the steps to lower prices for consumers described in subsection (b)(1).\n##### (e) Consultation\nIn carrying out the regulations promulgated pursuant to this section, the Secretary of the Treasury shall consult as appropriate with the heads of other relevant Federal departments and agencies.\n##### (f) Deadline for refunds\n**(1) In general**\nThe Secretary of the Treasury, in coordination with the heads of other relevant Federal departments and agencies, as appropriate, shall take such steps as may be necessary to ensure that all tariffs and other duties described in subsection (a) are refunded not later than 180 days after the date of the enactment of this Act, except to the extent that covered importers are unable to meet the applicable requirements of the program established by such subsection.\n**(2) Voluntary price reduction**\nNothing in this subsection may be construed to prohibit or limit any importer that paid any amount in tariffs or other duties described in subsection (a) from voluntarily lowering prices in the manner described in subsection (b)(1).\n##### (g) Definitions\nIn this Act:\n**(1)**\nThe term covered importer means an entity that paid $5,000,000 or more in tariffs or other duties described in subsection (a) as of February 19, 2026, other than any such entity whose ultimate parent entity earned less than $10,000,000 in revenue in calendar year 2025.\n**(2)**\nThe term essential consumer goods means\u2014\n**(A)**\ninfant formula and infant and toddler food goods;\n**(B)**\ndiapers and essential infant clothing and safety products;\n**(C)**\nhygiene and health care products;\n**(D)**\nfoodstuffs eligible to be purchased with supplemental nutrition assistance program benefits, as identified by the Secretary of Agriculture;\n**(E)**\nbasic clothing items, including shoes;\n**(F)**\nchildren\u2019s toys and sporting goods with a manufacturer\u2019s suggested retail price of less than $50; and\n**(G)**\nsuch other consumer goods as the Secretary of the Treasury determines appropriate.",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-03-30T23:05:58Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7822ih.xml"
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
      "title": "Tariff Relief for Consumers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T03:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tariff Relief for Consumers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T03:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of the Treasury to promulgate regulations for the payment of refunds for tariffs invalidly assessed using authorities provided by the International Emergency Economic Powers Act to entities that demonstrably lower consumer prices, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T03:03:23Z"
    }
  ]
}
```
