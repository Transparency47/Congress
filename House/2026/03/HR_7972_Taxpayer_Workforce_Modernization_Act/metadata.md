# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7972?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7972
- Title: Taxpayer Workforce Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 7972
- Origin chamber: House
- Introduced date: 2026-03-18
- Update date: 2026-03-24T01:40:01Z
- Update date including text: 2026-03-24T01:40:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-18: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-03-18: Introduced in House

## Actions

- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-18",
    "latestAction": {
      "actionDate": "2026-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7972",
    "number": "7972",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001183",
        "district": "1",
        "firstName": "David",
        "fullName": "Rep. Schweikert, David [R-AZ-1]",
        "lastName": "Schweikert",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Taxpayer Workforce Modernization Act",
    "type": "HR",
    "updateDate": "2026-03-24T01:40:01Z",
    "updateDateIncludingText": "2026-03-24T01:40:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-18",
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
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-18",
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
          "date": "2026-03-18T14:00:45Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7972ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7972\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2026 Mr. Schweikert introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo require the Internal Revenue Service to establish a fellowship program within the Internal Revenue Service to recruit qualified data scientists to partner with tax law specialists and provide insights and identify emerging and complex issues in tax administration, ranging from data acquisition and quality through developing advanced analytics, statistics, and models to improve core tax administration activities in services and enforcement.\n#### 1. Short title\nThis Act may be cited as the Taxpayer Workforce Modernization Act .\n#### 2. IRS Fellowship Program\n##### (a) Establishment\nNot later than September 30, 2026, the Commissioner of Internal Revenue (hereinafter known as the Commissioner ), after consultation with the Chief Counsel of the Internal Revenue Service (hereinafter known as the Chief Counsel ) and the Chief Data and Analytics Officer of the Internal Revenue Service (hereinafter known as the Chief Data Officer ), shall establish within the Internal Revenue Service a fellowship program (hereinafter known as the program ) to recruit qualified data scientists in the private sector to join the Internal Revenue Service to create and participate in the task force established under subsection (e).\n##### (b) Objective\nThe Commissioner, after consultation with the Chief Counsel and Chief Data Officer, shall design the program in a manner such that the program\u2014\n**(1)**\naddresses such tax cases handled by the Internal Revenue Service as the Commissioner determines\u2014\n**(A)**\nare the most complex, or\n**(B)**\ninclude new and emerging issues, and\n**(2)**\nrecruits and retains outstanding and qualified tax experts.\n##### (c) Advertisement of program\nThe Commissioner shall advertise the program in such a way as to attract qualified data scientists and such other tax professionals as the Commissioner determines are appropriately qualified to handle the most complex tax cases.\n##### (d) Structure\n**(1) In general**\nThe program shall be staffed by not fewer than 10 fellows at the discretion of the Commissioner based on the needs of the Internal Revenue Service and the availability of qualified candidates.\n**(2) Term of service**\n**(A) In general**\nEach fellow shall be hired for a 2-, 3-, or 4-year term of service.\n**(B) Extensions**\n**(i) In general**\nA fellow may apply for, and the Commissioner may grant, a 1-year extension of the fellowship.\n**(ii) No limit on number of extensions**\nThere shall be no limit on the number of extensions under clause (i).\n**(3) Fellowship vacancies**\nThe Commissioner, after consultation with the Chief Counsel and Chief Data Officer, shall fill vacant fellowships\u2014\n**(A)**\nin such a manner as to ensure that the program is staffed with no fewer than 5 fellows, and\n**(B)**\nas soon as practicable after the vacancy arises.\n**(4) Hiring authority**\nThe Commissioner shall have authority to permanently hire a fellow at the end of the term of service for such fellow.\n##### (e) Task force\nNot later than the date on which the first fellowship is awarded under this section, the Commissioner shall establish a task force within the Internal Revenue Service and the office of the Chief Counsel in both national and regional office placements that includes the fellows hired pursuant to subsection (d), the purpose of which is to\u2014\n**(1)**\ndevelop, test, and refine data-driven methodologies to support audit case selection,\n**(2)**\neducate Internal Revenue Service employees on the use, interpretation, and limitations of data analytics, models, and emerging analytic techniques relevant to tax administration,\n**(3)**\nsupport, in coordination with examiners and tax experts, the audit of selected taxpayers through advanced data analysis, transaction-level testing, and quantitative modeling,\n**(4)**\nsupport efforts to address offshore tax evasion and issues implicating the Foreign Account Tax Compliance Act through data integration, anomaly detection, and network analysis,\n**(5)**\nidentify, mentor, and train junior employees from the Internal Revenue Service with respect to using data analytics and emerging analytic techniques to identify risk and facilitate task administration improvements,\n**(6)**\nreview existing use cases of artificial intelligence and data analytics with respect to tax administration, provide recommendations to improve on such existing cases, and identify new such cases, and\n**(7)**\nprovide data-driven recommendations for improving audit effectiveness and efficiency and for improving improper tax payments.\n##### (f) Composition\nThe task force established under subsection (e) may be composed of both\u2014\n**(1)**\nfellows, and\n**(2)**\npermanent employees of the Internal Revenue Service.\n##### (g) Pay of fellows\n**(1) In general**\nThe Secretary of the Treasury (or the Secretary\u2019s delegate) shall determine, subject to the provisions of this subsection, the pay of fellows recruited under subsection (a).\n**(2) Pay scale**\nFor purposes of paragraph (1), the pay of a fellow shall not be less than the minimum rate payable for GS\u201315 of the General Schedule and shall not exceed the amount of annual compensation (excluding expenses) specified in section 102 of title 3, United States Code.\n##### (h) Administration of program\nThe Secretary of the Treasury (or the Secretary\u2019s delegate) may appoint a lead program officer to administer and advertise the program.\n##### (i) Annual review and report\nNot later than 1 year after the date on which the first fellowship is awarded under this section, and annually thereafter, the Commissioner shall submit to Congress a report containing\u2014\n**(1)**\nan analysis of the effects of the program,\n**(2)**\nan analysis of the return on investment of the program, including calculations of all costs incurred and benefits incurred, which may include predicted revenue increases based on task force recommendations; tax revenue and penalties recommended, assessed, or collected due to the work of the task force; and operational improvements in taxpayer service,\n**(3)**\na description of the total number of fellows who apply each year, and\n**(4)**\nrecommendations for changes to the program, if any.\n##### (j) Rules and regulations\nThe Commissioner, with the approval of the Secretary of the Treasury (or the Secretary\u2019s delegate, other than the Commissioner), shall promulgate such rules and regulations as may be necessary for the efficient administration of the program.\n##### (k) Qualified data scientist defined\nIn this subsection, the term qualified data scientist means a specialized professional who has demonstrated skills applying advanced analytics, statistical modeling, or machine learning in complex regulatory, financial, or compliance environments while working alongside tax law specialists and other tax subject matter experts.",
      "versionDate": "2026-03-18",
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
        "name": "Taxation",
        "updateDate": "2026-03-24T01:40:01Z"
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
      "date": "2026-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7972ih.xml"
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
      "title": "Taxpayer Workforce Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T08:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Taxpayer Workforce Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T08:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Internal Revenue Service to establish a fellowship program within the Internal Revenue Service to recruit qualified data scientists to partner with tax law specialists and provide insights and identify emerging and complex issues in tax administration, ranging from data acquisition and quality through developing advanced analytics, statistics, and models to improve core tax administration activities in services and enforcement.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T08:18:19Z"
    }
  ]
}
```
