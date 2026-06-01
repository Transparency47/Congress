# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1500?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1500
- Title: Access to Breast Cancer Diagnosis Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1500
- Origin chamber: Senate
- Introduced date: 2025-04-28
- Update date: 2026-05-20T11:03:28Z
- Update date including text: 2026-05-20T11:03:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-28: Introduced in Senate
- 2025-04-28 - IntroReferral: Introduced in Senate
- 2025-04-28 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-04-28: Introduced in Senate

## Actions

- 2025-04-28 - IntroReferral: Introduced in Senate
- 2025-04-28 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-28",
    "latestAction": {
      "actionDate": "2025-04-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1500",
    "number": "1500",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Access to Breast Cancer Diagnosis Act of 2025",
    "type": "S",
    "updateDate": "2026-05-20T11:03:28Z",
    "updateDateIncludingText": "2026-05-20T11:03:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-28",
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
      "actionDate": "2025-04-28",
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
            "date": "2025-04-28T22:24:56Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-28T22:24:56Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "AL"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "WV"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "GA"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-10-22",
      "state": "MS"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "CA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "RI"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "NY"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "PA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1500is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1500\nIN THE SENATE OF THE UNITED STATES\nApril 28, 2025 Mrs. Shaheen (for herself, Mrs. Britt , and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend title XXVII of the Public Health Service Act to prohibit group health plans and health insurance issuers offering group or individual health insurance coverage from imposing cost-sharing requirements with respect to diagnostic and supplemental breast examinations.\n#### 1. Short title\nThis Act may be cited as the Access to Breast Cancer Diagnosis Act of 2025 .\n#### 2. Requiring diagnostic and supplemental breast examinations to be covered with no cost-sharing requirements\n##### (a) In general\nSubpart II of part A of title XXVII of the Public Health Service Act ( 42 U.S.C. 300gg\u201311 et seq. ) is amended by adding at the end the following new section:\n2730. Diagnostic and supplemental breast examinations (a) In general In the case of a group health plan, or a health insurance issuer offering group or individual health insurance coverage, that provides benefits with respect to diagnostic and supplemental breast examinations furnished to an individual enrolled under such plan or such coverage, such plan or coverage shall not impose any cost-sharing requirements for these benefits. (b) Construction Nothing in this section shall be construed\u2014 (1) to prohibit a group health plan or health insurance issuer from requiring timely prior authorization or imposing other appropriate utilization controls in approving coverage for any diagnostic and supplemental breast examination; or (2) to supersede a State law that provides greater protections with respect to the coverage of diagnostic and supplemental breast examinations than is provided under this section. (c) Definitions In this section: (1) Cost-sharing requirements The term cost-sharing requirements means a deductible, coinsurance, copayment, and any maximum limitation on the application of such a deductible, coinsurance, copayment or similar out-of-pocket expense. (2) Diagnostic breast examination The term diagnostic breast examination means a medically necessary and appropriate (in accordance with National Comprehensive Cancer Network Guidelines) examination of the breast (including, but not limited to such an examination using diagnostic mammography, breast magnetic resonance imaging, or breast ultrasound) that is\u2014 (A) used to evaluate an abnormality seen or suspected from a screening examination for breast cancer; or (B) used to evaluate an abnormality detected by another means of examination. (3) Supplemental breast examinations The term supplemental breast examination means a medically necessary and appropriate (in accordance with National Comprehensive Cancer Network Guidelines) examination of the breast (including, but not limited to such an examination using breast magnetic resonance imaging or breast ultrasound) that is\u2014 (A) used to screen for breast cancer when there is no abnormality seen or suspected; and (B) furnished based on personal or family medical history or additional factors that may increase the individual\u2019s risk of breast cancer. .\n##### (b) Application to grandfathered health plans\nSection 1251(a)(4)(A) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18011(a)(4)(A) ) is amended\u2014\n**(1)**\nby striking title and inserting title, or as added after the date of the enactment of this Act ; and\n**(2)**\nby adding at the end the following new clause:\n(v) Section 2730 (relating to coverage for diagnostic and supplemental breast examinations). .\n##### (c) Application to high deductible health plans with health savings account eligibility\nSection 223(c)(2) of the Internal Revenue Code of 1986 is amended by adding at the end the following:\n(H) Safe harbor for absence of deductible for diagnostic and supplemental breast examinations In the case of plan years beginning on or after January 1, 2026, a plan shall not fail to be treated as a high deductible health plan by reason of failing to have a deductible for diagnostic and supplemental breast examinations. .\n##### (d) Effective date\nThe amendments made by this section shall apply with respect to plan years beginning on or after January 1, 2026.",
      "versionDate": "2025-04-28",
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
        "actionDate": "2025-04-28",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3037",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Access to Breast Cancer Diagnosis Act of 2025",
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
        "updateDate": "2025-05-21T10:43:11Z"
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
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1500is.xml"
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
      "title": "Access to Breast Cancer Diagnosis Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T11:03:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Access to Breast Cancer Diagnosis Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XXVII of the Public Health Service Act to prohibit group health plans and health insurance issuers offering group or individual health insurance coverage from imposing cost-sharing requirements with respect to diagnostic and supplemental breast examinations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T03:33:23Z"
    }
  ]
}
```
