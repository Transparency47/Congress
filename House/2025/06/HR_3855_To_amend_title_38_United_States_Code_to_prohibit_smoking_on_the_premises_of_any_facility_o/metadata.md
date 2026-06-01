# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3855?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3855
- Title: To amend title 38, United States Code, to prohibit smoking on the premises of any facility of the Veterans Health Administration, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 3855
- Origin chamber: House
- Introduced date: 2025-06-10
- Update date: 2026-02-04T04:26:31Z
- Update date including text: 2026-02-04T04:26:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-10: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-23 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-06-10: Introduced in House

## Actions

- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-23 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-10",
    "latestAction": {
      "actionDate": "2025-06-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3855",
    "number": "3855",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000628",
        "district": "2",
        "firstName": "Neal",
        "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
        "lastName": "Dunn",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "To amend title 38, United States Code, to prohibit smoking on the premises of any facility of the Veterans Health Administration, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-02-04T04:26:31Z",
    "updateDateIncludingText": "2026-02-04T04:26:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-23",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-10",
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
          "date": "2025-06-10T14:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-23T18:14:28Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3855ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3855\nIN THE HOUSE OF REPRESENTATIVES\nJune 10, 2025 Mr. Dunn of Florida (for himself and Ms. Underwood ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to prohibit smoking on the premises of any facility of the Veterans Health Administration, and for other purposes.\n#### 1. Prohibition on smoking in facilities of the Veterans Health Administration\n##### (a) Prohibition\nSection 1715 of title 38, United States Code, is amended to read as follows:\n1715. Prohibition on smoking in facilities of the Veterans Health Administration (a) Prohibition No person (including any veteran, patient, resident, employee of the Department, contractor, or visitor) may smoke on the premises of any facility of the Veterans Health Administration. (b) Definitions In this section: (1) The term smoke includes\u2014 (A) the use of cigarettes, cigars, pipes, and any other combustion or heating of tobacco; and (B) the use of any electronic nicotine delivery system, including electronic or e-cigarettes, vape pens, and e-cigars. (2) The term facility of the Veterans Health Administration means any land or building (including any medical center, nursing home, domiciliary facility, outpatient clinic, or center that provides readjustment counseling) that is\u2014 (A) under the jurisdiction of the Department of Veterans Affairs; (B) under the control of the Veterans Health Administration; and (C) not under the control of the General Services Administration. .\n##### (b) Conforming amendments\n**(1) Table of sections**\nThe table of sections at the beginning of chapter 17 of such title is amended by striking the item relating to section 1715 and inserting the following:\n1715. Prohibition on smoking in facilities of the Veterans Health Administration. .\n**(2) Veterans Health Care Act of 1992**\nSection 526 of the Veterans Health Care Act of 1992 ( Public Law 102\u2013585 ) is repealed.",
      "versionDate": "2025-06-10",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-06-25",
        "text": "Read twice and referred to the Committee on Veterans' Affairs. (text: CR S3534)"
      },
      "number": "2171",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A bill to amend title 38, United States Code, to prohibit smoking on the premises of any facility of the Veterans Health Administration, and for other purposes.",
      "type": "S"
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
        "updateDate": "2025-06-24T20:20:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-10",
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
          "measure-id": "id119hr3855",
          "measure-number": "3855",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-10",
          "originChamber": "HOUSE",
          "update-date": "2025-08-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3855v00",
            "update-date": "2025-08-14"
          },
          "action-date": "2025-06-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill prohibits smoking on the premises of any Veterans Health Administration facility. The bill defines smoking as the use of cigarettes, cigars, and pipes (i.e., the heating or combustion of tobacco), as well as the use of any electronic nicotine delivery system.</p>"
        },
        "title": "To amend title 38, United States Code, to prohibit smoking on the premises of any facility of the Veterans Health Administration, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3855.xml",
    "summary": {
      "actionDate": "2025-06-10",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill prohibits smoking on the premises of any Veterans Health Administration facility. The bill defines smoking as the use of cigarettes, cigars, and pipes (i.e., the heating or combustion of tobacco), as well as the use of any electronic nicotine delivery system.</p>",
      "updateDate": "2025-08-14",
      "versionCode": "id119hr3855"
    },
    "title": "To amend title 38, United States Code, to prohibit smoking on the premises of any facility of the Veterans Health Administration, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-06-10",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill prohibits smoking on the premises of any Veterans Health Administration facility. The bill defines smoking as the use of cigarettes, cigars, and pipes (i.e., the heating or combustion of tobacco), as well as the use of any electronic nicotine delivery system.</p>",
      "updateDate": "2025-08-14",
      "versionCode": "id119hr3855"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3855ih.xml"
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
      "title": "To amend title 38, United States Code, to prohibit smoking on the premises of any facility of the Veterans Health Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-13T05:48:16Z"
    },
    {
      "title": "To amend title 38, United States Code, to prohibit smoking on the premises of any facility of the Veterans Health Administration, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-11T08:06:22Z"
    }
  ]
}
```
