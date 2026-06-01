# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3944?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3944
- Title: Women’s Heart Health Expansion Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3944
- Origin chamber: Senate
- Introduced date: 2026-02-26
- Update date: 2026-05-01T18:53:03Z
- Update date including text: 2026-05-01T18:53:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-26: Introduced in Senate
- 2026-02-26 - IntroReferral: Introduced in Senate
- 2026-02-26 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2026-02-26: Introduced in Senate

## Actions

- 2026-02-26 - IntroReferral: Introduced in Senate
- 2026-02-26 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-26",
    "latestAction": {
      "actionDate": "2026-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3944",
    "number": "3944",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "A000382",
        "district": "",
        "firstName": "Angela",
        "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
        "lastName": "Alsobrooks",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Women\u2019s Heart Health Expansion Act of 2026",
    "type": "S",
    "updateDate": "2026-05-01T18:53:03Z",
    "updateDateIncludingText": "2026-05-01T18:53:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-26",
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
      "actionDate": "2026-02-26",
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
            "date": "2026-03-19T14:01:18Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-02-26T18:31:23Z",
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
      "sponsorshipDate": "2026-02-26",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3944is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3944\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2026 Ms. Alsobrooks (for herself and Mrs. Britt ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to reauthorize the WISEWOMAN program.\n#### 1. Short title\nThis Act may be cited as the Women\u2019s Heart Health Expansion Act of 2026 .\n#### 2. Reauthorization of WISEWOMAN program\nSection 1509 of the Public Health Service Act ( 42 U.S.C. 300n\u20134a ) is amended to read as follows:\n1509. Supplemental grants for additional preventive health services (a) Screening and referral projects The Secretary, acting through the Director of the Centers for Disease Control and Prevention, may award supplemental grants to recipients of grants under section 1501 to carry out projects for the purposes of\u2014 (1) providing preventive health services in addition to the services authorized in such section, including\u2014 (A) screenings regarding blood pressure, cholesterol, obesity, and other relevant risk factors; and (B) evidence-based health education offered by a qualified provider to improve a measurable health outcome, such as blood pressure, cholesterol, diabetes, or obesity; (2) providing appropriate referrals for medical treatment of women receiving services pursuant to paragraph (1) and ensuring, to the extent practicable, the provision of appropriate follow-up services; and (3) evaluating activities conducted under paragraphs (1) and (2) through appropriate surveillance or program-monitoring activities and reporting to the Secretary on such activities. (b) Eligibility for services Women eligible for services pursuant to a grant under subsection (a) shall include\u2014 (1) women eligible for services pursuant to a grant made under section 1501; and (2) other women who are high-risk and meet such eligibility criteria as the Secretary may specify. (c) Authorized providers Health services provided pursuant to a grant under subsection (a) shall be provided by\u2014 (1) an entity screening women for breast and cervical cancer pursuant to a grant under section 1501; or (2) other health care entities, as the Secretary determines. (d) Funding To carry out this section, there is authorized to be appropriated $250,000,000 for the period of fiscal years 2027 through 2031. .\n#### 3. GAO study\nNot later than September 30, 2027, the Comptroller General of the United States shall report to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives on the work of the Well-Integrated Screening and Evaluation for Women Across the Nation Program, including\u2014\n**(1)**\nan estimate of the number of individuals eligible for services provided under such program;\n**(2)**\na summary of trends in the number of individuals served through such program;\n**(3)**\nan assessment of any factors that may be driving the trends identified under paragraph (2), including any barriers to accessing cardiovascular health screenings provided by such program; and\n**(4)**\nan analysis of the cost-effectiveness of such program with respect to patient outcomes, such as blood pressure, cholesterol, diabetes, or obesity.",
      "versionDate": "2026-02-26",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Cardiovascular and respiratory health",
            "updateDate": "2026-05-01T18:52:58Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-05-01T18:53:03Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-05-01T18:52:38Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2026-05-01T18:52:44Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2026-05-01T18:52:52Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2026-05-01T18:52:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-03-19T14:40:47Z"
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
      "date": "2026-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3944is.xml"
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
      "title": "Women\u2019s Heart Health Expansion Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Women\u2019s Heart Health Expansion Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-17T04:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to reauthorize the WISEWOMAN program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-17T04:18:29Z"
    }
  ]
}
```
