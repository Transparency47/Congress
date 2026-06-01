# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6470?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6470
- Title: Increasing Baseline Updates Act
- Congress: 119
- Bill type: HR
- Bill number: 6470
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-01-14T15:34:15Z
- Update date including text: 2026-01-14T15:34:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on the Budget.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on the Budget.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6470",
    "number": "6470",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001213",
        "district": "1",
        "firstName": "Blake",
        "fullName": "Rep. Moore, Blake D. [R-UT-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Increasing Baseline Updates Act",
    "type": "HR",
    "updateDate": "2026-01-14T15:34:15Z",
    "updateDateIncludingText": "2026-01-14T15:34:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
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
      "text": "Referred to the House Committee on the Budget.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T14:07:45Z",
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
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "VA"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "NC"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "GA"
    },
    {
      "bioguideId": "A000375",
      "district": "19",
      "firstName": "Jodey",
      "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Arrington",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6470ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6470\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Mr. Moore of Utah (for himself, Mr. Cline , Mr. Edwards , and Mr. Carter of Georgia ) introduced the following bill; which was referred to the Committee on the Budget\nA BILL\nTo amend the Congressional Budget and Impoundment Control Act of 1974 to require the Congressional Budget Office to provide baseline updates, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Increasing Baseline Updates Act .\n#### 2. Congressional Budget Office updates to baseline\nSection 202(e) of the Congressional Budget and Impoundment Control Act of 1974 ( 2 U.S.C. 602(e) ) is amended by adding at the end the following:\n(4) (A) Unless directed otherwise by the chairs of the Committees on the Budget of the House of Representatives and the Senate, the Director shall, to the extent practicable, submit to such committees at least two updates to the report submitted under paragraph (1), at least one of which shall include economic data used by the Director to calculate such update. (B) Nothing in this paragraph shall be construed to limit the Director from providing any other update to the baseline during such year. .\n#### 3. Annual technical budget data submission by the President\nSection 1106 of title 31, United States Code, is amended by adding at the end the following:\n(d) To the extent practicable, on or before February 1 of each calendar year, the President shall submit to Congress technical budget data for the fiscal year beginning in the ensuing calendar year, which shall include up-to-date estimates for current year and prior year data and credit reestimates for the current year (as included in the Federal credit supplement of such budget). .",
      "versionDate": "2025-12-04",
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
        "updateDate": "2026-01-07T17:01:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-04",
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
          "measure-id": "id119hr6470",
          "measure-number": "6470",
          "measure-type": "hr",
          "orig-publish-date": "2025-12-04",
          "originChamber": "HOUSE",
          "update-date": "2026-01-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6470v00",
            "update-date": "2026-01-14"
          },
          "action-date": "2025-12-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Increasing Baseline Updates Act</strong></p><p>This bill requires the Congressional Budget Office (CBO) to submit to Congress at least two updates to its annual baseline unless CBO is otherwise directed by the chairs of the congressional budget committees. At least one of the updates must include the economic data used by CBO to calculate the update.</p><p>(A baseline is a projection of federal spending and receipts during a fiscal year under current law. Under current law, CBO is required to publish the baseline by February 15 of each year. While there is no statutory requirement for specific updates, CBO generally provides an update with its analysis of the President's annual budget request. It has also provided some updates during the summer, depending on the timing of the President's budget request.)</p><p>The bill also requires the President to submit technical budget data to Congress on or before February 1 of each year to the extent this is practicable. Currently, federal agencies provide the data to Congress as part of the President's budget request.</p>"
        },
        "title": "Increasing Baseline Updates Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6470.xml",
    "summary": {
      "actionDate": "2025-12-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Increasing Baseline Updates Act</strong></p><p>This bill requires the Congressional Budget Office (CBO) to submit to Congress at least two updates to its annual baseline unless CBO is otherwise directed by the chairs of the congressional budget committees. At least one of the updates must include the economic data used by CBO to calculate the update.</p><p>(A baseline is a projection of federal spending and receipts during a fiscal year under current law. Under current law, CBO is required to publish the baseline by February 15 of each year. While there is no statutory requirement for specific updates, CBO generally provides an update with its analysis of the President's annual budget request. It has also provided some updates during the summer, depending on the timing of the President's budget request.)</p><p>The bill also requires the President to submit technical budget data to Congress on or before February 1 of each year to the extent this is practicable. Currently, federal agencies provide the data to Congress as part of the President's budget request.</p>",
      "updateDate": "2026-01-14",
      "versionCode": "id119hr6470"
    },
    "title": "Increasing Baseline Updates Act"
  },
  "summaries": [
    {
      "actionDate": "2025-12-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Increasing Baseline Updates Act</strong></p><p>This bill requires the Congressional Budget Office (CBO) to submit to Congress at least two updates to its annual baseline unless CBO is otherwise directed by the chairs of the congressional budget committees. At least one of the updates must include the economic data used by CBO to calculate the update.</p><p>(A baseline is a projection of federal spending and receipts during a fiscal year under current law. Under current law, CBO is required to publish the baseline by February 15 of each year. While there is no statutory requirement for specific updates, CBO generally provides an update with its analysis of the President's annual budget request. It has also provided some updates during the summer, depending on the timing of the President's budget request.)</p><p>The bill also requires the President to submit technical budget data to Congress on or before February 1 of each year to the extent this is practicable. Currently, federal agencies provide the data to Congress as part of the President's budget request.</p>",
      "updateDate": "2026-01-14",
      "versionCode": "id119hr6470"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6470ih.xml"
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
      "title": "Increasing Baseline Updates Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-27T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Increasing Baseline Updates Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Congressional Budget and Impoundment Control Act of 1974 to require the Congressional Budget Office to provide baseline updates, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:21Z"
    }
  ]
}
```
