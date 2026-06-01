# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1850?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1850
- Title: CRUDE Act
- Congress: 119
- Bill type: HR
- Bill number: 1850
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-05-08T12:54:34Z
- Update date including text: 2026-05-08T12:54:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1850",
    "number": "1850",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "A000375",
        "district": "19",
        "firstName": "Jodey",
        "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
        "lastName": "Arrington",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "CRUDE Act",
    "type": "HR",
    "updateDate": "2026-05-08T12:54:34Z",
    "updateDateIncludingText": "2026-05-08T12:54:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "WA"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1850ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1850\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Arrington (for himself, Mr. Weber of Texas , Mr. Fallon , Mr. Newhouse , and Mr. Crenshaw ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo revise the authority provided to the President to impose export licensing requirements or other restrictions on the export of crude oil from the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Continuing Robust and Uninhibited Drilling and Exporting Act or the CRUDE Act .\n#### 2. Crude oil export licensing requirements and other restrictions\nSection 101(d)(1) of division O of the Consolidated Appropriations Act, 2016 ( 42 U.S.C. 6212a(d)(1) ) is amended\u2014\n**(1)**\nby amending subparagraph (A) to read as follows:\n(A) (i) the Secretary of Defense, the Secretary of Energy, and the Secretary of Commerce jointly find and report to the President and to the Congress that\u2014 (I) the export of crude oil pursuant to this Act has caused sustained material oil supply shortages or sustained oil prices significantly above world market levels that are directly attributable to the export of crude oil produced in the United States; and (II) those supply shortages or price increases have caused or are likely to cause sustained material adverse employment effects in the United States; and (ii) the President declares a national emergency based on the findings of a report under clause (i) and formally notices the declaration of a national emergency in the Federal Register; or ;\n**(2)**\nin subparagraph (B), by striking ; or and inserting a period; and\n**(3)**\nby striking subparagraph (C).",
      "versionDate": "2025-03-05",
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
        "name": "Energy",
        "updateDate": "2025-03-21T16:52:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-05",
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
          "measure-id": "id119hr1850",
          "measure-number": "1850",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-05",
          "originChamber": "HOUSE",
          "update-date": "2026-05-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1850v00",
            "update-date": "2026-05-08"
          },
          "action-date": "2025-03-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Continuing Robust and Uninhibited Drilling and Exporting Act or the CRUDE Act</strong></p><p>This bill limits the President's authority to restrict the export of crude oil from the United States.</p><p>Currently, the President may restrict the export of oil for up to a year if</p><ul><li>the President declares a national emergency;</li><li>the restrictions are sanctions or trade restrictions that apply to countries, persons, or organizations for national security reasons; or</li><li>the Department of Commerce, in consultation with the Department of Energy (DOE), finds and reports to the President that the export of U.S. crude oil has caused sustained material oil supply shortages or sustained oil prices significantly above world market levels that have caused or are likely to cause sustained material adverse employment effects.</li></ul><p>However, this bill only allows the President to impose such restrictions if</p><ul><li>the President declares a national emergency based on findings\u00a0that are jointly issued by Department of Defense, DOE, and Commerce and include the conclusions described above\u00a0about oil supply shortages or increased oil prices; or\u00a0</li><li>the restrictions are sanctions or trade restrictions\u00a0that apply to countries, persons, or organization for national security reasons.</li></ul>"
        },
        "title": "CRUDE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1850.xml",
    "summary": {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Continuing Robust and Uninhibited Drilling and Exporting Act or the CRUDE Act</strong></p><p>This bill limits the President's authority to restrict the export of crude oil from the United States.</p><p>Currently, the President may restrict the export of oil for up to a year if</p><ul><li>the President declares a national emergency;</li><li>the restrictions are sanctions or trade restrictions that apply to countries, persons, or organizations for national security reasons; or</li><li>the Department of Commerce, in consultation with the Department of Energy (DOE), finds and reports to the President that the export of U.S. crude oil has caused sustained material oil supply shortages or sustained oil prices significantly above world market levels that have caused or are likely to cause sustained material adverse employment effects.</li></ul><p>However, this bill only allows the President to impose such restrictions if</p><ul><li>the President declares a national emergency based on findings\u00a0that are jointly issued by Department of Defense, DOE, and Commerce and include the conclusions described above\u00a0about oil supply shortages or increased oil prices; or\u00a0</li><li>the restrictions are sanctions or trade restrictions\u00a0that apply to countries, persons, or organization for national security reasons.</li></ul>",
      "updateDate": "2026-05-08",
      "versionCode": "id119hr1850"
    },
    "title": "CRUDE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Continuing Robust and Uninhibited Drilling and Exporting Act or the CRUDE Act</strong></p><p>This bill limits the President's authority to restrict the export of crude oil from the United States.</p><p>Currently, the President may restrict the export of oil for up to a year if</p><ul><li>the President declares a national emergency;</li><li>the restrictions are sanctions or trade restrictions that apply to countries, persons, or organizations for national security reasons; or</li><li>the Department of Commerce, in consultation with the Department of Energy (DOE), finds and reports to the President that the export of U.S. crude oil has caused sustained material oil supply shortages or sustained oil prices significantly above world market levels that have caused or are likely to cause sustained material adverse employment effects.</li></ul><p>However, this bill only allows the President to impose such restrictions if</p><ul><li>the President declares a national emergency based on findings\u00a0that are jointly issued by Department of Defense, DOE, and Commerce and include the conclusions described above\u00a0about oil supply shortages or increased oil prices; or\u00a0</li><li>the restrictions are sanctions or trade restrictions\u00a0that apply to countries, persons, or organization for national security reasons.</li></ul>",
      "updateDate": "2026-05-08",
      "versionCode": "id119hr1850"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1850ih.xml"
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
      "title": "CRUDE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CRUDE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Continuing Robust and Uninhibited Drilling and Exporting Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To revise the authority provided to the President to impose export licensing requirements or other restrictions on the export of crude oil from the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:24Z"
    }
  ]
}
```
