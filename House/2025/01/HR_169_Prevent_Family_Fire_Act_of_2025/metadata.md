# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/169?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/169
- Title: Prevent Family Fire Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 169
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-02-18T09:05:49Z
- Update date including text: 2026-02-18T09:05:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Ways and Means.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/169",
    "number": "169",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000593",
        "district": "49",
        "firstName": "Mike",
        "fullName": "Rep. Levin, Mike [D-CA-49]",
        "lastName": "Levin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Prevent Family Fire Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-18T09:05:49Z",
    "updateDateIncludingText": "2026-02-18T09:05:49Z"
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
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
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
          "date": "2025-01-03T16:19:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "NY"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-01-03",
      "state": "PA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "CA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "OR"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "PA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "state": "WA"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-04-14",
      "state": "NJ"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NY"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-17",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr169ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 169\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Levin (for himself, Mr. Lawler , Mr. Boyle of Pennsylvania , and Mrs. Kim ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow for a credit against tax for sales at retail of safe firearm storage devices.\n#### 1. Short title\nThis Act may be cited as the Prevent Family Fire Act of 2025 .\n#### 2. Safe firearm storage credit\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Safe firearm storage credit (a) Allowance of credit For purposes of section 38, the safe firearm storage credit determined under this section for the taxable year is an amount equal to 10 percent of amounts received from the first retail sale of each safe firearm storage device sold by the taxpayer for use within the United States during the taxable year. (b) Limitations (1) $400 per device The amounts received from a first retail sale that are taken into account under subsection (a) with respect to a safe firearm storage device shall not exceed $400 per device. (2) Fair market value The amount taken into account under subsection (a) shall not include amounts in excess of the fair market value of such safe firearm storage device. (c) Definitions and special rules For purposes of this section\u2014 (1) Determination of price In determining price, there shall be excluded, if stated as a separate charge, the amount of any retail sales tax imposed by any State or political subdivision thereof or the District of Columbia, whether the liability for such tax is imposed on the vendor or vendee. (2) First retail sale The term first retail sale means the first sale, for a purpose other than for resale or leasing in a long-term lease, after production, manufacture, or importation. (3) Safe firearm storage device (A) In general The term safe firearm storage device means a device that is\u2014 (i) designed and marketed for the principal purpose of denying unauthorized access to, or rendering inoperable, a firearm or ammunition, and (ii) secured by a combination lock, key lock, or lock based on biometric information which\u2014 (I) is integrated into the design of the device, and (II) once locked, is incapable of being opened without the combination, key, or biometric information, respectively. (B) Exclusion The term safe firearm storage device does not include\u2014 (i) any device which is incorporated to any extent into the design of a firearm or of ammunition, or (ii) any device that, as of the date of the sale described in subsection (a), has been subject to a mandatory recall by the Consumer Product Safety Commission. (C) Firearm; ammunition The terms firearm and ammunition have the meanings given such terms in section 921 of title 18, United States Code (without regard to all that follows firearm silencer in paragraph (3) of such section). (d) Recapture (1) In general The Secretary shall, by regulations, provide for recapturing the benefit of any credit allowable under subsection (a) if such credit is improperly or excessively claimed. (2) Documentation The Secretary may require such information or registration as the Secretary deems necessary for purposes of recapture under paragraph (1). (e) Termination This section shall not apply to sales after December 31, 2032. .\n##### (b) Credit made part of general business credit\nSubsection (b) of section 38 of the Internal Revenue Code of 1986 is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) the safe firearm storage credit determined under section 45BB(a). .\n##### (c) Credit allowed against AMT\nSection 38(c)(4)(B) of such Code is amended by redesignating clauses (x) through (xii) as clauses (xi) through (xiii), respectively, and by inserting after clause (ix) the following new clause:\n(x) the credit determined under section 45BB, .\n##### (d) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following new item:\nSec. 45BB. Safe firearm storage credit.\n##### (e) Report\nThe Secretary of the Treasury shall make publicly available an annual report of the credits against tax allowed by reason of section 45BB (as added by this section), disaggregated by State.\n##### (f) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-03-03T18:22:54Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-03T18:23:06Z"
          },
          {
            "name": "Income tax credits",
            "updateDate": "2025-03-03T18:23:29Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2025-03-03T18:23:38Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-02-05T14:48:39Z"
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
          "measure-id": "id119hr169",
          "measure-number": "169",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr169v00",
            "update-date": "2025-02-14"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Prevent Family Fire Act of 2025 </strong></p><p>This bill establishes a new business tax credit on the sale of a safe firearm storage device on or before December 31, 2032.\u00a0</p><p>The amount of the tax credit is 10% of the retail sales price (up to a maximum price of $400 and excluding separately stated sales tax) of a safe firearm storage device. The tax credit is allowed only on the first retail sale of a safe firearm storage device for a use other than resale or long-term lease.</p><p>The bill defines <em>safe firearm storage device</em> as a device that is (1) designed and marketed to deny unauthorized access to a firearm or ammunition or render such items inoperable;\u00a0and (2) is secured by a combination lock, key lock, or lock based on biometric information.</p><p>\u00a0</p>"
        },
        "title": "Prevent Family Fire Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr169.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Prevent Family Fire Act of 2025 </strong></p><p>This bill establishes a new business tax credit on the sale of a safe firearm storage device on or before December 31, 2032.\u00a0</p><p>The amount of the tax credit is 10% of the retail sales price (up to a maximum price of $400 and excluding separately stated sales tax) of a safe firearm storage device. The tax credit is allowed only on the first retail sale of a safe firearm storage device for a use other than resale or long-term lease.</p><p>The bill defines <em>safe firearm storage device</em> as a device that is (1) designed and marketed to deny unauthorized access to a firearm or ammunition or render such items inoperable;\u00a0and (2) is secured by a combination lock, key lock, or lock based on biometric information.</p><p>\u00a0</p>",
      "updateDate": "2025-02-14",
      "versionCode": "id119hr169"
    },
    "title": "Prevent Family Fire Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Prevent Family Fire Act of 2025 </strong></p><p>This bill establishes a new business tax credit on the sale of a safe firearm storage device on or before December 31, 2032.\u00a0</p><p>The amount of the tax credit is 10% of the retail sales price (up to a maximum price of $400 and excluding separately stated sales tax) of a safe firearm storage device. The tax credit is allowed only on the first retail sale of a safe firearm storage device for a use other than resale or long-term lease.</p><p>The bill defines <em>safe firearm storage device</em> as a device that is (1) designed and marketed to deny unauthorized access to a firearm or ammunition or render such items inoperable;\u00a0and (2) is secured by a combination lock, key lock, or lock based on biometric information.</p><p>\u00a0</p>",
      "updateDate": "2025-02-14",
      "versionCode": "id119hr169"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr169ih.xml"
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
      "title": "Prevent Family Fire Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-04T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prevent Family Fire Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow for a credit against tax for sales at retail of safe firearm storage devices.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T05:33:20Z"
    }
  ]
}
```
