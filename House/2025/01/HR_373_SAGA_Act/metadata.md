# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/373?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/373
- Title: SAGA Act
- Congress: 119
- Bill type: HR
- Bill number: 373
- Origin chamber: House
- Introduced date: 2025-01-13
- Update date: 2025-05-20T08:05:52Z
- Update date including text: 2025-05-20T08:05:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-13: Introduced in House

## Actions

- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/373",
    "number": "373",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "T000478",
        "district": "24",
        "firstName": "Claudia",
        "fullName": "Rep. Tenney, Claudia [R-NY-24]",
        "lastName": "Tenney",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "SAGA Act",
    "type": "HR",
    "updateDate": "2025-05-20T08:05:52Z",
    "updateDateIncludingText": "2025-05-20T08:05:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-13",
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
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T17:00:30Z",
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
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "CA"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "NY"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "CO"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr373ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 373\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2025 Ms. Tenney (for herself, Mr. LaMalfa , and Mr. Langworthy ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to limit the authority of States and localities to regulate conduct, or impose penalties or taxes, in relation to rifles or shotguns.\n#### 1. Short title\nThis Act may be cited as the Second Amendment Guarantee Act or the SAGA Act .\n#### 2. Limitation on authority of States and localities to regulate conduct in relation to rifles or shotguns\nSection 927 of title 18, United States Code, is amended\u2014\n**(1)**\nby striking No and inserting (a) Except as provided in subsection (b), no ; and\n**(2)**\nby adding after and below the end the following:\n(b) (1) A State or a political subdivision of a State may not impose any regulation, prohibition, or registration or licensing requirement with respect to the design, manufacture, importation, sale, transfer, possession, or marking of a rifle or shotgun that has moved in, or any such conduct that affects, interstate or foreign commerce, that is more restrictive, or impose any penalty, tax, fee, or charge with respect to such a rifle or shotgun or such conduct, in an amount greater, than is provided under Federal law. To the extent that a law of a State or political subdivision of a State, whether enacted before, on, or after the date of the enactment of this subsection, violates the preceding sentence, the law shall have no force or effect. For purposes of this subsection, the term rifle or shotgun includes any part of a rifle or shotgun, any detachable magazine or ammunition feeding device, and any type of pistol grip or stock design. (2) In an action brought for damages or relief from a violation of paragraph (1), the court shall award the prevailing plaintiff a reasonable attorney\u2019s fee in addition to any other damages or relief awarded. .",
      "versionDate": "2025-01-13",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-02-19T21:20:24Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-02-19T21:20:24Z"
          },
          {
            "name": "Federal preemption",
            "updateDate": "2025-02-19T21:20:24Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-02-19T21:20:24Z"
          },
          {
            "name": "Legal fees and court costs",
            "updateDate": "2025-02-19T21:20:24Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-02-19T21:20:24Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-02-19T21:20:24Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-02-19T21:20:24Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2025-02-19T21:20:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-14T18:49:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119hr373",
          "measure-number": "373",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-13",
          "originChamber": "HOUSE",
          "update-date": "2025-04-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr373v00",
            "update-date": "2025-04-23"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Second Amendment Guarantee Act or the SAGA Act</b></p> <p>This bill prohibits a state or local government from establishing a regulation, prohibition, or registration or licensing requirement with respect to a rifle or shotgun that is more restrictive (or that imposes a greater penalty or tax) than federal law.</p>"
        },
        "title": "SAGA Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr373.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Second Amendment Guarantee Act or the SAGA Act</b></p> <p>This bill prohibits a state or local government from establishing a regulation, prohibition, or registration or licensing requirement with respect to a rifle or shotgun that is more restrictive (or that imposes a greater penalty or tax) than federal law.</p>",
      "updateDate": "2025-04-23",
      "versionCode": "id119hr373"
    },
    "title": "SAGA Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Second Amendment Guarantee Act or the SAGA Act</b></p> <p>This bill prohibits a state or local government from establishing a regulation, prohibition, or registration or licensing requirement with respect to a rifle or shotgun that is more restrictive (or that imposes a greater penalty or tax) than federal law.</p>",
      "updateDate": "2025-04-23",
      "versionCode": "id119hr373"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr373ih.xml"
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
      "title": "SAGA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAGA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Second Amendment Guarantee Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to limit the authority of States and localities to regulate conduct, or impose penalties or taxes, in relation to rifles or shotguns.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:48:38Z"
    }
  ]
}
```
