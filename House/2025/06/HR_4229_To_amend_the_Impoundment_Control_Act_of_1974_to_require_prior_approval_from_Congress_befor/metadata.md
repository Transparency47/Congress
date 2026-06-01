# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4229?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4229
- Title: To amend the Impoundment Control Act of 1974 to require prior approval from Congress before the Comptroller General may pursue a civil action under such Act, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 4229
- Origin chamber: House
- Introduced date: 2025-06-27
- Update date: 2025-09-26T16:16:05Z
- Update date including text: 2025-09-26T16:16:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-27: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-27 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-27: Introduced in House

## Actions

- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-27 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-27",
    "latestAction": {
      "actionDate": "2025-06-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4229",
    "number": "4229",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "H001052",
        "district": "1",
        "firstName": "Andy",
        "fullName": "Rep. Harris, Andy [R-MD-1]",
        "lastName": "Harris",
        "party": "R",
        "state": "MD"
      }
    ],
    "title": "To amend the Impoundment Control Act of 1974 to require prior approval from Congress before the Comptroller General may pursue a civil action under such Act, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-09-26T16:16:05Z",
    "updateDateIncludingText": "2025-09-26T16:16:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-27",
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
      "text": "Referred to the Committee on the Budget, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-27",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Budget, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-27",
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
          "date": "2025-06-27T13:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-27T13:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
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
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "IL"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "GA"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "CO"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "AZ"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "TX"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4229ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4229\nIN THE HOUSE OF REPRESENTATIVES\nJune 27, 2025 Mr. Harris of Maryland (for himself, Mrs. Miller of Illinois , Mr. Clyde , Ms. Boebert , Mr. Gosar , Mr. Gill of Texas , and Mr. Higgins of Louisiana ) introduced the following bill; which was referred to the Committee on the Budget , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Impoundment Control Act of 1974 to require prior approval from Congress before the Comptroller General may pursue a civil action under such Act, and for other purposes.\n#### 1. Congressional approval before pursuing civil action under Impoundment Control Act of 1974\nSection 1016 of the Impoundment Control Act of 1974 ( 2 U.S.C. 687 ) is amended\u2014\n**(1)**\nby striking If, and inserting (a) In general .\u2014If, ;\n**(2)**\nby striking is hereby expressly empowered and inserting may, subject to approval by the Congress under subsection (b), ; and\n**(3)**\nby adding at the end the following:\n(b) Prior congressional approval required The Comptroller General may not bring a civil action under subsection (a) unless the Congress has enacted a concurrent resolution authorizing the Comptroller General to bring such civil action. .",
      "versionDate": "2025-06-27",
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-09-09T16:05:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-27",
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
          "measure-id": "id119hr4229",
          "measure-number": "4229",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-27",
          "originChamber": "HOUSE",
          "update-date": "2025-09-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4229v00",
            "update-date": "2025-09-26"
          },
          "action-date": "2025-06-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill prohibits the Government Accountability Office (GAO) from bringing a civil action under the Impoundment Control Act of 1974 (ICA) to compel the release of appropriated funds\u00a0unless Congress has enacted a concurrent resolution authorizing GAO to bring the action.</p><p>The ICA generally limits the authority of the President to impound (i.e., withhold from obligation or expenditure) funds that have been appropriated by Congress and establishes related procedures. Under current law, GAO is authorized to bring a civil action to compel a federal agency to release budget authority for obligation if the budget authority is required to be released under the ICA, and the agency has not released the funds. This bill prohibits GAO from bringing such an action without prior congressional approval.\u00a0</p>"
        },
        "title": "To amend the Impoundment Control Act of 1974 to require prior approval from Congress before the Comptroller General may pursue a civil action under such Act, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4229.xml",
    "summary": {
      "actionDate": "2025-06-27",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill prohibits the Government Accountability Office (GAO) from bringing a civil action under the Impoundment Control Act of 1974 (ICA) to compel the release of appropriated funds\u00a0unless Congress has enacted a concurrent resolution authorizing GAO to bring the action.</p><p>The ICA generally limits the authority of the President to impound (i.e., withhold from obligation or expenditure) funds that have been appropriated by Congress and establishes related procedures. Under current law, GAO is authorized to bring a civil action to compel a federal agency to release budget authority for obligation if the budget authority is required to be released under the ICA, and the agency has not released the funds. This bill prohibits GAO from bringing such an action without prior congressional approval.\u00a0</p>",
      "updateDate": "2025-09-26",
      "versionCode": "id119hr4229"
    },
    "title": "To amend the Impoundment Control Act of 1974 to require prior approval from Congress before the Comptroller General may pursue a civil action under such Act, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-06-27",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill prohibits the Government Accountability Office (GAO) from bringing a civil action under the Impoundment Control Act of 1974 (ICA) to compel the release of appropriated funds\u00a0unless Congress has enacted a concurrent resolution authorizing GAO to bring the action.</p><p>The ICA generally limits the authority of the President to impound (i.e., withhold from obligation or expenditure) funds that have been appropriated by Congress and establishes related procedures. Under current law, GAO is authorized to bring a civil action to compel a federal agency to release budget authority for obligation if the budget authority is required to be released under the ICA, and the agency has not released the funds. This bill prohibits GAO from bringing such an action without prior congressional approval.\u00a0</p>",
      "updateDate": "2025-09-26",
      "versionCode": "id119hr4229"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4229ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Impoundment Control Act of 1974 to require prior approval from Congress before the Comptroller General may pursue a civil action under such Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T10:48:24Z"
    },
    {
      "title": "To amend the Impoundment Control Act of 1974 to require prior approval from Congress before the Comptroller General may pursue a civil action under such Act, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-28T08:06:18Z"
    }
  ]
}
```
