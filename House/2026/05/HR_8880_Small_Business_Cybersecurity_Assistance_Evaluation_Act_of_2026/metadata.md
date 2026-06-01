# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8880?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8880
- Title: Small Business Cybersecurity Assistance Evaluation Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8880
- Origin chamber: House
- Introduced date: 2026-05-19
- Update date: 2026-05-20T08:23:26Z
- Update date including text: 2026-05-20T16:28:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-19: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the House Committee on Small Business.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported by the Yeas and Nays: 23 - 0.
- Latest action: 2026-05-19: Introduced in House

## Actions

- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the House Committee on Small Business.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported by the Yeas and Nays: 23 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-19",
    "latestAction": {
      "actionDate": "2026-05-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8880",
    "number": "8880",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "S001231",
        "district": "12",
        "firstName": "Lateefah",
        "fullName": "Rep. Simon, Lateefah [D-CA-12]",
        "lastName": "Simon",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Small Business Cybersecurity Assistance Evaluation Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-20T08:23:26Z",
    "updateDateIncludingText": "2026-05-20T16:28:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 23 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-19",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Small Business.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-19",
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
        "item": [
          {
            "date": "2026-05-20T21:44:54Z",
            "name": "Markup By"
          },
          {
            "date": "2026-05-19T16:01:10Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
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
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8880ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8880\nIN THE HOUSE OF REPRESENTATIVES\nMay 19, 2026 Ms. Simon (for herself and Mr. Bresnahan ) introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo require the Comptroller General to evaluate Federal cybersecurity assistance to small business concerns, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Small Business Cybersecurity Assistance Evaluation Act of 2026 .\n#### 2. GAO study on small business cybersecurity assistance\n##### (a) Study\nThe Comptroller General of the United States shall conduct a study of current Federal cybersecurity initiatives, programs, resources, tools, and services intended to assist owners of small business concerns (as defined under section 3 of the Small Business Act ( 15 U.S.C. 632 )) with\u2014\n**(1)**\nidentifying cyber risks, cyber threats, and cybersecurity vulnerabilities relating to such concerns;\n**(2)**\nassessing the preparedness of such concerns for such risks, threats, and vulnerabilities;\n**(3)**\nplanning for, mitigating, and recovering from cyberattacks and incidents of social engineering, scams, and fraud (including developing, adopting, and implementing cybersecurity measures, training, protocols, tools, and infrastructure); and\n**(4)**\nidentifying sources of capital, or obtaining capital, to carry out the activities specified in paragraphs (1), (2), and (3).\n##### (b) Required content\nThe study required by subsection (a) shall include\u2014\n**(1)**\ninformation on the most common cyberattacks affecting small business concerns;\n**(2)**\nan identification and description of the Federal cybersecurity initiatives, programs, resources, tools, and services included in the study described in subsection (a);\n**(3)**\nan assessment of the awareness and use of such Federal cybersecurity initiatives, programs, resources, tools, and services by small business concerns and reasons for differences in levels of such awareness and use;\n**(4)**\nan assessment of the coordination and integration among such Federal cybersecurity initiatives, programs, resources, tools, and services;\n**(5)**\nan assessment of the effectiveness of such Federal cybersecurity initiatives, programs, resources, tools, and services in assisting small business concerns with the activities listed in paragraphs (1) through (4) of subsection (a);\n**(6)**\nan identification of any foundational cybersecurity concepts absent from such Federal cybersecurity initiatives, programs, resources, tools, and services; and\n**(7)**\nrecommendations on how to improve the effectiveness, awareness, and coordination of such Federal cybersecurity initiatives, programs, resources, tools, and services for small business concerns.\n##### (c) Report\nThe Comptroller General shall submit to the Committee on Small Business of the House of Representatives and the Committee on Small Business and Entrepreneurship of the Senate a report containing all findings and determinations made in carrying out the study required under subsection (a).\n#### 3. Compliance with CUTGO\nNo additional amounts are authorized to carry out this Act.",
      "versionDate": "2026-05-19",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8880ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Small Business Cybersecurity Assistance Evaluation Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-20T08:23:26Z"
    },
    {
      "title": "Small Business Cybersecurity Assistance Evaluation Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T08:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Comptroller General to evaluate Federal cybersecurity assistance to small business concerns, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-20T08:19:36Z"
    }
  ]
}
```
