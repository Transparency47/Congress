# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1753?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1753
- Title: End Price Gouging for Medications Act
- Congress: 119
- Bill type: S
- Bill number: 1753
- Origin chamber: Senate
- Introduced date: 2025-05-14
- Update date: 2025-12-05T21:45:57Z
- Update date including text: 2026-05-30T16:27:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in Senate
- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-05-14: Introduced in Senate

## Actions

- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1753",
    "number": "1753",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "End Price Gouging for Medications Act",
    "type": "S",
    "updateDate": "2025-12-05T21:45:57Z",
    "updateDateIncludingText": "2026-05-30T16:27:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-14",
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
      "actionDate": "2025-05-14",
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
          "date": "2025-05-14T16:15:40Z",
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
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "VT"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-05-14",
      "state": "VT"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1753is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1753\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2025 Mr. Merkley (for himself, Mr. Welch , Mr. Sanders , and Mr. Durbin ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo require the Secretary of Health and Human Services to establish reference prices for prescription drugs for purposes of Federal health programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the End Price Gouging for Medications Act .\n#### 2. Reference prices for prescription drugs\n##### (a) Reference prices\nThe Secretary of Health and Human Services (referred to in this section as the Secretary ), in accordance with subsection (b), shall establish annual reference prices for each prescription drug. Notwithstanding any other provision of law, with respect to enrollees or beneficiaries in any of the Federal health programs described in subsection (c), the retail list price for a drug shall not exceed the reference price for such drug.\n##### (b) Criteria\n**(1) In general**\nEach year, the Secretary shall establish the reference price for each prescription drug under subsection (a)\u2014\n**(A)**\nby determining the lowest retail list price for the drug among the reference countries in which the drug is available, if drug pricing information is available for at least 3 of such countries; or\n**(B)**\nin the case of a drug for which drug pricing information or dosage equivalents are not available for at least 3 of the reference countries, by determining an appropriate price based on the Secretary's determination of\u2014\n**(i)**\nthe added therapeutic effect of the drug;\n**(ii)**\nthe value of the drug;\n**(iii)**\npatient access to the drug;\n**(iv)**\nthe costs associated with researching and developing the drug; and\n**(v)**\nother factors, as the Secretary determines appropriate.\n**(2) Reference countries**\nFor purposes of paragraph (1), the reference countries are Australia, Austria, Belgium, Canada, France, Germany, Italy, Japan, the Netherlands, Sweden, Switzerland, and the United Kingdom.\n##### (c) Federal health programs\nThe reference prices established under subsection (a) shall apply with respect to covered inpatient and outpatient drugs under\u2014\n**(1)**\nthe Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. );\n**(2)**\na State Medicaid plan under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. );\n**(3)**\nthe State Children's Health Insurance Program under title XXI of the Social Security Act ( 42 U.S.C. 1397aa et seq. );\n**(4)**\nthe TRICARE program under chapter 55 of title 10, United States Code;\n**(5)**\nhospital care and medical services furnished by the Department of Veterans Affairs under chapters 17 and 18 of title 38, United States Code;\n**(6)**\nthe Federal Employees Health Benefits Program established under chapter 89 of title 5, United States Code; and\n**(7)**\nany health program, service, function, activity, or facility funded, in whole or part, under the Indian Health Care Improvement Act ( 25 U.S.C. 1601 et seq. ), including through direct or contract care provided under such Act or through a contract or compact under the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 et seq. ).\n##### (d) Applicability to other purchasers of drugs\nNotwithstanding any other provision of law, a drug manufacturer shall offer prescription drugs at the reference price to all individuals, including individuals who are not insured and individuals who are covered under a group health plan or group or individual health insurance coverage. In the case of individuals covered by a group health plan or group or individual health insurance coverage, such requirement is met if the amount covered under such plan or coverage plus the cost-sharing amount does not exceed the reference price.\n##### (e) Enforcement\n**(1) Civil penalty**\nA drug manufacturer who does not comply with the requirements of subsection (a) shall be subject to a civil penalty, for each year in which the violation occurs and with respect to each drug for which the violation occurs, in an amount equal to 5 times the difference between\u2014\n**(A)**\nthe total amount received by the manufacturer for sales of the drug under the Federal health programs under subsection (c) for the year; less\n**(B)**\nthe total amount the manufacturer would have received for sales of the drug under such programs for the year if the manufacturer had complied with subsection (a).\n**(2) Amounts collected**\nEach year, the Secretary of the Treasury shall transfer to the Director of the National Institutes of Health an amount equal to the amount collected in civil penalties under subsection (e) for the previous year. The Director of the National Institutes of Health shall use amounts so transferred for purposes of conducting drug research and development.\n##### (f) Applicability to brand and generic drugs\nThe reference price established under subsection (a) shall apply to drugs approved under subsection (c) or (j) of section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) or under subsection (a) or (k) of section 351 of the Public Health Service Act ( 42 U.S.C. 262 ).",
      "versionDate": "2025-05-14",
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
        "actionDate": "2025-07-02",
        "text": "Referred to the Subcommittee on Health."
      },
      "number": "3391",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "End Price Gouging for Medications Act",
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
        "updateDate": "2025-06-10T15:03:05Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1753is.xml"
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
      "title": "End Price Gouging for Medications Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T04:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "End Price Gouging for Medications Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T04:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Health and Human Services to establish reference prices for prescription drugs for purposes of Federal health programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T04:03:52Z"
    }
  ]
}
```
