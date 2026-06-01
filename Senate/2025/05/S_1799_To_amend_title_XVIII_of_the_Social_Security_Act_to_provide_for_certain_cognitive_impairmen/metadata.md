# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1799?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1799
- Title: A bill to amend title XVIII of the Social Security Act to provide for certain cognitive impairment detection in the Medicare annual wellness visit and initial preventative physical examination.
- Congress: 119
- Bill type: S
- Bill number: 1799
- Origin chamber: Senate
- Introduced date: 2025-05-19
- Update date: 2025-12-04T11:56:26Z
- Update date including text: 2025-12-04T11:56:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-19: Introduced in Senate
- 2025-05-19 - IntroReferral: Introduced in Senate
- 2025-05-19 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-19: Introduced in Senate

## Actions

- 2025-05-19 - IntroReferral: Introduced in Senate
- 2025-05-19 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-19",
    "latestAction": {
      "actionDate": "2025-05-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1799",
    "number": "1799",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001047",
        "district": "",
        "firstName": "Shelley",
        "fullName": "Sen. Capito, Shelley Moore [R-WV]",
        "lastName": "Capito",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "A bill to amend title XVIII of the Social Security Act to provide for certain cognitive impairment detection in the Medicare annual wellness visit and initial preventative physical examination.",
    "type": "S",
    "updateDate": "2025-12-04T11:56:26Z",
    "updateDateIncludingText": "2025-12-04T11:56:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-19",
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
      "actionDate": "2025-05-19",
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
          "date": "2025-05-19T20:35:45Z",
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "VA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1799is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1799\nIN THE SENATE OF THE UNITED STATES\nMay 19, 2025 Mrs. Capito (for herself and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to provide for certain cognitive impairment detection in the Medicare annual wellness visit and initial preventive physical examination.\n#### 1. Findings\nCongress finds the following:\n**(1)**\nIt is estimated that 6,900,000 Americans are living with Alzheimer\u2019s disease, a number that is estimated to rise to nearly 13,800,000 by 2060. About 1 in 11 people age 65 and older has Alzheimer\u2019s disease.\n**(2)**\nOlder Black Americans are 2 times as likely, and Latino Americans are 1.5 times as likely, to have Alzheimer\u2019s disease than older White Americans. Nearly 2/3 of Americans with Alzheimer\u2019s disease are women.\n**(3)**\nAlzheimer\u2019s disease is the fifth-leading cause of death in America among Americans aged 65 and older.\n**(4)**\nBetween 2000 and 2021, deaths from stroke, heart disease, and HIV decreased, whereas reported deaths from Alzheimer's disease increased more than 140 percent.\n**(5)**\nAddressing modifiable risk factors for Alzheimer\u2019s disease and other dementias, such as hypertension, physical inactivity, smoking, depression, diabetes, obesity, and poor nutrition, might prevent or delay up to 40 percent of dementia cases. In 2021, the National Plan to Addresses Alzheimer\u2019s Disease issued by the Secretary of Health and Human Services under the National Alzheimer's Project Act ( Public Law 111\u2013375 ) was updated to include a new goal to focus on reducing the risk of developing dementia.\n**(6)**\nAn early, documented diagnosis, communicated to the patient and caregiver, enables early access to care planning services and available medical and nonmedical treatments, and optimizes an individual's ability to build a care team, participate in support services, and enroll in clinical trials.\n**(7)**\nAlzheimer\u2019s disease exacts an emotional and physical toll on caregivers, resulting in higher incidence of heart disease, cancer, depression, and other health consequences.\n**(8)**\nIn 2023, more than 11,500,000 Americans provided nearly $347,000,000,000 in unpaid care for individuals with Alzheimer\u2019s disease or other dementias.\n**(9)**\nIn 2024, it is estimated that Alzheimer\u2019s and related dementias will cost the United States $360,000,000,000, not including the value of unpaid caregiving. By 2050, it is estimated that these direct costs will increase to nearly $1,100,000,000,000.\n**(10)**\nMedicare and Medicaid are expected to cover nearly $231,000,000,000 of care for individuals with Alzheimer's disease and related dementias, only about 64 percent of the total healthcare and long-term care payments for individuals with Alzheimer's disease and related dementias. Out-of-pocket spending for such care is expected to be about $91,000,000,000, or about 25 percent of total healthcare and long-term care payments for such individuals.\n#### 2. Cognitive impairment detection benefit in the Medicare annual wellness visit and initial preventive physical examination\n##### (a) Annual wellness visit\n**(1) In general**\nSection 1861(hhh)(2) of the Social Security Act ( 42 U.S.C. 1395x(hhh)(2) ) is amended by striking subparagraph (D) and inserting the following:\n(D) Detection of any cognitive impairment that shall\u2014 (i) be performed using 1 of the cognitive impairment detection tools identified by the National Institute on Aging as meeting its criteria for selecting instruments to detect cognitive impairment in the primary care setting; and (ii) include documentation of the tool used for detecting cognitive impairment and results of the assessment in the individual\u2019s medical record. .\n**(2) Effective date**\nThe amendment made by paragraph (1) shall apply to annual wellness visits furnished on or after January 1, 2026.\n##### (b) Initial preventive physical examination\n**(1) In general**\nSection 1861(ww)(1) of the Social Security Act ( 42 U.S.C. 1395x(ww)(1) ) is amended by striking agreement with the individual, and and inserting agreement with the individual, detection of any cognitive impairment as described in subsection (hhh)(2)(D), and .\n**(2) Effective date**\nThe amendment made by paragraph (1) shall apply to initial preventive physical examinations furnished on or after January 1, 2026.",
      "versionDate": "2025-05-19",
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
        "actionDate": "2025-05-19",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3501",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend title XVIII of the Social Security Act to provide for certain cognitive impairment detection in the Medicare annual wellness visit and initial preventive physical examination.",
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
        "updateDate": "2025-06-03T12:58:23Z"
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
      "date": "2025-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1799is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to provide for certain cognitive impairment detection in the Medicare annual wellness visit and initial preventative physical examination.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:33:26Z"
    },
    {
      "title": "A bill to amend title XVIII of the Social Security Act to provide for certain cognitive impairment detection in the Medicare annual wellness visit and initial preventative physical examination.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T10:56:15Z"
    }
  ]
}
```
