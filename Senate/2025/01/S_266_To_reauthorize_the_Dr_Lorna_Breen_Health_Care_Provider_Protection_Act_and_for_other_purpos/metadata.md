# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/266?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/266
- Title: Dr. Lorna Breen Health Care Provider Protection Reauthorization Act
- Congress: 119
- Bill type: S
- Bill number: 266
- Origin chamber: Senate
- Introduced date: 2025-01-28
- Update date: 2026-02-05T17:33:49Z
- Update date including text: 2026-02-05T17:33:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in Senate
- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-01-28: Introduced in Senate

## Actions

- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/266",
    "number": "266",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000384",
        "district": "",
        "firstName": "Timothy",
        "fullName": "Sen. Kaine, Tim [D-VA]",
        "lastName": "Kaine",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Dr. Lorna Breen Health Care Provider Protection Reauthorization Act",
    "type": "S",
    "updateDate": "2026-02-05T17:33:49Z",
    "updateDateIncludingText": "2026-02-05T17:33:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
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
            "date": "2025-01-28T16:48:19Z",
            "name": "Referred To"
          },
          {
            "date": "2025-01-28T16:48:19Z",
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
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "IN"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "RI"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "KS"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "NH"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "AK"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "VA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "WV"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "WI"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s266is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 266\nIN THE SENATE OF THE UNITED STATES\nJanuary 28, 2025 Mr. Kaine (for himself, Mr. Young , Mr. Reed , Mr. Marshall , Mrs. Shaheen , Ms. Murkowski , Mr. Warner , and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo reauthorize the Dr. Lorna Breen Health Care Provider Protection Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Dr. Lorna Breen Health Care Provider Protection Reauthorization Act .\n#### 2. Education and awareness initiative encouraging use of mental health and substance use disorder services by health care professionals\nSection 3 of the Dr. Lorna Breen Health Care Provider Protection Act ( Public Law 117\u2013105 ) is amended\u2014\n**(1)**\nin subsection (b), by inserting and annually thereafter, after of this Act, ; and\n**(2)**\nin subsection (c), by striking 2022 through 2024 and inserting 2025 through 2029 .\n#### 3. Programs to promote mental health among the health professional workforce\nThe second section 764 of the Public Health Service Act ( 42 U.S.C. 294t ), as added by section 4 of the Dr. Lorna Breen Health Care Provider Protection Act ( Public Law 117\u2013105 ), is amended\u2014\n**(1)**\nby redesignating such section 764 as section 764A;\n**(2)**\nin subsection (a)(3)\u2014\n**(A)**\nby striking to eligible entities in and inserting \u201cto eligible entities that\u2014\n(A) are in ;\n**(B)**\nby striking the period and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(B) have a focus on the reduction of administrative burden on health care workers. ;\n**(3)**\nin subsection (c), by inserting not less than after period of ; and\n**(4)**\nin subsection (f), by striking 2022 through 2024 and inserting 2025 through 2029 .",
      "versionDate": "2025-01-28",
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
        "actionDate": "2026-02-03",
        "text": "Became Public Law No: 119-75."
      },
      "number": "7148",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Consolidated Appropriations Act, 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-04",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "929",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Dr. Lorna Breen Health Care Provider Protection Reauthorization Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
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
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2025-04-01T15:17:48Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-04-01T15:17:48Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-04-01T15:17:48Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-04-01T15:17:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-03T16:11:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119s266",
          "measure-number": "266",
          "measure-type": "s",
          "orig-publish-date": "2025-01-28",
          "originChamber": "SENATE",
          "update-date": "2025-05-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s266v00",
            "update-date": "2025-05-28"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Dr. Lorna Breen Health Care Provider Protection Reauthorization Act</strong></p><p>This bill\u00a0reauthorizes through FY2029 and revises Health Resources and Services Administration (HRSA) grants for programs and training to improve mental health among health care professionals and a Centers for Disease Control and Prevention (CDC) initiative to educate health care professionals about their mental health and related services.</p><p>Specifically, the bill reauthorizes HRSA grants to health care service providers and medical professional associations to implement programs supporting these professionals\u2019 mental health, such as through peer-support programs or providing mental health care. It also authorizes\u00a0HRSA to prioritize applicants that focus on reducing administrative burden on health care workers.</p><p>Also, the bill reauthorizes HRSA grants to government and certain educational entities for training health care students and professionals on how to address mental health and related issues. It also specifies that grants or contracts awarded under the program must be for not less than three years.</p><p>Additionally, the bill\u00a0reauthorizes a CDC education and awareness initiative to help health care professionals understand and seek support for their mental health. It also requires the\u00a0CDC to submit annual reports to specified congressional committees on the initiative\u2019s activities and outcomes.</p>"
        },
        "title": "Dr. Lorna Breen Health Care Provider Protection Reauthorization Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s266.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Dr. Lorna Breen Health Care Provider Protection Reauthorization Act</strong></p><p>This bill\u00a0reauthorizes through FY2029 and revises Health Resources and Services Administration (HRSA) grants for programs and training to improve mental health among health care professionals and a Centers for Disease Control and Prevention (CDC) initiative to educate health care professionals about their mental health and related services.</p><p>Specifically, the bill reauthorizes HRSA grants to health care service providers and medical professional associations to implement programs supporting these professionals\u2019 mental health, such as through peer-support programs or providing mental health care. It also authorizes\u00a0HRSA to prioritize applicants that focus on reducing administrative burden on health care workers.</p><p>Also, the bill reauthorizes HRSA grants to government and certain educational entities for training health care students and professionals on how to address mental health and related issues. It also specifies that grants or contracts awarded under the program must be for not less than three years.</p><p>Additionally, the bill\u00a0reauthorizes a CDC education and awareness initiative to help health care professionals understand and seek support for their mental health. It also requires the\u00a0CDC to submit annual reports to specified congressional committees on the initiative\u2019s activities and outcomes.</p>",
      "updateDate": "2025-05-28",
      "versionCode": "id119s266"
    },
    "title": "Dr. Lorna Breen Health Care Provider Protection Reauthorization Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Dr. Lorna Breen Health Care Provider Protection Reauthorization Act</strong></p><p>This bill\u00a0reauthorizes through FY2029 and revises Health Resources and Services Administration (HRSA) grants for programs and training to improve mental health among health care professionals and a Centers for Disease Control and Prevention (CDC) initiative to educate health care professionals about their mental health and related services.</p><p>Specifically, the bill reauthorizes HRSA grants to health care service providers and medical professional associations to implement programs supporting these professionals\u2019 mental health, such as through peer-support programs or providing mental health care. It also authorizes\u00a0HRSA to prioritize applicants that focus on reducing administrative burden on health care workers.</p><p>Also, the bill reauthorizes HRSA grants to government and certain educational entities for training health care students and professionals on how to address mental health and related issues. It also specifies that grants or contracts awarded under the program must be for not less than three years.</p><p>Additionally, the bill\u00a0reauthorizes a CDC education and awareness initiative to help health care professionals understand and seek support for their mental health. It also requires the\u00a0CDC to submit annual reports to specified congressional committees on the initiative\u2019s activities and outcomes.</p>",
      "updateDate": "2025-05-28",
      "versionCode": "id119s266"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s266is.xml"
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
      "title": "Dr. Lorna Breen Health Care Provider Protection Reauthorization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-04T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Dr. Lorna Breen Health Care Provider Protection Reauthorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reauthorize the Dr. Lorna Breen Health Care Provider Protection Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T03:48:23Z"
    }
  ]
}
```
