# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1971?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1971
- Title: Nutrition CARE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1971
- Origin chamber: Senate
- Introduced date: 2025-06-05
- Update date: 2026-01-21T05:12:00Z
- Update date including text: 2026-01-21T05:12:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-05: Introduced in Senate
- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-05: Introduced in Senate

## Actions

- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1971",
    "number": "1971",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001076",
        "district": "",
        "firstName": "Maggie",
        "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
        "lastName": "Hassan",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Nutrition CARE Act of 2025",
    "type": "S",
    "updateDate": "2026-01-21T05:12:00Z",
    "updateDateIncludingText": "2026-01-21T05:12:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-05",
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
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T17:09:25Z",
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
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "AK"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "MN"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1971is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1971\nIN THE SENATE OF THE UNITED STATES\nJune 5, 2025 Ms. Hassan (for herself, Ms. Murkowski , Ms. Klobuchar , and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to provide coverage of medical nutrition therapy services for individuals with eating disorders under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Nutrition Counseling Aiding Recovery for Eating Disorders Act of 2025 or the Nutrition CARE Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\n28,800,000 individuals in the United Sates, or 9 percent of the national population, will have an eating disorder in their lifetime. It is estimated that 1,619,300 to 2,080,600 individuals on Medicare part B are affected by an eating disorder, including 420,500 to 560,700 beneficiaries who identify as Black, Indigenous, or People of Color.\n**(2)**\n10,200 deaths per year in the United States occur as a direct result of an eating disorder, equating to 1 death every 52 minutes. Eating disorders have one of the highest mortality rates of all mental illness due to serious medical comorbidities such as stroke, diabetes, and gastric rupture, in addition to the fact that longitudinal studies have found that the suicide risk for those with an eating disorder is 23 times the expected risk.\n**(3)**\nEating disorders can be successfully treated with care encompassing the 4 pillars of successful treatment: medical, psychiatric, therapy, and medical nutrition therapy. In general, Medicare provides some, but not all, care necessary for eating disorders treatment. It doesn\u2019t cover medical nutrition therapy at the outpatient level and provides no coverage at the intensive outpatient or residential treatment levels.\n**(4)**\nEating disorders are expensive. The yearly economic cost of eating disorders is $64,700,000,000, with families and individuals experiencing an economic loss of $23,500,000,000 per year. Each year, eating disorders are directly responsible for 23,560 inpatient hospitalizations costing $209,700,000 and 53,918 emergency room visits costing $29,300,000.\n**(5)**\nEating disorders in the elderly are particularly serious because chronic disorders or diseases may already compromise a patient\u2019s health and make a patient more prone to serious comorbidities associated with eating disorders, including cardiac, metabolic, gastric, and bone conditions. Early diagnosis and proper treatment of this population is essential.\n#### 3. Providing coverage of medical nutrition therapy services for individuals with eating disorders under the Medicare program\nSection 1861 of the Social Security Act ( 42 U.S.C. 1395x ) is amended\u2014\n**(1)**\nin subsection (s)(2)(V)\u2014\n**(A)**\nby redesignating clauses (i) through (iii) as subclauses (I) through (III), respectively, and adjusting the margins accordingly;\n**(B)**\nin subclause (III), as so redesignated, by striking the semicolon at the end and inserting ; or ;\n**(C)**\nby striking beneficiary with diabetes and inserting the following:\nbeneficiary\u2014 (i) with diabetes ; and\n**(D)**\nby adding at the end the following new clause:\n(ii) beginning January 1, 2026, with an eating disorder (as defined by the Secretary in accordance with most recent edition of the Diagnostic and Statistical Manual of Mental Disorders published by the American Psychiatric Association); ; and\n**(2)**\nin subsection (vv)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby inserting (including management of an eating disorder (as defined for purposes of subsection (s)(2)(V)(ii))) after disease management ; and\n**(ii)**\nby striking which are furnished by and all that follows through the period and inserting \u201cwhich are furnished\u2014\n(A) by a registered dietitian or nutrition professional (as defined in paragraph (2)); (B) pursuant to a referral by\u2014 (i) a physician (as defined in subsection (r)(1)); or (ii) a psychologist (or other mental health professional to the extent authorized under State law); and (C) in the case of such services furnished to an individual for the purpose of management of such an eating disorder, at the times specified in paragraph (4). ; and\n**(B)**\nby adding at the end the following new paragraph:\n(4) (A) For purposes of paragraph (1)(C), the times specified in this paragraph are, with respect to medical nutrition therapy services furnished to an individual for purposes of management of an eating disorder, at least the following: (i) 13 hours (including a 1-hour initial assessment and 12 hours of reassessment and intervention) during the 1-year period beginning on the date such individual is first furnished such services. (ii) Subject to subparagraph (B), 4 hours during each subsequent 1-year period. (B) The Secretary may apply such other reasonable limitations with respect to the furnishing of medical nutrition therapy services for purposes of management of an eating disorder during a period described in subparagraph (A)(ii) as the Secretary determines appropriate. .",
      "versionDate": "2025-06-05",
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
        "actionDate": "2025-03-31",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2495",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Nutrition CARE Act of 2025",
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
        "updateDate": "2025-06-24T13:47:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-05",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s1971",
          "measure-number": "1971",
          "measure-type": "s",
          "orig-publish-date": "2025-06-05",
          "originChamber": "SENATE",
          "update-date": "2025-07-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1971v00",
            "update-date": "2025-07-25"
          },
          "action-date": "2025-06-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Nutrition Counseling Aiding Recovery for Eating Disorders Act of 2025\u00a0or the Nutrition CARE Act of 2025</strong><strong></strong></p><p>This bill provides for Medicare coverage of medical nutrition therapy services for individuals with eating disorders. Such services must be furnished by a registered dietitian or nutrition professional pursuant to a referral from a physician, psychologist, or other authorized mental health professional.</p>"
        },
        "title": "Nutrition CARE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1971.xml",
    "summary": {
      "actionDate": "2025-06-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Nutrition Counseling Aiding Recovery for Eating Disorders Act of 2025\u00a0or the Nutrition CARE Act of 2025</strong><strong></strong></p><p>This bill provides for Medicare coverage of medical nutrition therapy services for individuals with eating disorders. Such services must be furnished by a registered dietitian or nutrition professional pursuant to a referral from a physician, psychologist, or other authorized mental health professional.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s1971"
    },
    "title": "Nutrition CARE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Nutrition Counseling Aiding Recovery for Eating Disorders Act of 2025\u00a0or the Nutrition CARE Act of 2025</strong><strong></strong></p><p>This bill provides for Medicare coverage of medical nutrition therapy services for individuals with eating disorders. Such services must be furnished by a registered dietitian or nutrition professional pursuant to a referral from a physician, psychologist, or other authorized mental health professional.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s1971"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1971is.xml"
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
      "title": "Nutrition CARE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-11T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Nutrition CARE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-11T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Nutrition Counseling Aiding Recovery for Eating Disorders Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-11T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to provide coverage of medical nutrition therapy services for individuals with eating disorders under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-11T03:48:35Z"
    }
  ]
}
```
