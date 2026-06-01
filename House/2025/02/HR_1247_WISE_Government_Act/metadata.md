# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1247?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1247
- Title: WISE Government Act
- Congress: 119
- Bill type: HR
- Bill number: 1247
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2025-05-02T14:43:45Z
- Update date including text: 2025-05-02T14:43:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1247",
    "number": "1247",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "F000454",
        "district": "11",
        "firstName": "Bill",
        "fullName": "Rep. Foster, Bill [D-IL-11]",
        "lastName": "Foster",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "WISE Government Act",
    "type": "HR",
    "updateDate": "2025-05-02T14:43:45Z",
    "updateDateIncludingText": "2025-05-02T14:43:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
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
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:02:00Z",
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
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "IL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1247ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1247\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Mr. Foster (for himself, Mr. Takano , Mr. Quigley , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo secure Federal access to scientific literature and other subscription services by requiring Federal agencies and legislative branch research arms to make recommendations on increasing agency library access to serials, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Well-Informed, Scientific, & Efficient Government Act of 2025 or the WISE Government Act .\n#### 2. Agency journal subscriptions\n##### (a) Prohibition on nondisclosure provision for journal subscriptions\nThe head of an agency may not enter into any contract for a journal subscription that prohibits disclosure of the cost of the subscription to another agency or the Library of Congress.\n##### (b) Employee access to library subscriptions\nNot later than 6 months after the date of the enactment of this Act, the head of each agency shall require that each library of the agency make easily and clearly available to the employees of the agency, including regional employees, through the intranet any policy or procedure for employee access to a subscription of the library.\n##### (c) Report on increasing access to serials\nNot later than 12 months after the date of the enactment of this Act, the Administrator, in consultation with the Library of Congress, the applicable agency libraries, and other relevant stakeholders (including the Defense Technical Information Center, the National Library of Medicine, the Education Resources Information Center, and the National Technical Information Service) shall submit to Congress and each agency library a report on increasing agency library access to serials that includes\u2014\n**(1)**\na survey of subscriptions purchased and cost data for applicable agency libraries and the Library of Congress;\n**(2)**\nan outline of any issues with agency access to scientific serials and subscriptions, which may include contract issues, concerns arising with new publishing media (including print, online, and aggregated services), the ability of agency employees to use agency library subscriptions in headquarters and regional offices, purchasing system inefficiencies, and price concerns; and\n**(3)**\nrecommendations on addressing issues, including short-term and long-term solutions and assessing the potential need for greater interagency transparency and new purchasing models.\n##### (d) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of General Services.\n**(2) Agency**\nThe term agency has the meaning given that term in section 551 of title 5, United States Code.\n**(3) Applicable agency library**\nThe term applicable agency library means the libraries of\u2014\n**(A)**\nthe Executive departments listed in section 101 of title 5, United States Code;\n**(B)**\nthe military departments listed in section 102 of title 5, United States Code; and\n**(C)**\nany agency with a scientific focus, including the Environmental Protection Agency and the National Aeronautics and Space Administration.\n**(4) Director**\nThe term Director means the Director of the Office of Management and Budget.\n##### (e) Rule of construction\nNothing in this section may be construed as requiring the disclosure of matters that are otherwise not subject to disclosure under section 552(b) of title 5, United States Code (commonly referred to as the Freedom of Information Act).",
      "versionDate": "2025-02-12",
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
            "name": "Congressional oversight",
            "updateDate": "2025-05-02T15:00:03Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-05-02T15:00:03Z"
          },
          {
            "name": "Government ethics and transparency, public corruption",
            "updateDate": "2025-05-02T15:00:03Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-05-02T15:00:03Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-05-02T15:00:03Z"
          },
          {
            "name": "Library of Congress",
            "updateDate": "2025-05-02T15:00:03Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-05-02T15:00:03Z"
          },
          {
            "name": "Scientific communication",
            "updateDate": "2025-05-02T15:00:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-04-02T14:31:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
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
          "measure-id": "id119hr1247",
          "measure-number": "1247",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-12",
          "originChamber": "HOUSE",
          "update-date": "2025-05-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1247v00",
            "update-date": "2025-05-02"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Well-Informed, Scientific, &</strong> <strong> Efficient Government Act of 2025 or the WISE Government Act</strong></p><p>This bill prohibits an agency from entering into a contract for a journal subscription that prohibits disclosure of the cost of the subscription to another agency or the Library of Congress.</p><p>Each agency library must make policies and procedures for employee access to library subscriptions easily and clearly available to the agency's employees, including regional employees, through the intranet.</p><p>The General Services Administration must submit to Congress and each agency library a report on increasing agency library access to serials.</p>"
        },
        "title": "WISE Government Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1247.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Well-Informed, Scientific, &</strong> <strong> Efficient Government Act of 2025 or the WISE Government Act</strong></p><p>This bill prohibits an agency from entering into a contract for a journal subscription that prohibits disclosure of the cost of the subscription to another agency or the Library of Congress.</p><p>Each agency library must make policies and procedures for employee access to library subscriptions easily and clearly available to the agency's employees, including regional employees, through the intranet.</p><p>The General Services Administration must submit to Congress and each agency library a report on increasing agency library access to serials.</p>",
      "updateDate": "2025-05-02",
      "versionCode": "id119hr1247"
    },
    "title": "WISE Government Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Well-Informed, Scientific, &</strong> <strong> Efficient Government Act of 2025 or the WISE Government Act</strong></p><p>This bill prohibits an agency from entering into a contract for a journal subscription that prohibits disclosure of the cost of the subscription to another agency or the Library of Congress.</p><p>Each agency library must make policies and procedures for employee access to library subscriptions easily and clearly available to the agency's employees, including regional employees, through the intranet.</p><p>The General Services Administration must submit to Congress and each agency library a report on increasing agency library access to serials.</p>",
      "updateDate": "2025-05-02",
      "versionCode": "id119hr1247"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1247ih.xml"
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
      "title": "WISE Government Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-14T09:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "WISE Government Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Well-Informed, Scientific, & Efficient Government Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To secure Federal access to scientific literature and other subscription services by requiring Federal agencies and legislative branch research arms to make recommendations on increasing agency library access to serials, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T09:18:27Z"
    }
  ]
}
```
