# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2531?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2531
- Title: Uterine Fibroid Intervention and Gynecological Health Treatment Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2531
- Origin chamber: Senate
- Introduced date: 2025-07-30
- Update date: 2026-05-14T11:03:27Z
- Update date including text: 2026-05-14T11:03:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-30: Introduced in Senate
- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2025-07-30: Introduced in Senate

## Actions

- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-30",
    "latestAction": {
      "actionDate": "2025-07-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2531",
    "number": "2531",
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
    "title": "Uterine Fibroid Intervention and Gynecological Health Treatment Act of 2025",
    "type": "S",
    "updateDate": "2026-05-14T11:03:27Z",
    "updateDateIncludingText": "2026-05-14T11:03:27Z"
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
      "actionDate": "2025-07-30",
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
      "actionDate": "2025-07-30",
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
            "date": "2026-03-19T14:00:40Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-07-30T15:21:31Z",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-30",
      "state": "WY"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "KS"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2531is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2531\nIN THE SENATE OF THE UNITED STATES\nJuly 30, 2025 Ms. Alsobrooks (for herself and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo authorize the Secretary of Health and Human Services to award grants to increase early detection of and intervention for uterine fibroids, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Uterine Fibroid Intervention and Gynecological Health Treatment Act of 2025 .\n#### 2. Research on uterine fibroid early detection and intervention\n##### (a) In general\nThe Secretary of Health and Human Services (referred to in this Act as the Secretary ) shall\u2014\n**(1)**\nconduct or support research on increasing early detection of, and intervention for, uterine fibroids; and\n**(2)**\nbased on the results of such research and other relevant information, formulate evidence-based or evidence-informed strategies to increase early detection in health care settings.\n##### (b) Timeline\nThe Secretary shall finalize the evidence-based or evidence-informed strategies required by subsection (a)(2) as expeditiously as possible in order to make such strategies available to grantees under section 3 to implement such strategies pursuant to section 3(b)(3).\n#### 3. Grants with respect to uterine fibroid early detection and intervention\n##### (a) In general\nThe Secretary may award grants to States for carrying out programs\u2014\n**(1)**\nto increase early detection of, and intervention for, uterine fibroids; and\n**(2)**\nto develop and implement public awareness and education campaigns for the early detection of, and intervention for, uterine fibroids.\n##### (b) Use of funds\nA State receiving a grant under this section may use the grant for the following activities, with respect to increasing early detection of, and intervention for, uterine fibroids:\n**(1)**\nScreening procedures, including advanced gynecological imaging, including payment for such procedures.\n**(2)**\nPatient navigation services.\n**(3)**\nImplementation of evidence-based or evidence-informed strategies formulated under section 2(a)(2).\n**(4)**\nFacilitating access to health care settings.\n#### 4. Research with respect to uterine fibroid early detection and intervention\nThe Secretary may award grants to States for the purpose of conducting research, which may include clinical trials, related to\u2014\n**(1)**\ndisparities in pain control and management in uterine fibroid surgical treatment; or\n**(2)**\nAsherman\u2019s Syndrome, intrauterine adhesions, and other intrauterine conditions, as the Secretary determines appropriate.\n#### 5. Reports to Congress\n##### (a) Reports on grants\nNot later 2 years after the initial award of grants under section 2 or 3, and every 2 years thereafter, the Secretary shall submit to Congress, and make publicly available on the website of the Department of Health and Human Services\u2014\n**(1)**\na report summarizing the findings and results of programs and activities funded through grants awarded under this Act; and\n**(2)**\na report outlining research developments and findings related to\u2014\n**(A)**\ndisparities in pain control and management in uterine fibroid surgical treatment; and\n**(B)**\nAsherman\u2019s Syndrome, intrauterine adhesions, and other intrauterine conditions, as the Secretary determines appropriate.",
      "versionDate": "2025-07-30",
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
            "name": "Congressional oversight",
            "updateDate": "2026-04-16T19:08:22Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2026-04-16T19:08:02Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2026-04-16T19:08:09Z"
          },
          {
            "name": "Medical research",
            "updateDate": "2026-04-16T19:07:44Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2026-04-16T19:08:17Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2026-04-16T19:07:55Z"
          },
          {
            "name": "Sex and reproductive health",
            "updateDate": "2026-04-16T19:08:26Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2026-04-16T19:07:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-09-17T16:26:46Z"
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
      "date": "2025-07-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2531is.xml"
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
      "title": "Uterine Fibroid Intervention and Gynecological Health Treatment Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T11:03:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Uterine Fibroid Intervention and Gynecological Health Treatment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T05:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the Secretary of Health and Human Services to award grants to increase early detection of and intervention for uterine fibroids, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-07T05:18:18Z"
    }
  ]
}
```
