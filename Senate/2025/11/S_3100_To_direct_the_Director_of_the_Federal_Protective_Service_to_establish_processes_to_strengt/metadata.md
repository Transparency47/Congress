# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3100?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3100
- Title: POST Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3100
- Origin chamber: Senate
- Introduced date: 2025-11-04
- Update date: 2026-04-21T19:59:11Z
- Update date including text: 2026-04-21T19:59:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-04: Introduced in Senate
- 2025-11-04 - IntroReferral: Introduced in Senate
- 2025-11-04 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-11-04: Introduced in Senate

## Actions

- 2025-11-04 - IntroReferral: Introduced in Senate
- 2025-11-04 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3100",
    "number": "3100",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "POST Act of 2025",
    "type": "S",
    "updateDate": "2026-04-21T19:59:11Z",
    "updateDateIncludingText": "2026-04-21T19:59:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-04",
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
      "actionDate": "2025-11-04",
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
            "date": "2025-11-04T22:29:45Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-04T22:29:45Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "NH"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3100is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3100\nIN THE SENATE OF THE UNITED STATES\nNovember 4, 2025 Mr. Curtis (for himself and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo direct the Director of the Federal Protective Service to establish processes to strengthen oversight, performance, and accountability of contract security personnel engaged in the protection of certain buildings and grounds, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Personnel Oversight and Shift Tracking Act of 2025 or the POST Act of 2025 .\n#### 2. Improved data collection and performance accountability\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Director of the Federal Protective Service shall establish processes to strengthen oversight, performance, and accountability of contract security personnel engaged in the protection of buildings and grounds that are owned, occupied, or secured by the General Services Administration Public Buildings Service.\n##### (b) Oversight of contract security personnel\nIn carrying out the activities described in subsection (a), the Director shall\u2014\n**(1)**\nestablish standards for the collection, maintenance, and analysis of covert testing data, including the creation of a comprehensive and uniform method for documenting test outcomes, identifying root causes of failures, and categorizing types of vulnerabilities detected;\n**(2)**\nbegin conducting quarterly analytical reviews of covert testing data to identify trends, recurring deficiencies, and opportunities for operational improvement across all covered facilities;\n**(3)**\ndirect the security contractor who is providing security services to the Federal Protective Service to establish a mandatory, cause-specific corrective training and performance improvement plan for any contract security personnel who fail a covert test and review the security contractor\u2019s performance improvement plan to ensure that the security contractor has and will provide appropriate training and procedures to avoid any future covert testing failures; and\n**(4)**\ndevelop updated security training guidance for contract security personnel to reflect findings from covert testing data, emerging threats, and best practices.\n##### (c) Report to Congress\nUpon completion of the activities described in subsection (b), and annually thereafter, the Director shall submit to the Committee on Transportation and Infrastructure of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report on the implementation of the requirements of this section, including any identified challenges and recommendations for additional legislative action.\n#### 3. Personnel shift management and system modernization\n##### (a) Evaluation of the personnel tracking system\nNot later than 180 days after the date of enactment of this Act, the Director of the Federal Protective Service shall\u2014\n**(1)**\nconduct a comprehensive evaluation of the personnel tracking system used to manage and monitor the deployment availability of contract security personnel;\n**(2)**\ndetermine whether to replace the system described in paragraph (1) with a more reliable personnel tracking platform, including private sector solutions, or whether to implement corrective actions to improve the system described in paragraph (1), including technical, operational, or administrative fixes; and\n**(3)**\ndevelop and publish an implementation plan that includes\u2014\n**(A)**\na timeline for completion of system replacement or corrective actions; and\n**(B)**\nprocedures to ensure timely and accurate communication to building tenants regarding contract security personnel shortages or absences or security coverage gaps.\n##### (b) Report to Congress\nNot later than 1 year after the date of enactment of this Act, and annually thereafter for 3 years, the Director shall submit to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives a report that includes\u2014\n**(1)**\nthe determination made under subsection (a)(2);\n**(2)**\na detailed summary of any implementation actions undertaken pursuant to subsection (a);\n**(3)**\nan evaluation of the effectiveness of tenant communication protocols; and\n**(4)**\nany recommendations for additional legislative or administrative actions.\n#### 4. Savings clause\nNothing in this Act shall be construed as designating an employee of a contractor of the Department of Homeland Security who is engaged in the protection of Federal property pursuant to section 1315 of title 40, United States Code, as a Federal employee.",
      "versionDate": "2025-11-04",
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
        "actionDate": "2025-09-09",
        "text": "Received in the Senate and Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "3425",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Personnel Oversight and Shift Tracking Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Computers and information technology",
            "updateDate": "2026-04-09T15:33:32Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-09T15:33:32Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-09T15:33:32Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2026-04-09T15:33:32Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2026-04-09T15:33:32Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2026-04-09T15:33:32Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2026-04-09T15:33:32Z"
          },
          {
            "name": "Personnel records",
            "updateDate": "2026-04-09T15:33:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-12-02T20:31:35Z"
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
      "date": "2025-11-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3100is.xml"
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
      "title": "POST Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-14T12:03:37Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "POST Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-08T05:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Personnel Oversight and Shift Tracking Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-08T05:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Director of the Federal Protective Service to establish processes to strengthen oversight, performance, and accountability of contract security personnel engaged in the protection of certain buildings and grounds, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-08T05:18:16Z"
    }
  ]
}
```
