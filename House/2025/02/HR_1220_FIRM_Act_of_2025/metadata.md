# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1220?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1220
- Title: FIRM Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1220
- Origin chamber: House
- Introduced date: 2025-02-11
- Update date: 2026-01-05T17:59:23Z
- Update date including text: 2026-01-05T17:59:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-11: Introduced in House

## Actions

- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1220",
    "number": "1220",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "W000812",
        "district": "2",
        "firstName": "Ann",
        "fullName": "Rep. Wagner, Ann [R-MO-2]",
        "lastName": "Wagner",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "FIRM Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-05T17:59:23Z",
    "updateDateIncludingText": "2026-01-05T17:59:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-11",
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
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T15:01:25Z",
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
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "TX"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1220ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1220\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2025 Mrs. Wagner (for herself and Mr. Gill of Texas ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to direct the Secretary of State to increase the fee imposed on aliens filing an application abroad for a visa authorizing admission to the United States as a nonimmigrant described in section 101(a)(15)(B) who are nationals of certain countries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fee Increases for Reckless Mismanagement Act of 2025 or FIRM Act of 2025 .\n#### 2. Fee increase for certain nonimmigrant visa applicants\n##### (a) In general\nThe Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ) is amended by inserting after section 281 the following:\n281A. Fee increase for certain nonimmigrant visa applicants (a) Fee increase The Secretary of State shall increase the fee imposed under section 281 on an alien filing an application abroad for a visa authorizing admission to the United States as a nonimmigrant described in section 101(a)(15)(B) in accordance with subsection (b) for any alien who is a national of a country with respect to which the Secretary determines any of the following: (1) The Secretary of Homeland Security has reported to the Secretary of State under section 243(d) that the government of the country has denied or unreasonably delayed accepting an alien who is a citizen, subject, national, or resident of that country after the Secretary of Homeland Security asked whether the government would accept the alien. (2) The Secretary of State has designated the country as a state sponsor of international terrorism (as such term is defined in section 214(c)(4)(F)(ii)). (3) The country is listed as a tier 3 country in the most recent Trafficking in Persons report of the Office to Monitor and Combat Trafficking in Persons of the Department of State. (b) Amount of increase The Secretary shall increase the fee described in subsection (a) as follows: (1) If the Secretary determines that the country meets one of the criteria described in paragraphs (1) through (3) of subsection (a), the Secretary shall increase such fee by not less than 50 percent. (2) If the Secretary determines that the country meets two of the criteria described in paragraphs (1) through (3) of subsection (a), the Secretary shall increase such fee by not less than 100 percent. (3) If the Secretary determines that the country meets three of the criteria described in paragraphs (1) through (3) of subsection (a), the Secretary shall increase such fee by not less than 150 percent. (c) Periodic review On the first day of each month, the Secretary shall review the determinations under subsection (a), to determine whether any increase imposed should be reduced, or whether an increase should be imposed on nationals of any additional countries. .\n##### (b) Clerical amendment\nThe table of contents for the Immigration and Nationality Act is amended by inserting after the item related to section 281 the following:\n281A. Fee increase for certain nonimmigrant visa applicants. .",
      "versionDate": "2025-02-11",
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
        "updateDate": "2025-03-13T13:23:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-11",
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
          "measure-id": "id119hr1220",
          "measure-number": "1220",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-11",
          "originChamber": "HOUSE",
          "update-date": "2026-01-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1220v00",
            "update-date": "2026-01-05"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fee Increases for Reckless Mismanagement Act of 2025 or FIRM Act of 2025</strong></p><p>This bill requires the Department of State to increase the fee for certain nonimmigrant visa applicants (i.e., those who are visiting temporarily for business or pleasure) who are nationals of certain countries. In particular, the State Department must increase the fee on the nationals of a country if the State Department determines that the government of the country has denied or delayed the acceptance of certain\u00a0non-U.S. nationals, if the State Department has designated the country as a state sponsor of international terrorism, or if the country is not meeting certain standards for combating human trafficking.</p><p>The fee increases with each of the criteria the country meets. The State Department must evaluate countries based on the criteria monthly and adjust the fee accordingly.\u00a0</p>"
        },
        "title": "FIRM Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1220.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fee Increases for Reckless Mismanagement Act of 2025 or FIRM Act of 2025</strong></p><p>This bill requires the Department of State to increase the fee for certain nonimmigrant visa applicants (i.e., those who are visiting temporarily for business or pleasure) who are nationals of certain countries. In particular, the State Department must increase the fee on the nationals of a country if the State Department determines that the government of the country has denied or delayed the acceptance of certain\u00a0non-U.S. nationals, if the State Department has designated the country as a state sponsor of international terrorism, or if the country is not meeting certain standards for combating human trafficking.</p><p>The fee increases with each of the criteria the country meets. The State Department must evaluate countries based on the criteria monthly and adjust the fee accordingly.\u00a0</p>",
      "updateDate": "2026-01-05",
      "versionCode": "id119hr1220"
    },
    "title": "FIRM Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fee Increases for Reckless Mismanagement Act of 2025 or FIRM Act of 2025</strong></p><p>This bill requires the Department of State to increase the fee for certain nonimmigrant visa applicants (i.e., those who are visiting temporarily for business or pleasure) who are nationals of certain countries. In particular, the State Department must increase the fee on the nationals of a country if the State Department determines that the government of the country has denied or delayed the acceptance of certain\u00a0non-U.S. nationals, if the State Department has designated the country as a state sponsor of international terrorism, or if the country is not meeting certain standards for combating human trafficking.</p><p>The fee increases with each of the criteria the country meets. The State Department must evaluate countries based on the criteria monthly and adjust the fee accordingly.\u00a0</p>",
      "updateDate": "2026-01-05",
      "versionCode": "id119hr1220"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1220ih.xml"
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
      "title": "FIRM Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T11:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FIRM Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T11:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fee Increases for Reckless Mismanagement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T11:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to direct the Secretary of State to increase the fee imposed on aliens filing an application abroad for a visa authorizing admission to the United States as a nonimmigrant described in section 101(a)(15)(B) who are nationals of certain countries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T11:18:33Z"
    }
  ]
}
```
