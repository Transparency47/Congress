# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3843?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3843
- Title: Baseload Reliability Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 3843
- Origin chamber: House
- Introduced date: 2025-06-09
- Update date: 2026-03-27T08:06:53Z
- Update date including text: 2026-03-27T08:06:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-09: Introduced in House
- 2025-06-09 - IntroReferral: Introduced in House
- 2025-06-09 - IntroReferral: Introduced in House
- 2025-06-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-06-09: Introduced in House

## Actions

- 2025-06-09 - IntroReferral: Introduced in House
- 2025-06-09 - IntroReferral: Introduced in House
- 2025-06-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-09",
    "latestAction": {
      "actionDate": "2025-06-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3843",
    "number": "3843",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "F000482",
        "district": "",
        "firstName": "Julie",
        "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
        "lastName": "Fedorchak",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "Baseload Reliability Protection Act",
    "type": "HR",
    "updateDate": "2026-03-27T08:06:53Z",
    "updateDateIncludingText": "2026-03-27T08:06:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-09",
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
      "actionDate": "2025-06-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-09",
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
          "date": "2025-06-09T16:02:00Z",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "TX"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "TX"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "TX"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "OH"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "WV"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "OH"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "MT"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "IN"
    },
    {
      "bioguideId": "H001072",
      "district": "2",
      "firstName": "J.",
      "fullName": "Rep. Hill, J. French [R-AR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hill",
      "middleName": "French",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "AR"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "NY"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "IL"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "FL"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "WA"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "FL"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "CO"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "IN"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "NC"
    },
    {
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "VA"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "NC"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "MO"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "SD"
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
      "sponsorshipDate": "2025-10-08",
      "state": "VA"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "AZ"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2026-01-09",
      "state": "KY"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "GA"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3843ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3843\nIN THE HOUSE OF REPRESENTATIVES\nJune 9, 2025 Ms. Fedorchak (for herself, Mr. Weber of Texas , Mr. Goldman of Texas , Mr. Pfluger , Mr. Rulli , Mrs. Miller of West Virginia , and Mr. Balderson ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Power Act to prohibit retirements of baseload electric generating units in any area that is served by a Regional Transmission Organization or an Independent System Operator and that the North American Electric Reliability Corporation categorizes as at elevated risk or high risk of electricity supply shortfalls, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Baseload Reliability Protection Act .\n#### 2. Prohibition on retirements and conversion of fuel source for electric generating units in areas at high risk or elevated risk of electricity supply shortfalls\n##### (a) In general\nPart II of the Federal Power Act ( 16 U.S.C. 824 et seq. ) is amended by adding after section 215A the following:\n215B. Prohibition on retirements and conversion of fuel source for electric generating units in areas at high risk or elevated risk of electricity supply shortfalls (a) Prohibition No operator or partial or sole owner of a covered electric generating unit that is located in a covered area may\u2014 (1) retire such covered electric generating unit; or (2) convert the fuel source for such covered electric generating unit. (b) Exemptions (1) Operator or owner petition Not later than 90 days after the publication of the most recent long-term reliability assessment categorizing the relevant covered area as at high risk or elevated risk of electricity supply shortfalls, an operator or owner of a covered electric generating unit located in such covered area may submit to the Commission a petition for an exemption from a prohibition under subsection (a) with respect to such covered electric generating unit. (2) Final determination (A) Deadline (i) In general Except as otherwise provided in this paragraph, not later than 90 days after a petition for an exemption is submitted to the Commission under paragraph (1), the Commission shall issue a final determination granting such exemption or denying the petition for such exemption. (ii) Petitions based on unprofitability or financial losses Subject to subparagraph (C), with respect to a petition for an exemption under this subsection for a covered electric generating unit that is based on unprofitability or sustained financial losses, if the Commission determines that retirement of, or converting the fuel source for, such covered electric generating unit would hinder the reliable operation of the bulk-power system, the Commission shall, not later than 180 days after such petition is submitted to the Commission under paragraph (1), issue a final determination granting such exemption or denying the petition for such exemption. (B) Criteria Subject to subparagraph (C), the Commission shall issue a final determination granting an exemption under this subsection if the Commission determines\u2014 (i) that the applicable operator or owner of a covered electric generating unit has demonstrated in a petition submitted under paragraph (1) of this subsection that compliance with the relevant prohibition under subsection (a) will result in\u2014 (I) unprofitability of such covered electric generating unit; (II) sustained financial losses for such operator or owner; or (III) elevated risk to the safety of workers or public safety; or (ii) in consultation with the relevant Regional Transmission Organization or Independent System Operator\u2014 (I) that the applicable operator or owner of a covered electric generating unit has demonstrated in a petition submitted under paragraph (1) of this subsection for an exemption from the prohibition under subsection (a)(1) that retirement of the covered electric generating unit will not hinder the reliable operation of the bulk-power system; (II) that the applicable operator or owner of a covered electric generating unit has demonstrated in a petition submitted under paragraph (1) of this subsection for an exemption from the prohibition under subsection (a)(1), and subject to paragraph (3), that such operator or owner will replace such covered electric generating unit through the construction or acquisition of one or more covered electric generating units with comparable or greater reliability attributes, considering, at a minimum, the dispatchability and availability during peak system demand of the covered electric generating unit that will be retired; or (III) that the applicable operator or owner of a covered electric generating unit has demonstrated in a petition submitted under paragraph (1) of this subsection for an exemption from the prohibition under subsection (a)(2) that converting the fuel source for such covered electric generating unit will not diminish the covered electric generating unit\u2019s dispatchability or availability during peak system demand, or otherwise hinder the reliable operation of the bulk-power system. (C) DOE grant or loan for continued operation (i) Referral With respect to a petition for an exemption under this subsection from the prohibition under subsection (a)(1) for a covered electric generating unit that is based on unprofitability or sustained financial losses, if the Commission determines that retirement of such covered electric generating unit would hinder the reliable operation of the bulk-power system, the Commission shall refer the petition to the Secretary of Energy. (ii) Loan or grant With respect to any petition referred to the Secretary of Energy under clause (i), the Secretary shall use funds made available to carry out this clause to make a grant or loan to the applicable operator or owner of the covered electric generating unit in accordance with paragraph (4). (iii) Treatment of petition If an operator or owner of a covered electric generating unit receives, not later than 180 days after the relevant petition for an exemption is submitted to the Commission under paragraph (1), a grant or loan pursuant to clause (ii) of this subparagraph, such petition shall be deemed denied for purposes of this subsection. (3) Replacement An operator or owner of a covered electric generating unit for which an exemption is granted under this subsection based on a demonstration that such operator or owner will replace the covered electric generating unit through the construction or acquisition of one or more other covered electric generating units with comparable or greater reliability attributes may not retire such covered electric generating unit until such covered electric generating unit has been so replaced and such one or more other covered electric generating units have been placed in service. (4) DOE grant or loan terms and funding (A) Funds The Secretary of Energy may use unobligated amounts made available to the Secretary under the Infrastructure Investment and Jobs Act ( Public Law 117\u201358 ) or Public Law 117\u2013169 to make grants and loans under paragraph (2)(C)(ii) and subparagraph (D) of this paragraph. (B) Grants The Secretary of Energy, in consultation with other agencies as the Secretary determines appropriate, may, if the Secretary determines it to be necessary and appropriate, make a grant to an operator or owner of a covered electric generating unit under paragraph (2)(C)(ii) of this subsection in order to provide for the prudent costs for the operation of such covered electric generating unit during any time the prohibition under subsection (a)(1) is in effect with respect to such covered electric generating unit. (C) Loans (i) Use of loan funds A loan made under paragraph (2)(C)(ii)\u2014 (I) shall be made for purposes of\u2014 (aa) keeping the relevant covered electric generating unit operating; and (bb) providing for the minimum costs for the operation of such covered electric generating unit during any time the prohibition under subsection (a)(1) is in effect with respect to such covered electric generating unit; and (II) may be made for the additional purposes of\u2014 (aa) providing for the costs of upgrading the capacity of the relevant covered electric generating unit; (bb) if the relevant covered electric generating unit is a nuclear power plant, uprating such covered electric generating unit; or (cc) modernizing the relevant covered electric generating unit for purposes of extending its lifespan. (ii) Terms and conditions Any loan under paragraph (2)(C)(ii) or subparagraph (D) of this paragraph shall be made on such terms and conditions as the Secretary of Energy determines appropriate. (iii) Revenue Any payments of interest on loans made under paragraph (2)(C)(ii) or subparagraph (D) of this paragraph shall be deposited in the general fund of the Treasury for the sole purpose of deficit reduction. (D) Other loans and grants The Secretary of Energy may make a loan or grant to an operator or owner of a covered electric generating unit that is subject to an order under section 202(c) in order to provide for the prudent costs for the operation of such covered electric generating unit during any time such order in effect with respect to such covered electric generating unit. (5) Other considerations In making a final determination under paragraph (2)\u2014 (A) the Commission may not consider the greenhouse gas emissions of a covered electric generating unit, including any impacts of such emissions on atmospheric temperatures or weather systems; and (B) with respect to a petition for an exemption under this subsection for a covered electric generating unit that is based on unprofitability or sustained financial losses, the Commission shall take into consideration any costs alleviated by the protection from penalties under subsection (c). (6) Judicial review Notwithstanding section 313, an operator or owner of an electric generating unit who is adversely affected or aggrieved by a final determination issued by the Commission under paragraph (2) may, not later than 60 days after the final determination is issued, file a petition for review of the final determination in the United States Court of Appeals for the District of Columbia Circuit or in the court of appeals for the United States for the circuit in which the party resides or has its principal place of business. Upon the filing of such petition such court shall have jurisdiction to affirm, set aside, or overturn such final determination. (c) Protection from penalties An action or omission taken by an operator or owner of a covered electric generating unit to comply with a prohibition under subsection (a) shall be treated as an action or omission taken to comply with an order issued under section 202(c) for purposes of such section. No operator or owner or a covered electric generating unit shall be required to undertake an expenditure in furtherance of a Federal, State, or local environmental law or regulation, performance for which is excused due to the existence of a prohibition under subsection (a). (d) Standardized criteria for categorization of risk Not later than 60 days after the date of enactment of this section, the Electric Reliability Organization shall determine and publish a standardized probabilistic assessment methodology and standardized criteria for categorizing areas as being at high risk, elevated risk, or normal risk of electricity supply shortfalls to be used in each long-term reliability assessment. Such standardized methodology and criteria shall be at least as rigorous as the methodology and criteria used in the 2024 long-term reliability assessment. (e) Definitions In this section: (1) Bulk-power system The term bulk-power system has the meaning given such term in section 215(a). (2) Covered area The term covered area means an area that\u2014 (A) is served by a Regional Transmission Organization or an Independent System Operator; and (B) the Electric Reliability Organization categorizes, in the most recent long-term reliability assessment, as at elevated risk or high risk of electricity supply shortfalls. (3) Covered electric generating unit The term covered electric generating unit means a dispatchable electric generating unit that\u2014 (A) has greater than or equal to 25 megawatts of nameplate capacity; (B) is interconnected to the bulk-power system; and (C) does not derive its primary energy input from intermittent renewable sources, with or without energy storage. (4) Electric Reliability Organization The term Electric Reliability Organization has the meaning given such term in section 215(a). (5) Long-term reliability assessment The term long-term reliability assessment means an annual assessment, conducted by the Electric Reliability Organization pursuant to section 215(g), of the reliability and adequacy of the bulk-power system in North America over a 10-year period. (6) Reliable operation The term reliable operation has the meaning given such term in section 215(a). .\n##### (b) Enforcement\nNot later than 1 year after the date of enactment of this Act, the Federal Energy Regulatory Commission shall submit to Congress a report on whether existing oversight and enforcement mechanisms for section 215B of the Federal Power Act, as added by subsection (a) of this section, are sufficient, including any recommendations to improve such mechanisms.",
      "versionDate": "2025-06-09",
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
        "name": "Energy",
        "updateDate": "2025-07-01T13:17:08Z"
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
      "date": "2025-06-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3843ih.xml"
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
      "title": "Baseload Reliability Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-17T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Baseload Reliability Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-17T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Power Act to prohibit retirements of baseload electric generating units in any area that is served by a Regional Transmission Organization or an Independent System Operator and that the North American Electric Reliability Corporation categorizes as at elevated risk or high risk of electricity supply shortfalls, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-17T05:18:23Z"
    }
  ]
}
```
