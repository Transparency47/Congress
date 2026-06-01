# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/64?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/64
- Title: Grant’s Law
- Congress: 119
- Bill type: HR
- Bill number: 64
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-02-25T09:06:14Z
- Update date including text: 2026-02-25T09:06:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/64",
    "number": "64",
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
    "title": "Grant\u2019s Law",
    "type": "HR",
    "updateDate": "2026-02-25T09:06:14Z",
    "updateDateIncludingText": "2026-02-25T09:06:14Z"
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
          "date": "2025-01-03T16:21:10Z",
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
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "FL"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr64ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 64\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself and Mrs. Luna ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo require the Secretary of Homeland Security to detain any alien who is unlawfully present in the United States and is arrested for certain criminal offenses.\n#### 1. Short title\nThis Act may be cited as Grant\u2019s Law .\n#### 2. Mandatory detention for certain aliens arrested for the commission of certain offenses\nSection 236(c) of the Immigration and Nationality Act ( 8 U.S.C. 1226(c)(1) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (C), by striking or at the end;\n**(B)**\nin subparagraph (D), by adding or at the end; and\n**(C)**\nby inserting after subparagraph (D) the following:\n(E) is\u2014 (i) determined by the Secretary of Homeland Security to be unlawfully present in the United States; and (ii) arrested for any offense described in subparagraphs (A) through (D) the conviction of which would render the alien inadmissible under section 212(a) or deportable under section 237(a), ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby striking The Attorney General and inserting the following:\n(A) In general Except as provided in subparagraph (B), the Secretary of Homeland Security ;\n**(B)**\nby striking the Attorney General each place such term appears and inserting the Secretary ; and\n**(C)**\nby adding at the end the following:\n(B) Arrested but not convicted aliens The Secretary of Homeland Security may release any alien held pursuant to paragraph (1)(E) to the appropriate authority for any proceedings subsequent to the arrest. The Secretary shall resume custody of the alien during any period pending the final disposition of any such proceedings that the alien is not in the custody of such appropriate authority. If the alien is not convicted of the offense for which the alien was arrested, the Secretary shall continue to detain the alien until removal proceedings are completed. .\n#### 3. Expedited initiation of removal proceedings\nSection 239(d) of the Immigration and Nationality Act ( 8 U.S.C. 1229(d) ) is amended by adding at the end the following:\n(3) In the case of any alien held pursuant to section 236(c)(1)(E), the Secretary of Homeland Security shall complete removal proceedings by not later than 90 days after such alien is detained. .",
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
            "name": "Administrative remedies",
            "updateDate": "2025-06-10T16:05:04Z"
          },
          {
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-06-10T16:05:04Z"
          },
          {
            "name": "Detention of persons",
            "updateDate": "2025-06-10T16:05:04Z"
          },
          {
            "name": "Immigration status and procedures",
            "updateDate": "2025-06-10T16:05:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-02-04T12:59:51Z"
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
          "measure-id": "id119hr64",
          "measure-number": "64",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr64v00",
            "update-date": "2025-02-11"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Grant's Law</strong></p><p>This bill requires the Department of Justice to detain a non-U.S. national (<em>alien</em> under federal law) found to be unlawfully present in the United States and arrested for various crimes that would render the individual deportable or inadmissible.</p><p>The Department of Homeland Security (DHS) may release the individual to an appropriate authority for proceedings related to the arrest, but DHS must resume custody for any period that the individual is not in such authority's custody.</p><p>If the individual is not convicted of crimes for which the individual was arrested, DHS must continue to detain the individual until removal proceedings are completed. DHS must complete such removal proceedings within 90 days.</p>"
        },
        "title": "Grant\u2019s Law"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr64.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Grant's Law</strong></p><p>This bill requires the Department of Justice to detain a non-U.S. national (<em>alien</em> under federal law) found to be unlawfully present in the United States and arrested for various crimes that would render the individual deportable or inadmissible.</p><p>The Department of Homeland Security (DHS) may release the individual to an appropriate authority for proceedings related to the arrest, but DHS must resume custody for any period that the individual is not in such authority's custody.</p><p>If the individual is not convicted of crimes for which the individual was arrested, DHS must continue to detain the individual until removal proceedings are completed. DHS must complete such removal proceedings within 90 days.</p>",
      "updateDate": "2025-02-11",
      "versionCode": "id119hr64"
    },
    "title": "Grant\u2019s Law"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Grant's Law</strong></p><p>This bill requires the Department of Justice to detain a non-U.S. national (<em>alien</em> under federal law) found to be unlawfully present in the United States and arrested for various crimes that would render the individual deportable or inadmissible.</p><p>The Department of Homeland Security (DHS) may release the individual to an appropriate authority for proceedings related to the arrest, but DHS must resume custody for any period that the individual is not in such authority's custody.</p><p>If the individual is not convicted of crimes for which the individual was arrested, DHS must continue to detain the individual until removal proceedings are completed. DHS must complete such removal proceedings within 90 days.</p>",
      "updateDate": "2025-02-11",
      "versionCode": "id119hr64"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr64ih.xml"
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
      "title": "Grant\u2019s Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-04T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Grant\u2019s Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Homeland Security to detain any alien who is unlawfully present in the United States and is arrested for certain criminal offenses.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T05:18:18Z"
    }
  ]
}
```
