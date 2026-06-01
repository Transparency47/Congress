# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2496?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2496
- Title: Keep Kids Covered Act
- Congress: 119
- Bill type: S
- Bill number: 2496
- Origin chamber: Senate
- Introduced date: 2025-07-29
- Update date: 2025-12-05T22:53:34Z
- Update date including text: 2025-12-05T22:53:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in Senate
- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-07-29: Introduced in Senate

## Actions

- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2496",
    "number": "2496",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001267",
        "district": "",
        "firstName": "Michael",
        "fullName": "Sen. Bennet, Michael F. [D-CO]",
        "lastName": "Bennet",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Keep Kids Covered Act",
    "type": "S",
    "updateDate": "2025-12-05T22:53:34Z",
    "updateDateIncludingText": "2025-12-05T22:53:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-29",
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
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T15:28:06Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2496is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2496\nIN THE SENATE OF THE UNITED STATES\nJuly 29, 2025 Mr. Bennet introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend titles XIX and XXI of the Social Security Act to provide for continuous eligibility for certain children under the Medicaid program and the Children\u2019s Health Insurance Program.\n#### 1. Short title\nThis Act may be cited as the Keep Kids Covered Act .\n#### 2. Requiring States to provide for continuous eligibility for children under Medicaid and CHIP\n##### (a) Continuous eligibility for deemed newborns until age 6\n**(1) Medicaid**\nSection 1902(e)(4) of the Social Security Act ( 42 U.S.C. 1396a(e)(4) ) is amended by striking one year and inserting 6 years .\n**(2) CHIP**\nSection 2112(e) of the Social Security Act ( 42 U.S.C. 1397ll(e) ) is amended by striking 1 year of age and inserting 6 years of age (except that such a child who is enrolled under the State child health plan or waiver may be transferred to the Medicaid program under title XIX for the remaining duration of the 6-year continuous eligibility period, if the child becomes eligible for full benefits under title XIX during such period) .\n##### (b) Continuous eligibility for children under age 19 and former foster youth\n**(1) Medicaid**\nSection 1902(e)(12) of the Social Security Act ( 42 U.S.C. 1396a(e)(12) ) is amended\u2014\n**(A)**\nin the paragraph heading, by striking 1 year of continuous and inserting Continuous ;\n**(B)**\nin the text preceding subparagraph (A), by inserting has attained the age of 6 and after an individual who ;\n**(C)**\nin subparagraph (A), by striking the 12-month period and inserting the 24-month period ;\n**(D)**\nby redesignating subparagraphs (A) through (C) as clauses (i) through (iii), respectively, and adjusting the margins accordingly;\n**(E)**\nby striking The State plan and inserting:\n(A) Children under age 6 The State plan (or waiver of such State plan) shall provide that an individual who is under the age of 6 and who is determined to be eligible for benefits under a State plan (or waiver of such plan) approved under this title under subsection (a)(10)(A) shall remain eligible for such benefits until the earlier of\u2014 (i) the time that such individual attains the age of 6; or (ii) the date that such individual ceases to be a resident of such State. (B) Children ages 6 through 18 The State plan ; and\n**(F)**\nby adding at the end the following new subparagraph:\n(C) Former foster youth The State plan (or waiver of such State plan) shall provide that an individual who is determined to be eligible for benefits under a State plan (or waiver of such plan) approved under this title under subsection (a)(10)(A)(i)(IX) shall remain eligible for such benefits until the earlier of\u2014 (i) the time that such individual attains the age of 26; or (ii) the date that such individual ceases to be a resident of such State. .\n**(2) CHIP**\nSection 2107(e)(1)(L) of the Social Security Act ( 42 U.S.C. 1397gg(e)(1)(L) ), as redesignated by section 71103(b)(1) of Public Law 119\u201321 , is amended\u2014\n**(A)**\nby striking 1 year of ; and\n**(B)**\nby striking 12-month and inserting applicable .\n##### (c) Updating contact information during continuous eligibility period\n**(1) Medicaid**\nSection 1902(a) of the Social Security Act ( 42 U.S.C. 1396a(a) ), as amended by sections 71103(a)(1) and 71104 of Public Law 119\u201321 , is amended\u2014\n**(A)**\nin paragraph (88), by striking and at the end;\n**(B)**\nin paragraph (89), by striking the period at the end and inserting ; and ; and\n**(C)**\nby inserting after paragraph (89) the following new paragraph:\n(90) provide for a process\u2014 (A) to obtain, not less frequently than annually, the up-to-date contact information for individuals enrolled under such plan (or a waiver of such plan) who have been so enrolled for a period of longer than 12 months pursuant to a continuous eligibility provision under this title; and (B) to inform each such individual of their enrollment under such plan (or waiver) pursuant to such continuous eligibility provision and of the remaining duration of the applicable period of continuous eligibility. .\n**(2) CHIP**\nSection 2107(e)(1) of the Social Security Act ( 42 U.S.C. 1397gg(e)(1) ), as redesignated by sections 71103(b)(1) and 71109(b) of Public Law 119\u201321 , is amended\u2014\n**(A)**\nby redesignating subparagraphs (I) through (W) as subparagraphs (J) through (X), respectively; and\n**(B)**\nby inserting after subparagraph (H) the following new subparagraph:\n(I) Section 1902(a)(90) (relating to the verification of contact information and provision of information regarding enrollment during a period of continuous eligibility). .\n##### (d) Effective date\nThe amendments made by this section shall take effect on the date that is 1 year after the date of the enactment of this section.\n#### 3. Adjusting application of provision providing coverage continuity for former foster children up to age 26 under Medicaid\nSection 1002(a)(2) of the SUPPORT for Patients and Communities Act ( 42 U.S.C. 1396a note) is amended by striking shall take effect with respect to and all that follows through the period at the end and inserting the following:\nshall apply\u2014 (A) beginning January 1, 2023, with respect to foster youth who attain 18 years of age on or after such date; and (B) beginning on the date that is 180 days after the date of enactment of the Keep Kids Covered Act, with respect to foster youth not described in subparagraph (A). .",
      "versionDate": "2025-07-31",
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
        "actionDate": "2025-07-23",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "4641",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Keep Kids Covered Act",
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
        "updateDate": "2025-09-17T16:42:31Z"
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
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2496is.xml"
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
      "title": "Keep Kids Covered Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Keep Kids Covered Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend titles XIX and XXI of the Social Security Act to provide for continuous eligibility for certain children under the Medicaid program and the Children's Health Insurance Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:41Z"
    }
  ]
}
```
