# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2066?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2066
- Title: Medicare Transaction Fraud Prevention Act
- Congress: 119
- Bill type: S
- Bill number: 2066
- Origin chamber: Senate
- Introduced date: 2025-06-12
- Update date: 2025-12-05T22:05:51Z
- Update date including text: 2025-12-05T22:05:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in Senate
- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-12: Introduced in Senate

## Actions

- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2066",
    "number": "2066",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Medicare Transaction Fraud Prevention Act",
    "type": "S",
    "updateDate": "2025-12-05T22:05:51Z",
    "updateDateIncludingText": "2025-12-05T22:05:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-12",
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
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T17:53:01Z",
          "name": "Referred To"
        }
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NH"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "MO"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2066is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2066\nIN THE SENATE OF THE UNITED STATES\nJune 12, 2025 Mr. Sheehy (for himself, Ms. Hassan , Mr. Schmitt , and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XI of the Social Security Act to establish a pilot program for testing the use of a predictive risk-scoring algorithm to provide oversight of payments for durable medical equipment and clinical diagnostic laboratory tests under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Medicare Transaction Fraud Prevention Act .\n#### 2. Pilot program testing use of predictive risk-scoring algorithm to provide oversight of payments for durable medical equipment and clinical diagnostic laboratory tests under the Medicare program\nSection 1128K of the Social Security Act ( 42 U.S.C. 1320a\u20137n ) is amended\u2014\n**(1)**\nin the section heading by inserting ; pilot program testing use of predictive risk-scoring algorithm to provide oversight of payments for durable medical equipment and clinical diagnostic laboratory tests under the Medicare program after abuse ; and\n**(2)**\nby adding at the end the following new subsection:\n(d) Pilot program testing use of predictive risk-Scoring algorithm To provide oversight of payments for durable medical equipment and clinical diagnostic laboratory tests under the Medicare program (1) In general The Secretary shall establish a pilot program to test the use of predictive risk-scoring algorithms to provide oversight of relevant transactions (as defined in paragraph (8)(B)). (2) Duration The pilot program shall be conducted for a period of 2 years, beginning not later than January 1, 2026. (3) Scope (A) In general The Secretary shall limit the implementation of the pilot program to relevant transactions involving applicable items or services furnished to applicable beneficiaries (as defined in subparagraph (B)). (B) Applicable beneficiary defined In this subsection, the term applicable beneficiary means an individual who has opted in to\u2014 (i) receive electronic Medicare Summary Notices; and (ii) participate in the pilot program in accordance with subparagraph (C). (C) Voluntary participation An applicable beneficiary may participate in the pilot program on a voluntary basis and may terminate participation at any time. (4) Considerations The Secretary may, for purposes of identifying and calculating the risks of relevant transactions under the pilot program, consider the following factors: (A) The absence of a prior relationship between the beneficiary and a provider of services (as defined in section 1861(u)) or supplier (as defined in section 1861(d)). (B) Aberrant billing patterns for a provider of services or supplier with regards to volume of claims in one particular area. (C) Electronic fund transfer (EFT) changes. (D) Changes in ownership of a provider of services or supplier. (5) Collaboration The Secretary shall work with industry representatives (including suppliers of durable medical equipment) on the development and implementation of the pilot program. (6) Requirements Under the pilot program, the Secretary shall\u2014 (A) adopt a predictive risk-scoring algorithm that would learn from beneficiary data to score relevant transactions from 1 (least risky) to 99 (most risky); (B) prior to implementation of any predictive risk-scoring algorithm adopted under subparagraph (A) under the pilot program\u2014 (i) require sufficient testing, evaluation, and review of such algorithm, taking into consideration Executive Order 14179 (90 Fed. Reg. 8741; relating to removing barriers to American leadership in artificial intelligence); (ii) establish methods for notifying applicable beneficiaries and providers of services and suppliers impacted by the use of the algorithm regarding such usage (including information regarding how beneficiary data is collected and processed under the pilot program to produce a risk score for relevant transactions and the possible implications associated with the use of the algorithm); and (iii) establish methods of communication with the Office of the Inspector General of the Department of Health and Human Service, and the ability to waive or forgo notice to an applicable beneficiary or a provider of services or supplier if appropriate; (C) for any relevant transaction involving an item or service furnished to an applicable beneficiary identified by a predictive risk-scoring algorithm adopted under subparagraph (A) and implemented under subparagraph (B) as having a risk score that exceeds a level of risk specified by the Secretary\u2014 (i) review the relevant transaction to determine whether it should be suspended pending the applicable beneficiary's response under clause (ii); (ii) provide the applicable beneficiary the opportunity, by email or phone call response\u2014 (I) to cure a high-risk score or suspended transaction that the beneficiary believes is based on inaccurate underlying data; and (II) confirm the relevant transaction; and (iii) if, based on the results of the review, the relevant transaction is suspended\u2014 (I) trigger an automatic alert to the applicable beneficiary by electronically sending a Medicare Summary Notice that includes the relevant transaction; (II) require that all subsequent Medicare Summary Notices involving the relevant transaction be sent electronically and in two week intervals for 3 months after the first alert is sent under subclause (I); and (III) include on such Medicare Summary Notices, as determined appropriate by the Secretary, information explaining how the beneficiary may report suspected fraud to relevant law enforcement agencies; and (D) have the authority to determine when a Medicare card must be terminated or a new card issued to prevent fraud and abuse. (7) Clarification Any suspension of an account or transaction under the pilot program shall be based on a human review process, informed through the implementation of the predictive risk-scoring algorithm. (8) Definitions In this subsection: (A) Applicable item or service The term applicable item or service means\u2014 (i) an item of durable medical equipment (as defined in section 1861(n)); and (ii) a clinical diagnostic laboratory test. (B) Relevant transaction The term relevant transaction means a claim for payment for an applicable item or service furnished to an applicable beneficiary, as determined by the Secretary. .",
      "versionDate": "2025-06-12",
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
        "actionDate": "2025-06-12",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3996",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Medicare Transaction Fraud Prevention Act",
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
        "updateDate": "2025-07-14T14:24:25Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2066is.xml"
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
      "title": "Medicare Transaction Fraud Prevention Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-02T01:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Medicare Transaction Fraud Prevention Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XI of the Social Security Act to establish a pilot program for testing the use of a predictive risk-scoring algorithm to provide oversight of payments for durable medical equipment and clinical diagnostic laboratory tests under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-02T01:18:57Z"
    }
  ]
}
```
