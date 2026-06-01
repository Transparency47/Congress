# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6400?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6400
- Title: Rx ACCESS Act
- Congress: 119
- Bill type: HR
- Bill number: 6400
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-05-20T08:07:55Z
- Update date including text: 2026-05-20T08:07:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-12-03: Introduced in House

## Actions

- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6400",
    "number": "6400",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Rx ACCESS Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:07:55Z",
    "updateDateIncludingText": "2026-05-20T08:07:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T15:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NH"
    },
    {
      "bioguideId": "L000603",
      "district": "8",
      "firstName": "Morgan",
      "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Luttrell",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "TX"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "PA"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "NC"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "IL"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "NV"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "MD"
    },
    {
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "OH"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "WI"
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
      "sponsorshipDate": "2026-04-21",
      "state": "DC"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "AR"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NY"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "TX"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-15",
      "state": "NY"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6400ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6400\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Mrs. Kiggans of Virginia (for herself, Ms. Goodlander , Mr. Luttrell , and Ms. Houlahan ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to improve access to certain medications under the TRICARE program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rx Access, Choice, Cost Equity, and Supply Stability Act or the Rx ACCESS Act .\n#### 2. Improvements relating to access, fairness, and transparency under TRICARE pharmacy benefits program\n##### (a) Beneficiary election of prescription refill means\nSection 1074g(a)(9) of title 10, United States Code, is amended\u2014\n**(1)**\nin subparagraph (A), by inserting , and ending on October 1, 2026 after Beginning on October 1, 2015 ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(D) Beginning on October 1, 2026, an eligible covered beneficiary may elect to receive non-generic prescription maintenance medications through any means described in paragraph (2)(E). .\n##### (b) Pharmacy benefit manager reimbursement standards; independent audits\nSection 1074g of title 10, United States Code, as amended by subsection (a), is further amended\u2014\n**(1)**\nby redesignating subsections (i) and (j) as subsections (j) and (k), respectively; and\n**(2)**\nby inserting after subsection (h) the following new subsection:\n(i) Pharmacy benefit manager reimbursement standards (1) The Secretary of Defense shall ensure that, as a condition of any contract entered into for the administration of the TRICARE pharmacy benefits program, reimbursement to a TRICARE retail pharmacy described in subsection (a)(2)(E)(ii) for a pharmaceutical agent provided under such program shall be an amount that is at least equal to the sum of\u2014 (A) either\u2014 (i) the actual cost to the pharmacy of acquiring such pharmaceutical agent from a wholesaler, or (ii) in the case of a pharmaceutical agent included on the national average drug acquisition cost index published by the Administrator for the Centers for Medicare and Medicaid Services, a proxy amount calculated at a rate that is not lower than the national average acquisition cost for such pharmaceutical agent, as identified on such cost index as of the date of the adjudication of the claim for such reimbursement, and (B) a professional dispensing fee that is equal to the professional dispensing fee paid by the State in which the pharmacy is located under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) for dispensing a prescription drug. (2) The contractor administering the TRICARE pharmacy benefits program may not impose any fees on a TRICARE retail pharmacy, including point-of-sale fees, retroactive fees, or other indirect or hidden fees. (3) (A) Not less frequently than annually, the Comptroller General of the United States\u2014 (i) shall conduct an audit of\u2014 (I) data reported by the contractor responsible for the administration of the TRICARE pharmacy benefits program relating to the rates of reimbursement under paragraph (1) and any price concessions; and (II) the adequacy of the TRICARE retail pharmacy network and access by eligible covered beneficiaries to such network, including with respect to continuity of care, geographic accessibility (taking into account factors in addition to travel time to and from a pharmacy, with special consideration for rural and underserved areas), and the extent to which elections by such beneficiaries under subsection (a)(9) reflect personal preference; and (ii) submit the results of such audit to the Committees on Armed Services of the House of Representatives and the Senate. (B) The Secretary shall ensure that, as a condition of any contract entered into for the administration of the TRICARE pharmacy benefits program, the contractor provides the Comptroller General information required to conduct the audit under subparagraph (A). .\n##### (c) Report\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Defense shall submit to the congressional defense committees (as defined in section 101(a)(16) of title 10, United States Code) a plan for the implementation of this section.",
      "versionDate": "2025-12-03",
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
        "actionDate": "2026-04-13",
        "text": "Star Print ordered on the bill."
      },
      "number": "4106",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Rx ACCESS Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Accounting and auditing",
            "updateDate": "2026-04-14T13:40:10Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-14T13:40:10Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2026-04-14T13:40:10Z"
          },
          {
            "name": "Military medicine",
            "updateDate": "2026-04-14T13:40:10Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2026-04-14T13:40:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-04T20:33:49Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6400ih.xml"
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
      "title": "Rx ACCESS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T09:23:38Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rx ACCESS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T09:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rx Access, Choice, Cost Equity, and Supply Stability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T09:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 10, United States Code, to improve access to certain medications under the TRICARE program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T09:18:31Z"
    }
  ]
}
```
