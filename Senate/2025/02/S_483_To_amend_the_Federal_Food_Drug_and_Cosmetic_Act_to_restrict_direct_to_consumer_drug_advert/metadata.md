# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/483?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/483
- Title: Responsibility in Drug Advertising Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 483
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2026-01-21T06:25:39Z
- Update date including text: 2026-01-21T06:25:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/483",
    "number": "483",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000383",
        "district": "",
        "firstName": "Angus",
        "fullName": "Sen. King, Angus S., Jr. [I-ME]",
        "lastName": "King",
        "party": "I",
        "state": "ME"
      }
    ],
    "title": "Responsibility in Drug Advertising Act of 2025",
    "type": "S",
    "updateDate": "2026-01-21T06:25:39Z",
    "updateDateIncludingText": "2026-01-21T06:25:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
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
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T22:21:09Z",
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
      "sponsorshipDate": "2025-02-06",
      "state": "VA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s483is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 483\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. King (for himself, Mr. Kaine , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to restrict direct-to-consumer drug advertising.\n#### 1. Short title\nThis Act may be cited as the Responsibility in Drug Advertising Act of 2025 .\n#### 2. Direct-to-consumer drug advertising\nThe Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 et seq. ) is amended\u2014\n**(1)**\nin section 301 ( 21 U.S.C. 331 ), by adding at the end the following:\n(jjj) The conduct of direct-to-consumer advertising of a drug in violation of section 506M. ; and\n**(2)**\nin chapter V, by inserting after section 506L ( 21 U.S.C. 356l ) the following:\n506M. Direct-to-consumer drug advertising (a) Prohibitions (1) First 3 years (A) In general Subject to subparagraph (B), no person shall conduct direct-to-consumer advertising, including on a social media platform, of a drug approved under section 505(c) before the end of the 3-year period beginning on the date of such approval. (B) Waiver The Secretary may waive the application of subparagraph (A) to a drug during the third year of the 3-year period described in such subparagraph if\u2014 (i) the sponsor of the drug submits an application to the Secretary pursuant to subparagraph (C); and (ii) the Secretary, after considering the application and any accompanying materials, determines that direct-to-consumer advertising of the drug would have an affirmative value to public health. (C) Application for waiver To seek a waiver under subparagraph (B), the sponsor of a drug shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require. (2) Subsequent years The Secretary may prohibit direct-to-consumer advertising, including on social media platforms, of a drug during the period beginning at the end of the 3-year period described in paragraph (1)(A) if the Secretary determines that the drug has significant adverse health effects based on post-approval studies, risk-benefit analyses, adverse event reports, the scientific literature, any clinical or observational studies, or any other appropriate resource. (b) Regulations Not later than 1 year after the date of the enactment of this section, the Secretary shall revise the regulations promulgated under this Act governing drug advertisements to the extent necessary to implement this section. (c) Rule of construction This section shall not be construed to diminish the authority of the Secretary to prohibit or regulate direct-to-consumer advertising of drugs, including on social media platforms, under any other provision of law. (d) Effective date This section applies only with respect to a drug approved under section 505(c) on or after the date that is 1 year before the date of enactment of this section. .",
      "versionDate": "2025-02-06",
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
        "actionDate": "2025-02-07",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1117",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Responsibility in Drug Advertising Act of 2025",
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
            "name": "Broadcasting, cable, digital technologies",
            "updateDate": "2025-04-24T16:09:19Z"
          },
          {
            "name": "Drug safety, medical device, and laboratory regulation",
            "updateDate": "2025-04-24T16:09:13Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-04-24T16:09:24Z"
          },
          {
            "name": "Marketing and advertising",
            "updateDate": "2025-04-24T16:08:54Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-04-24T16:09:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-12T16:21:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119s483",
          "measure-number": "483",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2025-06-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s483v00",
            "update-date": "2025-06-09"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Responsibility in Drug Advertising Act of 2025</strong></p><p>This bill prohibits direct-to-consumer advertising of new drugs during the first three years following their approval by the Food and Drug Administration (FDA). Direct-to-consumer advertising includes advertising via social media.\u00a0</p><p>Upon request from a drug\u2019s sponsor, the FDA may waive the prohibition during the third year following a drug\u2019s approval if it determines that the direct-to-consumer advertising of the drug would have an affirmative value to public health. Conversely, the FDA may prohibit such advertising beyond the three-year period following approval if it determines that the drug has significant adverse health effects based on post-approval studies, adverse event reports, and other appropriate resources.\u00a0</p><p>The prohibition applies to new drugs approved beginning one year before the bill\u2019s enactment.</p>"
        },
        "title": "Responsibility in Drug Advertising Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s483.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Responsibility in Drug Advertising Act of 2025</strong></p><p>This bill prohibits direct-to-consumer advertising of new drugs during the first three years following their approval by the Food and Drug Administration (FDA). Direct-to-consumer advertising includes advertising via social media.\u00a0</p><p>Upon request from a drug\u2019s sponsor, the FDA may waive the prohibition during the third year following a drug\u2019s approval if it determines that the direct-to-consumer advertising of the drug would have an affirmative value to public health. Conversely, the FDA may prohibit such advertising beyond the three-year period following approval if it determines that the drug has significant adverse health effects based on post-approval studies, adverse event reports, and other appropriate resources.\u00a0</p><p>The prohibition applies to new drugs approved beginning one year before the bill\u2019s enactment.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119s483"
    },
    "title": "Responsibility in Drug Advertising Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Responsibility in Drug Advertising Act of 2025</strong></p><p>This bill prohibits direct-to-consumer advertising of new drugs during the first three years following their approval by the Food and Drug Administration (FDA). Direct-to-consumer advertising includes advertising via social media.\u00a0</p><p>Upon request from a drug\u2019s sponsor, the FDA may waive the prohibition during the third year following a drug\u2019s approval if it determines that the direct-to-consumer advertising of the drug would have an affirmative value to public health. Conversely, the FDA may prohibit such advertising beyond the three-year period following approval if it determines that the drug has significant adverse health effects based on post-approval studies, adverse event reports, and other appropriate resources.\u00a0</p><p>The prohibition applies to new drugs approved beginning one year before the bill\u2019s enactment.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119s483"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s483is.xml"
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
      "title": "Responsibility in Drug Advertising Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:23:35Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Responsibility in Drug Advertising Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Food, Drug, and Cosmetic Act to restrict direct-to-consumer drug advertising.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:18:59Z"
    }
  ]
}
```
