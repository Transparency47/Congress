# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/567?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/567
- Title: Expanding Labor Representation in the Workforce System Act
- Congress: 119
- Bill type: HR
- Bill number: 567
- Origin chamber: House
- Introduced date: 2025-01-20
- Update date: 2025-07-31T13:29:19Z
- Update date including text: 2025-07-31T13:29:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-20: Introduced in House
- 2025-01-20 - IntroReferral: Introduced in House
- 2025-01-20 - IntroReferral: Introduced in House
- 2025-01-20 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-01-20: Introduced in House

## Actions

- 2025-01-20 - IntroReferral: Introduced in House
- 2025-01-20 - IntroReferral: Introduced in House
- 2025-01-20 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-20",
    "latestAction": {
      "actionDate": "2025-01-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/567",
    "number": "567",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "S001207",
        "district": "11",
        "firstName": "Mikie",
        "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
        "lastName": "Sherrill",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Expanding Labor Representation in the Workforce System Act",
    "type": "HR",
    "updateDate": "2025-07-31T13:29:19Z",
    "updateDateIncludingText": "2025-07-31T13:29:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-20",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-20",
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
          "date": "2025-01-20T15:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-20",
      "state": "PA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-01-20",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr567ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 567\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 20, 2025 Ms. Sherrill (for herself, Mr. Fitzpatrick , and Mrs. Hayes ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo expand labor representation on State and local workforce development boards, to provide a definition of labor organization, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Expanding Labor Representation in the Workforce System Act .\n#### 2. State workforce development boards\nSection 101(b)(1)(C)(ii) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3111(b)(1)(C)(ii) ) is amended by striking 20 percent and inserting 30 percent .\n#### 3. Local workforce development boards\nSection 107(b)(2)(B) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3122(b)(2)(B) ) is amended by striking 20 and inserting 30 .\n#### 4. Definition of labor organization\nSection 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ) is amended by adding at the end the following:\n(72) Labor organization The term labor organization has the meaning given the term in section 2(5) of the National Labor Relations Act ( 29 U.S.C. 152(5) ), except that such term shall also include\u2014 (A) any organization composed of labor organizations, such as a labor union federation or a State or municipal labor body; and (B) any organization which would be included in the definition for such term under such section 2(5) but for the fact that the organization represents\u2014 (i) individuals employed by the United States, any wholly owned Government corporation, any Federal Reserve Bank, or any State or political subdivision thereof; (ii) individuals employed by persons subject to the Railway Labor Act ( 45 U.S.C. 151 et seq. ); or (iii) individuals employed as agricultural laborers. .",
      "versionDate": "2025-01-20",
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
            "name": "Advisory bodies",
            "updateDate": "2025-03-19T15:03:28Z"
          },
          {
            "name": "Labor-management relations",
            "updateDate": "2025-03-19T15:03:35Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-03-19T15:03:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-02-20T16:42:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-20",
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
          "measure-id": "id119hr567",
          "measure-number": "567",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-20",
          "originChamber": "HOUSE",
          "update-date": "2025-07-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr567v00",
            "update-date": "2025-07-31"
          },
          "action-date": "2025-01-20",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Expanding Labor Representation in the Workforce System Act</strong></p><p>This bill increases from 20% to 30% the workforce representation on state and local workforce development boards.</p><p>Workforce development boards perform a variety of functions to carry out the programs and services authorized under the Workforce Innovation and Opportunity Act, including by developing and implementing plans for workforce development and investment activities. \u00a0</p><p>Current law specifies that boards must include representatives of labor organizations, among others with relevant expertise. The bill specifies that labor organizations include organizations that</p><ul><li>are considered labor organizations based on the definition included in the National Labor Relations Act (e.g., unions); </li><li>are composed of labor organizations (e.g., a labor union federation or a state or municipal labor body); or</li><li> would be considered labor organizations but for the fact that the organization represents agricultural laborers\u00a0or individuals employed by a federal agency, a government\u00a0corporation, a Federal Reserve Bank, a state or local government, or an employer that is subject to the Railway Labor Act.</li></ul><p>\u00a0</p>"
        },
        "title": "Expanding Labor Representation in the Workforce System Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr567.xml",
    "summary": {
      "actionDate": "2025-01-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Expanding Labor Representation in the Workforce System Act</strong></p><p>This bill increases from 20% to 30% the workforce representation on state and local workforce development boards.</p><p>Workforce development boards perform a variety of functions to carry out the programs and services authorized under the Workforce Innovation and Opportunity Act, including by developing and implementing plans for workforce development and investment activities. \u00a0</p><p>Current law specifies that boards must include representatives of labor organizations, among others with relevant expertise. The bill specifies that labor organizations include organizations that</p><ul><li>are considered labor organizations based on the definition included in the National Labor Relations Act (e.g., unions); </li><li>are composed of labor organizations (e.g., a labor union federation or a state or municipal labor body); or</li><li> would be considered labor organizations but for the fact that the organization represents agricultural laborers\u00a0or individuals employed by a federal agency, a government\u00a0corporation, a Federal Reserve Bank, a state or local government, or an employer that is subject to the Railway Labor Act.</li></ul><p>\u00a0</p>",
      "updateDate": "2025-07-31",
      "versionCode": "id119hr567"
    },
    "title": "Expanding Labor Representation in the Workforce System Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Expanding Labor Representation in the Workforce System Act</strong></p><p>This bill increases from 20% to 30% the workforce representation on state and local workforce development boards.</p><p>Workforce development boards perform a variety of functions to carry out the programs and services authorized under the Workforce Innovation and Opportunity Act, including by developing and implementing plans for workforce development and investment activities. \u00a0</p><p>Current law specifies that boards must include representatives of labor organizations, among others with relevant expertise. The bill specifies that labor organizations include organizations that</p><ul><li>are considered labor organizations based on the definition included in the National Labor Relations Act (e.g., unions); </li><li>are composed of labor organizations (e.g., a labor union federation or a state or municipal labor body); or</li><li> would be considered labor organizations but for the fact that the organization represents agricultural laborers\u00a0or individuals employed by a federal agency, a government\u00a0corporation, a Federal Reserve Bank, a state or local government, or an employer that is subject to the Railway Labor Act.</li></ul><p>\u00a0</p>",
      "updateDate": "2025-07-31",
      "versionCode": "id119hr567"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr567ih.xml"
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
      "title": "Expanding Labor Representation in the Workforce System Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-20T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expanding Labor Representation in the Workforce System Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To expand labor representation on State and local workforce development boards, to provide a definition of labor organization, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-20T04:18:24Z"
    }
  ]
}
```
