# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3549?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3549
- Title: PBM FAIR Act
- Congress: 119
- Bill type: S
- Bill number: 3549
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-01-26T13:57:50Z
- Update date including text: 2026-01-26T13:57:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3549",
    "number": "3549",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "PBM FAIR Act",
    "type": "S",
    "updateDate": "2026-01-26T13:57:50Z",
    "updateDateIncludingText": "2026-01-26T13:57:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T22:07:28Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "sponsorshipDate": "2025-12-17",
      "state": "VA"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "IA"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3549is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3549\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Mr. Marshall (for himself, Mr. Kaine , Mr. Grassley , and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Employee Retirement Income Security Act of 1974 to ensure that pharmacy benefit managers are considered fiduciaries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the PBM Fiduciary Accountability, Integrity, and Reform (FAIR) Act or the PBM FAIR Act .\n#### 2. Establishing fiduciary duties of pharmacy benefit managers\n##### (a) Deeming pharmacy benefit managers as ERISA fiduciaries\nSection 3(21) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1002(21) ) is amended by adding at the end the following:\n(C) A person or entity shall be deemed to be a fiduciary with respect to a group health plan for the purposes of this Act if the person or entity\u2014 (i) maintains for the group health plan, the plan sponsor or plan administrator of such plan, or a health insurance issuer offering group health insurance coverage a prescription drug provider network or prescription drug formulary through the purchase of prescription drugs from a drug manufacturer, distributor, wholesaler, rebate aggregator, group purchasing organization, or any associated third party; or (ii) engages in, on behalf of, or in connection with, the group health plan, the plan sponsor or plan administrator of such plan, or a health insurance issuer offering group health insurance coverage\u2014 (I) the negotiation or aggregation of rebates, fees, discounts, or other price concessions for prescription drugs; (II) the processing and payment of claims for prescription drugs; or (III) the performance of utilization review and management for prescription drugs on behalf of a group health plan. .\n##### (b) Required compensation disclosures from pharmacy benefit managers and third party administrators\nSection 408(b)(2)(B)(ii)(I)(bb) of the Employee Retirement Income Security Act of 1974 (29 U.S.C. 1108(b)(2)(B)(ii)(I)(bb)) is amended by adding at the end the following:\n(CC) Pharmacy benefit management services provided to a covered plan, for which the covered service provider, an affiliate, or a subcontractor reasonably expects to receive indirect compensation or direct compensation described in item (dd), including the establishment and maintenance of a prescription drug provider network or prescription drug formulary or through the purchase of prescription drugs from a drug manufacturer, distributor, wholesaler, rebate aggregator, group purchasing organization, or any associated third party for the covered plan. (DD) Third party administrative services provided to a covered plan, for which the covered service provider, an affiliate, or a subcontractor reasonably expects to receive indirect compensation or direct compensation described in item (dd), including establishing and maintaining a network of medical providers, adjudicating or processing health claims, maintaining records, and negotiating reimbursement rates for the covered plan. .\n##### (c) Clarification of responsible plan fiduciary\nSection 408(b)(2)(B)(ii)(I)(ee) of the Employee Retirement Income Security Act of 1974 (29 U.S.C. 1108(b)(2)(B)(ii)(I)(ee)) is amended by inserting at the end the following: A covered service provider may not be the responsible plan fiduciary for purposes of the disclosures required under clause (iii). Notwithstanding the preceding sentence, in the case of a pharmacy benefit manager who sponsors a covered plan for the employees of the pharmacy benefit manager, the pharmacy benefit manager may be considered the responsible plan fiduciary for such plan. .\n##### (d) Prohibition on indemnification for breaches by a section 3(21)(C) fiduciary\nSection 410(a) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1110(a) ) is amended\u2014\n**(1)**\nby striking Except and inserting (1) Except ; and\n**(2)**\nby adding at the end the following:\n(2) Except as provided in subsection (b)(2), no person or entity deemed to be a fiduciary under section 3(21)(C) may be indemnified, directly or indirectly, or otherwise relieved from liability for any responsibility, obligation, or duty of such person or entity under this part. (3) Any provision of contract in violation of paragraph (2) shall be void as against public policy. .\n##### (e) Technical amendment\nSection 408(b)(2)(B)(i) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1108(b)(2)(B)(i) ) is amended by striking this clause and inserting this subparagraph .\n##### (f) Effective date\nThe amendments made by this section shall apply with respect to plan years beginning with the first plan year that begins at least 12 months after the date of enactment of this Act.",
      "versionDate": "2025-12-17",
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
        "actionDate": "2025-12-18",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "6837",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend the Employee Retirement Income Security Act of 1974 to ensure that pharmacy benefit managers are considered fiduciaries, and for other purposes.",
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
        "updateDate": "2026-01-26T13:57:50Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3549is.xml"
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
      "title": "PBM FAIR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-22T03:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PBM FAIR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-22T03:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PBM Fiduciary Accountability, Integrity, and Reform (FAIR) Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-22T03:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Employee Retirement Income Security Act of 1974 to ensure that pharmacy benefit managers are considered fiduciaries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-22T03:33:19Z"
    }
  ]
}
```
