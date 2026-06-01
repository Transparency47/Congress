# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/960?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/960
- Title: Justice for Murder Victims Act
- Congress: 119
- Bill type: S
- Bill number: 960
- Origin chamber: Senate
- Introduced date: 2025-03-11
- Update date: 2026-04-07T19:59:20Z
- Update date including text: 2026-04-07T19:59:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in Senate
- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - Floor: Introduced in the Senate, read twice, considered, read the third time, and passed without amendment by Unanimous Consent. (consideration: CR S1675-1676; text: CR S1676)
- 2025-03-11 - Floor: Passed/agreed to in Senate: Introduced in the Senate, read twice, considered, read the third time, and passed without amendment by Unanimous Consent.
- 2025-03-12 - Floor: Message on Senate action sent to the House.
- 2025-03-14 09:03:20 - Floor: Received in the House.
- 2025-03-14 09:03:30 - Floor: Held at the desk.
- Latest action: 2025-03-11: Introduced in Senate

## Actions

- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - Floor: Introduced in the Senate, read twice, considered, read the third time, and passed without amendment by Unanimous Consent. (consideration: CR S1675-1676; text: CR S1676)
- 2025-03-11 - Floor: Passed/agreed to in Senate: Introduced in the Senate, read twice, considered, read the third time, and passed without amendment by Unanimous Consent.
- 2025-03-12 - Floor: Message on Senate action sent to the House.
- 2025-03-14 09:03:20 - Floor: Received in the House.
- 2025-03-14 09:03:30 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/960",
    "number": "960",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Justice for Murder Victims Act",
    "type": "S",
    "updateDate": "2026-04-07T19:59:20Z",
    "updateDateIncludingText": "2026-04-07T19:59:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-03-14",
      "actionTime": "09:03:30",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-03-14",
      "actionTime": "09:03:20",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-03-12",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Introduced in the Senate, read twice, considered, read the third time, and passed without amendment by Unanimous Consent. (consideration: CR S1675-1676; text: CR S1676)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Introduced in the Senate, read twice, considered, read the third time, and passed without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-11",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "GA"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s960cps.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 960\nIN THE SENATE OF THE UNITED STATES\nMarch 11 (legislative day, March 10), 2025 Mr. Grassley (for himself, Mr. Ossoff , and Mr. Lee ) introduced the following bill; which was read twice, considered, read the third time, and passed\nA BILL\nTo ensure that homicides can be prosecuted under Federal law without regard to the time elapsed between the act or omission that caused the death of the victim and the death itself.\n#### 1. Short title\nThis Act may be cited as the Justice for Murder Victims Act .\n#### 2. Homicide offenses\n##### (a) In general\nChapter 51 of title 18, United States Code, is amended by adding at the end the following:\n1123. No maximum time period between act or omission and death of victim (a) In general A prosecution may be instituted for any homicide offense under this title without regard to the time that elapsed between\u2014 (1) the act or omission that caused the death of the victim; and (2) the death of the victim. (b) Relation to statute of limitations Nothing in subsection (a) shall be construed to supersede the limitations period under section 3282(a), to the extent applicable. (c) Maximum time period applicable if death penalty imposed A sentence of death may not be imposed for a homicide offense under this title unless the Government proves beyond a reasonable doubt that not more than 1 year and 1 day elapsed between\u2014 (1) the act or omission that caused the death of the victim; and (2) the death of the victim. .\n##### (b) Table of contents\nThe table of sections for chapter 51 of title 18, United States Code, is amended by adding at the end the following:\n1123. No maximum time period between act or omission and death of victim. .\n##### (c) Applicability\nSection 1123(a) of title 18, United States Code, as added by subsection (a), shall apply with respect to an act or omission described in that section that occurs after the date of enactment of this Act.\n##### (d) Maximum penalty for first-Degree murder based on time period between act or omission and death of victim\nSection 1111(b) of title 18, United States Code, is amended by inserting after imprisonment for life the following: , unless the death of the victim occurred more than 1 year and 1 day after the act or omission that caused the death of the victim, in which case the punishment shall be imprisonment for any term of years or for life .",
      "versionDate": "2025-03-11",
      "versionType": "Considered and Passed Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s960es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 960\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo ensure that homicides can be prosecuted under Federal law without regard to the time elapsed between the act or omission that caused the death of the victim and the death itself.\n#### 1. Short title\nThis Act may be cited as the Justice for Murder Victims Act .\n#### 2. Homicide offenses\n##### (a) In general\nChapter 51 of title 18, United States Code, is amended by adding at the end the following:\n1123. No maximum time period between act or omission and death of victim (a) In general A prosecution may be instituted for any homicide offense under this title without regard to the time that elapsed between\u2014 (1) the act or omission that caused the death of the victim; and (2) the death of the victim. (b) Relation to statute of limitations Nothing in subsection (a) shall be construed to supersede the limitations period under section 3282(a), to the extent applicable. (c) Maximum time period applicable if death penalty imposed A sentence of death may not be imposed for a homicide offense under this title unless the Government proves beyond a reasonable doubt that not more than 1 year and 1 day elapsed between\u2014 (1) the act or omission that caused the death of the victim; and (2) the death of the victim. .\n##### (b) Table of contents\nThe table of sections for chapter 51 of title 18, United States Code, is amended by adding at the end the following:\n1123. No maximum time period between act or omission and death of victim. .\n##### (c) Applicability\nSection 1123(a) of title 18, United States Code, as added by subsection (a), shall apply with respect to an act or omission described in that section that occurs after the date of enactment of this Act.\n##### (d) Maximum penalty for first-degree murder based on time period between act or omission and death of victim\nSection 1111(b) of title 18, United States Code, is amended by inserting after imprisonment for life the following: , unless the death of the victim occurred more than 1 year and 1 day after the act or omission that caused the death of the victim, in which case the punishment shall be imprisonment for any term of years or for life .",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-02-13",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1353",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Justice for Murder Victims Act",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-03-19T16:00:37Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2025-03-19T16:00:37Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-03-19T16:00:37Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-03-19T16:00:37Z"
          },
          {
            "name": "U.S. Sentencing Commission",
            "updateDate": "2025-03-19T16:00:37Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2025-03-19T16:00:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-07T14:20:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
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
          "measure-id": "id119s960",
          "measure-number": "960",
          "measure-type": "s",
          "orig-publish-date": "2025-03-11",
          "originChamber": "SENATE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s960v55",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-03-11",
          "action-desc": "Passed Senate",
          "summary-text": "<p><b>Justice for Murder Victims Act</b></p> <p>This bill allows a prosecution to be instituted for any federal homicide offense without regard to the time that elapsed between the act or omission that caused the death of the victim and the death of the victim. </p>"
        },
        "title": "Justice for Murder Victims Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s960.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Passed Senate",
      "text": "<p><b>Justice for Murder Victims Act</b></p> <p>This bill allows a prosecution to be instituted for any federal homicide offense without regard to the time that elapsed between the act or omission that caused the death of the victim and the death of the victim. </p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119s960"
    },
    "title": "Justice for Murder Victims Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Passed Senate",
      "text": "<p><b>Justice for Murder Victims Act</b></p> <p>This bill allows a prosecution to be instituted for any federal homicide offense without regard to the time that elapsed between the act or omission that caused the death of the victim and the death of the victim. </p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119s960"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s960cps.xml"
        }
      ],
      "type": "Considered and Passed Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s960es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Justice for Murder Victims Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T11:03:20Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Justice for Murder Victims Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-03-12T11:08:20Z"
    },
    {
      "title": "A bill to ensure that homicides can be prosecuted under Federal law without regard to the time elapsed between the act or omission that caused the death of the victim and the death itself.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T10:56:16Z"
    }
  ]
}
```
