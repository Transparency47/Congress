# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7224?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7224
- Title: Secure Revenue Clearance Channel Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7224
- Origin chamber: House
- Introduced date: 2026-01-22
- Update date: 2026-03-09T18:27:19Z
- Update date including text: 2026-03-09T18:27:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-22: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-01-22: Introduced in House

## Actions

- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Ways and Means.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7224",
    "number": "7224",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001205",
        "district": "1",
        "firstName": "Carol",
        "fullName": "Rep. Miller, Carol D. [R-WV-1]",
        "lastName": "Miller",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "Secure Revenue Clearance Channel Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-09T18:27:19Z",
    "updateDateIncludingText": "2026-03-09T18:27:19Z"
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
          "date": "2026-01-22T14:03:50Z",
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
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7224ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7224\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2026 Mrs. Miller of West Virginia (for herself and Mr. Beyer ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo provide for informal entry of certain shipments of merchandise, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Secure Revenue Clearance Channel Act of 2026 .\n#### 2. Informal entry of certain shipments of merchandise\n##### (a) Entry requirements\n**(1) In general**\nAn express consignment carrier or operator of a shipment of merchandise of a value that does not exceed $600 may, notwithstanding the provisions of section 484 of the Tariff Act of 1930 ( 19 U.S.C. 1484 ), satisfy the requirements for entry of the shipment of merchandise if\u2014\n**(A)**\nthe carrier or operator submits to U.S. Customs and Border Protection in electronic format the advanced manifest of the carrier or operator for purposes of the applicable entry documentation for the shipment of merchandise; and\n**(B)**\nU.S. Customs and Border Protection approves both\u2014\n**(i)**\nthe electronic format; and\n**(ii)**\nthe advanced manifest.\n**(2) Reference**\nThe entry requirements of this subsection may be referred to as the Secure Revenue Clearance Channel .\n##### (b) Exceptions\nThis entry requirements of subsection (a) shall not apply with respect to shipments of merchandise that are subject to\u2014\n**(1)**\nantidumping and countervailing duties under title VII of the Tariff Act of 1930;\n**(2)**\ntariff-rate quotas;\n**(3)**\na tax imposed under the Internal Revenue Code of 1986 that is collected by a Federal department or agency other than U.S. Customs and Border Protection, including alcohol and tobacco products; or\n**(4)**\na fee imposed by a Federal department or agency other than U.S. Customs and Border Protection and such department or agency does not waive the fee.\n##### (c) Definitions\nIn this section\u2014\n**(1)**\nthe term closely integrated administrative control \u2014\n**(A)**\nmeans operations that are sufficiently integrated at both ends of the service (for example, both pick-up and delivery) so that the express consignment carrier or operator can exercise a high degree of control over the shipment of merchandise, particularly in regard to the reliability of information supplied for customs purposes; and\n**(B)**\nmay be indicated by\u2014\n**(i)**\na substantial common ownership between the local carrier or operator and the foreign affiliate; or\n**(ii)**\na very close contractual relationship between the local carrier or operator and its foreign affiliate, such as through the use of a franchise arrangement; and\n**(2)**\nthe term express consignment operator or carrier means an entity that\u2014\n**(A)**\noperates in any mode or intermodally moving merchandise by special express commercial service under closely integrated administrative control and whose services are offered to the public under advertised, reliable timely delivery on a door-to-door basis;\n**(B)**\nassumes liability to U.S. Customs and Border Protection for the merchandise in the same manner as if it were the sole carrier of the merchandise;\n**(C)**\nadministers both hubs and express consignment facilities; and\n**(D)**\nhas signed and is implementing\u2014\n**(i)**\na narcotics information sharing agreement with U.S. Customs and Border Protection; and\n**(ii)**\na narcotics enforcement agreement with U.S. Immigration and Customs Enforcement.\n##### (d) Amendment\nSection 498(a) of the Tariff Act of 1930 ( 19 U.S.C. 1498(a) ) is amended by adding at the end the following:\n(13) Merchandise that qualifies for entry under section 2 of the Secure Revenue Clearance Channel Act of 2025. .\n#### 3. Fee for importation of merchandise entered under section 2\n##### (a) In general\nAn express consignment operator or carrier of merchandise entered under section 2 for consumption, or withdrawn from warehouse for consumption, subject to such regulations as the Commissioner of U.S. Customs and Border Protection, shall collect a fee on the importation of such merchandise in an amount equal to one of the following, at the election of the importer of record:\n**(1)**\n20 percent ad valorem of the merchandise.\n**(2)**\nThe equivalent tariff rate the merchandise would be subject to if the merchandise were entered as a formal entry under section 484 of the Tariff Act of 1930 ( 19 U.S.C. 1484 ).\n**(3)**\nAny other fixed or ad valorem duty rates that may be imposed based on the country of origin of the merchandise, including any such rates charged for international postal shipments.\n##### (b) Fee in lieu of other charges and duties\nThe fee required by subsection (a) shall be imposed and collected in lieu of the following:\n**(1)**\nAny charges under paragraphs (9) and (10) of section 13031(a) of the Consolidated Omnibus Budget Reconciliation Act of 1985 ( 19 U.S.C. 58c(a) ).\n**(2)**\nAny duties otherwise applicable with respect to the same merchandise, including\u2014\n**(A)**\nthe most-favored nation rates established in the Harmonized Tariff Schedule of the United States; and\n**(B)**\nduties imposed under section 232 of the Trade Expansion Act of 1962.\n##### (c) Collection and deposit of fees\nAll amounts collected in fees required by subsection (a)\u2014\n**(1)**\nshall be remitted in full on a quarterly basis by the express consignment operator or carrier of the shipment of merchandise to the Commissioner of U.S. Customs and Border Protection in accordance with regulations prescribed by the Secretary of Homeland Security; and\n**(2)**\nshall be deposited in the general fund of the Treasury.\n#### 4. Effective date\nThis Act shall take effect on the date that is 30 days after the date of the enactment of this Act.",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-03-09T18:27:19Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7224ih.xml"
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
      "title": "Secure Revenue Clearance Channel Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T05:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Secure Revenue Clearance Channel Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-05T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for informal entry of certain shipments of merchandise, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-05T05:18:29Z"
    }
  ]
}
```
