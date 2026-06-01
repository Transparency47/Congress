# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7871?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7871
- Title: MVP Act
- Congress: 119
- Bill type: HR
- Bill number: 7871
- Origin chamber: House
- Introduced date: 2026-03-09
- Update date: 2026-05-27T08:06:19Z
- Update date including text: 2026-05-27T08:06:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-03-09: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-09 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-09: Introduced in House

## Actions

- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-09 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7871",
    "number": "7871",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000558",
        "district": "2",
        "firstName": "Brett",
        "fullName": "Rep. Guthrie, Brett [R-KY-2]",
        "lastName": "Guthrie",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "MVP Act",
    "type": "HR",
    "updateDate": "2026-05-27T08:06:19Z",
    "updateDateIncludingText": "2026-05-27T08:06:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-09",
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
          "date": "2026-03-09T17:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-09T17:02:20Z",
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
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "MA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "IA"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "PA"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "CA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "NC"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "CA"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "MD"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "TX"
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
      "sponsorshipDate": "2026-05-12",
      "state": "GA"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "FL"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "FL"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7871ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7871\nIN THE HOUSE OF REPRESENTATIVES\nMarch 9, 2026 Mr. Guthrie (for himself, Mr. Auchincloss , Mrs. Miller-Meeks , Mr. Joyce of Pennsylvania , Mr. Peters , and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XIX of the Social Security Act to codify value-based purchasing arrangements under the Medicaid program and reforms related to price reporting under such arrangements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Medicaid VBPs for Patients Act or the MVP Act .\n#### 2. Codifying value-based purchasing arrangements under Medicaid and reforms related to price reporting under such arrangements\n##### (a) Codifying multiple best price points\n**(1) In general**\nSection 1927(c)(1)(C)(ii) of the Social Security Act ( 42 U.S.C. 1396r\u20138(c)(1)(C)(ii) ) is amended\u2014\n**(A)**\nin subclause (III), by adding a semicolon at the end;\n**(B)**\nin subclause (IV), by striking and at the end;\n**(C)**\nin subclause (V), by striking the period and inserting ; and ; and\n**(D)**\nby adding at the end the following new subclause:\n(VI) may include multiple best price points for a single dosage form and strength of a drug of a manufacturer subject to a value-based purchasing arrangement (as defined in subsection (k)(12)), but only if such manufacturer offers such arrangement to all States. .\n**(2) Rule of construction**\nNothing in the amendments made by this subsection may be construed to prohibit a manufacturer from treating a value-based purchasing arrangement as a bundled sale.\n##### (b) Definition of average manufacturer price\n**(1) In general**\nSection 1927(k)(1) of the Social Security Act ( 42 U.S.C. 1396r\u20138(k)(1) ) is amended\u2014\n**(A)**\nin subparagraph (B)(i)\u2014\n**(i)**\nin subclause (IV), by adding a semicolon at the end;\n**(ii)**\nin subclause (VII), by striking at the end and ;\n**(iii)**\nin subclause (VIII), by striking the period at the end and inserting ; and ; and\n**(iv)**\nby adding at the end the following new subclause:\n(IX) with respect to a covered outpatient drug that is sold under a value-based purchasing arrangement (as defined in paragraph (12)) during the rebate period, including such a drug that is an inhalation, infusion, instilled, implanted, or injectable drug that is not generally dispensed through a retail community pharmacy\u2014 (aa) a refund, rebate, reimbursement, or free goods from the manufacturer or third party on behalf of the manufacturer; or (bb) the withholding or reduction of a payment to the manufacturer or third party on behalf of the manufacturer; that is triggered by a patient who fails to achieve outcomes or measures defined under the terms of such value-based purchasing arrangement during the period for which such arrangement is effective. ; and\n**(B)**\nby adding at the end the following new subparagraph:\n(D) Special rule for certain value-based purchasing arrangements For purposes of subparagraph (A), in determining the average price paid to a manufacturer for a covered outpatient drug that is sold under a value-based purchasing arrangement (as defined in paragraph (12)) that provides that payment for such drug is made in installments over the course of such arrangement, such price shall be determined as if the aggregate price per the terms of the arrangement were paid in full in the first installment during the rebate period. .\n**(2) Rulemaking**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Health and Human Services shall implement the amendments made by this subsection through rulemaking.\n##### (c) Definition of value-Based purchasing arrangement\nSection 1927(k) of the Social Security Act ( 42 U.S.C. 1396r\u20138(k) ) is amended by adding at the end the following paragraph:\n(12) Value-Based Purchasing Arrangement The term value-based purchasing arrangement has the meaning given such term in section 447.502 of title 42, Code of Federal Regulations (or any successor regulation). .\n#### 3. Calculation of average sales price under Medicare\nSection 1847A(c)(3) of the Social Security Act (42 U.S.C. 1395w\u20133a(c)(3)) is amended\u2014\n**(1)**\nby striking In calculating and inserting the following:\n(A) In general Subject to subparagraph (B), in calculating ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(B) Certain remuneration under value-based purchasing arrangements excluded In calculating the manufacturer\u2019s average sales price under this subsection for a drug or biological that is sold under a value-based purchasing arrangement (as defined in section 1927(k)(12)) and with respect to which the manufacturer of such drug or biological has elected to include multiple best price points (as described in section 1927(c)(1)(C)(ii)(VI)) in reporting the best price of such drug under section 1927(b), such manufacturer's average sales price shall not include any amount that is excluded from the calculation of the average manufacturer price of such drug or biological under section 1927(k)(1)(B)(i)(IX). .\n#### 4. Guidance on value-based purchasing arrangements for inpatient drugs under Medicaid\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Health and Human Services shall issue guidance to State Medicaid agencies on the option of entering into a value-based purchasing arrangement (as defined in section 1927(k)(12) of the Social Security Act ( 42 U.S.C. 1396r\u20138(k)(12) )) with manufacturers for drugs or biological products provided as part of, or as incident to and in the same setting as, inpatient hospital services furnished under a State plan under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ), or under a waiver of such plan, where such drugs or biological products are reimbursed directly and not paid for as part of payment for such inpatient hospital services, including guidance on how multiple States may enter into agreements with one another and with manufacturers which permit the transfer of funds between the participating States so that individuals who reside in a State different from the State in which they receive a drug subject to a value-based purchasing arrangement as an inpatient may be treated as if they received such drug in the State in which they reside.\n#### 5. Exception under the antikickback statute\n##### (a) In general\nSection 1128B(b)(3) of the Social Security Act (42 U.S.C. 1320a\u20137b(b)(3)) is amended\u2014\n**(1)**\nin subparagraph (J), by moving the left margin of such subparagraph 2 ems to the left;\n**(2)**\nin subparagraph (K)\u2014\n**(A)**\nby moving the left margin of such subparagraph 2 ems to the left; and\n**(B)**\nby striking and at the end;\n**(3)**\nin subparagraph (L)(iii), by striking the period and inserting ; and ; and\n**(4)**\nby adding at the end the following new subparagraph:\n(M) any remuneration provided by a manufacturer or third party on behalf of a manufacturer to a State under a value-based purchasing arrangement (as defined in section 1927(k)(12)) under a State plan under title XIX (or waiver of such plan) in the case a patient fails to achieve outcomes or measures defined in such arrangement following the administration of a covered outpatient drug (as defined in section 1927(k)(2)). .\n##### (b) Rulemaking\nNot later than 180 days after the date of the enactment of this Act, the Inspector General of the Department of Health and Human Services shall through rulemaking implement the amendments made by this section.\n#### 6. GAO study and report on use of value-based purchasing arrangements\n##### (a) Study\nThe Comptroller General of the United States shall conduct a study on the extent to which value-based purchasing arrangements (as defined in section 1927(k)(12) of the Social Security Act ( 42 U.S.C. 1396r\u20138(k)(12) )) facilitate patient access to covered outpatient drugs, improve patient outcomes, lower overall health system costs, and lower costs for patients in Federal health care programs. In conducting such study, the Comptroller General shall\u2014\n**(1)**\nstudy the impact of this Act on\u2014\n**(A)**\naccess to transformative therapies, including rare disease gene therapies, generally;\n**(B)**\nmitigating socioeconomic disparities in accessing covered outpatient drugs sold under value-based purchasing arrangements through its requirement that State Medicaid programs have access to the same value-based purchasing arrangement pricing structure that are available in the commercial market for such drugs;\n**(C)**\nthe Medicaid drug rebate program under section 1927 of the Social Security Act ( 42 U.S.C. 1396r\u20138 ), the 340B drug pricing program under section 340B of the Public Health Service Act ( 42 U.S.C. 256b ), and part B of title XVIII of the Social Security Act ( 42 U.S.C. 1395j et seq. ), including compliance with such programs;\n**(D)**\nexpenditures under State Medicaid programs; and\n**(E)**\nprices for such drugs under the Medicaid program in States that do not enter into such arrangements;\n**(2)**\nanalyze all the types of value-based purchasing arrangement pricing structures, which structures are working well (as measured by price and ease of implementing), and which need improvement; and\n**(3)**\nstudy the potential long-term savings for States that enter into such arrangements under State Medicaid programs.\n##### (b) Report\nNot later than June 30, 2029, the Comptroller General of the United States shall submit to Congress a report containing the results of the study conducted under subsection (a).",
      "versionDate": "2026-03-09",
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
        "actionDate": "2025-05-07",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1637",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "MVP Act",
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
        "updateDate": "2026-03-11T14:46:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-09",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr7871",
          "measure-number": "7871",
          "measure-type": "hr",
          "orig-publish-date": "2026-03-09",
          "originChamber": "HOUSE",
          "update-date": "2026-03-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7871v00",
            "update-date": "2026-03-30"
          },
          "action-date": "2026-03-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Medicaid VBPs for Patients Act or the MVP Act</strong></p><p>This bill provides statutory authority for regulations that allow for the use of varying best price points under value-based purchasing arrangements for purposes of the Medicaid Drug Rebate Program. (<em>Value-based purchasing arrangements </em>refer to arrangements in which the price of a drug is linked to clinical outcomes; such arrangements are particularly used for new high-cost treatments, such as gene therapies.)</p><p>The Government Accountability Office must study the impact of value-based purchasing arrangements on federal health care programs, including with respect to the bill's changes.</p><p>Additionally, the bill (1) exempts sales of drugs that are made under value-based purchasing arrangements from calculations of the manufacturer average sales price for purposes of payments under Medicare medical services, if the manufacturer reports multiple best prices under Medicaid in accordance with the bill's changes; and (2) requires the Centers for Medicare & Medicaid Services to issue guidance on how\u00a0state Medicaid programs may cover drugs in inpatient settings via value-based purchasing arrangements.</p><p></p>"
        },
        "title": "MVP Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7871.xml",
    "summary": {
      "actionDate": "2026-03-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Medicaid VBPs for Patients Act or the MVP Act</strong></p><p>This bill provides statutory authority for regulations that allow for the use of varying best price points under value-based purchasing arrangements for purposes of the Medicaid Drug Rebate Program. (<em>Value-based purchasing arrangements </em>refer to arrangements in which the price of a drug is linked to clinical outcomes; such arrangements are particularly used for new high-cost treatments, such as gene therapies.)</p><p>The Government Accountability Office must study the impact of value-based purchasing arrangements on federal health care programs, including with respect to the bill's changes.</p><p>Additionally, the bill (1) exempts sales of drugs that are made under value-based purchasing arrangements from calculations of the manufacturer average sales price for purposes of payments under Medicare medical services, if the manufacturer reports multiple best prices under Medicaid in accordance with the bill's changes; and (2) requires the Centers for Medicare & Medicaid Services to issue guidance on how\u00a0state Medicaid programs may cover drugs in inpatient settings via value-based purchasing arrangements.</p><p></p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119hr7871"
    },
    "title": "MVP Act"
  },
  "summaries": [
    {
      "actionDate": "2026-03-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Medicaid VBPs for Patients Act or the MVP Act</strong></p><p>This bill provides statutory authority for regulations that allow for the use of varying best price points under value-based purchasing arrangements for purposes of the Medicaid Drug Rebate Program. (<em>Value-based purchasing arrangements </em>refer to arrangements in which the price of a drug is linked to clinical outcomes; such arrangements are particularly used for new high-cost treatments, such as gene therapies.)</p><p>The Government Accountability Office must study the impact of value-based purchasing arrangements on federal health care programs, including with respect to the bill's changes.</p><p>Additionally, the bill (1) exempts sales of drugs that are made under value-based purchasing arrangements from calculations of the manufacturer average sales price for purposes of payments under Medicare medical services, if the manufacturer reports multiple best prices under Medicaid in accordance with the bill's changes; and (2) requires the Centers for Medicare & Medicaid Services to issue guidance on how\u00a0state Medicaid programs may cover drugs in inpatient settings via value-based purchasing arrangements.</p><p></p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119hr7871"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7871ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MVP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-10T08:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Medicaid VBPs for Patients Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-10T08:23:22Z"
    },
    {
      "title": "MVP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-10T08:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to codify value-based purchasing arrangements under the Medicaid program and reforms related to price reporting under such arrangements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-10T08:18:29Z"
    }
  ]
}
```
