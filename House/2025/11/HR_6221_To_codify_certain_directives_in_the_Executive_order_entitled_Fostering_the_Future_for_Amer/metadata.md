# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6221?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6221
- Title: Fostering the Future for American Children and Families Act
- Congress: 119
- Bill type: HR
- Bill number: 6221
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-02-04T09:06:46Z
- Update date including text: 2026-02-04T09:06:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6221",
    "number": "6221",
    "originChamber": "House",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Fostering the Future for American Children and Families Act",
    "type": "HR",
    "updateDate": "2026-02-04T09:06:46Z",
    "updateDateIncludingText": "2026-02-04T09:06:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-11-20T15:06:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-20T15:06:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "OH"
    },
    {
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "NE"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "VA"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6221ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6221\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mr. Nunn of Iowa (for himself, Mr. Landsman , Mr. Fong , and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo codify certain directives in the Executive order entitled Fostering the Future for American Children and Families .\n#### 1. Short title\nThis Act may be cited as the Fostering the Future for American Children and Families Act .\n#### 2. Study of Federal, State, and private sector programs that support technical job training, on-the-job training, and apprenticeships for current and former foster youth\n##### (a) In general\nThe Secretary of Health and Human Services, in coordination with the Secretary of Labor, shall conduct a comprehensive study of the Federal, State, and private sector programs that support technical job training, on-the-job training, and apprenticeships for current and former foster youth. The study shall evaluate the effectiveness of the programs, gaps in services provided under the programs, the barriers to accessing the programs, and the opportunities to expand career pathways for youth transitioning out of the child welfare system.\n##### (b) Report to Congress\nWithin 1 year after the date of the enactment of this Act, the Secretaries shall submit to the Congress a report containing findings and recommendations of the study required by subsection (a) for improving alignment of the matters referred to in subsection (a), the need for additional funding to do so, and the modernization of the relevant programs.\n#### 3. Fostering the Future Pipeline Program\n##### (a) Establishment\nAfter completing the study required by section 2, the Secretary of Health and Human Services, in consultation with the Secretary of Labor, shall establish in the Department of Health and Human Services a program, which shall be known as the Fostering the Future Pipeline Program , under which grants are made to States, academic institutions, private-sector employers, and nonprofit or faith-based organizations, on a competitive basis, to expand access to industry-aligned technical job training and apprenticeships for current and former foster youth, including through training or apprenticeships in high-demand fields such as skilled trades, manufacturing, health care, information technology, and agriculture.\n##### (b) Limitations on authorization of appropriations\nTo carry out this section, there are authorized to be appropriated to the Secretary of Health and Human Services not more than $50,000,000 for each fiscal year.\n#### 4. Authority to use education and training vouchers provided pursuant to the John H. Chafee Foster Care Program for Successful Transition to Adulthood to increase flexibility for youth exiting foster care\nSection 477(i)(4) of the Social Security Act ( 42 U.S.C. 677(i)(4) ) is amended\u2014\n**(1)**\nby striking and at the end of subparagraph (A); and\n**(2)**\nby redesignating subparagraph (B) and subparagraph (C) and inserting after subparagraph (A) the following:\n(B) may be available for short-term, career-focused, credential-granting programs, including registered apprenticeships, certificate programs, and other rapid-employment pathways; and .\n#### 5. Effective date\nThis Act and the amendments made by this Act shall take effect 6 months after the date of the enactment of this Act.",
      "versionDate": "2025-11-20",
      "versionType": "Introduced in House"
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
        "name": "Families",
        "updateDate": "2025-12-17T15:55:43Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6221ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Fostering the Future for American Children and Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-16T06:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fostering the Future for American Children and Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-16T06:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To codify certain directives in the Executive order entitled \"Fostering the Future for American Children and Families\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-16T06:48:17Z"
    }
  ]
}
```
