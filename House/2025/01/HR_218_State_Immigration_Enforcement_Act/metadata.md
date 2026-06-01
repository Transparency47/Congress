# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/218?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/218
- Title: State Immigration Enforcement Act
- Congress: 119
- Bill type: HR
- Bill number: 218
- Origin chamber: House
- Introduced date: 2025-01-07
- Update date: 2025-11-21T12:04:26Z
- Update date including text: 2025-11-21T12:04:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-07: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-07: Introduced in House

## Actions

- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-07",
    "latestAction": {
      "actionDate": "2025-01-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/218",
    "number": "218",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
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
    "title": "State Immigration Enforcement Act",
    "type": "HR",
    "updateDate": "2025-11-21T12:04:26Z",
    "updateDateIncludingText": "2025-11-21T12:04:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-07",
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
      "actionDate": "2025-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-07",
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
          "date": "2025-01-07T16:01:00Z",
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
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "SC"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "FL"
    },
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr218ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 218\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2025 Mr. Biggs of Arizona (for himself, Ms. Mace , and Mrs. Luna ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo authorize State enforcement of immigration laws, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the State Immigration Enforcement Act .\n#### 2. State enforcement of immigration laws\nStates, or political subdivisions of States, may enact, implement and enforce criminal penalties that penalize the same conduct that is prohibited in the criminal provisions of immigration laws (as defined in section 101(a)(17) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(17) )), as long as the criminal penalties do not exceed the relevant Federal criminal penalties (without regard to ancillary issues such as the availability of probation or pardon). States, or political subdivisions of States, may enact, implement and enforce civil penalties that penalize the same conduct that is prohibited in the civil provisions of immigration laws (as defined in such section 101(a)(17)), as long as the civil penalties do not exceed the relevant Federal civil penalties.\n#### 3. Conforming amendment\nSection 274A(h) of the Immigration and Nationality Act ( 8 U.S.C. 1324a(h) ) is amended by striking paragraph (2).",
      "versionDate": "2025-01-07",
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
        "name": "Immigration",
        "updateDate": "2025-02-08T12:56:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-07",
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
          "measure-id": "id119hr218",
          "measure-number": "218",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-07",
          "originChamber": "HOUSE",
          "update-date": "2025-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr218v00",
            "update-date": "2025-02-25"
          },
          "action-date": "2025-01-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>State Immigration Enforcement Act</b></p> <p>This bill authorizes state and local governments to enact and enforce laws that penalize conduct prohibited under federal immigration law. Such state and local laws may only impose civil and criminal penalties that do not exceed the penalties imposed by federal law.</p> <p>The bill also revokes a federal law that preempts (blocks) state and local laws that impose civil or criminal penalties for employing non-U.S. nationals who are not authorized to work in the United States.</p>"
        },
        "title": "State Immigration Enforcement Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr218.xml",
    "summary": {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><b>State Immigration Enforcement Act</b></p> <p>This bill authorizes state and local governments to enact and enforce laws that penalize conduct prohibited under federal immigration law. Such state and local laws may only impose civil and criminal penalties that do not exceed the penalties imposed by federal law.</p> <p>The bill also revokes a federal law that preempts (blocks) state and local laws that impose civil or criminal penalties for employing non-U.S. nationals who are not authorized to work in the United States.</p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119hr218"
    },
    "title": "State Immigration Enforcement Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><b>State Immigration Enforcement Act</b></p> <p>This bill authorizes state and local governments to enact and enforce laws that penalize conduct prohibited under federal immigration law. Such state and local laws may only impose civil and criminal penalties that do not exceed the penalties imposed by federal law.</p> <p>The bill also revokes a federal law that preempts (blocks) state and local laws that impose civil or criminal penalties for employing non-U.S. nationals who are not authorized to work in the United States.</p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119hr218"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr218ih.xml"
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
      "title": "State Immigration Enforcement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-07T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "State Immigration Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-07T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize State enforcement of immigration laws, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-07T04:18:19Z"
    }
  ]
}
```
