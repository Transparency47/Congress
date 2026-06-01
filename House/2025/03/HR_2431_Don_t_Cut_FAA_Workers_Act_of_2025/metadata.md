# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2431?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2431
- Title: Don't Cut FAA Workers Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2431
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2025-08-11T19:06:43Z
- Update date including text: 2025-08-11T19:06:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-27 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-27 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2431",
    "number": "2431",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Don't Cut FAA Workers Act of 2025",
    "type": "HR",
    "updateDate": "2025-08-11T19:06:43Z",
    "updateDateIncludingText": "2025-08-11T19:06:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:04:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-27T20:47:51Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "systemCode": "hspw00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2431ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2431\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Mr. Gottheimer introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to limit mass layoffs of employees of the Federal Aviation Administration within 1 year of a major aviation accident, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Don't Cut FAA Workers Act of 2025 .\n#### 2. Limitation on mass layoffs in event of major aviation accident\n##### (a) In general\nChapter 401 of title 49, United States Code, is amended by adding at the end the following:\n40133. Limitation on mass layoffs in event of major aviation accident. (a) Limitation on mass layoffs Except as provided in subparagraph (b), the Administrator of the Federal Aviation Administration may not carry out, or otherwise facilitate, a mass layoff during the 1-year period following a major aviation accident in air transportation. (b) Congressional approval for mass layoff (1) Notification Before carrying out a mass layoff described in subsection (a), the Administrator shall submit to Congress notification of such a layoff that includes the number and type of employees proposed to be laid off. (2) Congressional approval In any case in which, not later than 60 days after receipt of a notification under paragraph (1), Congress enacts a joint resolution approving the proposed mass layoff for which such notification was submitted, the Administrator may carry out such mass layoff. (c) Definitions In this section: (1) Mass layoff The term \u2018mass layoff\u2019 means a reduction in force or other termination of employment that results in a personnel loss during any 90-day period\u2014 (A) of 10 or more employees of the Federal Aviation Administration at a single site of employment, as calculated under paragraph (2); or (B) of 250 or more employees of the Administration, irrespective of employment site. (2) Calculation The number of employees at a single site of employment who suffer an employment loss shall be calculated in a manner that includes\u2014 (A) all such employees who work at the physical location of the site; and (B) all such employees who work remotely and\u2014 (i) are assigned to or otherwise associated with the site; (ii) receive assignments or training from the site; (iii) report to a manager associated with the site; or (iv) whose job loss was a foreseeable consequence of a reduction in force or other termination of employment at the site. (3) Major aviation accident The term \u201cmajor aviation accident\u201d means an aircraft accident in which a fatal aviation injury occurs. (4) Aircraft accident The term aircraft accident means an occurrence associated with the operation of a civil aircraft that takes place between the time any individual boards the aircraft with the intention of flight and the time at which the last individual disembarks such aircraft in which any individual suffers death or serious injury, or in which the aircraft receives substantial damage. (5) Fatal aviation injury The term fatal aviation injury means any injury due to an aircraft accident that results in the death of an individual as a result of such accident within 30 days of such accident. .\n##### (b) Clerical amendment\nThe analysis for chapter 401 of title 49, United States Code, is amended by adding at the end the following:\n40133. Limitation on reduction in force. .",
      "versionDate": "2025-03-27",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-02T10:46:30Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-27",
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
          "measure-id": "id119hr2431",
          "measure-number": "2431",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-27",
          "originChamber": "HOUSE",
          "update-date": "2025-08-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2431v00",
            "update-date": "2025-08-11"
          },
          "action-date": "2025-03-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Don't Cut FAA Workers Act of 2025</strong></p><p>This bill prohibits the Federal Aviation Administration (FAA) from carrying out a mass layoff within one\u00a0year of a major aviation accident\u00a0(i.e., an aircraft accident in which a fatal aviation injury occurs), unless the FAA receives congressional approval.\u00a0</p><p>Specifically, the FAA must notify Congress of plans to carry out or\u00a0facilitate a mass layoff following a major aviation accident. The notification must\u00a0include\u00a0the number and type of employees proposed to be laid off. The FAA may only carry out the layoff if Congress enacts a joint resolution approving the proposal no later than 60 days after receiving the notification.</p><p>Under the bill, a\u00a0<em>mass layoff</em> means a reduction in force or other termination of employment that results in a personnel loss during any 90-day period of (1) 10 or more FAA employees at a single\u00a0employment site; or (2) 250 or more FAA employees, irrespective of the employment site.</p>"
        },
        "title": "Don't Cut FAA Workers Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2431.xml",
    "summary": {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Don't Cut FAA Workers Act of 2025</strong></p><p>This bill prohibits the Federal Aviation Administration (FAA) from carrying out a mass layoff within one\u00a0year of a major aviation accident\u00a0(i.e., an aircraft accident in which a fatal aviation injury occurs), unless the FAA receives congressional approval.\u00a0</p><p>Specifically, the FAA must notify Congress of plans to carry out or\u00a0facilitate a mass layoff following a major aviation accident. The notification must\u00a0include\u00a0the number and type of employees proposed to be laid off. The FAA may only carry out the layoff if Congress enacts a joint resolution approving the proposal no later than 60 days after receiving the notification.</p><p>Under the bill, a\u00a0<em>mass layoff</em> means a reduction in force or other termination of employment that results in a personnel loss during any 90-day period of (1) 10 or more FAA employees at a single\u00a0employment site; or (2) 250 or more FAA employees, irrespective of the employment site.</p>",
      "updateDate": "2025-08-11",
      "versionCode": "id119hr2431"
    },
    "title": "Don't Cut FAA Workers Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Don't Cut FAA Workers Act of 2025</strong></p><p>This bill prohibits the Federal Aviation Administration (FAA) from carrying out a mass layoff within one\u00a0year of a major aviation accident\u00a0(i.e., an aircraft accident in which a fatal aviation injury occurs), unless the FAA receives congressional approval.\u00a0</p><p>Specifically, the FAA must notify Congress of plans to carry out or\u00a0facilitate a mass layoff following a major aviation accident. The notification must\u00a0include\u00a0the number and type of employees proposed to be laid off. The FAA may only carry out the layoff if Congress enacts a joint resolution approving the proposal no later than 60 days after receiving the notification.</p><p>Under the bill, a\u00a0<em>mass layoff</em> means a reduction in force or other termination of employment that results in a personnel loss during any 90-day period of (1) 10 or more FAA employees at a single\u00a0employment site; or (2) 250 or more FAA employees, irrespective of the employment site.</p>",
      "updateDate": "2025-08-11",
      "versionCode": "id119hr2431"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2431ih.xml"
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
      "title": "Don't Cut FAA Workers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-16T02:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Don't Cut FAA Workers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-16T02:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to limit mass layoffs of employees of the Federal Aviation Administration within 1 year of a major aviation accident, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-16T02:48:15Z"
    }
  ]
}
```
