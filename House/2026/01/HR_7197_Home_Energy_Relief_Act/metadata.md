# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7197?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7197
- Title: Home Energy Relief Act
- Congress: 119
- Bill type: HR
- Bill number: 7197
- Origin chamber: House
- Introduced date: 2026-01-22
- Update date: 2026-02-11T21:30:51Z
- Update date including text: 2026-02-11T21:30:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-22: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-01-22: Introduced in House

## Actions

- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-22",
    "latestAction": {
      "actionDate": "2026-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7197",
    "number": "7197",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "B001324",
        "district": "1",
        "firstName": "Wesley",
        "fullName": "Rep. Bell, Wesley [D-MO-1]",
        "lastName": "Bell",
        "party": "D",
        "state": "MO"
      }
    ],
    "title": "Home Energy Relief Act",
    "type": "HR",
    "updateDate": "2026-02-11T21:30:51Z",
    "updateDateIncludingText": "2026-02-11T21:30:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-22",
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
      "actionDate": "2026-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-22",
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
          "date": "2026-01-22T14:07:35Z",
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
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "NY"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7197ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7197\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2026 Mr. Bell (for himself and Mr. Mannion ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend Public Law 117\u2013169 to improve access to home energy-efficiency rebates for working families, renters, and owners of older homes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Home Energy Relief Act .\n#### 2. Elimination of prohibition on combining rebates provided under HOMES rebate programs and high-efficiency electric home rebate programs with other Federal grants and rebates\n##### (a) Home energy performance-Based, whole-House rebates\n**(1) Repeal**\nParagraph (7) of section 50121(c) of Public Law 117\u2013169 ( 42 U.S.C. 18795(c) ) is repealed.\n**(2) Conforming amendments**\nSection 50121(b) of Public Law 117\u2013169 ( 42 U.S.C. 18795(b) ) is amended\u2014\n**(A)**\nin paragraph (4)(B), by striking retrofit; and inserting retrofit; and ;\n**(B)**\nin paragraph (5), by striking program; and and inserting program. ; and\n**(C)**\nby striking paragraph (6).\n##### (b) High-Efficiency electric home rebate program\n**(1) Repeal**\nParagraph (8) of section 50122(c) of Public Law 117\u2013169 ( 42 U.S.C. 18795a(c) ) is repealed.\n**(2) Conforming amendments**\nSection 50122(b) of Public Law 117\u2013169 ( 42 U.S.C. 18795a(b) ) is amended\u2014\n**(A)**\nin paragraph (2), by striking sale; and inserting sale; and ;\n**(B)**\nby striking paragraph (3); and\n**(C)**\nby redesignating paragraph (4) as paragraph (3).\n#### 3. High-cost urban retrofit bonus rebates\nSection 50122(c) of Public Law 117\u2013169 ( 42 U.S.C. 18795a(c) ) is amended by adding at the end the following:\n(10) Bonus rebates for upgrades and purchases relating to certain housing (A) In general From the amount of any grant provided under this section, a State energy office or Indian Tribe may provide to an eligible entity that received a rebate from the State energy office or Indian Tribe under a high-efficiency electric home rebate program a bonus rebate for the purchase of an appliance or a nonappliance upgrade under a qualified electrification project carried out or relating to housing built prior to January 1, 1970. (B) Amount of bonus rebate (i) In general A bonus rebate provided under this paragraph may not be greater than 20 percent of the amount of the initial rebate provided under the high-efficiency electric home rebate program. (ii) Exception to max amount Subsection (c)(3)(C) shall not apply to a bonus rebate provided under this paragraph. (iii) Not in excess of costs An eligible entity may not receive a sum of rebates under this section that exceeds the cost of the qualified electrification project. .\n#### 4. Reports to Congress\n##### (a) In general\nNot later than two years after the date of enactment of this Act, and annually thereafter, the Secretary of Energy shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Energy and Natural Resources of the Senate a report that includes\u2014\n**(1)**\nthe number of households that received a rebate under a HOMES rebate program or a high-efficiency electric home rebate program during the year preceding the report;\n**(2)**\nthe household average energy savings resulting from upgrades, purchases, and retrofits for which a rebate was provided under a HOMES rebate program or a high-efficiency electric home rebate program; and\n**(3)**\nrecommendations for further increasing the access of low-income and high-energy-burden households to such rebates.\n##### (b) Definitions\nIn this section:\n**(1) HOMES rebate program**\nThe term HOMES rebate program has the meaning given such term in section 50121(d) of Public Law 117\u2013169 ( 42 U.S.C. 18795(d) ).\n**(2) High-efficiency electric home rebate program**\nThe term high-efficiency electric home rebate program has the meaning given such term in section 50122(d) of Public Law 117\u2013169 ( 42 U.S.C. 18795a(d) ).",
      "versionDate": "2026-01-22",
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
        "updateDate": "2026-02-11T21:30:51Z"
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
      "date": "2026-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7197ih.xml"
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
      "title": "Home Energy Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T06:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Home Energy Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-11T06:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend Public Law 117-169 to improve access to home energy-efficiency rebates for working families, renters, and owners of older homes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-11T06:18:21Z"
    }
  ]
}
```
