# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3005?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3005
- Title: Non-Essential Workers Transparency Act
- Congress: 119
- Bill type: S
- Bill number: 3005
- Origin chamber: Senate
- Introduced date: 2025-10-14
- Update date: 2025-11-06T14:37:41Z
- Update date including text: 2025-11-06T14:37:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-14: Introduced in Senate
- 2025-10-14 - IntroReferral: Introduced in Senate
- 2025-10-14 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-10-14: Introduced in Senate

## Actions

- 2025-10-14 - IntroReferral: Introduced in Senate
- 2025-10-14 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-14",
    "latestAction": {
      "actionDate": "2025-10-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3005",
    "number": "3005",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Non-Essential Workers Transparency Act",
    "type": "S",
    "updateDate": "2025-11-06T14:37:41Z",
    "updateDateIncludingText": "2025-11-06T14:37:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-14",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-14",
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
          "date": "2025-10-14T20:59:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3005is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3005\nIN THE SENATE OF THE UNITED STATES\nOctober 14, 2025 Ms. Ernst introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require Executive agencies to submit reports to Congress and to the Office of Personnel Management regarding employees who are furloughed during any period during which there is a lapse in appropriations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Non-Essential Workers Transparency Act .\n#### 2. Reporting requirements\n##### (a) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means, with respect to an Executive agency\u2014\n**(A)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate;\n**(B)**\nthe Committee on Oversight and Government Reform of the House of Representatives; and\n**(C)**\nany other committee of Congress with jurisdiction with respect to the Executive agency.\n**(2) Covered employee**\nThe term covered employee means an employee of an Executive agency who is subject to furlough during a covered period with respect to that Executive agency.\n**(3) Covered period**\nThe term covered period means a period during which there is a lapse in appropriations with respect to an Executive agency.\n**(4) Director**\nThe term Director means the Director of the Office of Personnel Management.\n**(5) Executive agency**\nThe term Executive agency has the meaning given the term in section 105 of title 5, United States Code.\n##### (b) Requirements\nNot later than 30 days after the date on which a covered period with respect to an Executive agency ends, the Under Secretary (or the equivalent) of that Executive agency shall electronically submit to the appropriate congressional committees with respect to that Executive agency, and to the Director, a report that contains\u2014\n**(1)**\nthe total number of employees (including contract employees) employed by the Executive agency, as of the day before the day on which that covered period began;\n**(2)**\nthe total amount expended by the Executive agency on salaries of employees during the fiscal year preceding the fiscal year in which that covered period began;\n**(3)**\nthe total number of employees of the Executive agency who were covered employees during that covered period;\n**(4)**\nthe sum obtained by adding the annual rate of basic pay of each employee described in paragraph (3);\n**(5)**\nthe total number of employees of the Executive agency who were not covered employees during that covered period; and\n**(6)**\nthe sum obtained by adding the annual rate of basic pay of each employee described in paragraph (5).\n##### (c) Procedures\n**(1) Classification**\nEach Executive agency submitting a report under subsection (b), or an update to such a report, shall submit that report or update in unclassified form, but that report or update may include a classified annex.\n**(2) Publication**\nNot later than 30 days after the date on which an appropriate congressional committee receives a report submitted under subsection (b), that appropriate congressional committee shall publish the report on the website of the appropriate congressional committee.\n**(3) OPM requirements**\nNot later than 60 days after the date on which a covered period with respect to 1 or more Executive agencies ends, the Director shall\u2014\n**(A)**\nconsolidate all reports submitted to the Director under subsection (b) with respect to that covered period into a single report; and\n**(B)**\npublish the consolidated report created under subparagraph (A) on the website of the Office of Personnel Management.",
      "versionDate": "2025-10-14",
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
        "actionDate": "2025-11-04",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "5908",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Non-Essential Workers Transparency Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-10-24T12:42:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-14",
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
          "measure-id": "id119s3005",
          "measure-number": "3005",
          "measure-type": "s",
          "orig-publish-date": "2025-10-14",
          "originChamber": "SENATE",
          "update-date": "2025-10-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3005v00",
            "update-date": "2025-10-27"
          },
          "action-date": "2025-10-14",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Non-Essential Workers Transparency Act</strong></p><p>This bill requires federal agencies to submit reports to Congress and the Office of Personnel Management (OPM) regarding employees who were furloughed during a lapse in appropriations (i.e, government shutdown), the total number of employees, and the cost of salaries.\u00a0</p><p>Specifically, each federal agency\u00a0must submit a report to specified congressional committees and OPM within 30 days of the end of a lapse in appropriations. The report must include specified details regarding</p><ul><li>the total number of employees (including contract employees) employed by the agency before the lapse began,</li><li>the total number of employees who were furloughed during the lapse,</li><li>the total number of employees who were not furloughed during the lapse, and\u00a0</li><li>the total annual cost of the salaries for each group of employees.\u00a0</li></ul><p>The report must be submitted in an unclassified form, but it may include a classified annex. Each congressional committee that receives a report must publish the report on its website within 30 days.\u00a0</p><p>OPM must consolidate all of the reports submitted with respect to a lapse in appropriations and publish the consolidated report on its website.\u00a0</p>"
        },
        "title": "Non-Essential Workers Transparency Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3005.xml",
    "summary": {
      "actionDate": "2025-10-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Non-Essential Workers Transparency Act</strong></p><p>This bill requires federal agencies to submit reports to Congress and the Office of Personnel Management (OPM) regarding employees who were furloughed during a lapse in appropriations (i.e, government shutdown), the total number of employees, and the cost of salaries.\u00a0</p><p>Specifically, each federal agency\u00a0must submit a report to specified congressional committees and OPM within 30 days of the end of a lapse in appropriations. The report must include specified details regarding</p><ul><li>the total number of employees (including contract employees) employed by the agency before the lapse began,</li><li>the total number of employees who were furloughed during the lapse,</li><li>the total number of employees who were not furloughed during the lapse, and\u00a0</li><li>the total annual cost of the salaries for each group of employees.\u00a0</li></ul><p>The report must be submitted in an unclassified form, but it may include a classified annex. Each congressional committee that receives a report must publish the report on its website within 30 days.\u00a0</p><p>OPM must consolidate all of the reports submitted with respect to a lapse in appropriations and publish the consolidated report on its website.\u00a0</p>",
      "updateDate": "2025-10-27",
      "versionCode": "id119s3005"
    },
    "title": "Non-Essential Workers Transparency Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Non-Essential Workers Transparency Act</strong></p><p>This bill requires federal agencies to submit reports to Congress and the Office of Personnel Management (OPM) regarding employees who were furloughed during a lapse in appropriations (i.e, government shutdown), the total number of employees, and the cost of salaries.\u00a0</p><p>Specifically, each federal agency\u00a0must submit a report to specified congressional committees and OPM within 30 days of the end of a lapse in appropriations. The report must include specified details regarding</p><ul><li>the total number of employees (including contract employees) employed by the agency before the lapse began,</li><li>the total number of employees who were furloughed during the lapse,</li><li>the total number of employees who were not furloughed during the lapse, and\u00a0</li><li>the total annual cost of the salaries for each group of employees.\u00a0</li></ul><p>The report must be submitted in an unclassified form, but it may include a classified annex. Each congressional committee that receives a report must publish the report on its website within 30 days.\u00a0</p><p>OPM must consolidate all of the reports submitted with respect to a lapse in appropriations and publish the consolidated report on its website.\u00a0</p>",
      "updateDate": "2025-10-27",
      "versionCode": "id119s3005"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3005is.xml"
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
      "title": "Non-Essential Workers Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-05T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Non-Essential Workers Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-23T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require Executive agencies to submit reports to Congress and to the Office of Personnel Management regarding employees who are furloughed during any period during which there is a lapse in appropriations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-23T02:48:25Z"
    }
  ]
}
```
