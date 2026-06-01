# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3727?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3727
- Title: Putting an N to Learing about Fraud Act
- Congress: 119
- Bill type: S
- Bill number: 3727
- Origin chamber: Senate
- Introduced date: 2026-01-29
- Update date: 2026-02-25T17:18:14Z
- Update date including text: 2026-02-25T17:18:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-29: Introduced in Senate
- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-01-29: Introduced in Senate

## Actions

- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-29",
    "latestAction": {
      "actionDate": "2026-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3727",
    "number": "3727",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Putting an N to Learing about Fraud Act",
    "type": "S",
    "updateDate": "2026-02-25T17:18:14Z",
    "updateDateIncludingText": "2026-02-25T17:18:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-29",
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
      "actionDate": "2026-01-29",
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
          "date": "2026-01-29T17:10:05Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3727is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3727\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2026 Ms. Ernst introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo combat fraud in Federal programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Putting an N to Learing about Fraud Act .\n#### 2. Preventing fraud in child care services\n##### (a) State plan\nSection 658E of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858c ) is amended\u2014\n**(1)**\nin subsection (c)(2), by adding by striking subparagraph (S) and inserting the following:\n(S) Attendance-based billing The plan shall include an assurance that the lead agency will provide payment under this subchapter to a child care provider based on recorded attendance, rather than enrollment alone, in the program of the provider. ; and\n**(2)**\nby adding at the end the following:\n(e) Timing of payment Nothing in this subchapter shall be construed to require a lead agency to make a payment to a child care provider prior to the provision of child care services. The lead agency shall make a payment under this subchapter to such a provider as reimbursement, in a timely manner, and on the basis of the provider's provision of child care services. .\n##### (b) Audits\nSection 658K of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858i ) is amended by adding at the end the following:\n(c) Federal audits Each child care provider that receives a payment under this subchapter shall prepare a record of attendance in the provider's program and of the provider's provision of child care services, and maintain the record for a period of 7 years after the date of preparation of such record. The provider shall make such records available for audits by the Secretary, the Attorney General, and the Comptroller General of the United States. .\n#### 3. Identifying fraud in health care services\n##### (a) Medicare\n**(1) In general**\nThe Secretary of Health and Human Services shall, not later than 60 days after making a determination described in paragraph (2), notify the Inspector General of the Department of Health and Human Services of such determination.\n**(2) Determination**\nA determination described in this paragraph is a determination that\u2014\n**(A)**\nthe aggregate amount paid under the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ) for an item or service or items or services in a zip code and county or county equivalent increased by more than 100 percent in a single year; or\n**(B)**\nthe number of provider of services or suppliers (as those terms are defined under section 1861 of the Social Security Act ( 42 U.S.C. 1395x )) who received payment for items or services furnished under the Medicare program increased in a zip code and county or county equivalent by more than 100 percent in a single year.\n##### (b) Qualified health plans under the American Health Benefit Exchanges\n**(1) In general**\nThe Secretary of Health and Human Services shall, not later than 60 days after making a determination described in paragraph (2), notify the Inspector General of the Department of Health and Human Services of such determination.\n**(2) Determination**\nA determination described in this paragraph is a determination that\u2014\n**(A)**\nthe aggregate amount paid under all qualified health plans offered through the American Health Benefit Exchanges established under sections 1311 and 1321 of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18031 , 18041) for an item or service or items or services in a zip code and county or county equivalent increased by more than 100 percent in a single year; or\n**(B)**\nthe number of providers of services who received payment for items or services under such qualified health plans increased in a zip code and county or county equivalent by more than 100 percent in a single year.\n**(3) Requirement to submit certain information**\nAnnually, each American Health Benefit Exchange established under section 1311 or 1321 of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18031 , 18041) shall collect from each qualified health plan offered through such an Exchange, and submit to the Secretary of Health and Human Services, the information necessary for the Secretary to make a determination described in paragraph (2).\n##### (c) Medicaid and CHIP\n**(1) Medicaid**\nSection 1902 of the Social Security Act ( 42 U.S.C. 1396a ) is amended\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (88), by striking ; and and inserting a semicolon;\n**(ii)**\nin paragraph (89), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding after paragraph (89) the following new paragraph:\n(90) provide that, not later than 60 days after making a determination described in subsection (yy), the State agency shall notify the Secretary and the Inspector General of the Department of Health and Human Services of such determination. ; and\n**(B)**\nby adding at the end the following new subsection:\n(yy) Determination of certain increased payments or providers in a single year For purposes of subsection (a)(90), a determination described in this subsection is a determination that\u2014 (1) the aggregate amount paid under the State plan under this title, or under a waiver of such plan, for an item or service or items or services in a zip code and county or county equivalent increased by more than 100 percent in a single year; or (2) the number of providers of items or services who received payments for items or services furnished in a zip code and county or county equivalent under such State plan or waiver increased by more than 100 percent in a single year. .\n**(2) CHIP**\nSection 2107(e)(1) of the Social Security Act ( 42 U.S.C. 1397gg(e)(1) ) is amended by\u2014\n**(A)**\nredesignating subparagraphs (I) through (W) as subparagraphs (J) through (X), respectively; and\n**(B)**\ninserting after subparagraph (H) the following subparagraph:\n(I) Subsections (a)(90) and (yy) of section 1902 (relating to determination of certain increased payments or providers in a single year and notification to the Secretary and the Inspector General of Health and Human Services). .\n##### (d) Audit by the Inspector General of Health and Human Services\nNot later than 5 years after the date of enactment of this Act, and annually thereafter, the Inspector General of Health and Human Services shall\u2014\n**(1)**\nidentify, based on the results of any notifications received under subsection (a) or (b), or under section 1902(a)(90) of the Social Security Act ( 42 U.S.C. 1396a(a)(90) ) or section 2107(e)(1)(I) of such Act ( 42 U.S.C. 1397gg(e)(1)(I) ), any program or State plan or waiver (in the case of Medicaid and the State Children's Health Insurance Program) under which the aggregate amount paid for an item or service or items or services in a zip code and county or county equivalent or the number of providers of items or services or suppliers, as applicable, who received payments for items or services furnished in a zip code and county or county equivalent increased by at least 400 percent during the preceding 5-year period; and\n**(2)**\naudit any such program, State plan, or waiver.\n##### (e) Effective date\n**(1) Medicare**\nSubsection (a) shall take effect on the date that is 180 days after the date of enactment of this Act.\n**(2) Qualified health plans under the American Health Benefit Exchanges**\nSubsection (b) shall take effect on the date that is 180 days after the date of enactment of this Act.\n**(3) Medicaid and CHIP**\n**(A) In general**\nExcept as provided in subparagraph (B), the amendments made by subsection (c) shall take effect on the date that is 180 days after the date of enactment of this Act.\n**(B) Delay permitted if State legislation required**\nIn the case of a State plan approved under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) or title XXI of such Act ( 42 U.S.C. 1397aa et seq. ) which the Secretary of Health and Human Services determines requires State legislation (other than legislation appropriating funds) in order for the plan to meet the additional requirements imposed by the amendments made by subsection (c), the State plan shall not be regarded as failing to comply with the requirements of such title XIX or XXI (as applicable) solely on the basis of the failure of the plan to meet such additional requirements before the first day of the first calendar quarter beginning after the close of the first regular session of the State legislature that ends after the 1-year period beginning with the date of the enactment of this section. For purposes of the preceding sentence, in the case of a State that has a 2-year legislative session, each year of the session is deemed to be a separate regular session of the State legislature.\n#### 4. Recovering improper payments\n##### (a) Guidance\nThe Director of the Office of Management and Budget shall prescribe guidance to all agencies (as defined in section 551 of title 5, United States Code) to ensure that all improper payments (as defined in section 3351 of title 31, United States Code) are recovered.\n##### (b) Annual Inspector General report\nSection 3353(a)(1) of title 31, United States Code, is amended\u2014\n**(1)**\nin subparagraph (A), by striking and at the end;\n**(2)**\nin subparagraph (B)(iv), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(C) include in each report submitted under subparagraph (B) the amount of improper payments recovered by the executive agency in the fiscal year covered by the report. .",
      "versionDate": "2026-01-29",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-02-25T17:18:14Z"
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
      "date": "2026-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3727is.xml"
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
      "title": "Putting an N to Learing about Fraud Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-20T11:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Putting an N to Learing about Fraud Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-20T11:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to combat fraud in Federal programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-20T11:03:25Z"
    }
  ]
}
```
