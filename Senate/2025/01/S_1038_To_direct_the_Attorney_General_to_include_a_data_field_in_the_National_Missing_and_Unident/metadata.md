# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1038?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1038
- Title: TRACE Act
- Congress: 119
- Bill type: S
- Bill number: 1038
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2026-04-01T16:10:32Z
- Update date including text: 2026-04-01T16:10:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-07-24 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-07-28 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2025-07-28 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2025-07-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 126.
- 2025-09-02 - Floor: Passed Senate with an amendment by Unanimous Consent. (consideration: CR S5987; text: CR S5987)
- 2025-09-02 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2025-09-04 - Floor: Message on Senate action sent to the House.
- 2025-09-04 11:20:10 - Floor: Received in the House.
- 2025-09-04 11:24:45 - Floor: Held at the desk.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-07-24 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-07-28 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2025-07-28 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2025-07-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 126.
- 2025-09-02 - Floor: Passed Senate with an amendment by Unanimous Consent. (consideration: CR S5987; text: CR S5987)
- 2025-09-02 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2025-09-04 - Floor: Message on Senate action sent to the House.
- 2025-09-04 11:20:10 - Floor: Received in the House.
- 2025-09-04 11:24:45 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1038",
    "number": "1038",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "TRACE Act",
    "type": "S",
    "updateDate": "2026-04-01T16:10:32Z",
    "updateDateIncludingText": "2026-04-01T16:10:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-09-04",
      "actionTime": "11:24:45",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-09-04",
      "actionTime": "11:20:10",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-09-04",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-09-02",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate with an amendment by Unanimous Consent. (consideration: CR S5987; text: CR S5987)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-09-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-07-28",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 126.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-07-28",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-07-28",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-24",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-13",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-13",
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
            "date": "2025-07-28T19:57:29Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-24T19:03:14Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-13T18:00:34Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "CA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "WV"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "CT"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "CT"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1038is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1038\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Tillis (for himself, Mr. Padilla , Mrs. Capito , Mr. Blumenthal , and Mr. Murphy ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo direct the Attorney General to include a data field in the National Missing and Unidentified Persons System to indicate whether the last known location of a missing person was confirmed or was suspected to have been on Federal land, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tracking and Reporting Absent Community-Members Everywhere Act or the TRACE Act .\n#### 2. Definitions\nIn this Act:\n**(1) Attorney General**\nThe term Attorney General means the Attorney General, acting through the Director of the National Institute of Justice.\n**(2) Federal land**\nThe term Federal land means land owned by the United States that is under the administrative jurisdiction of\u2014\n**(A)**\nthe Secretary of Agriculture;\n**(B)**\nthe Secretary of the Interior (except land held in trust for the benefit of an Indian Tribe); or\n**(C)**\nthe Secretary of Defense only with respect to land and water resources projects administered by the Corps of Engineers.\n#### 3. Data field in the National Missing and Unidentified Persons System related to Federal land\nThe Attorney General shall include in the National Missing and Unidentified Persons System a data field to indicate whether the last known location of the missing person was confirmed or was suspected to have been on Federal land, including any specific location details about the unit of Federal land that was the last known location of the missing person.\n#### 4. Report\nNot later than January 15 of the second calendar year that begins after the date of enactment of this Act, and annually thereafter, the Attorney General shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report that contains, for the previous calendar year, the number of cases in the National Missing and Unidentified Persons System for which the missing person\u2019s last known location was confirmed or was suspected to have been on Federal land.",
      "versionDate": "2025-03-13",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1038rs.xml",
      "text": "II\nCalendar No. 126\n119th CONGRESS\n1st Session\nS. 1038\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Tillis (for himself, Mr. Padilla , Mrs. Capito , Mr. Blumenthal , Mr. Murphy , and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nJuly 28, 2025 Reported by Mr. Grassley , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo direct the Attorney General to include a data field in the National Missing and Unidentified Persons System to indicate whether the last known location of a missing person was confirmed or was suspected to have been on Federal land, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tracking and Reporting Absent Community-Members Everywhere Act or the TRACE Act .\n#### 2. Definitions\nIn this Act:\n**(1) Attorney General**\nThe term Attorney General means the Attorney General, acting through the Director of the National Institute of Justice.\n**(2) Federal land**\nThe term Federal land means land owned by the United States that is under the administrative jurisdiction of\u2014\n**(A)**\nthe Secretary of Agriculture;\n**(B)**\nthe Secretary of the Interior (except land held in trust for the benefit of an Indian Tribe); or\n**(C)**\nthe Secretary of Defense only with respect to land and water resources projects administered by the Corps of Engineers.\n#### 3. Data field in the National Missing and Unidentified Persons System related to Federal land\nThe Attorney General shall include in the National Missing and Unidentified Persons System a data field to indicate whether the last known location of the missing person was confirmed or was suspected to have been on Federal land, including any specific location details about the unit of Federal land that was the last known location of the missing person.\n#### 4. Report\nNot later than January 15 of the second calendar year that begins after the date of enactment of this Act, and annually thereafter, the Attorney General shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report that contains, for the previous calendar year, the number of cases in the National Missing and Unidentified Persons System for which the missing person\u2019s last known location was confirmed or was suspected to have been on Federal land.",
      "versionDate": "2025-07-28",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1038es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 1038\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo direct the Attorney General to include a data field in the National Missing and Unidentified Persons System to indicate whether the last known location of a missing person was confirmed or was suspected to have been on Federal land, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tracking and Reporting Absent Community-Members Everywhere Act or the TRACE Act .\n#### 2. Definitions\nIn this Act:\n**(1) Attorney General**\nThe term Attorney General means the Attorney General, acting through the Director of the National Institute of Justice.\n**(2) Federal land**\nThe term Federal land means land owned by the United States that is under the administrative jurisdiction of\u2014\n**(A)**\nthe Secretary of Agriculture;\n**(B)**\nthe Secretary of the Interior (except land held in trust for the benefit of an Indian Tribe); or\n**(C)**\nthe Secretary of Defense only with respect to land and water resources projects administered by the Corps of Engineers.\n**(3) Territorial waters of the United States**\nThe term territorial waters of the United States means all waters of the territorial sea of the United States, 12 nautical miles wide, adjacent to the coast of the United States and seaward of the territorial baseline, as described in Presidential Proclamation 5928 of December 27, 1988.\n#### 3. Data field in the National Missing and Unidentified Persons System related to Federal land and territorial waters\nThe Attorney General shall include in the National Missing and Unidentified Persons System a data field to indicate whether the last known location of the missing person was confirmed or was suspected to have been on Federal land or in the territorial waters of the United States, including any specific location details about the unit of Federal land or the area of the territorial waters of the United States that was the last known location of the missing person.\n#### 4. Report\nNot later than January 15 of the second calendar year that begins after the date of enactment of this Act, and annually thereafter, the Attorney General shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report that contains, for the previous calendar year, the number of cases in the National Missing and Unidentified Persons System for which the missing person\u2019s last known location was confirmed or was suspected to have been on Federal land or in the territorial waters of the United States.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
            "updateDate": "2025-08-07T17:53:03Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-08-07T17:53:03Z"
          },
          {
            "name": "Criminal justice information and records",
            "updateDate": "2025-08-07T17:53:03Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-08-07T17:53:03Z"
          },
          {
            "name": "Missing persons",
            "updateDate": "2025-08-07T17:53:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-13T17:50:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-02",
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
          "measure-id": "id119s1038",
          "measure-number": "1038",
          "measure-type": "s",
          "orig-publish-date": "2025-09-02",
          "originChamber": "SENATE",
          "update-date": "2026-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1038v55",
            "update-date": "2026-04-01"
          },
          "action-date": "2025-09-02",
          "action-desc": "Passed Senate",
          "summary-text": "<p><strong>Tracking and Reporting Absent Community-Members Everywhere Act or the TRACE Act</strong></p><p>This bill requires the National Institute of Justice to include in the National Missing and Unidentified Persons System (NamUs) an additional data field for information about whether the last known location of a missing person was on federal land or in the territorial waters of the United States.</p><p>NamUs is a national information clearinghouse and resource center for cases involving missing persons and unidentified or unclaimed remains.</p>"
        },
        "title": "TRACE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1038.xml",
    "summary": {
      "actionDate": "2025-09-02",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>Tracking and Reporting Absent Community-Members Everywhere Act or the TRACE Act</strong></p><p>This bill requires the National Institute of Justice to include in the National Missing and Unidentified Persons System (NamUs) an additional data field for information about whether the last known location of a missing person was on federal land or in the territorial waters of the United States.</p><p>NamUs is a national information clearinghouse and resource center for cases involving missing persons and unidentified or unclaimed remains.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119s1038"
    },
    "title": "TRACE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-02",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>Tracking and Reporting Absent Community-Members Everywhere Act or the TRACE Act</strong></p><p>This bill requires the National Institute of Justice to include in the National Missing and Unidentified Persons System (NamUs) an additional data field for information about whether the last known location of a missing person was on federal land or in the territorial waters of the United States.</p><p>NamUs is a national information clearinghouse and resource center for cases involving missing persons and unidentified or unclaimed remains.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119s1038"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1038is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-07-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1038rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1038es.xml"
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
      "title": "TRACE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-05T11:03:18Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "TRACE Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-09-03T04:08:18Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Tracking and Reporting Absent Community-Members Everywhere Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-09-03T04:08:18Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Tracking and Reporting Absent Community-Members Everywhere Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-07-30T06:38:22Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "TRACE Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-07-30T06:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Attorney General to include a data field in the National Missing and Unidentified Persons System to indicate whether the last known location of a missing person was confirmed or was suspected to have been on Federal land, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:33:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "TRACE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Tracking and Reporting Absent Community-Members Everywhere Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:21Z"
    }
  ]
}
```
