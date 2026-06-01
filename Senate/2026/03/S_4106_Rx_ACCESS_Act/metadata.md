# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4106?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4106
- Title: Rx ACCESS Act
- Congress: 119
- Bill type: S
- Bill number: 4106
- Origin chamber: Senate
- Introduced date: 2026-03-17
- Update date: 2026-04-14T13:39:46Z
- Update date including text: 2026-04-15T06:18:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-17: Introduced in Senate
- 2026-03-17 - IntroReferral: Introduced in Senate
- 2026-03-17 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- 2026-04-13 - Floor: Star Print ordered on the bill.
- Latest action: 2026-03-17: Introduced in Senate

## Actions

- 2026-03-17 - IntroReferral: Introduced in Senate
- 2026-03-17 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- 2026-04-13 - Floor: Star Print ordered on the bill.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-17",
    "latestAction": {
      "actionDate": "2026-03-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4106",
    "number": "4106",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Rx ACCESS Act",
    "type": "S",
    "updateDate": "2026-04-14T13:39:46Z",
    "updateDateIncludingText": "2026-04-15T06:18:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-13",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Star Print ordered on the bill.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": [
          {
            "name": "Judiciary Committee",
            "systemCode": "ssju00"
          },
          {
            "name": "Armed Services Committee",
            "systemCode": "ssas00"
          }
        ]
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-17",
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
        "item": {
          "date": "2026-03-17T15:14:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "VA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "WV"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-04-13",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4106is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4106\nIN THE SENATE OF THE UNITED STATES\nMarch 17, 2026 Mr. Cotton (for himself and Mr. Kaine ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to improve access to certain medications under the TRICARE program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rx Access, Choice, Cost Equity, and Supply Stability Act or the Rx ACCESS Act .\n#### 2. Improvements relating to access, fairness, and transparency under TRICARE pharmacy benefits program\n##### (a) Beneficiary election of prescription refill means\nSection 1074g(a)(9) of title 10, United States Code, is amended\u2014\n**(1)**\nin subparagraph (A), by inserting , and ending on October 1, 2026 after Beginning on October 1, 2015 ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(D) Beginning on October 1, 2026, an eligible covered beneficiary may elect to receive non-generic prescription maintenance medications through any means described in paragraph (2)(E). .\n##### (b) Pharmacy benefit manager reimbursement standards; independent audits\nSection 1074g of title 10, United States Code, as amended by subsection (a), is further amended\u2014\n**(1)**\nby redesignating subsections (i) and (j) as subsections (j) and (k), respectively; and\n**(2)**\nby inserting after subsection (h) the following new subsection:\n(i) Pharmacy benefit manager reimbursement standards (1) The Secretary of Defense shall ensure that, as a condition of any contract entered into for the administration of the pharmacy benefits program, reimbursement to a retail pharmacy described in subsection (a)(2)(E)(ii) for a pharmaceutical agent provided under such program shall be an amount that is equal to not less than the sum of\u2014 (A) either\u2014 (i) the actual cost to the pharmacy of acquiring such pharmaceutical agent from a wholesaler, or (ii) in the case of a pharmaceutical agent included on the national average drug acquisition cost index published by the Administrator of the Centers for Medicare & Medicaid Services, a proxy amount calculated at a rate that is not lower than the national average acquisition cost for such pharmaceutical agent, as identified on such cost index as of the date of the adjudication of the claim for such reimbursement, and (B) a professional dispensing fee that is equal to the professional dispensing fee paid by the State in which the pharmacy is located under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) for dispensing a prescription drug. (2) The contractor administering the pharmacy benefits program may not impose any fees on a retail pharmacy described in subsection (a)(2)(E)(ii), including point-of-sale fees, retroactive fees, or other indirect or hidden fees. (3) (A) Not less frequently than annually, the Comptroller General of the United States shall\u2014 (i) conduct an audit of\u2014 (I) data reported by the contractor responsible for the administration of the pharmacy benefits program relating to the rates of reimbursement under paragraph (1) and any price concessions; and (II) the adequacy of the retail pharmacy network under the TRICARE program and access by eligible covered beneficiaries to such network, including with respect to continuity of care, geographic accessibility (taking into account factors in addition to travel time to and from a pharmacy, with special consideration for rural and underserved areas), and the extent to which elections by such beneficiaries under subsection (a)(9) reflect personal preference; and (ii) submit the results of such audit to the Committee on Armed Services of the Senate and the Committee on Armed Services of the House of Representatives. (B) The Secretary shall ensure that, as a condition of any contract entered into for the administration of the pharmacy benefits program, the contractor provides the Comptroller General information required to conduct the audit under subparagraph (A). .\n##### (c) Report\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Defense shall submit to the congressional defense committees (as defined in section 101(a)(16) of title 10, United States Code) a plan for the implementation of this section.",
      "versionDate": "2026-03-17",
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
        "actionDate": "2025-12-03",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "6400",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Rx ACCESS Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Accounting and auditing",
            "updateDate": "2026-04-14T13:39:40Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-14T13:39:46Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2026-04-14T13:39:36Z"
          },
          {
            "name": "Military medicine",
            "updateDate": "2026-04-14T13:39:26Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2026-04-14T13:39:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2026-03-31T20:35:27Z"
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
      "date": "2026-03-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4106is.xml"
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
      "title": "Rx ACCESS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rx ACCESS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rx Access, Choice, Cost Equity, and Supply Stability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 10, United States Code, to improve access to certain medications under the TRICARE program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T03:48:28Z"
    }
  ]
}
```
