# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5836?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5836
- Title: Keep WIC Working Act
- Congress: 119
- Bill type: HR
- Bill number: 5836
- Origin chamber: House
- Introduced date: 2025-10-28
- Update date: 2025-11-05T09:05:47Z
- Update date including text: 2025-11-05T09:05:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-28: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Referred to the House Committee on Appropriations.
- Latest action: 2025-10-28: Introduced in House

## Actions

- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Referred to the House Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-28",
    "latestAction": {
      "actionDate": "2025-10-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5836",
    "number": "5836",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001327",
        "district": "8",
        "firstName": "Robert",
        "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
        "lastName": "Bresnahan",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Keep WIC Working Act",
    "type": "HR",
    "updateDate": "2025-11-05T09:05:47Z",
    "updateDateIncludingText": "2025-11-05T09:05:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-28",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "hsap00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-28",
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
          "date": "2025-10-28T17:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Appropriations Committee",
      "systemCode": "hsap00",
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
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "IA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "PA"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "KS"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "PA"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5836ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5836\nIN THE HOUSE OF REPRESENTATIVES\nOctober 28, 2025 Mr. Bresnahan (for himself, Mr. Nunn of Iowa , and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Appropriations\nA BILL\nTo make continuing appropriations for the Special Supplemental Nutrition Program for Women, Infants, and Children in the event of a Government shutdown.\n#### 1. Short title\nThis Act may be cited as the Keep WIC Working Act .\n#### 2. Uninterrupted benefits under WIC\n##### (a) In general\nIn fiscal year 2026, during any period of a lapse in discretionary appropriations for the Department of Agriculture, there are appropriated to the Secretary of Agriculture, out of any money in the Treasury not otherwise appropriated, such sums as are necessary to carry out the special supplemental nutrition program for women, infants, and children established under section 17 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786 ) (referred to in this section as WIC ).\n##### (b) Retroactive benefits\nThe appropriations under subsection (a) shall include any amounts necessary for reimbursement of State agencies for any State funds used, during the period beginning on September 30, 2025, and ending on the date of the enactment of this section, to carry out operations necessary to maintain participation in WIC.\n##### (c) Termination\nAppropriations shall be made available pursuant to subsection (a) until the date of the enactment of appropriations for the Department of Agriculture for fiscal year 2026 (including a continuing appropriation).",
      "versionDate": "2025-10-28",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-10-30T13:48:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-28",
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
          "measure-id": "id119hr5836",
          "measure-number": "5836",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-28",
          "originChamber": "HOUSE",
          "update-date": "2025-10-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5836v00",
            "update-date": "2025-10-30"
          },
          "action-date": "2025-10-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Keep WIC Working Act</strong></p><p>This bill provides appropriations for the Department of Agriculture (USDA) to carry out the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC) during any lapse in FY2026 discretionary appropriations for USDA. WIC provides nutrition-rich foods, nutrition education, and health care and social services referrals to eligible low-income women, infants, and children.</p><p>The bill also provides appropriations for USDA to reimburse state agencies for any state funds used to carry out operations necessary to maintain participation in WIC during the period that began on September 30, 2025, and ends on the date that this bill is enacted.</p><p>The appropriations provided by this bill are available until legislation is enacted that provides FY2026 appropriations for USDA (including continuing appropriations for USDA).\u00a0</p>"
        },
        "title": "Keep WIC Working Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5836.xml",
    "summary": {
      "actionDate": "2025-10-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Keep WIC Working Act</strong></p><p>This bill provides appropriations for the Department of Agriculture (USDA) to carry out the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC) during any lapse in FY2026 discretionary appropriations for USDA. WIC provides nutrition-rich foods, nutrition education, and health care and social services referrals to eligible low-income women, infants, and children.</p><p>The bill also provides appropriations for USDA to reimburse state agencies for any state funds used to carry out operations necessary to maintain participation in WIC during the period that began on September 30, 2025, and ends on the date that this bill is enacted.</p><p>The appropriations provided by this bill are available until legislation is enacted that provides FY2026 appropriations for USDA (including continuing appropriations for USDA).\u00a0</p>",
      "updateDate": "2025-10-30",
      "versionCode": "id119hr5836"
    },
    "title": "Keep WIC Working Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Keep WIC Working Act</strong></p><p>This bill provides appropriations for the Department of Agriculture (USDA) to carry out the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC) during any lapse in FY2026 discretionary appropriations for USDA. WIC provides nutrition-rich foods, nutrition education, and health care and social services referrals to eligible low-income women, infants, and children.</p><p>The bill also provides appropriations for USDA to reimburse state agencies for any state funds used to carry out operations necessary to maintain participation in WIC during the period that began on September 30, 2025, and ends on the date that this bill is enacted.</p><p>The appropriations provided by this bill are available until legislation is enacted that provides FY2026 appropriations for USDA (including continuing appropriations for USDA).\u00a0</p>",
      "updateDate": "2025-10-30",
      "versionCode": "id119hr5836"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5836ih.xml"
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
      "title": "Keep WIC Working Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-30T09:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Keep WIC Working Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-30T09:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To make continuing appropriations for the Special Supplemental Nutrition Program for Women, Infants, and Children in the event of a Government shutdown.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-30T09:03:20Z"
    }
  ]
}
```
