# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/422?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/422
- Title: A resolution recognizing the seriousness of polycystic ovary syndrome (PCOS) and expressing support for the designation of September 2025 as "PCOS Awareness Month".
- Congress: 119
- Bill type: SRES
- Bill number: 422
- Origin chamber: Senate
- Introduced date: 2025-09-30
- Update date: 2026-04-09T21:08:20Z
- Update date including text: 2026-04-09T21:08:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-30: Introduced in Senate
- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-10-06 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-10-06 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-10-06 - Discharge: Senate Committee on Health, Education, Labor, and Pensions discharged by Unanimous Consent.
- 2025-10-06 - Committee: Senate Committee on Health, Education, Labor, and Pensions discharged by Unanimous Consent.
- Latest action: 2025-09-30: Introduced in Senate

## Actions

- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-10-06 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-10-06 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-10-06 - Discharge: Senate Committee on Health, Education, Labor, and Pensions discharged by Unanimous Consent.
- 2025-10-06 - Committee: Senate Committee on Health, Education, Labor, and Pensions discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/422",
    "number": "422",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "A resolution recognizing the seriousness of polycystic ovary syndrome (PCOS) and expressing support for the designation of September 2025 as \"PCOS Awareness Month\".",
    "type": "SRES",
    "updateDate": "2026-04-09T21:08:20Z",
    "updateDateIncludingText": "2026-04-09T21:08:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-06",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-10-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-10-06",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Health, Education, Labor, and Pensions discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-10-06",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Health, Education, Labor, and Pensions discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-30",
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
            "date": "2025-10-06T23:28:37Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-09-30T15:31:14Z",
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
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NE"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MD"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "KS"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "OK"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres422is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 422\nIN THE SENATE OF THE UNITED STATES\nSeptember 30, 2025 Ms. Warren (for herself, Mrs. Fischer , Mr. Blumenthal , Mr. Padilla , Mr. Van Hollen , Mr. Marshall , Mr. Lankford , and Mr. Warnock ) submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nRecognizing the seriousness of polycystic ovary syndrome (PCOS) and expressing support for the designation of September 2025 as PCOS Awareness Month .\nThat the Senate\u2014\n**(1)**\nrecognizes polycystic ovary syndrome (referred to in this resolution as PCOS ) as a serious disorder that impacts many aspects of health, including cardiometabolic, reproductive, and mental health, and quality of life;\n**(2)**\nexpresses support for the designation of September 2025 as PCOS Awareness Month ;\n**(3)**\nsupports the goals and ideals of PCOS Awareness Month, which are\u2014\n**(A)**\nto increase awareness of, and education about, PCOS and its connection to comorbidities, such as type 2 diabetes, endometrial cancer, cardiovascular disease, nonalcoholic fatty liver disease, and mental health disorders, among the general public, women, girls, and health care professionals;\n**(B)**\nto improve diagnosis and treatment of PCOS;\n**(C)**\nto disseminate information on diagnosis, treatment, and management of PCOS, including prevention of comorbidities such as type 2 diabetes, endometrial cancer, cardiovascular disease, nonalcoholic fatty liver disease, and eating disorders; and\n**(D)**\nto improve quality of life and outcomes for women and girls with PCOS;\n**(4)**\nrecognizes the need for further research, improved treatment and care options, and a cure for PCOS;\n**(5)**\nacknowledges the struggles affecting all women and girls who have PCOS in the United States;\n**(6)**\nurges medical researchers and health care professionals to advance their understanding of PCOS to improve research, diagnosis, and treatment of PCOS for women and girls; and\n**(7)**\nencourages States, territories, and localities to support the goals and ideals of PCOS Awareness Month.",
      "versionDate": "2025-09-30",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres422ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 422\nIN THE SENATE OF THE UNITED STATES\nSeptember 30, 2025 Ms. Warren (for herself, Mrs. Fischer , Mr. Blumenthal , Mr. Padilla , Mr. Van Hollen , Mr. Marshall , Mr. Lankford , and Mr. Warnock ) submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nOctober 6, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nRecognizing the seriousness of polycystic ovary syndrome (PCOS) and expressing support for the designation of September 2025 as PCOS Awareness Month .\nThat the Senate\u2014\n**(1)**\nrecognizes polycystic ovary syndrome (referred to in this resolution as PCOS ) as a serious disorder that impacts many aspects of health, including cardiometabolic, reproductive, and mental health, and quality of life;\n**(2)**\nexpresses support for the designation of September 2025 as PCOS Awareness Month ;\n**(3)**\nsupports the goals and ideals of PCOS Awareness Month, which are\u2014\n**(A)**\nto increase awareness of, and education about, PCOS and its connection to comorbidities, such as type 2 diabetes, endometrial cancer, cardiovascular disease, nonalcoholic fatty liver disease, and mental health disorders, among the general public, women, girls, and health care professionals;\n**(B)**\nto improve diagnosis and treatment of PCOS;\n**(C)**\nto disseminate information on diagnosis, treatment, and management of PCOS, including prevention of comorbidities such as type 2 diabetes, endometrial cancer, cardiovascular disease, nonalcoholic fatty liver disease, and eating disorders; and\n**(D)**\nto improve quality of life and outcomes for women and girls with PCOS;\n**(4)**\nrecognizes the need for further research, improved treatment and care options, and a cure for PCOS;\n**(5)**\nacknowledges the struggles affecting all women and girls who have PCOS in the United States;\n**(6)**\nurges medical researchers and health care professionals to advance their understanding of PCOS to improve research, diagnosis, and treatment of PCOS for women and girls; and\n**(7)**\nencourages States, territories, and localities to support the goals and ideals of PCOS Awareness Month.",
      "versionDate": "2025-10-06",
      "versionType": "ATS"
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
            "name": "Cardiovascular and respiratory health",
            "updateDate": "2025-11-18T19:36:41Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-11-18T19:36:41Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-11-18T19:36:41Z"
          },
          {
            "name": "Medical research",
            "updateDate": "2025-11-18T19:36:41Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2025-11-18T19:36:41Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-11-18T19:36:41Z"
          },
          {
            "name": "Sex and reproductive health",
            "updateDate": "2025-11-18T19:36:41Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-11-18T19:36:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-11-18T18:47:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-06",
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
          "measure-id": "id119sres422",
          "measure-number": "422",
          "measure-type": "sres",
          "orig-publish-date": "2025-10-06",
          "originChamber": "SENATE",
          "update-date": "2026-04-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres422v55",
            "update-date": "2026-04-09"
          },
          "action-date": "2025-10-06",
          "action-desc": "Passed Senate",
          "summary-text": "<p>This resolution expresses support for designating September 2025 as PCOS Awareness Month. Polycystic ovary syndrome (PCOS) is caused by a hormone imbalance and can cause symptoms such as infertility, weight gain, excess hair growth, and acne.</p>"
        },
        "title": "A resolution recognizing the seriousness of polycystic ovary syndrome (PCOS) and expressing support for the designation of September 2025 as \"PCOS Awareness Month\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres422.xml",
    "summary": {
      "actionDate": "2025-10-06",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution expresses support for designating September 2025 as PCOS Awareness Month. Polycystic ovary syndrome (PCOS) is caused by a hormone imbalance and can cause symptoms such as infertility, weight gain, excess hair growth, and acne.</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119sres422"
    },
    "title": "A resolution recognizing the seriousness of polycystic ovary syndrome (PCOS) and expressing support for the designation of September 2025 as \"PCOS Awareness Month\"."
  },
  "summaries": [
    {
      "actionDate": "2025-10-06",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution expresses support for designating September 2025 as PCOS Awareness Month. Polycystic ovary syndrome (PCOS) is caused by a hormone imbalance and can cause symptoms such as infertility, weight gain, excess hair growth, and acne.</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119sres422"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres422is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-10-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres422ats.xml"
        }
      ],
      "type": "ATS"
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
      "title": "A resolution recognizing the seriousness of polycystic ovary syndrome (PCOS) and expressing support for the designation of September 2025 as \"PCOS Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-01T13:33:12Z"
    },
    {
      "title": "A resolution recognizing the seriousness of polycystic ovary syndrome (PCOS) and expressing support for the designation of September 2025 as \"PCOS Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T10:56:20Z"
    }
  ]
}
```
