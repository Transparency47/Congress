# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3159?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3159
- Title: Preserving Patient Access to Long-Term Care Pharmacies Act
- Congress: 119
- Bill type: S
- Bill number: 3159
- Origin chamber: Senate
- Introduced date: 2025-11-07
- Update date: 2026-04-29T11:03:32Z
- Update date including text: 2026-04-29T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in Senate
- 2025-11-07 - IntroReferral: Introduced in Senate
- 2025-11-07 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-11-07: Introduced in Senate

## Actions

- 2025-11-07 - IntroReferral: Introduced in Senate
- 2025-11-07 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3159",
    "number": "3159",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000575",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Lankford, James [R-OK]",
        "lastName": "Lankford",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Preserving Patient Access to Long-Term Care Pharmacies Act",
    "type": "S",
    "updateDate": "2026-04-29T11:03:32Z",
    "updateDateIncludingText": "2026-04-29T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-07",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
            "date": "2025-11-07T20:49:17Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-07T20:49:17Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "OK"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "TN"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "MS"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3159is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3159\nIN THE SENATE OF THE UNITED STATES\nNovember 7, 2025 Mr. Lankford (for himself and Mr. Mullin ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to temporarily provide for long-term care pharmacy supply fees in connection with the dispensing of certain drugs.\n#### 1. Short title\nThis Act may be cited as the Preserving Patient Access to Long-Term Care Pharmacies Act .\n#### 2. Long term care pharmacy supply fee\n##### (a) In general\nSection 1860D\u20134(b)(1) of the Social Security Act ( 42 U.S.C. 1395w\u2013104(b)(1) ) is amended by adding at the end the following new subparagraph:\n(F) Long-term care pharmacy supply fees (i) Plan reimbursement to pharmacy (I) In general For plan years 2026 and 2027, for each specified prescription dispensed by a long-term care pharmacy to an enrollee during such plan year, each PDP sponsor of a prescription drug plan and each MA organization offering an MA\u2013PD plan shall pay such pharmacy a supply fee in an amount equal to\u2014 (aa) for plan year 2026, $30; and (bb) for plan year 2027, the amount of the supply fee for the prior plan year, increased by the annual percentage increase described in section 1860D\u20132(b)(6). (II) Clarification The supply fee under this subparagraph shall be paid at the same time and in addition to any other pharmacy reimbursements, including ingredient costs, dispensing fees, or other payments negotiated between the PDP sponsor or MA organization and the long-term care pharmacy, and shall not result in a reduction to such other reimbursements. (ii) Enforcement (I) Civil money penalty The Secretary shall impose a civil money penalty on each PDP sponsor of a prescription drug plan and MA organization offering an MA\u2013PD plan that fails to pay a supply fee for a specified prescription dispensed to an enrollee in accordance with this subparagraph for each such failure in an amount of not less than $10,000. (II) Application The provisions of section 1128A (other than subsections (a) and (b)) shall apply to a civil money penalty under this clause in the same manner as such provisions apply to a penalty or proceeding under section 1128A(a). (iii) Definitions In this subparagraph: (I) Applicable maximum fair price eligible individual The term applicable maximum fair price eligible individual means, with respect to a specified prescription, a maximum fair price eligible individual who, with respect to such prescription, is described in section 1191(c)(2)(A). (II) Long-term care pharmacy The term long-term care pharmacy means a pharmacy with a national provider identifier associated with taxonomy code 3336L0003X (or a successor code), as maintained by the National Uniform Claim Committee. (III) Maximum fair price The term maximum fair price has the meaning given such term in section 1191(c)(3). (IV) Maximum fair price eligible individual The term maximum fair price eligible individual has the meaning given such term in section 1191(c)(2). (V) Specified prescription The term specified prescription means a covered part D drug dispensed by a long-term care pharmacy to an applicable maximum fair price eligible individual at the maximum fair price pursuant to section 1193(a)(3)(A). .\n##### (b) Repayment of long-Term pharmacy supply fees\nSection 1860D\u201315 of the Social Security Act ( 42 U.S.C. 1395w\u2013115 ) is amended by adding at the end the following new subsection:\n(i) Repayment of long-Term pharmacy supply fees (1) In general In addition to amounts otherwise payable under this section to a PDP sponsor of a prescription drug plan or an MA organization offering an MA\u2013PD plan, for plan years 2026 and 2027, the Secretary shall provide the PDP sponsor or MA organization offering the plan subsidies in an amount equal to the aggregate amount of supply fees paid by such sponsor or organization to long-term care pharmacies pursuant to section 1860D\u20134(b)(1)(F) during the plan year. (2) Timing The Secretary shall provide a subsidy under paragraph (1), as applicable, not later than 18 months following the end of the applicable plan year. .\n##### (c) GAO study and report\n**(1) In general**\nNot later than 12 months after the date of enactment of this section, the Comptroller General of the United States shall complete a study and submit to Congress a report on the economic sustainability of the participation of long-term care pharmacies in the Medicare prescription drug program. Such report shall include\u2014\n**(A)**\nan analysis of\u2014\n**(i)**\npayment to long-term care pharmacies under the Medicare prescription drug program with respect to\u2014\n**(I)**\ningredient costs\u2014\n**(aa)**\nfor brand-name drugs; and\n**(bb)**\nfor generic drugs; and\n**(II)**\ndispensing fees;\n**(ii)**\nthe costs to long-term care pharmacies of compliance with the performance and service criteria for network long-term care pharmacies, as described in the Medicare Prescription Drug Benefit Manual; and\n**(iii)**\nchanges to payment to long-term care pharmacies under the Medicare prescription drug program during the 5-year period preceding the date of enactment of this section; and\n**(B)**\nrecommendations on steps that Congress and the Secretary of Health and Human Services should consider for purposes of creating a sustainable payment system under the Medicare prescription drug program for long-term care pharmacies that would ensure that Medicare beneficiaries with long-term care needs have uninterrupted access to long-term care pharmacy services in all markets, particularly rural markets.\n**(2) Definitions**\nIn this subsection:\n**(A) Long-term care pharmacy**\nThe term long-term care pharmacy has the meaning given such term in subparagraph (F)(iii)(II) of section 1860D\u20134(b)(1) of the Social Security Act ( 42 U.S.C. 1395w\u2013104(b)(1) ), as added by subsection (a).\n**(B) Medicare beneficiary**\nThe term Medicare beneficiary means an individual who is entitled to benefits under part A of title XVIII of the Social Security Act ( 42 U.S.C. 1395c et seq. ) or enrolled under part B of such title ( 42 U.S.C. 1395j et seq. ).\n**(C) Medicare prescription drug program**\nThe term Medicare prescription drug program means the program under part D of title XVIII of the Social Security Act ( 42 U.S.C. 1395w\u2013101 et seq. ).",
      "versionDate": "2025-11-07",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-08-22",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5031",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Preserving Patient Access to Long-Term Care Pharmacies Act",
      "type": "HR"
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
        "updateDate": "2025-11-19T13:28:41Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3159is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Preserving Patient Access to Long-Term Care Pharmacies Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preserving Patient Access to Long-Term Care Pharmacies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-11T06:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to temporarily provide for long-term care pharmacy supply fees in connection with the dispensing of certain drugs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-11T06:48:23Z"
    }
  ]
}
```
