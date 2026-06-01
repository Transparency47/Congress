# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3359?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3359
- Title: Veterans’ Security and Pay Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 3359
- Origin chamber: House
- Introduced date: 2025-05-13
- Update date: 2025-12-12T09:07:08Z
- Update date including text: 2025-12-12T09:07:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-13: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-06 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- Latest action: 2025-05-13: Introduced in House

## Actions

- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-06 - Committee: Referred to the Subcommittee on Oversight and Investigations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3359",
    "number": "3359",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001214",
        "district": "1",
        "firstName": "Frank",
        "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
        "lastName": "Mrvan",
        "party": "D",
        "state": "IN"
      }
    ],
    "title": "Veterans\u2019 Security and Pay Transparency Act",
    "type": "HR",
    "updateDate": "2025-12-12T09:07:08Z",
    "updateDateIncludingText": "2025-12-12T09:07:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-06",
      "committees": {
        "item": {
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Oversight and Investigations.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-13",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-13",
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
          "date": "2025-05-13T16:06:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-06T15:45:18Z",
              "name": "Referred to"
            }
          },
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "VA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3359ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3359\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2025 Mr. Mrvan (for himself and Mrs. Kiggans of Virginia ) introduced the following bill; which was referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to report annually on compensation for police officers of the Department of Veterans Affairs.\n#### 1. Short title\nThis Act may be cited as the Veterans\u2019 Security and Pay Transparency Act .\n#### 2. Annual report on compensation for police officers of the Department of Veterans Affairs\n##### (a) Establishment\nChapter 9 of title 38, United States Code, is amended by adding at the end the following new section:\n906. Annual report on compensation for Department police officers (a) Requirement Not less than once each calendar year, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a report on compensation paid to Department police officers. Each such report shall include the following elements, disaggregated by facility of the Department and positions described in subsection (b): (1) Salaries. (2) Availability pay under section 5545a of title 5. (3) Bonuses to recruit or retain Department police officers. (4) Any other compensation paid to a Department police officer. (b) Positions A position described in this subsection is a position in the following series (or successor classifications) of the General Schedule: (1) Chief of Police (GS\u20130080). (2) Deputy Chief of Police (GS\u20130080). (3) Supervisory Police Officer (GS\u20130083). (4) Criminal Investigator (GS\u20131811). (5) Police Detective (GS\u20130083). (6) Police Officer (GS\u20130083). (7) Training Officer (GS\u20130083). (8) Physical Security Specialist (GS\u20130080). (9) Security Specialist Assistant (GS\u20130086). (10) Dispatcher (GS\u20130086). (11) Administrative Officer (GS\u20130303 or GS\u20130341). .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by adding at the end the following new item:\n906. Annual report on compensation for Department police officers. .\n##### (c) Implementation\nThe Secretary of Veterans Affairs shall submit the first report under section 906 of such title, as added by this section, not later than six months after the date of the enactment of this Act.",
      "versionDate": "2025-05-13",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-03T19:48:39Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-13",
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
          "measure-id": "id119hr3359",
          "measure-number": "3359",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-13",
          "originChamber": "HOUSE",
          "update-date": "2025-08-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3359v00",
            "update-date": "2025-08-12"
          },
          "action-date": "2025-05-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veterans\u2019 Security and Pay Transparency Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to annually report to Congress on compensation paid to VA police officers.</p>"
        },
        "title": "Veterans\u2019 Security and Pay Transparency Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3359.xml",
    "summary": {
      "actionDate": "2025-05-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans\u2019 Security and Pay Transparency Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to annually report to Congress on compensation paid to VA police officers.</p>",
      "updateDate": "2025-08-12",
      "versionCode": "id119hr3359"
    },
    "title": "Veterans\u2019 Security and Pay Transparency Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans\u2019 Security and Pay Transparency Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to annually report to Congress on compensation paid to VA police officers.</p>",
      "updateDate": "2025-08-12",
      "versionCode": "id119hr3359"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3359ih.xml"
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
      "title": "Veterans\u2019 Security and Pay Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans\u2019 Security and Pay Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to direct the Secretary of Veterans Affairs to report annually on compensation for police officers of the Department of Veterans Affairs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:03:34Z"
    }
  ]
}
```
