# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/357?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/357
- Title: Back to Work Act
- Congress: 119
- Bill type: HR
- Bill number: 357
- Origin chamber: House
- Introduced date: 2025-01-13
- Update date: 2025-05-27T21:27:51Z
- Update date including text: 2025-05-27T21:27:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-01-13: Introduced in House

## Actions

- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/357",
    "number": "357",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
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
    "title": "Back to Work Act",
    "type": "HR",
    "updateDate": "2025-05-27T21:27:51Z",
    "updateDateIncludingText": "2025-05-27T21:27:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-13",
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
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T17:04:05Z",
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
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr357ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 357\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2025 Mr. Nunn of Iowa (for himself and Mr. Newhouse ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 5, United States Code, to provide limitations on Federal teleworking, and for other purposes.\n#### 1. Short title\nThis title may be cited as the Back to Work Act .\n#### 2. Modification of telework requirements for Federal employees\n##### (a) In general\nChapter 65 of title 5, United States Code, is amended\u2014\n**(1)**\nin section 6502\u2014\n**(A)**\nin subsection (b)(2)\u2014\n**(i)**\nin subparagraph (A), by striking and at the end; and\n**(ii)**\nby adding at the end the following:\n(C) provides that, subject to subsection (d), an employee may not telework for more than 40 percent of the work days of the employee per pay period; (D) shall be reviewed on an annual basis by, and be subject to the annual approval of, the head of the executive agency; and (E) provides that the executive agency, by using remote technical means and other appropriate methods, will monitor and evaluate the applicable employee when the employee is engaged in telework; ; and\n**(B)**\nby adding at the end the following:\n(d) Adjustments to the permitted number of telework days With respect to the limitation under subsection (b)(2)(C), the head of an executive agency may\u2014 (1) further limit the number of work days per pay period that an employee of the executive agency may telework based on the specific role of the employee or other circumstances determined appropriate by the head of the executive agency, including\u2014 (A) the frequency with which the employee needs to access classified information; (B) whether the employee is newly appointed; and (C) whether the employee occupies a managerial position within the executive agency; or (2) waive that limitation with respect to an employee of the executive agency if\u2014 (A) the employee is a spouse of\u2014 (i) a member of the Armed Forces; or (ii) a Federal law enforcement officer; (B) the employee occupies a position\u2014 (i) the duties of which require\u2014 (I) highly specialized expertise; or (II) frequent travel; or (ii) for which finding qualified candidates is challenging; or (C) inclement weather or other exigent circumstances prevent the employee from reaching the worksite of the employee during a pay period. (e) Limitations on pay With respect to any employee who has entered into a written agreement under subsection (b)(2), and notwithstanding any other provision of this title, such employee shall\u2014 (1) not be eligible for any adjustment to pay under section 5303; and (2) receive locality-based comparability payments under section 5304 or 5304a at the percentage for the Rest of United States locality pay area. ; and\n**(2)**\nin section 6506, by adding at the end the following:\n(e) Executive agency reports (1) In general Not later than 1 year after the date of enactment of this subsection, and annually thereafter, the head of each executive agency shall submit to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Government Reform of the House of Representatives a report that describes, for the period covered by the report, the following: (A) What metrics and methods the executive agency uses to determine the productivity of employees who telework. (B) What barriers, if any, prevent the executive agency from enforcing the limitation under section 6502(b)(2)(C) and any initiatives of the executive agency to address those barriers. (C) Any negative effects of telework, including whether telework results in increased costs, security vulnerabilities, lower employee morale, decreased employee productivity, or waste, fraud, or abuse. (D) Any actions taken by the executive agency (or a detailed justification for any lack of action) in response to any findings of, or recommendations made by, the Inspector General of the executive agency with respect to telework. (2) GAO report With respect to each report submitted by the head of an executive agency under paragraph (1), the Comptroller General of the United States shall submit an accompanying report that evaluates the accuracy and thoroughness of the report submitted by the head of the executive agency with respect to the matters required to be included in the report of the executive agency under that paragraph. .\n##### (b) Effective date\nThe amendments made by subsection (a) shall take effect on the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "2025-01-13",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Commuting",
            "updateDate": "2025-03-05T16:11:10Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-03-05T16:11:16Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-05T16:11:21Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-03-05T16:11:05Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-26T20:07:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119hr357",
          "measure-number": "357",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-13",
          "originChamber": "HOUSE",
          "update-date": "2025-05-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr357v00",
            "update-date": "2025-05-27"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Back to Work Act</strong></p><p>This bill limits\u00a0federal agency employees' telework to up to 40% of the work days\u00a0in any pay period and eliminates certain pay increases for teleworking employees.</p><p>Under current law, executive agencies must maintain policies detailing how their employees may work remotely and enter into telework agreements with participating employees. The bill requires telework agreements to cap employees' telework at 40% of the work days\u00a0in a pay period, specify\u00a0that the agency will monitor employees' telework via remote technical methods, and make telework\u00a0subject to annual review by the agency.\u00a0The bill also\u00a0eliminates locality-based and automatic annual pay adjustments for employees with telework agreements.</p><p>The bill authorizes agencies to further restrict the amount of telework permitted based on an employee's specific role or other circumstances (e.g., working with classified information). Agencies may also waive the limitation for inclement weather or\u00a0exigent circumstances or for an employee who (1) is married to a member of the Armed Forces or federal law enforcement officer; (2) holds a position requiring highly specialized experience or frequent travel; or (3) holds a\u00a0position that is difficult to fill.</p><p>Additionally, the bill requires annual agency reports to Congress\u00a0describing the effectiveness of agency telework policies. The Government Accountability Office must evaluate the accuracy and thoroughness of each report\u00a0in an accompanying report to Congress.</p>"
        },
        "title": "Back to Work Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr357.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Back to Work Act</strong></p><p>This bill limits\u00a0federal agency employees' telework to up to 40% of the work days\u00a0in any pay period and eliminates certain pay increases for teleworking employees.</p><p>Under current law, executive agencies must maintain policies detailing how their employees may work remotely and enter into telework agreements with participating employees. The bill requires telework agreements to cap employees' telework at 40% of the work days\u00a0in a pay period, specify\u00a0that the agency will monitor employees' telework via remote technical methods, and make telework\u00a0subject to annual review by the agency.\u00a0The bill also\u00a0eliminates locality-based and automatic annual pay adjustments for employees with telework agreements.</p><p>The bill authorizes agencies to further restrict the amount of telework permitted based on an employee's specific role or other circumstances (e.g., working with classified information). Agencies may also waive the limitation for inclement weather or\u00a0exigent circumstances or for an employee who (1) is married to a member of the Armed Forces or federal law enforcement officer; (2) holds a position requiring highly specialized experience or frequent travel; or (3) holds a\u00a0position that is difficult to fill.</p><p>Additionally, the bill requires annual agency reports to Congress\u00a0describing the effectiveness of agency telework policies. The Government Accountability Office must evaluate the accuracy and thoroughness of each report\u00a0in an accompanying report to Congress.</p>",
      "updateDate": "2025-05-27",
      "versionCode": "id119hr357"
    },
    "title": "Back to Work Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Back to Work Act</strong></p><p>This bill limits\u00a0federal agency employees' telework to up to 40% of the work days\u00a0in any pay period and eliminates certain pay increases for teleworking employees.</p><p>Under current law, executive agencies must maintain policies detailing how their employees may work remotely and enter into telework agreements with participating employees. The bill requires telework agreements to cap employees' telework at 40% of the work days\u00a0in a pay period, specify\u00a0that the agency will monitor employees' telework via remote technical methods, and make telework\u00a0subject to annual review by the agency.\u00a0The bill also\u00a0eliminates locality-based and automatic annual pay adjustments for employees with telework agreements.</p><p>The bill authorizes agencies to further restrict the amount of telework permitted based on an employee's specific role or other circumstances (e.g., working with classified information). Agencies may also waive the limitation for inclement weather or\u00a0exigent circumstances or for an employee who (1) is married to a member of the Armed Forces or federal law enforcement officer; (2) holds a position requiring highly specialized experience or frequent travel; or (3) holds a\u00a0position that is difficult to fill.</p><p>Additionally, the bill requires annual agency reports to Congress\u00a0describing the effectiveness of agency telework policies. The Government Accountability Office must evaluate the accuracy and thoroughness of each report\u00a0in an accompanying report to Congress.</p>",
      "updateDate": "2025-05-27",
      "versionCode": "id119hr357"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr357ih.xml"
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
      "title": "Back to Work Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Back to Work Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 5, United States Code, to provide limitations on Federal teleworking, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:03:26Z"
    }
  ]
}
```
