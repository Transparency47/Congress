# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5908?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5908
- Title: Non-Essential Workers Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 5908
- Origin chamber: House
- Introduced date: 2025-11-04
- Update date: 2025-12-04T09:07:00Z
- Update date including text: 2025-12-04T09:07:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-11-04: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-11-04: Introduced in House

## Actions

- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-04",
    "latestAction": {
      "actionDate": "2025-11-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5908",
    "number": "5908",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "F000472",
        "district": "18",
        "firstName": "Scott",
        "fullName": "Rep. Franklin, Scott [R-FL-18]",
        "lastName": "Franklin",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Non-Essential Workers Transparency Act",
    "type": "HR",
    "updateDate": "2025-12-04T09:07:00Z",
    "updateDateIncludingText": "2025-12-04T09:07:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-04",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-04",
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
          "date": "2025-11-04T19:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "FL"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "NY"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "VA"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "FL"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "TX"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "VA"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "FL"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5908ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5908\nIN THE HOUSE OF REPRESENTATIVES\nNovember 4, 2025 Mr. Scott Franklin of Florida (for himself, Mr. Webster of Florida , Ms. Stefanik , Mr. Cline , Mr. Buchanan , and Mr. Fallon ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require Executive agencies to submit reports to Congress regarding employees who are furloughed during any period during which there is a lapse in appropriations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Non-Essential Workers Transparency Act .\n#### 2. Reporting requirements\n##### (a) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means, with respect to an Executive agency\u2014\n**(A)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate;\n**(B)**\nthe Committee on Oversight and Government Reform of the House of Representatives; and\n**(C)**\nany other committee of Congress with jurisdiction with respect to the Executive agency.\n**(2) Covered employee**\nThe term covered employee means an employee of an Executive agency who is furloughed (as defined in section 7511(a) of title 5, United States Code) during a covered period with respect to that Executive agency.\n**(3) Covered period**\nThe term covered period means, with respect to an Executive agency, a period beginning on the date which a lapse in appropriations with respect to such Executive agency begins and ending on the date on which such lapse in appropriation ends.\n**(4) Executive agency**\nThe term Executive agency has the meaning given the term in section 105 of title 5, United States Code.\n##### (b) Requirements\nNot later than 30 days after the date on which a covered period with respect to an Executive agency ends, the Under Secretary (or the equivalent) of that Executive agency shall electronically submit to the appropriate congressional committees with respect to that Executive agency a report that contains\u2014\n**(1)**\nthe total number of employees (including contract employees) employed by the Executive agency, as of the day before the day on which that covered period began;\n**(2)**\nthe total amount expended by the Executive agency on salaries of employees during the fiscal year preceding the fiscal year in which that covered period began;\n**(3)**\nthe total number of employees of the Executive agency who were covered employees during that covered period;\n**(4)**\nthe sum obtained by adding the annual rate of basic pay of each employee described in paragraph (3);\n**(5)**\nthe total number of employees of the Executive agency who were not covered employees during that covered period; and\n**(6)**\nthe sum obtained by adding the annual rate of basic pay of each employee described in paragraph (5).\n##### (c) Procedures\n**(1) Classification**\nEach Executive agency submitting a report under subsection (b), or an update to such a report, shall submit that report or update in unclassified form, but that report or update may include a classified annex.\n**(2) Publication**\nNot later than 30 days after the date on which an appropriate congressional committee receives a report submitted under subsection (b), that appropriate congressional committee shall publish the report on the website of the appropriate congressional committee.\n##### (d) Economic effect report\nNot later than 30 days after the date on which a covered period ends, the Director of the Congressional Budget Office shall submit to Congress and make publicly available on a website of the Congressional Budget Office a report on the effects on the economy of the United States of the lapse in appropriations occurring during such covered period.",
      "versionDate": "2025-11-04",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-10-14",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "3005",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Non-Essential Workers Transparency Act",
      "type": "S"
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
        "updateDate": "2025-11-06T14:37:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-04",
    "originChamber": "House",
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
          "measure-id": "id119hr5908",
          "measure-number": "5908",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-04",
          "originChamber": "HOUSE",
          "update-date": "2025-11-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5908v00",
            "update-date": "2025-11-06"
          },
          "action-date": "2025-11-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Non-Essential Workers Transparency Act</strong></p><p>This bill requires federal agencies to submit reports to Congress\u00a0regarding employees who were furloughed during a lapse in appropriations (i.e, government shutdown), the total number of employees, and the cost of salaries.\u00a0</p><p>Specifically, each federal agency must submit a report to specified congressional committees\u00a0within 30 days of the end of a lapse in appropriations. The report must include specified details regarding</p><ul><li>the total number of employees (including contract employees) employed by the agency before the lapse began,</li><li>the total number of employees who were furloughed during the lapse,</li><li>the total number of employees who were not furloughed during the lapse, and\u00a0</li><li>the total annual cost of the salaries for each group of employees.\u00a0</li></ul><p>The report must be submitted in an unclassified form, but it may include a classified annex. Each congressional committee that receives a report must publish the report on its website within 30 days.\u00a0</p><p>The bill also requires the Congressional Budget Office (CBO) to submit a report to Congress\u00a0regarding the economic effects of each lapse in appropriations.\u00a0CBO must submit the report within 30 days of the end of a lapse in appropriations and make the report available on its website.\u00a0</p>"
        },
        "title": "Non-Essential Workers Transparency Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5908.xml",
    "summary": {
      "actionDate": "2025-11-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Non-Essential Workers Transparency Act</strong></p><p>This bill requires federal agencies to submit reports to Congress\u00a0regarding employees who were furloughed during a lapse in appropriations (i.e, government shutdown), the total number of employees, and the cost of salaries.\u00a0</p><p>Specifically, each federal agency must submit a report to specified congressional committees\u00a0within 30 days of the end of a lapse in appropriations. The report must include specified details regarding</p><ul><li>the total number of employees (including contract employees) employed by the agency before the lapse began,</li><li>the total number of employees who were furloughed during the lapse,</li><li>the total number of employees who were not furloughed during the lapse, and\u00a0</li><li>the total annual cost of the salaries for each group of employees.\u00a0</li></ul><p>The report must be submitted in an unclassified form, but it may include a classified annex. Each congressional committee that receives a report must publish the report on its website within 30 days.\u00a0</p><p>The bill also requires the Congressional Budget Office (CBO) to submit a report to Congress\u00a0regarding the economic effects of each lapse in appropriations.\u00a0CBO must submit the report within 30 days of the end of a lapse in appropriations and make the report available on its website.\u00a0</p>",
      "updateDate": "2025-11-06",
      "versionCode": "id119hr5908"
    },
    "title": "Non-Essential Workers Transparency Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Non-Essential Workers Transparency Act</strong></p><p>This bill requires federal agencies to submit reports to Congress\u00a0regarding employees who were furloughed during a lapse in appropriations (i.e, government shutdown), the total number of employees, and the cost of salaries.\u00a0</p><p>Specifically, each federal agency must submit a report to specified congressional committees\u00a0within 30 days of the end of a lapse in appropriations. The report must include specified details regarding</p><ul><li>the total number of employees (including contract employees) employed by the agency before the lapse began,</li><li>the total number of employees who were furloughed during the lapse,</li><li>the total number of employees who were not furloughed during the lapse, and\u00a0</li><li>the total annual cost of the salaries for each group of employees.\u00a0</li></ul><p>The report must be submitted in an unclassified form, but it may include a classified annex. Each congressional committee that receives a report must publish the report on its website within 30 days.\u00a0</p><p>The bill also requires the Congressional Budget Office (CBO) to submit a report to Congress\u00a0regarding the economic effects of each lapse in appropriations.\u00a0CBO must submit the report within 30 days of the end of a lapse in appropriations and make the report available on its website.\u00a0</p>",
      "updateDate": "2025-11-06",
      "versionCode": "id119hr5908"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5908ih.xml"
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
      "title": "Non-Essential Workers Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-05T09:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Non-Essential Workers Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-05T09:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require Executive agencies to submit reports to Congress regarding employees who are furloughed during any period during which there is a lapse in appropriations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-05T09:18:18Z"
    }
  ]
}
```
