# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/758?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/758
- Title: Apprenticeships to College Act
- Congress: 119
- Bill type: S
- Bill number: 758
- Origin chamber: Senate
- Introduced date: 2025-02-26
- Update date: 2026-04-08T15:36:54Z
- Update date including text: 2026-04-08T15:36:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in Senate
- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-02-26: Introduced in Senate

## Actions

- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/758",
    "number": "758",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Apprenticeships to College Act",
    "type": "S",
    "updateDate": "2026-04-08T15:36:54Z",
    "updateDateIncludingText": "2026-04-08T15:36:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-26",
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
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T21:45:03Z",
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
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s758is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 758\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2025 Ms. Klobuchar (for herself and Mr. Moran ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo support the establishment of an apprenticeship college consortium.\n#### 1. Short title\nThis Act may be cited as the Apprenticeships to College Act .\n#### 2. Apprenticeship college consortium\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, in order to cooperate with the Secretary of Education and promote awareness and adoption of apprenticeship programs, the Secretary of Labor shall\u2014\n**(1)**\nenter into an interagency agreement with the Secretary of Education to promote and support integration and alignment of programs under the national apprenticeship system with secondary, postsecondary, and adult education, through the activities described in this section; and\n**(2)**\nsubmit to the Committee on Education and Workforce of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate, such agreement and any modifications to such agreement.\n##### (b) Apprenticeship college consortium\nIn order to support the establishment of a college consortium of postsecondary educational institutions, related instruction providers, sponsors, qualified intermediaries, and employers (referred to in this Act as the Registered Apprenticeship College Consortium ) for the purposes of promoting stronger connections between programs under the national apprenticeship system and participating 2- and 4-year postsecondary educational institutions, the interagency agreement under subsection (a) shall include a description of how the Secretaries will\u2014\n**(1)**\nsupport data sharing systems that align education records and records of programs under the national apprenticeship system regarding whether program participants who receive financial aid under title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1070 et seq. ) enroll in, or complete, postsecondary coursework while participating in a program under such system;\n**(2)**\nprovide guidance on how to align eligible funding from, planning processes for, and the requirements of, the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2301 et seq. ), the Rehabilitation Act of 1973 ( 29 U.S.C. 701 et seq. ), and the Higher Education Act of 1965 ( 20 U.S.C. 1001 et seq. ) with this Act;\n**(3)**\nrequire all participants of the Registered Apprenticeship College Consortium to enter into agreements to\u2014\n**(A)**\nhave an articulation agreement with a participating sponsor of an apprenticeship program, which may include a 2- or 4-year postsecondary educational institution;\n**(B)**\ncreate or expand the awarding and articulation of academic credit for related instruction completed and credentials awarded to program participants as part of a program under the national apprenticeship system; and\n**(C)**\nsupport the creation or expansion of electronic transcripts for apprenticeship programs and all academic content, including related instruction and on-the-job training;\n**(4)**\nprovide technical assistance on eligible uses of financial aid, including the Federal work study program under part C of title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1087\u201351 et seq. ), for related instruction for programs under the national apprenticeship system;\n**(5)**\nprovide to Registered Apprenticeship College Consortium participants or potential participants information regarding\u2014\n**(A)**\na list of apprenticeship programs in related occupations offered in the State or available under the Office of Apprenticeship that may become part of the Registered Apprenticeship College Consortium;\n**(B)**\ninformation on how to develop an apprenticeship program;\n**(C)**\ninformation on Federal, State, and local financial resources available to assist with the establishment and implementation of apprenticeship programs; and\n**(D)**\ninformation on related qualified intermediaries or industry or sector partnerships supporting apprenticeship programs, as applicable; and\n**(6)**\nsupport information regarding the Registered Apprenticeship College Consortium being made available on a publicly accessible website, including\u2014\n**(A)**\na list of participating members of the Registered Apprenticeship College Consortium, apprenticeship programs provided, credentials awarded with each program, and available apprenticeable occupations; and\n**(B)**\nmodels of articulation agreements, prior learning assessments, and competency-based curriculum for related instruction for illustrative purposes.\n##### (c) Limitations\nNothing in this Act shall require\u2014\n**(1)**\nan institution of higher education to participate in the Registered Apprenticeship College Consortium; or\n**(2)**\nan apprenticeship sponsor to participate in the Registered Apprenticeship College Consortium.",
      "versionDate": "2025-02-26",
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
            "name": "Adult education and literacy",
            "updateDate": "2026-01-28T21:04:53Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-28T21:04:53Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-08T15:36:54Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2026-01-28T21:04:53Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2026-01-28T21:04:53Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-01-28T21:04:53Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2026-01-28T21:04:53Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2026-01-28T21:04:53Z"
          },
          {
            "name": "Student records",
            "updateDate": "2026-01-28T21:04:53Z"
          },
          {
            "name": "Temporary and part-time employment",
            "updateDate": "2026-01-28T21:04:53Z"
          },
          {
            "name": "Vocational and technical education",
            "updateDate": "2026-01-28T21:04:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-03-21T17:26:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
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
          "measure-id": "id119s758",
          "measure-number": "758",
          "measure-type": "s",
          "orig-publish-date": "2025-02-26",
          "originChamber": "SENATE",
          "update-date": "2026-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s758v00",
            "update-date": "2026-03-27"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>A<b>pprenticeships to College Act</b></p> <p>This bill requires the Department of Labor to enter into an interagency agreement with the Department of Education to promote and support integration and alignment of programs under the national apprenticeship system with secondary, two- and four-year postsecondary, and adult education.</p>"
        },
        "title": "Apprenticeships to College Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s758.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p>A<b>pprenticeships to College Act</b></p> <p>This bill requires the Department of Labor to enter into an interagency agreement with the Department of Education to promote and support integration and alignment of programs under the national apprenticeship system with secondary, two- and four-year postsecondary, and adult education.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119s758"
    },
    "title": "Apprenticeships to College Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p>A<b>pprenticeships to College Act</b></p> <p>This bill requires the Department of Labor to enter into an interagency agreement with the Department of Education to promote and support integration and alignment of programs under the national apprenticeship system with secondary, two- and four-year postsecondary, and adult education.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119s758"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s758is.xml"
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
      "title": "Apprenticeships to College Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Apprenticeships to College Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to support the establishment of an apprenticeship college consortium.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:05Z"
    }
  ]
}
```
