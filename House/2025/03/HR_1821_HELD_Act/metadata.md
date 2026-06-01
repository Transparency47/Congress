# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1821?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1821
- Title: HELD Act
- Congress: 119
- Bill type: HR
- Bill number: 1821
- Origin chamber: House
- Introduced date: 2025-03-04
- Update date: 2026-04-03T15:40:36Z
- Update date including text: 2026-04-03T15:40:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-04: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-03-04: Introduced in House

## Actions

- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-04",
    "latestAction": {
      "actionDate": "2025-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1821",
    "number": "1821",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C000059",
        "district": "41",
        "firstName": "Ken",
        "fullName": "Rep. Calvert, Ken [R-CA-41]",
        "lastName": "Calvert",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "HELD Act",
    "type": "HR",
    "updateDate": "2026-04-03T15:40:36Z",
    "updateDateIncludingText": "2026-04-03T15:40:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-04",
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
      "actionDate": "2025-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-04",
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
          "date": "2025-03-04T15:01:15Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1821ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1821\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2025 Mr. Calvert introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo deny Federal funding to any State or political subdivision of a State that has in effect any law, policy, or procedure that prevents or impedes a State or local law enforcement official from maintaining custody of an alien pursuant to an immigration detainer issued by the Secretary of Homeland Security, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the\u2014\n**(1)**\nHelp Ensure Legal Detainers Act ; or\n**(2)**\nHELD Act .\n#### 2. Denial of Federal funding to States and units of local government that fail to respond to immigration detainers\n##### (a) In general\nWith respect to fiscal years beginning after the date of the enactment of this Act, no Federal funds may be used to assist any project or activity carried out by a State, or a political subdivision of a State, described in subsection (b).\n##### (b) States and political subdivisions described\nA State, or political subdivision of a State, described in this subsection is any State, or political subdivision of a State, that has in effect any law, policy, or procedure that prevents or impedes State or local law enforcement officials from\u2014\n**(1)**\ntimely responding to an immigration notice issued by the Secretary of Homeland Security that requests information about an alien in State or local custody, including the alien\u2019s estimated release date, in order that the Secretary may arrange to assume custody of the alien upon such release; or\n**(2)**\nmaintaining custody of an alien for a period of up to 48 hours (excluding Saturdays, Sundays and holidays) pursuant to an immigration detainer issued by the Secretary of Homeland Security in order that the alien can be transferred to the custody of such Secretary to determine whether the alien should be detained, placed in removal proceedings, released, or removed.\n##### (c) Construction\nA political subdivision of a State that is not ineligible under subsection (a) to receive Federal funds, but is part of a State or another unit of government that is so ineligible, may submit, notwithstanding any other provision of law, an application for direct receipt of any funds that the political subdivision otherwise only would receive through subgrant, allocation, or allotment made by the ineligible State or government unit.",
      "versionDate": "2025-03-04",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-21T16:22:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-04",
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
          "measure-id": "id119hr1821",
          "measure-number": "1821",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-04",
          "originChamber": "HOUSE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1821v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2025-03-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Help Ensure Legal Detainers Act or the HELD Act</strong></p><p>This bill prohibits the use of federal funds by a state or local subdivision that has in effect a law, policy, or procedure that prevents or impedes</p><ul><li>a timely response to a request from U.S. Immigration and Customs Enforcement\u00a0(ICE) for information about an alien in state or local custody, including the alien's estimated release date; or</li><li>compliance with a request from ICE to hold an alien for up to 48 hours so that ICE may assume custody.</li></ul>"
        },
        "title": "HELD Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1821.xml",
    "summary": {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Help Ensure Legal Detainers Act or the HELD Act</strong></p><p>This bill prohibits the use of federal funds by a state or local subdivision that has in effect a law, policy, or procedure that prevents or impedes</p><ul><li>a timely response to a request from U.S. Immigration and Customs Enforcement\u00a0(ICE) for information about an alien in state or local custody, including the alien's estimated release date; or</li><li>compliance with a request from ICE to hold an alien for up to 48 hours so that ICE may assume custody.</li></ul>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr1821"
    },
    "title": "HELD Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Help Ensure Legal Detainers Act or the HELD Act</strong></p><p>This bill prohibits the use of federal funds by a state or local subdivision that has in effect a law, policy, or procedure that prevents or impedes</p><ul><li>a timely response to a request from U.S. Immigration and Customs Enforcement\u00a0(ICE) for information about an alien in state or local custody, including the alien's estimated release date; or</li><li>compliance with a request from ICE to hold an alien for up to 48 hours so that ICE may assume custody.</li></ul>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr1821"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1821ih.xml"
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
      "title": "HELD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HELD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Help Ensure Legal Detainers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To deny Federal funding to any State or political subdivision of a State that has in effect any law, policy, or procedure that prevents or impedes a State or local law enforcement official from maintaining custody of an alien pursuant to an immigration detainer issued by the Secretary of Homeland Security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:25Z"
    }
  ]
}
```
