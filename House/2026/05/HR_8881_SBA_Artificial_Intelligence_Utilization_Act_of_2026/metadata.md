# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8881?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8881
- Title: SBA Artificial Intelligence Utilization Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8881
- Origin chamber: House
- Introduced date: 2026-05-19
- Update date: 2026-05-20T08:23:27Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8881",
    "number": "8881",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "F000475",
        "district": "1",
        "firstName": "Brad",
        "fullName": "Rep. Finstad, Brad [R-MN-1]",
        "lastName": "Finstad",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "SBA Artificial Intelligence Utilization Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-20T08:23:27Z",
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
            "date": "2026-05-20T21:45:30Z",
            "name": "Markup By"
          },
          {
            "date": "2026-05-19T16:00:10Z",
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
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8881ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8881\nIN THE HOUSE OF REPRESENTATIVES\nMay 19, 2026 Mr. Finstad (for himself and Mr. Latimer ) introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo amend the Small Business Act to require the Administrator of the Small Business Administration to report on the use of artificial intelligence and machine learning by the Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the SBA Artificial Intelligence Utilization Act of 2026 .\n#### 2. Reports regarding artificial intelligence and machine learning use by the Small Business Administration\nSection 10(c) of the Small Business Act is amended to read as follows:\n(c) Artificial intelligence and machine learning use reports (1) Reports required Not later than 90 days after the date of the enactment of this subsection, and annually thereafter, the Administrator shall submit to the Committee on Small Business of the House of Representatives and the Committee on Small Business and Entrepreneurship of the Senate a report on\u2014 (A) the use of artificial intelligence and machine learning by the Administration; (B) the benefits and risks posed by the use of artificial intelligence and machine learning in the work of the Administration, including in impeding the operations of the Administration; and (C) measures that the Administrator can take to effectively identify, evaluate, and manage such benefits and risks, including explanations of how the Administrator can\u2014 (i) retain human involvement in important decisions informed by recommendations made by artificial intelligence or machine learning; (ii) identify tasks and functions that artificial intelligence or machine learning can and cannot reliably and effectively perform, including whether artificial intelligence and machine learning can improve operations, productivity, or customer service; (iii) determine which specific artificial intelligence or machine learning tools are appropriate for a particular task or function, if such task or function is determined to have the potential to be reliably and effectively performed by artificial intelligence or machine learning; and (iv) determine whether an artificial intelligence or machine learning tool adequately fills a need of the Administration and is worth adopting to fulfill such need. (2) Briefing required Not later than 30 days after the date on which the Administrator submits each report required under paragraph (1), the Administrator shall provide to the committees described in such paragraph a briefing on such report. (3) Definitions In this subsection, the terms artificial intelligence and machine learning have the meanings given, respectively, in section 5002 of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 15 U.S.C. 9401 ). .",
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8881ih.xml"
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
      "title": "SBA Artificial Intelligence Utilization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T08:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SBA Artificial Intelligence Utilization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-20T08:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Small Business Act to require the Administrator of the Small Business Administration to report on the use of artificial intelligence and machine learning by the Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-20T08:19:37Z"
    }
  ]
}
```
