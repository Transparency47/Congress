# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2685?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2685
- Title: Crime Doesn’t Fly Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2685
- Origin chamber: House
- Introduced date: 2025-04-07
- Update date: 2025-11-21T12:04:34Z
- Update date including text: 2025-11-21T12:04:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-07: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-04-07 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.
- Latest action: 2025-04-07: Introduced in House

## Actions

- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-04-07 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-07",
    "latestAction": {
      "actionDate": "2025-04-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2685",
    "number": "2685",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M000317",
        "district": "11",
        "firstName": "Nicole",
        "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
        "lastName": "Malliotakis",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Crime Doesn\u2019t Fly Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-21T12:04:34Z",
    "updateDateIncludingText": "2025-11-21T12:04:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-07",
      "committees": {
        "item": {
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Transportation and Maritime Security.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-07",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-07",
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
          "date": "2025-04-07T16:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-07T21:02:29Z",
              "name": "Referred to"
            }
          },
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2685ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2685\nIN THE HOUSE OF REPRESENTATIVES\nApril 7, 2025 Ms. Malliotakis introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo prohibit the Administrator of the Transportation Security Administration from accepting warrants for the arrest of aliens as valid proof of identification at aviation security checkpoints, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Crime Doesn\u2019t Fly Act of 2025 .\n#### 2. Prohibition of use of ICE arrest warrants as identification at aviation security checkpoints\n##### (a) In general\nExcept as provided in subsection (b), the Administrator of the Transportation Security Administration may not accept a prohibited document as valid proof of identification at an aviation security checkpoint.\n##### (b) Exception\nSubsection (a) shall not apply with respect to an alien who is being removed from the United States in accordance with the immigration laws (as such term is defined in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 )).\n##### (c) Prohibited document defined\nIn this section, the term prohibited document means any of the following:\n**(1)**\nImmigration and Customs Enforcement Form I\u2013200, Warrant for Arrest of Alien (or any successor form).\n**(2)**\nImmigration and Customs Enforcement Form I\u2013205, Warrant of Removal/Deportation (or any successor form).",
      "versionDate": "2025-04-07",
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
        "updateDate": "2025-05-05T13:47:13Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-07",
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
          "measure-id": "id119hr2685",
          "measure-number": "2685",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-07",
          "originChamber": "HOUSE",
          "update-date": "2025-05-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2685v00",
            "update-date": "2025-05-06"
          },
          "action-date": "2025-04-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Crime Doesn't Fly Act of 2025</strong></p><p>This bill prohibits the use of Immigration and Customs Enforcement warrants for the arrest, removal, or deportation of a non-U.S. national (<em>alien</em> under federal law) as proof of identity at an airport security checkpoint unless the non-U.S. national is being removed from the United States pursuant to immigration laws.</p>"
        },
        "title": "Crime Doesn\u2019t Fly Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2685.xml",
    "summary": {
      "actionDate": "2025-04-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Crime Doesn't Fly Act of 2025</strong></p><p>This bill prohibits the use of Immigration and Customs Enforcement warrants for the arrest, removal, or deportation of a non-U.S. national (<em>alien</em> under federal law) as proof of identity at an airport security checkpoint unless the non-U.S. national is being removed from the United States pursuant to immigration laws.</p>",
      "updateDate": "2025-05-06",
      "versionCode": "id119hr2685"
    },
    "title": "Crime Doesn\u2019t Fly Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Crime Doesn't Fly Act of 2025</strong></p><p>This bill prohibits the use of Immigration and Customs Enforcement warrants for the arrest, removal, or deportation of a non-U.S. national (<em>alien</em> under federal law) as proof of identity at an airport security checkpoint unless the non-U.S. national is being removed from the United States pursuant to immigration laws.</p>",
      "updateDate": "2025-05-06",
      "versionCode": "id119hr2685"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2685ih.xml"
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
      "title": "Crime Doesn\u2019t Fly Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-18T03:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Crime Doesn\u2019t Fly Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-18T03:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the Administrator of the Transportation Security Administration from accepting warrants for the arrest of aliens as valid proof of identification at aviation security checkpoints, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-18T03:18:21Z"
    }
  ]
}
```
