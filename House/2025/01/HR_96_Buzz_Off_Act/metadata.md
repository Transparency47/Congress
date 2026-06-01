# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/96?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/96
- Title: Buzz Off Act
- Congress: 119
- Bill type: HR
- Bill number: 96
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-03-03T14:09:59Z
- Update date including text: 2025-03-03T14:09:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/96",
    "number": "96",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Buzz Off Act",
    "type": "HR",
    "updateDate": "2025-03-03T14:09:59Z",
    "updateDateIncludingText": "2025-03-03T14:09:59Z"
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
          "date": "2025-01-03T16:06:15Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr96ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 96\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prevent agencies from using unmanned aerial vehicles to conduct surveillance of United States citizens, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Buzz Off Act .\n#### 2. Prohibiting use of unmanned aerial vehicles\n##### (a) Surveillance\nA Federal law enforcement agency may not use an unmanned aerial vehicle to intentionally conduct surveillance of, gather evidence or collect information about, or photographically or electronically record a specifically targeted United States citizen or the specifically targeted private property of a United States citizen.\n##### (b) Exception\nNotwithstanding subsection (a), a Federal law enforcement agency may use an unmanned aerial vehicle to photograph, or otherwise record a United States citizen for the purposes of publishing or otherwise publicly disseminating such photograph or recording if the agency obtains the written consent of such United States citizen.\n##### (c) Applicability\nSubsection (a) shall not apply in the case that\u2014\n**(1)**\nthe President, acting through the Secretary of Homeland Security, authorizes use of an unmanned aerial vehicle to conduct surveillance if the Secretary certifies in writing under oath that the surveillance is necessary to counter a high risk of a terrorist attack by a specific individual or organization; or\n**(2)**\nthe head of a Federal law enforcement agency first obtains a search warrant signed by a judge authorizing the use of an unmanned aerial vehicle.",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-26T16:27:04Z"
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
          "measure-id": "id119hr96",
          "measure-number": "96",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr96v00",
            "update-date": "2025-03-03"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Buzz Off Act</strong></p><p>This bill prohibits federal law enforcement from using unmanned aerial vehicles to intentionally conduct surveillance of a specifically targeted U.S. citizen or the property of such an individual, with certain exceptions.</p><p>Specifically, this prohibition shall not apply if (1) the federal law enforcement agency in question first obtains a search warrant, (2) the Department of Homeland Security certifies that such surveillance is necessary to counter a high risk of a terrorist attack by a specified person or organization, or (3) the citizen gives written consent for a photograph or recording that will be made available to the public.</p>"
        },
        "title": "Buzz Off Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr96.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Buzz Off Act</strong></p><p>This bill prohibits federal law enforcement from using unmanned aerial vehicles to intentionally conduct surveillance of a specifically targeted U.S. citizen or the property of such an individual, with certain exceptions.</p><p>Specifically, this prohibition shall not apply if (1) the federal law enforcement agency in question first obtains a search warrant, (2) the Department of Homeland Security certifies that such surveillance is necessary to counter a high risk of a terrorist attack by a specified person or organization, or (3) the citizen gives written consent for a photograph or recording that will be made available to the public.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hr96"
    },
    "title": "Buzz Off Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Buzz Off Act</strong></p><p>This bill prohibits federal law enforcement from using unmanned aerial vehicles to intentionally conduct surveillance of a specifically targeted U.S. citizen or the property of such an individual, with certain exceptions.</p><p>Specifically, this prohibition shall not apply if (1) the federal law enforcement agency in question first obtains a search warrant, (2) the Department of Homeland Security certifies that such surveillance is necessary to counter a high risk of a terrorist attack by a specified person or organization, or (3) the citizen gives written consent for a photograph or recording that will be made available to the public.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hr96"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr96ih.xml"
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
      "title": "Buzz Off Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T11:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Buzz Off Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T11:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prevent agencies from using unmanned aerial vehicles to conduct surveillance of United States citizens, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T11:03:27Z"
    }
  ]
}
```
