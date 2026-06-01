# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/194?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/194
- Title: Venue Named Under Exception Act
- Congress: 119
- Bill type: HR
- Bill number: 194
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-05-27T20:13:32Z
- Update date including text: 2025-05-27T20:13:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/194",
    "number": "194",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001224",
        "district": "3",
        "firstName": "Keith",
        "fullName": "Rep. Self, Keith [R-TX-3]",
        "lastName": "Self",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Venue Named Under Exception Act",
    "type": "HR",
    "updateDate": "2025-05-27T20:13:32Z",
    "updateDateIncludingText": "2025-05-27T20:13:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:16:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr194ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 194\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Self (for himself and Mr. Nehls ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend chapter 211 of title 18, United States Code, to modify venue for certain offenses.\n#### 1. Short title\nThis Act may be cited as the Venue Named Under Exception Act or the VENUE Act .\n#### 2. Venue for certain offenses\n##### (a) In general\nChapter 211 of title 18, United States Code, is amended by adding at the end the following:\n3245. Offenses committed in the National Capital Region (a) Offenses in National Capital Region In the case of an offense that is committed in the National Capital Region on property under the control of the Federal Government, an indictment or information shall be filed in the district of the last known residence of the offender or of any one of two or more joint offenders, or if no such residence is known, the indictment or information may be filed in the District of Columbia. (b) Transfer (1) Right to transfer Notwithstanding subsection (a), a district court shall, upon motion of the defendant, grant a transfer of an indictment or information to the district court encompassing the jurisdiction where the defendant is domiciled. (2) Multiple defendants If multiple defendants file a motion to transfer an indictment or information under paragraph (1), the district court shall grant the motion of the defendant who filed the motion first. (3) Defendants not domiciled in the United States A defendant not domiciled in the United States may not file a motion to transfer an indictment or information under paragraph (1). (c) Definition In this section: (1) The term National Capital Region means the geographic area located within the boundaries of\u2014 (A) the District of Columbia; (B) Montgomery and Prince George\u2019s Counties in the State of Maryland; (C) Arlington, Fairfax, Loudoun, and Prince William Counties and the Cities of Alexandria and Falls Church in the Commonwealth of Virginia; and (D) all cities and other units of government within the geographic areas of such District, Counties, and City. (2) The term property under the control of the Federal Government means property owned or leased by the United States, or any agency thereof, except in the case of the United States Postal Service. (d) Pending cases This section shall apply to any offense with respect to which a trial has not been scheduled as of the date of enactment of this section. (e) Limitation This section shall only apply to an offense not otherwise subject to section 3235, 3236, 3237, 3238, 3239, 3241, 3242, 3243 or 3244. .\n##### (b) Clerical amendment\nThe table of sections for chapter 211 of title 18, United States Code, is amended by adding at the end the following:\n3245. Offenses committed in the National Capital Region. .",
      "versionDate": "2025-01-03",
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
            "name": "District of Columbia",
            "updateDate": "2025-02-12T19:26:09Z"
          },
          {
            "name": "Federal district courts",
            "updateDate": "2025-02-12T19:26:16Z"
          },
          {
            "name": "Jurisdiction and venue",
            "updateDate": "2025-02-12T19:26:03Z"
          },
          {
            "name": "Maryland",
            "updateDate": "2025-02-12T19:26:21Z"
          },
          {
            "name": "Virginia",
            "updateDate": "2025-02-12T19:26:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-08T12:14:28Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr194",
          "measure-number": "194",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-05-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr194v00",
            "update-date": "2025-05-27"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Venue Named Under Exception Act or the VENUE Act</strong></p><p>This bill changes the venue rules for cases involving criminal offenses on federal property in the National Capital Region. <em>Venue </em>refers to the court where it is proper for a case to proceed.</p><p>Specifically, the bill requires certain cases involving criminal offenses committed on federal property in the National Capital Region (Washington, DC and specified regions of Maryland and Virginia) to be brought in the district of the last known residence of the offender (or of any one of two or more joint offenders). If the last residence of the offender is not known,\u00a0then the case may be brought in DC.\u00a0</p>"
        },
        "title": "Venue Named Under Exception Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr194.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Venue Named Under Exception Act or the VENUE Act</strong></p><p>This bill changes the venue rules for cases involving criminal offenses on federal property in the National Capital Region. <em>Venue </em>refers to the court where it is proper for a case to proceed.</p><p>Specifically, the bill requires certain cases involving criminal offenses committed on federal property in the National Capital Region (Washington, DC and specified regions of Maryland and Virginia) to be brought in the district of the last known residence of the offender (or of any one of two or more joint offenders). If the last residence of the offender is not known,\u00a0then the case may be brought in DC.\u00a0</p>",
      "updateDate": "2025-05-27",
      "versionCode": "id119hr194"
    },
    "title": "Venue Named Under Exception Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Venue Named Under Exception Act or the VENUE Act</strong></p><p>This bill changes the venue rules for cases involving criminal offenses on federal property in the National Capital Region. <em>Venue </em>refers to the court where it is proper for a case to proceed.</p><p>Specifically, the bill requires certain cases involving criminal offenses committed on federal property in the National Capital Region (Washington, DC and specified regions of Maryland and Virginia) to be brought in the district of the last known residence of the offender (or of any one of two or more joint offenders). If the last residence of the offender is not known,\u00a0then the case may be brought in DC.\u00a0</p>",
      "updateDate": "2025-05-27",
      "versionCode": "id119hr194"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr194ih.xml"
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
      "title": "Venue Named Under Exception Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T23:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Venue Named Under Exception Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T23:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend chapter 211 of title 18, United States Code, to modify venue for certain offenses.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T23:33:17Z"
    }
  ]
}
```
